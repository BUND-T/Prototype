"""
Tests for the born-digital extraction.

Everything runs against `assets/test_form.pdf`, a fixture built once by
`assets/make_test_form.py`. It contains two pages of text, a drawn table, and form fields
covering every readable type, all three states, both required values, options, tooltips,
prefilled values, a radio group of two widgets, and one field name repeated on page 2.

Uncovered on purpose: `pushbutton`, `signature` and `unknown` — reportlab cannot create
those, so no fixture can exercise them.
"""
import pytest
from pathlib import Path
from prototype.text_extraction import get_pdf_description, pdf_description_to_markdown, extract_pdf

TEST_PATH = Path(__file__).parent / "assets"
FORM = TEST_PATH / "test_form.pdf"

@pytest.fixture(scope="module")
def description():
    """ Reads the fixture once and hands the same result to every test. """
    assert FORM.exists(), f"missing fixture — run: uv run --with reportlab python {FORM.parent / 'make_test_form.py'}"
    return get_pdf_description(FORM)

@pytest.fixture(scope="module")
def field_name_dict(description):
    """ The fields keyed by (name, page) — the name alone is not unique across pages. """
    return {(field["name"], field["page"]): field for field in description["fields"]}


# --- the document as a whole ---------------------------------------------------------------
def test_document_summary(description):
    assert description["pages"] == 2
    assert description["has_form"] is True
    assert description["n_fields"] == 10, [f["name"] for f in description["fields"]]
    assert description["text_chars"] > 300, "the static text must be extracted, not just the fields"

def test_static_text_is_extracted_per_page(description):
    """ Text objects are read straight from the PDF — headings, paragraphs and table cells. """
    page_one, page_two = (page["text"] for page in description["page_details"])

    assert "Bund/t Testformular" in page_one
    assert "§ 1 Absatz 2" in page_one, "paragraph signs and umlauts must survive decoding"
    assert "Seite 2" in page_two and "seitenweise" in page_two

def test_table_cells_are_extracted_as_text(description):
    """
        A PDF has no table object — a table is text plus drawn lines. The cell contents are
        therefore readable, the grid itself is not.
    """
    page_one = description["page_details"][0]["text"]
    for cell in ("Feld", "Wert", "Ort", "Berlin", "Postleitzahl", "10115"):
        assert cell in page_one, cell


# --- field types ---------------------------------------------------------------------------

def test_every_field_type_in_the_fixture_is_named_correctly(field_name_dict):
    """ The type comes from a number; a hand-written mapping once shifted every entry by one. """
    assert field_name_dict[("Name", 1)]["type"] == "textfield"
    assert field_name_dict[("Einverstanden", 1)]["type"] == "checkbox"
    assert field_name_dict[("Status", 1)]["type"] == "radio"
    assert field_name_dict[("Landkreis", 1)]["type"] == "combobox"
    assert field_name_dict[("Auswahlliste", 2)]["type"] == "listbox"

def test_no_field_falls_through_the_type_mapping(description):
    assert all(field["type"] != "?" for field in description["fields"])


# --- state and required ---------------------------------------------------------------------

def test_all_three_states_are_recognised(field_name_dict):
    """
        Two different PDF flag sets feed this: the annotation flags say whether the box is
        drawn, the form flags whether it can be filled in.
    """
    assert field_name_dict[("Name", 1)]["state"] == "visible"
    assert field_name_dict[("NurLesbar", 1)]["state"] == "readonly"
    assert field_name_dict[("Versteckt", 1)]["state"] == "hidden"

def test_a_readonly_field_still_carries_its_value(field_name_dict):
    """ Read-only is not empty — the § 28 MuSchG form fills such fields from a dropdown. """
    assert field_name_dict[("NurLesbar", 1)]["value"] == "vom System gesetzt"

def test_required_is_read_from_the_field_flags(field_name_dict):
    assert field_name_dict[("Name", 1)]["required"] is True
    assert field_name_dict[("Vorbelegt", 1)]["required"] is False
    assert field_name_dict[("Datum", 2)]["required"] is True


# --- values, tooltips, options ---------------------------------------------------------------

def test_tooltip_and_prefilled_value_are_read(field_name_dict):
    field = field_name_dict[("Vorbelegt", 1)]
    assert field["tooltip"] == "bereits ausgefuellt"
    assert field["value"] == "Musterwert"

def test_choice_values_are_read_for_both_choice_types(field_name_dict):
    """
        The options are the counterpart of a FIM Codeliste. Passing pdfium no form handle
        returns -1 instead of raising, which silently produced empty lists.
    """
    assert field_name_dict[("Landkreis", 1)]["options"] == \
        ["Bitte waehlen", "Darmstadt", "Offenbach", "Bergstrasse"]
    assert field_name_dict[("Auswahlliste", 2)]["options"] == ["A", "B", "C"]

def test_fields_without_choices_have_no_options(field_name_dict):
    assert field_name_dict[("Name", 1)]["options"] == []


# --- grouping ---------------------------------------------------------------------------------

def test_a_radio_group_is_one_field_with_two_widgets(field_name_dict):
    """ Two boxes, one name, one value — listing them separately would invent a question. """
    status = field_name_dict[("Status", 1)]
    assert len(status["widgets"]) == 2
    assert status["type"] == "radio"

