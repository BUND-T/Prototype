"""
Text extraction for Bund/t — turns a document into auditable markdown.

Strategy:

1. Born-digital PDF (text objects and/or form fields present)
   → read it directly. No model, no recognition, full deterministic.
"""

import ctypes                    # lets Python call C functions directly — pdfium needs it
import json, os, re, sys
from pathlib import Path

import pypdfium2 as pdfium       # PDF engine (Google's pdfium): text, images, form fields
import pypdfium2.raw as raw      # the same engine's low-level C interface, for form fields

# from paddleocr import PaddleOCR, PaddleOCRVL   # OCR: line reader, and the vision-language model
# from functools import lru_cache  # caches a function's return value, so models load only once

# --- settings OCR ---------------------------------------------------------------------------
# pdfium reports a form field's type as a number; these are the names we print
# keyed by pdfium's own constants rather than by 0..7 — writing the numbers out by hand once
# shifted every entry after "combobox" by one, and textfields were reported as signatures
FIELD_TYPES = {
    raw.FPDF_FORMFIELD_UNKNOWN:     "unknown",
    raw.FPDF_FORMFIELD_PUSHBUTTON:  "pushbutton",
    raw.FPDF_FORMFIELD_CHECKBOX:    "checkbox",
    raw.FPDF_FORMFIELD_RADIOBUTTON: "radio",
    raw.FPDF_FORMFIELD_COMBOBOX:    "combobox",
    raw.FPDF_FORMFIELD_LISTBOX:     "listbox",
    raw.FPDF_FORMFIELD_TEXTFIELD:   "textfield",
    raw.FPDF_FORMFIELD_SIGNATURE:   "signature",
}
# DEVICE = "gpu"                # gpu only: paddlex picks its kernels from the build flag
# IMAGE_AREA_THRESHOLD = 0.02   # image objects smaller than this share of the page are decoration
# LOWCONF_LAYOUT = 0.7          # layout score below this gets marked in the markdown
# RISK_LABELS = ("table", "image", "chart", "seal", "formula")  # block kinds whose structure the model can get wrong
# HIGHLIGHT = "border:3px solid #c9a227; background:#fff8dc;"   # the yellow marking


# =========================================================================================
# born-digital PDFs: Directly read the text and form fields, no model involved
# =========================================================================================

