# test form

- **File path:** `c:\Users\Lreich\Documents\GitHub\Bewerbung\prototype\tests\assets\test_form.pdf`

- **Pages:** 2

- **Text characters:** 344

- **Form fields:** 10

## Page 1 — Text

Bund/t Testformular
Test Antrag
Rechtsgrundlage: § 1 Absatz 2
Feld Wert
Ort Berlin
Postleitzahl 10115
Name, Vorname:
Vorbelegtes Feld:
Vom System gesetzt:
Einverstanden:
Status: schwanger stillend
Landkreis:

## Page 2 — Text

Seite 2 — Weitere Angaben
Diese Seite prueft die seitenweise Zuordnung.
Name, Vorname (Wiederholung):
Datum:
Auswahlliste:

## Form fields

| # | Field | Type | State | Required | Tooltip | Value | Options | Page |
|---|---|---|---|---|---|---|---|---|
| 1 | Name | textfield | visible | yes | Name, Vorname |  |  | 1 |
| 2 | Vorbelegt | textfield | visible | no | bereits ausgefuellt | Musterwert |  | 1 |
| 3 | NurLesbar | textfield | readonly | no | wird automatisch befuellt | vom System gesetzt |  | 1 |
| 4 | Versteckt | textfield | hidden | no | unsichtbares Feld | verborgen |  | 1 |
| 5 | Einverstanden | checkbox | visible | yes | Zustimmung zur Verarbeitung | Off |  | 1 |
| 6 | Status (2 Fields) | radio | visible | yes | Status der Person | Off |  | 1 |
| 7 | Landkreis | combobox | visible | no | Bitte den Landkreis waehlen | Bitte waehlen | Bitte waehlen;Darmstadt;Offenbach;Bergstrasse | 1 |
| 8 | Name | textfield | visible | yes | Name, Vorname |  |  | 2 |
| 9 | Datum | textfield | visible | yes | Datum des Antrags |  |  | 2 |
| 10 | Auswahlliste | listbox | visible | no | Liste zum Aufklappen | A | A;B;C | 2 |
