import json, os, re, sys

from functools import lru_cache
from pathlib import Path

from paddleocr import PaddleOCRVL

# ---------------------------------------------------------------------
# text extraction
# 
# PaddleOCR-VL-1.6: 1.0B params, Apache-2.0, 96.33 on OmniDocBench v1.6.
# docs: http://www.paddleocr.ai/main/en/version3.x/pipeline_usage/PaddleOCR-VL.html
# 
# Strategy: 
# 1. Layout detection: the model returns a list of blocks in reading order, each with a label and a layout score.
# 2. VLM recognition: the model returns the text content of each block, along with its bounding box and other metadata.
# 3. Markdown rendering: the model renders the recognized text into markdown, preserving tables and formulas, and providing a machine-readable trail of the extraction process.

DEVICE = "gpu"  # gpu only: paddlex picks kernels off the build flag, so a cuda wheel needs a real gpu
LOWCONF_LAYOUT = 0.7   # layout score below this is marked in the markdown and logged in the confidence.json
RISK_LABELS = ("table", "image", "chart", "seal", "formula") # labels whose structure the model can plausibly get wrong, so we mark them even if the layout score is high

@lru_cache(maxsize=1) # caches the model weights and avoids reloading them on every call
def get_ocr_pipeline(device: str = DEVICE):
    """
        Layout detection + VLM recognition. First call downloads ~1GB of weights to ~/.paddlex.

        The orientation and unwarping models are loaded here even though the default pass runs
        without them: predict() can only switch on a stage the pipeline already built.
        We use them in the second pass to mark blocks whose text differs between the two readings.
    """
    if sys.platform == "win32":
        # paddle resolves cudnn64_9.dll off PATH, but the pip wheel drops it in site-packages.
        # On linux paddle depends on the same wheel and finds it via RPATH, so this is windows only.
        import nvidia.cudnn
        os.environ["PATH"] = f"{Path(nvidia.cudnn.__file__).parent / 'bin'}{os.pathsep}{os.environ['PATH']}"

    return PaddleOCRVL(device=device, use_doc_orientation_classify=True, use_doc_unwarping=True)

def extract_text(document: str | Path, device: str = DEVICE, **predict_kwargs) -> str:
    """
        Extracts an image / PDF / directory of pages to markdown, one chunk per page,
        with reading order, tables and formulas preserved.

        Scans and phone photos need the correction passes, they are off by default and
        cost one extra forward each: use_doc_orientation_classify=True, use_doc_unwarping=True.
    """
    return "\n\n".join(page.markdown["markdown_texts"]
                       for page in get_ocr_pipeline(device).predict(str(document), **predict_kwargs))

def _pretty_html(text: str) -> str:
    """
        Breaks PaddleOCR's single-line table HTML into one row and one cell per line for better readability.
    """
    if "<table" not in text:
        return text

    _ROW = re.compile(r"(</?(?:table|thead|tbody|tr)\b[^>]*>)") # breaks PaddleOCR's single-line table HTML into one row per line
    _CELL = re.compile(r"(<t[dh]\b[^>]*>)") # breaks PaddleOCR's single-line table HTML into one cell per line
    
    text = text.replace("\\n", "<br>") # PaddleOCR uses "\n" for line breaks, but the markdown renderer needs "<br>" to render them.
    broken = _CELL.sub(r"\n  \1", _ROW.sub(r"\n\1", text))
    return "\n".join(line.rstrip() for line in broken.split("\n") if line.strip())

HIGHLIGHT = "border:3px solid #c9a227; background:#fff8dc;"

def _run(document: str | Path, device: str, **predict_kwargs) -> list[tuple[dict, str]]:
    """ One OCR pass: (result dict, rendered markdown) per page. """
    return [(page.json["res"], page.markdown["markdown_texts"])
            for page in get_ocr_pipeline(device).predict(str(document), **predict_kwargs)]

def _plain(text: str) -> str:
    """ Tags and whitespace stripped, so the two passes are compared on characters alone. """
    return " ".join(re.sub(r"<[^>]+>", " ", text or "").split())

def _counterpart(block: dict, blocks: list[dict]) -> dict | None:
    """
        The block from the second pass covering the same area, by best box overlap.

        Unwarping shifts coordinates slightly and can merge or split blocks, so the match is
        by overlap rather than by index; below half overlap we call it missing rather than
        compare two unrelated blocks.
    """
    ax1, ay1, ax2, ay2 = block["block_bbox"]
    area = max((ax2 - ax1) * (ay2 - ay1), 1)
    best, best_overlap = None, 0.0
    for candidate in blocks:
        bx1, by1, bx2, by2 = candidate["block_bbox"]
        wide = max(0, min(ax2, bx2) - max(ax1, bx1))
        high = max(0, min(ay2, by2) - max(ay1, by1))
        overlap = wide * high / area
        if overlap > best_overlap:
            best, best_overlap = candidate, overlap
    return best if best_overlap >= 0.5 else None

