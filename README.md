# Prototype

Working prototype for **BUND/T**. It reads the approved FIM Bestand from the
FIM-Portal API and compiles each Stammdatenschema into a machine-readable
application graph plus a German, plain-language guide for an AI copilot.

This repository is the current status quo, not a product. It covers one of the
two directions the concept describes: **FIM → usable application**. The other
direction, Handlungsgrundlage → FIM draft, is the open work.

## Extracted data

**The extracted data lives in [`fim_data/`](fim_data).** One directory per
Datenschema, 107 in total, each named by its FIM-ID:

| File | What it is |
|---|---|
| `meta.json` | FIM-ID, version, Freigabestatus, Dokumentsteckbrief, Handlungsgrundlagen (`bezug`), rule count, source URL |
| `schema.xdf.xml` | raw XDatenfelder export, exactly as the FIM API delivers it |
| `graph.json` | the compiled application graph: fields, groups, containment, conditional edges |
| `graph.mmd` | the same graph as a Mermaid flowchart, for reading it by eye |
| `SKILL.md` | German instructions for an AI copilot: every field, its Hilfetext, its Rechtsgrundlage, and the rules that gate it |
| `<FIM-ID>.md` | the schema rendered as readable markdown |

All 107 are approved schemas (silber or gold) in XDF 3.0.

## Layout

```
src/prototype/
  fim_connector/
    fim_api_extension.py   FIM-Portal API client: schemas, fields, groups, translated rules
    fim_crawl.py           downloads approved schemas into fim_data/
    fim_markdown.py        renders a schema as markdown
  graph.py                 XDatenfelder -> application graph (containment + condition edges)
  rule_parser.py           reads FIM Regeln, both the translated-rules API and free-text German
  skill.py                 graph -> SKILL.md
  text_extraction.py       PDF -> text and form fields, via pdfium
  old_OCR.py               inactive OCR path, kept for reference
tests/                     53 tests, no network access needed
```

## Running it

Requires Python 3.13+.

```bash
uv sync
uv run pytest
```

Recrawl the corpus from the portal:

```bash
uv run python -m prototype.fim_connector.fim_crawl
```

## Known limits

These are measured, not guessed:

- **XDF 3.0 only.** `fim_crawl` reads the 3.0 namespace, so approved schemas
  still published as XDF 2.0 are skipped. The portal offers a converter; taking
  that path is the single largest coverage win available.
- **`feldart` and `datentyp` are not read.** Both are code-wrapped in XDF 3.0
  and `graph.py` reads the element text instead, so every field in every
  `graph.json` carries an empty `feldart`. This has to be fixed before anything
  can be rendered as a real form.
- **No Formularfeld to FIM-Datenfeld mapping.** `text_extraction.py` produces
  field lists from PDFs, but nothing maps them onto FIM elements yet. This is
  the central open work item.
- **No XDatenfelder emitter.** The prototype reads FIM, it does not yet write
  it.
- **OCR is inactive.** `old_OCR.py` is kept for reference only. It needs
  PaddleOCR and a CUDA GPU, neither of which is a dependency of this project;
  install them separately if you want to revive that path. Most source forms
  are born-digital PDFs, so pdfium handles them without OCR.
