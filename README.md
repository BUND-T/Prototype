# Prototype

Kompiliert freigegebene **FIM-Stammdatenschemata** zu maschinenlesbaren
Antragsgraphen und zu Anleitungen in einfacher Sprache, denen ein KI-Copilot
folgen kann.

Das ist der aktuelle Stand von **BUND/T**, kein fertiges Produkt.

## Warum

Verwaltungsleistungen in Deutschland werden über einen bundesweiten Standard
beschrieben: FIM, das Föderale Informationsmanagement. Der Standard ist richtig,
und die darauf aufbauende Redaktionskaskade ist es auch. Der Bund modelliert
eine Leistung aus dem Recht, die Länder verfeinern, die Kommunen ergänzen das
Ortsspezifische. Das Problem ist, dass die Kaskade weitgehend leer ist. Rund
4.000 freigegebenen Leistungssteckbriefen stehen etwa 700 freigegebene
Datenschemata gegenüber, also ein Schema je sechs Leistungen, weil
Stamminformationen bis heute von Hand entstehen.

Wo oben nichts veröffentlicht ist, baut unten jede Behörde ihre eigene Fassung.
BUND/T setzt an beiden Enden dieser Kette an:

- **Compiler** — erzeugt FIM-Entwürfe aus den Handlungsgrundlagen und dem
  bestehenden FIM-Bestand, mit Herkunftsnachweis an jedem Element.
- **Engine** — rendert jedes freigegebene Schema zu einem barrierefreien
  Antrag, den Bürgerinnen und Bürger tatsächlich ausfüllen können.

## Was dieses Repository heute zeigt

Die **Engine-Richtung**: FIM hinein, nutzbare Antragsstruktur heraus.

- Ein funktionierender Client gegen die API des FIM-Portals und ein Crawler, der
  freigegebene Schemata nach `fim_data/` lädt.
- **107 Datenschemata kompiliert** zu Antragsgraphen: Felder, Gruppen,
  Enthaltensein und die bedingten Kanten, die entscheiden, welche Frage wann
  erscheint.
- **93 % der hinterlegten Regeln sicher geparst**, über die
  `translated-rules`-API der FITKO, wo vorhanden, und über eine Grammatik für
  die deutschen Freitextregeln für den Rest.
- Eine `SKILL.md` je Leistung: jedes Feld in verständlichem Deutsch mit
  Hilfetext und Rechtsgrundlage, dazu die Regeln, die es steuern. Damit kann ein
  Copilot durch den Antrag führen, ohne etwas zu erfinden.
- Extraktion von PDFs zu Text und strukturierten Formularfeldern, über pdfium.

Noch nicht enthalten und der Kern der weiteren Arbeit: die
**Compiler-Richtung**, von der Rechtsquelle zum FIM-Entwurf.

## Extrahierte Daten

**Die extrahierten Daten liegen unter [`fim_data/`](fim_data).** Ein Verzeichnis
je Datenschema, insgesamt 107, benannt nach der jeweiligen FIM-ID:

| Datei | Inhalt |
|---|---|
| `meta.json` | FIM-ID, Version, Freigabestatus, Dokumentsteckbrief, Handlungsgrundlagen (`bezug`), Regelanzahl, Quell-URL |
| `schema.xdf.xml` | roher XDatenfelder-Export, genau so, wie die FIM-API ihn liefert |
| `graph.json` | der kompilierte Antragsgraph: Felder, Gruppen, Enthaltensein, bedingte Kanten |
| `graph.mmd` | derselbe Graph als Mermaid-Flowchart, zum Ansehen |
| `SKILL.md` | Anleitung für einen KI-Copiloten: jedes Feld, sein Hilfetext, seine Rechtsgrundlage und die Regeln, die es steuern |
| `<FIM-ID>.md` | das Schema als lesbares Markdown |

Alle 107 sind freigegebene Schemata (silber oder gold) im Format XDF 3.0.

## Aufbau

```
src/prototype/
  fim_connector/
    fim_api_extension.py   Client für die FIM-Portal-API: Schemata, Felder, Gruppen, übersetzte Regeln
    fim_crawl.py           lädt freigegebene Schemata nach fim_data/
    fim_markdown.py        rendert ein Schema als Markdown
  graph.py                 XDatenfelder -> Antragsgraph (Enthaltensein + bedingte Kanten)
  rule_parser.py           liest FIM-Regeln, sowohl über die translated-rules-API als auch aus deutschem Freitext
  skill.py                 Graph -> SKILL.md
  text_extraction.py       PDF -> Text und Formularfelder, über pdfium
  OCR.py                   inaktiver OCR-Pfad
tests/                     Tests
```

## Ausführen

Benötigt Python 3.13 oder neuer.

```bash
uv sync
uv run pytest
```

Den Korpus neu vom Portal laden:

```bash
uv run python -m prototype.fim_connector.fim_crawl
```

## Bekannte Grenzen

Diese sind gemessen, nicht geschätzt:

- **Nur XDF 3.0.** `fim_crawl` liest den 3.0-Namensraum, freigegebene Schemata
  im älteren Format XDF 2.0 werden deshalb übersprungen. Das Portal bietet einen
  Konverter an; dieser Weg ist der größte verfügbare Zugewinn an Abdeckung.
- **`feldart` und `datentyp` werden nicht gelesen.** Beide sind in XDF 3.0 in
  ein `code`-Element gewickelt, `graph.py` liest stattdessen den Elementtext.
  Dadurch trägt jedes Feld in jeder `graph.json` eine leere `feldart`. Das muss
  behoben sein, bevor sich daraus ein echtes Formular rendern lässt.
- **Keine Zuordnung von Formularfeldern zu FIM-Datenfeldern.**
  `text_extraction.py` liefert Feldlisten aus PDFs, aber nichts bildet sie auf
  FIM-Elemente ab. Das ist der zentrale offene Arbeitspunkt.
- **Kein XDatenfelder-Emitter.** Der Prototyp liest FIM, er schreibt es noch
  nicht.
- **OCR ist inaktiv.** `OCR.py` liegt nur zur Referenz bei. Es benötigt
  PaddleOCR und eine CUDA-GPU, beides ist keine Abhängigkeit dieses Projekts.
  Wer den Pfad wiederbeleben will, installiert es separat. Die meisten
  Ausgangsformulare sind digital erzeugte PDFs, pdfium reicht dafür aus.

## Wie es weitergeht

1. **Compiler-Prototyp** — von der Handlungsgrundlage zu einem validen
   XDatenfelder- und XZuFi-Entwurf mit Herkunftsnachweis je Feld. Gemessen über
   einen Rekonstruktionstest: freigegebene Schemata werden aus dem Pool
   zurückgehalten, allein aus ihren Rechtsquellen neu erzeugt und gegen das
   Original bewertet.
2. **Engine-MVP** — generisches Rendering beliebiger freigegebener Schemata im
   KERN-Designsystem, schemagebundener Copilot, Einreichung über FIT-Connect.
3. **Pilot mit einer Redaktion** — Ende-zu-Ende von der Rechtsquelle bis zum
   eingereichten Antrag, gemessen an der Durchlaufzeit bis zur freigegebenen
   Stamminformation.

Der Compiler umgeht die FIM-Governance nicht. Die methodische und die fachliche
Freigabe bleiben bei der zuständigen Stelle. Der Zweck ist, ihr Entwürfe zu
liefern, die prüffähig ankommen.