def _mark_block(md: str, block_content: str, reason: str) -> tuple[str, bool]:
    """
        Marks a whole layout block in the markdown, not one line inside it.

        Plain text blocks appear verbatim and get wrapped in <mark>. Tables do not — the
        renderer rewrites the opening tag — so the yellow goes onto the <table> element
        itself as a border. Marking a single cell was worse than useless: on the Mutterschutz
        form the mark landed on the consent clause while the OCR error sat two rows above,
        which reads as "this part was checked".

        Returns the markdown and whether the mark was placed.
    """
    text = (block_content or "").strip()
    if not text:
        return md, False

    if not text.startswith("<table"):
        if text in md:
            return md.replace(text, f'<mark title="{reason}">{text}</mark>', 1), True
        return md, False

    # locate which rendered table this block became, via a cell that survived the rewrite
    anchor = _anchor(text, md)
    if not anchor:
        return md, False
    start = md.rfind("<table", 0, md.find(anchor))
    if start < 0:
        return md, False
    end = md.find(">", start)
    if end < 0:
        return md, False

    tag = md[start:end + 1]
    if "style=" in tag:                      # merge into the renderer's own style attribute
        marked_tag = re.sub(r"style=(['\"])(.*?)\1",
                            lambda m: f'style={m.group(1)}{m.group(2)} {HIGHLIGHT}{m.group(1)}',
                            tag, count=1)
    else:
        marked_tag = tag[:-1] + f' style="{HIGHLIGHT}">'
    marked_tag = marked_tag[:-1] + f' title="{reason}">'
    return md[:start] + marked_tag + md[end + 1:], True

def _anchor(block_content: str, md: str) -> str:
    """
        Returns the longest line of a block that survives into the markdown, or returns "", if `block_content` is not found in `md`.

        PaddleOCR VL's markdown renderer reshapes tables and formulas, so the block text never matches verbatim.
        As we want to mark unsure or high risk extractions, we need to find a line that is present in the rendered markdown. 
        The longest line is chosen as it is likely to be the most specific and unique, reducing the chance of marking the wrong text. 

        # Example:
            - PaddleOCR block: `<table><tr><td colspan="5">Beurteilung der Arbeitsbedingungen:</td></tr>…`
            - Rendered markdown: `<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">Beurteilung der Arbeitsbedingungen:</td></tr>…`

            In this case, the block content does not match the markdown verbatim, but the line "Beurteilung der Arbeitsbedingungen:" is present in both.
    """
    # every tag becomes a newline, so "<td>Ort</td><td>Berlin</td>" falls apart into the cell
    # texts instead of one run-together string; `or ""` covers blocks with no content at all
    lines = (line.strip() for line in re.sub(r"<[^>]+>", "\n", block_content or "").split("\n"))

    # keep only cells that actually appear in the rendered markdown — the renderer reformats
    # the table around them but leaves the cell text alone. 
    # >12 chars because short cells ("ja", "Ort", a date) recur all over the page and would anchor the mark to the wrong one
    candidates = [line for line in lines if len(line) > 12 and line in md]
    # longest wins: the most specific match, so the <mark> lands in the intended table.
    # default="" means "found nothing"
    return max(candidates, key=len, default="")

