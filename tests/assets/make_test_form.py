"""
Builds `test_form.pdf`, the fixture the extraction tests run against.

The PDF is committed, so the test suite needs no PDF-authoring library. Run this only when
the fixture has to change:

    uv run --with reportlab python tests/assets/make_test_form.py

Every property `inspect_pdf` can report appears at least once: both pages carry text, the
fields cover all readable types, all three states, both required values, options, tooltips,
prefilled values, one name on two widgets, and one name repeated on the second page.
"""

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

TARGET = Path(__file__).parent / "test_form.pdf"
WIDTH, HEIGHT = A4

def draw_table(pdf, x, y, rows, col_width=170, row_height=24):
    """ A PDF has no table object — a table is text plus lines, so we draw both. """
    for row_index, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            left = x + col_index * col_width
            top = y - row_index * row_height
            pdf.rect(left, top - row_height, col_width, row_height)
            pdf.drawString(left + 6, top - row_height + 7, cell)

def build():
    pdf = canvas.Canvas(str(TARGET), pagesize=A4)
    form = pdf.acroForm

    # ----- page 1 -------------------------------------------------------------------------
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(60, HEIGHT - 70, "Bund/t Testformular")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(60, HEIGHT - 95, "Test Antrag")
    pdf.drawString(60, HEIGHT - 110, "Rechtsgrundlage: § 1 Absatz 2")

    draw_table(pdf, 60, HEIGHT - 140, [["Feld", "Wert"],
                                       ["Ort", "Berlin"],
                                       ["Postleitzahl", "10115"]])

    pdf.drawString(60, HEIGHT - 240, "Name, Vorname:")
    form.textfield(name="Name", tooltip="Name, Vorname",
                   x=200, y=int(HEIGHT - 245), width=220, height=18,
                   fieldFlags="required", borderWidth=1)

    pdf.drawString(60, HEIGHT - 275, "Vorbelegtes Feld:")
    form.textfield(name="Vorbelegt", tooltip="bereits ausgefuellt", value="Musterwert",
                   x=200, y=int(HEIGHT - 280), width=220, height=18, borderWidth=1)

    pdf.drawString(60, HEIGHT - 310, "Vom System gesetzt:")
    form.textfield(name="NurLesbar", tooltip="wird automatisch befuellt",
                   value="vom System gesetzt",
                   x=200, y=int(HEIGHT - 315), width=220, height=18,
                   fieldFlags="readOnly", borderWidth=1)

    # never drawn, but still part of the form — must come back as state "hidden"
    form.textfield(name="Versteckt", tooltip="unsichtbares Feld", value="verborgen",
                   x=200, y=int(HEIGHT - 350), width=220, height=18,
                   annotationFlags="hidden")

    pdf.drawString(60, HEIGHT - 385, "Einverstanden:")
    form.checkbox(name="Einverstanden", tooltip="Zustimmung zur Verarbeitung",
                  x=200, y=int(HEIGHT - 390), size=16, checked=False, borderWidth=1)

    # one name, two widgets — a radio group is one question with two boxes
    pdf.drawString(60, HEIGHT - 420, "Status:")
    form.radio(name="Status", tooltip="Status der Person", value="schwanger",
               x=200, y=int(HEIGHT - 425), size=16, selected=False, borderWidth=1)
    pdf.drawString(225, HEIGHT - 420, "schwanger")
    form.radio(name="Status", tooltip="Status der Person", value="stillend",
               x=300, y=int(HEIGHT - 425), size=16, selected=False, borderWidth=1)
    pdf.drawString(325, HEIGHT - 420, "stillend")

    pdf.drawString(60, HEIGHT - 455, "Landkreis:")
    form.choice(name="Landkreis", tooltip="Bitte den Landkreis waehlen",
                options=["Bitte waehlen", "Darmstadt", "Offenbach", "Bergstrasse"],
                value="Bitte waehlen", x=200, y=int(HEIGHT - 460), width=220, height=20,
                fieldFlags="combo", borderWidth=1)

    # no pushbutton: reportlab's AcroForm cannot create one, so that type stays uncovered
    pdf.showPage()

    # ----- page 2 -------------------------------------------------------------------------
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(60, HEIGHT - 70, "Seite 2 — Weitere Angaben")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(60, HEIGHT - 95, "Diese Seite prueft die seitenweise Zuordnung.")

    # the same field name as on page 1: fields are grouped per page, so this is a second entry
    pdf.drawString(60, HEIGHT - 130, "Name, Vorname (Wiederholung):")
    form.textfield(name="Name", tooltip="Name, Vorname",
                   x=260, y=int(HEIGHT - 135), width=200, height=18, borderWidth=1)

    pdf.drawString(60, HEIGHT - 165, "Datum:")
    form.textfield(name="Datum", tooltip="Datum des Antrags",
                   x=260, y=int(HEIGHT - 170), width=200, height=18,
                   fieldFlags="required", borderWidth=1)

    pdf.drawString(60, HEIGHT - 200, "Auswahlliste:")
    form.listbox(name="Auswahlliste", tooltip="Liste zum Aufklappen",
                 options=["A", "B", "C"], value="A",
                 x=260, y=int(HEIGHT - 215), width=200, height=40, borderWidth=1)

    pdf.showPage()
    pdf.save()
    print(f"written: {TARGET}  ({TARGET.stat().st_size} bytes)")

if __name__ == "__main__":
    build()