def _get_pdfium_string(pdfium_function, *args) -> str:
    """
        pdfium does not return strings. This helper function calls a pdfium function that returns a UTF-16 string, first to get the size, then to allocate a buffer, then to get the string into that buffer, and finally to decode it to a Python string. 
        If the string is empty, it returns an empty string.
    """

    size = pdfium_function(*args, None, 0)
    if size <= 2:
        return ""

    buffer = (ctypes.c_ushort * (size // 2))()
    pdfium_function(*args, buffer, size)

    return bytes(buffer)[:size - 2].decode("utf-16-le", "replace")

def _choice_values(form_env, annotation) -> list[str]:
    """
    The selectable values of a dropdown or list box — the counterpart of a FIM Codeliste.

    The form handle is not optional: without it pdfium returns -1 instead of raising, and
    the options come back as an empty list with no error anywhere.

    # Arguments
    - `form_env`: the document's form environment.
    - `annotation`: the widget being read.

    # Returns
    The option labels in the order the form offers them.
    """
    count = max(raw.FPDFAnnot_GetOptionCount(form_env, annotation), 0) # pdfium returns -1 on error, but we want an empty list
    return [_get_pdfium_string(raw.FPDFAnnot_GetOptionLabel, form_env, annotation, index)
            for index in range(count)]

def _field_state(form_env, annotation) -> str:
    """
    Whether a field can be filled in, read from two separate PDF flag sets.

    # Arguments
    - `form_env`: the document's form environment.
    - `annotation`: the widget being read.

    # Returns
    "hidden" if the box is not drawn, "readonly" if it is drawn but not fillable,
    otherwise "visible".
    """
    # both calls return a bitmask
    annot_flags = raw.FPDFAnnot_GetFlags(annotation)
    form_flags = raw.FPDFAnnot_GetFormFieldFlags(form_env, annotation)

    if annot_flags & (raw.FPDF_ANNOT_FLAG_HIDDEN | raw.FPDF_ANNOT_FLAG_NOVIEW):
        return "hidden"
    if form_flags & raw.FPDF_FORMFLAG_READONLY:
        return "readonly"
    return "visible"

def _field_required(form_env, annotation) -> bool:
    """ Whether the form marks this field as mandatory — the counterpart of FIM's `anzahl` 1:… """
    return bool(raw.FPDFAnnot_GetFormFieldFlags(form_env, annotation)
                & raw.FPDF_FORMFLAG_REQUIRED)

def get_page_fields(document, page_index: int) -> list[dict]:
    """
    Returns the interactive form fields on one page.

    # Arguments
    - `document`: an opened pdfium document with `init_forms()` already called.
    - `page_index`: zero-based page number.

    # Returns
    One dict per field: name, type, tooltip, value, options, page, and widget boxes.
    """
    page = document[page_index]
    field_dict: dict[str, dict] = {}

    for index in range(raw.FPDFPage_GetAnnotCount(page)):
        annotation = raw.FPDFPage_GetAnnot(page, index)
        try:
            # annotations include links and comments; only widgets are form fields
            if raw.FPDFAnnot_GetSubtype(annotation) != raw.FPDF_ANNOT_WIDGET:
                continue

            name = _get_pdfium_string(raw.FPDFAnnot_GetFormFieldName, document.formenv, annotation)
            rectangle = raw.FS_RECTF()
            raw.FPDFAnnot_GetRect(annotation, ctypes.byref(rectangle))
            
            # setdefault: if key does not exist, create value. If it exists return existing value for key.
            # Several widgets can share one name — a yes/no radio pair, or a field repeated in two places. 
            # They are one question with one value, so they are collected into one entry with .
            field = field_dict.setdefault(name, {
                "name": name,
                "type": FIELD_TYPES.get(
                    raw.FPDFAnnot_GetFormFieldType(document.formenv, annotation), "?"),
                "tooltip": _get_pdfium_string(raw.FPDFAnnot_GetFormFieldAlternateName,
                                        document.formenv, annotation),
                "value": _get_pdfium_string(raw.FPDFAnnot_GetFormFieldValue,
                                      document.formenv, annotation),
                "options": _choice_values(document.formenv, annotation),
                "state": _field_state(document.formenv, annotation),
                "required": _field_required(document.formenv, annotation),
                "page": page_index + 1,
                "widgets": [],
            })
            field["widgets"].append([round(rectangle.left, 1), round(rectangle.bottom, 1),
                                     round(rectangle.right, 1), round(rectangle.top, 1)])
        finally:
            raw.FPDFPage_CloseAnnot(annotation)   # pdfium hands out handles we must give back

    return list(field_dict.values())

def get_pdf_description(pdf: str | Path) -> dict:
    """
    Reads everything a PDF states about itself and stores all text and fields in a dictionary.

    # Arguments
    - `pdf`: path to the PDF.

    # Returns
    A dict describing the document.
    """
    document = pdfium.PdfDocument(Path(pdf))

    # check if the PDF has any form fields
    has_form = False
    try:
        document.init_forms() # switches on pdfium's form-field support, off by default
        has_form = document.get_formtype() != raw.FORMTYPE_NONE
    except Exception:
        pass

    pages, fields = [], []
    try:
        for index in range(len(document)): # loop through PDF pages
            page = document[index]
            width, height = page.get_size()
            text = page.get_textpage().get_text_range() # the embedded text, if the PDF has any

            pages.append({"page": index + 1, 
                          "width": round(width), 
                          "height": round(height),
                          "text": text, 
                          "chars": len(text.strip())})
            if has_form:
                fields += get_page_fields(document, index)
    finally:
        document.close() # free the file from memory

    text_total = sum(page["chars"] for page in pages)

    return {"document": str(pdf),       # the path the user passed in, not the absolute path
            "pages": len(pages),        # the number of pages in the PDF 
            "has_form": has_form,       # whether the PDF has any interactive form fields at all
            "n_fields": len(fields),    # the number of distinct form fields, not the number of widgets
            "text_chars": text_total,   # the number of characters in the embedded text, not counting whitespace
            "page_details": pages,      # one dict per page, with size, text, and character count
            "fields": fields}           # one dict per field, with name, type, tooltip, value, options, page, and widget boxes

def pdf_description_to_markdown(description: dict) -> str:
    """
    Renders an `inspect_pdf` result as a markdown.

    # Arguments
    - `description`: the dict returned by `inspect_pdf`.

    # Returns
    The markdown text.
    """
    lines = [f'# {Path(description["document"]).stem.replace("_", " ")}', "",
             f'- **File path:** `{description["document"]}`', "",
             f'- **Pages:** {description["pages"]}', "",
             f'- **Text characters:** {description["text_chars"]}', "",
             f'- **Form fields:** {description["n_fields"]}' if description["has_form"] else "- **Form fields:** none", ""]

    for page in description["page_details"]:
        if page["text"].strip():
            lines += [f'## Page {page["page"]} — Text', "", page["text"].strip(), ""]

    if description["fields"]:
        lines += ["## Form fields", "",
                  "| # | Field | Type | State | Required | Tooltip | Value | Options | Page |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for number, field in enumerate(description["fields"], 1):
            options = field["options"]
            # option 0 is usually the "please choose" placeholder, so preview from the second
            preview = f'{";".join(o.strip() for o in options) if options else ""}'
            boxes = f' ({len(field["widgets"])} Fields)' if len(field["widgets"]) > 1 else ""
            lines.append(f'| {number} | {field["name"]}{boxes} | {field["type"]} '
                         f'| {field["state"]} | {"yes" if field["required"] else "no"} '
                         f'| {field["tooltip"]} | {(field["value"] or "").strip()} '
                         f'| {preview} | {field["page"]} |')
        lines.append("")

    return "\n".join(lines)

def extract_pdf(pdf: str | Path, out_dir: str | Path) -> Path:
    """
    Extracts a born-digital PDF without any model.

    # Arguments
    - `pdf`: path to the PDF.
    - `out_dir`: directory for the two output files.

    # Returns
    Path of the written markdown file. A `<name>.form.json` sits next to it with the
    machine-readable version, including positions.
    """
    target = Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)
    description = get_pdf_description(pdf)

    name = Path(pdf).name.strip().replace(" ", "_")
    (target / f"{name}.md").write_text(pdf_description_to_markdown(description), encoding="utf-8")
    (target / f"{name}.form.json").write_text(
        json.dumps(description, ensure_ascii=False, indent=2), encoding="utf-8")
    return target / f"{name}.md"

# if __name__ == "__main__":
#     script_dir = Path.cwd()
#     examples_dir = script_dir / "prototype/examples/Mutterschutz_20-22Uhr"
#     a = get_pdf_description(examples_dir / "Antrag Arbeitgeber § 28 MuSchG RP Darmstadt 2022.pdf")
#     b = pdf_description_to_markdown(a)

#     with open("output.md", "w", encoding="utf-8") as f:
#         f.write(b)