def test_grouping_happens_per_page(description, field_name_dict):
    """ The same name on two pages stays two entries, because position matters. """
    named = [field for field in description["fields"] if field["name"] == "Name"]
    assert len(named) == 2
    assert {field["page"] for field in named} == {1, 2}
    assert field_name_dict[("Name", 1)] is not field_name_dict[("Name", 2)]

def test_widget_boxes_are_page_coordinates(field_name_dict):
    """ PDF coordinates start bottom-left and are measured in points; A4 is 595 x 842. """
    left, bottom, right, top = field_name_dict[("Name", 1)]["widgets"][0]
    assert 0 < left < right < 595 and 0 < bottom < top < 842


# --- markdown ------------------------------------------------------------------------------

def test_markdown_reports_the_summary(description):
    markdown = pdf_description_to_markdown(description)
    assert markdown.startswith("# ")
    assert "**Pages:** 2" in markdown
    assert "**Form fields:** 10" in markdown

def test_markdown_contains_the_page_text(description):
    markdown = pdf_description_to_markdown(description)
    assert "## Page 1 — Text" in markdown and "## Page 2 — Text" in markdown
    assert "Bund/t Testformular" in markdown
    assert "Postleitzahl" in markdown, "table cells must reach the reader"

def test_markdown_has_one_row_per_field(description):
    """ The table is the part a person audits against the paper form. """
    markdown = pdf_description_to_markdown(description)
    header = "| # | Field | Type | State | Required | Tooltip | Value | Options | Page |"
    assert header in markdown

    rows = [line for line in markdown.splitlines()
            if line.startswith("| ") and line[2:3].isdigit()]
    assert len(rows) == description["n_fields"]

def _table_row(markdown: str, field_name: str) -> str:
    """
        The table row for one field.

        Searching the whole markdown would hit the page text first — the form prints
        "Landkreis:" as a label long before the table lists the field.
    """
    rows = [line for line in markdown.splitlines()
            if line.startswith("| ") and f'| {field_name}' in line]
    assert len(rows) == 1, f"expected one table row for {field_name}, found {len(rows)}"
    return rows[0]

def test_markdown_shows_state_required_and_options(description):
    markdown = pdf_description_to_markdown(description)

    readonly_row = _table_row(markdown, "NurLesbar")
    assert "readonly" in readonly_row and "vom System gesetzt" in readonly_row

    assert "| yes |" in _table_row(markdown, "Datum")

    hidden_row = _table_row(markdown, "Versteckt")
    assert "hidden" in hidden_row and "| no |" in hidden_row

    options_row = _table_row(markdown, "Landkreis")
    assert "Darmstadt" in options_row and "Offenbach" in options_row

def test_markdown_marks_a_group_with_its_widget_count(description):
    markdown = pdf_description_to_markdown(description)
    assert "(2 Fields)" in _table_row(markdown, "Status")


# --- writing the files -----------------------------------------------------------------------

def test_extract_pdf_writes_markdown_and_json(tmp_path):
    """ Both outputs land next to each other and describe the same document. """
    import json

    output = extract_pdf(FORM, tmp_path)
    sidecar = output.parent / f"{FORM.name}.form.json"

    assert output.exists() and sidecar.exists()
    assert output.name == f"{FORM.name}.md", "the source name is kept, extension included"

    data = json.loads(sidecar.read_text("utf-8"))
    assert data["n_fields"] == 10
    assert len(data["fields"]) == 10
    assert "Bund/t Testformular" in output.read_text("utf-8")

def test_spaces_in_the_filename_become_underscores(tmp_path):
    """ Output names must be safe to use in a shell and in a URL. """
    spaced = tmp_path / "Antrag mit Leerzeichen.pdf"
    spaced.write_bytes(FORM.read_bytes())

    output = extract_pdf(spaced, tmp_path / "out")
    assert output.name == "Antrag_mit_Leerzeichen.pdf.md"

if __name__ == "__main__":
    descr = get_pdf_description(FORM)
    field_names = {(field["name"], field["page"]): field for field in descr["fields"]}

    test_document_summary(descr)
    test_static_text_is_extracted_per_page(descr)
    test_table_cells_are_extracted_as_text(descr)

    test_every_field_type_in_the_fixture_is_named_correctly(field_names)
    test_no_field_falls_through_the_type_mapping(descr)

    test_all_three_states_are_recognised(field_names)
    test_a_readonly_field_still_carries_its_value(field_names)
    test_required_is_read_from_the_field_flags(field_names)

    test_tooltip_and_prefilled_value_are_read(field_names)
    test_choice_values_are_read_for_both_choice_types(field_names)
    test_fields_without_choices_have_no_options(field_names)

    test_a_radio_group_is_one_field_with_two_widgets(field_names)
    test_grouping_happens_per_page(descr, field_names)
    test_widget_boxes_are_page_coordinates(field_names)

    test_markdown_reports_the_summary(descr)
    test_markdown_contains_the_page_text(descr)
    test_markdown_has_one_row_per_field(descr)
    test_markdown_shows_state_required_and_options(descr)
    test_markdown_marks_a_group_with_its_widget_count(descr)

    test_extract_pdf_writes_markdown_and_json(TEST_PATH)