def extract_to_markdown(document: str | Path, out_dir: str | Path, threshold: float = LOWCONF_LAYOUT,
                        risk_labels: tuple[str, ...] = RISK_LABELS, dual_pass: bool = True,
                        device: str = DEVICE, **predict_kwargs) -> Path:
    """
        Extracts one `document` to \\<name\\>.md, wrapping every risky block in \\<mark\\> so it
        renders yellow, and writes the machine-readable trail to \\<name\\>.confidence.json.

        Risky means: 
            - layout score below `threshold`, or 
            - a block label whose structure the model can plausibly get wrong. 
        
        # Arguments
        - `document`: path to a PDF, image, or directory of pages.
        - `out_dir`: directory to write the markdown and confidence.json to.
        - `threshold`: layout score below which a block is marked. Default: 0.
        - `risk_labels`: block labels whose structure the model can plausibly get wrong, so they are marked even if the layout score is high. Default: ("table", "image", "chart", "seal", "formula").
        - `dual_pass`: read the document twice and mark blocks whose text differs. Doubles runtime.
        - `device`: "cpu" or "gpu".

        A marked block is marked whole: text blocks are wrapped in \\<mark\\>, tables get a
        yellow border on the \\<table\\> element. Marking a single cell inside a table, as an
        earlier version did, pointed the reader at an arbitrary row and read as "checked" —
        on the Mutterschutz form the mark sat on the consent clause while the misread word
        was two rows above.

        With `dual_pass` the document is read a second time with orientation and unwarping
        correction on, and blocks whose text differs between the two readings are marked too.
        That disagreement is the only character-level signal available, because PaddleOCR-VL
        exposes no token confidence — the layout score says nothing about the characters.
    """
    if not Path(document).exists(): raise FileNotFoundError(document)

    target = Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)

    # the pipeline carries the correction stages; the first pass explicitly declines them so
    # the two passes actually read the page differently
    first = _run(document, device, **{"use_doc_orientation_classify": False,
                                      "use_doc_unwarping": False, **predict_kwargs})
    # Second pass with the correction stages on. Where the two readings of the same block
    # disagree, the recognition is unsure — the only character-level signal this pipeline
    # offers, since the VLM exposes no token logprobs. Costs one extra forward per block.
    second = _run(document, device, **{**predict_kwargs, "use_doc_orientation_classify": True,
                                       "use_doc_unwarping": True}) if dual_pass else []

    pages, flagged = [], []
    for page_no, (res, md) in enumerate(first):
        other = second[page_no][0]["parsing_res_list"] if page_no < len(second) else None
        scores = {box["order"]: box["score"] for box in res["layout_det_res"]["boxes"]} # dict of block_order -> layout score, for marking low-confidence blocks

        # labels the markdown renderer drops, so we don't mark them even if they are low-confidence or high-risk
        # Examples include "page_number" and "header" which are not part of the document content.
        dropped = set(res["model_settings"].get("markdown_ignore_labels") or ()) 

        # PaddleOCR VL's layout detector returns a list of blocks in reading order, each with a label and a layout score.
        # Example of such blocks are: "text", "title", "caption", "table", "formula", "image", "chart", "seal", etc.
        # We iterate over these blocks, and for each block we check if it is risky (low layout score or high-risk label). 
        # If it is risky, we mark it in the markdown and add it to the flagged list with its details (span, score, bbox, page, label, reason, marked).
        for block in res["parsing_res_list"]:
            score = scores.get(block["block_order"])
            label = block["block_label"]

            if label in dropped:
                continue

            # Determine the reason for marking the block. 
            # If the label is in risk_labels, we mark it as "Structure: <label>". 
            # If the score that a block is correctly classified (e.g. "text", "title", etc.) is below the threshold, we mark it as "Low block type score". 
            # If neither condition is met, this block is not marked.
            reasons = []
            if label in risk_labels:
                reasons.append("Structure: " + label)
            if score is None or score < threshold:
                reasons.append("Low block type score")

            text = (block["block_content"] or "").strip() # remove leading/trailing whitespace from the block content, as it may interfere with finding the text in the markdown
            if other is not None:
                twin = _counterpart(block, other)
                if twin is None:
                    reasons.append("Block missing in second pass")
                elif _plain(twin["block_content"]) != _plain(text):
                    reasons.append("Text differs between passes")

            if not reasons:
                continue
            reason = "; ".join(reasons)

            md, marked = _mark_block(md, text, reason)

            # a list, not a string: JSON escapes newlines inside a string, so a prettified
            # span would still sit on one physical line — and a longer one. An array with
            # indent=2 puts each line of the table on its own line in the file.
            flagged.append({"span": _pretty_html(text).split("\n"), "score": score,
                            "bbox": block["block_bbox"],
                            "page": res.get("page_index"), "label": label, "reason": reason, "marked": marked})
        # prettified only after all marking on this page is done — the anchor lookup above
        # matches against the renderer's own output and must see it unchanged
        pages.append(_pretty_html(md))

    # Write the markdown and confidence.json to the target directory.
    name = Path(document).name.strip().replace(" ", "_")
    (target / f"{name}.md").write_text("\n\n".join(pages), encoding="utf-8")
    (target / f"{name}.confidence.json").write_text(
        json.dumps({"document": str(document), "threshold": threshold,
                    "risk_labels": list(risk_labels),
                    "flagged": flagged}, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # return only the path to the markdown file as the main output for further processing
    return target / f"{name}.md"


script_dir = Path.cwd()
examples_dir = script_dir / "prototype/examples/Mutterschutz_20-22Uhr"
extract_to_markdown(examples_dir / "Antrag Arbeitgeber § 28 MuSchG RP Darmstadt 2022.pdf", examples_dir)