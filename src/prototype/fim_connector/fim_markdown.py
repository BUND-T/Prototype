import json

from pathlib import Path

from prototype.fim_connector.fim_api_extension import (NAMESPACE, get_child_value, get_node_identification,
                                get_node_in_XML)

# ---------------------------------------------------------------------
# XDF 3.0 → Markdown
#---------------------------------------------------------------------
""" 
The general structure of a xdf file is as follows:

<?xml version='1.0' encoding='utf-8'?>
<xdf3:xdatenfelder.stammdatenschema.0102 xmlns:xdf3="urn:xoev-de:fim:standard:xdatenfelder_3.0.0">
    <xdf3:header>
        <xdf3:nachrichtID>fimportal-export</xdf3:nachrichtID>
        <xdf3:erstellungszeitpunkt>2026-08-12T13:12:08.885944+00:00</xdf3:erstellungszeitpunkt>
    </xdf3:header>
    <xdf3:stammdatenschema>
        <xdf3:identifikation>
            <xdf3:id>S00000000362</xdf3:id>
            <xdf3:version>1.0.0</xdf3:version>
        </xdf3:identifikation>
        <xdf3:name>Antrag Beschäftigungserlaubnis bei Aufenthaltsgestattung Erteilung</xdf3:name>
        <xdf3:beschreibung>Originalwerte der XDF2-Datei:
				ID: S00000362
				Status: aktiv
				Zusätzliche intern übergebene Werte:
				Zugeordneter Dokumentsteckbrief: D00000575Antrag Beschäftigungserlaubnis Aufenthaltsgestattung Erteilung</xdf3:beschreibung>
        <xdf3:bezug link="https://www.gesetze-im-internet.de/asylvfg_1992/__61.html">§ 61 AsylG vom 15.07.2024</xdf3:bezug>
        <xdf3:bezug link="https://www.gesetze-im-internet.de/beschv_2013/__32.html">§ 32 BeschV vom 07.12.2023</xdf3:bezug>
        <xdf3:freigabestatus listURI="urn:xoev-de:xprozess:codeliste:status" listVersionID="2022-07-12">
            <code>6</code>
        </xdf3:freigabestatus>
        .
        .
        .
"""

TARGET_LOCATION = Path(__file__).parent.parent.parent.parent / "fim_data"

def _fields(struktur, depth: int = 0) -> list[str]:
    """ 
        Iterates struktur/enthaelt recursively.
        Returns a list of strings representing the fields and groups, with indentation based on depth. 
    """

    lines = []
    for wrapper in struktur.findall(NAMESPACE + "enthaelt"):
        for element in wrapper:
            type_tag = element.tag.split("}")[-1]
            anzahl = get_child_value(struktur, "anzahl", recursive=False)
            label = get_child_value(element, "bezeichnungEingabe", recursive=False) or get_child_value(element, "name", recursive=False)
            marker = "**Gruppe**" if type_tag == "datenfeldgruppe" else get_child_value(element, "feldart", recursive=False) or "Feld"
            lines.append(f"{'  ' * depth}- `{get_node_identification(element)}` {label} — {marker} ({anzahl})")
            for child in element.findall(NAMESPACE + "struktur"):
                lines += _fields(child, depth + 1)
    return lines

def to_markdown(xdf_path: Path, meta: dict | None = None) -> str:
    """
        Renders one XDF 3.0 schema file as markdown.

        # Arguments
        - `xdf_path`: path to a `schema.xdf.xml` as the FIM API delivers it.
        - `meta`: the harvest metadata next to it, for Reifegrad and source URL.

        # Returns
        The markdown text.
    """
    schema = get_node_in_XML(xdf_path, "stammdatenschema")
    # `find` should return None for anything that is not a Stammdatenschema
    if schema is None:
        raise ValueError(f"no <stammdatenschema> in {xdf_path} — expected an XDF 3.0 schema")

    meta = meta or {}
    title = get_child_value(schema, "bezeichnung", recursive=False) or get_child_value(schema, "name", recursive=False) or meta.get("name", "Ohne Titel")

    out = [f"# {title}", ""]
    out += [f"- **FIM-ID:** `{get_node_identification(schema)}`"]
    if meta.get("freigabe_status_label"):
        out.append(f"- **Reifegrad:** {meta['freigabe_status_label']}")
    for key, label in (("bezug", "Rechtsgrundlagen"),):
        values = [b.text.strip() for b in schema.findall(NAMESPACE + key) if b.text]
        if values:
            out.append(f"- **{label}:** {'; '.join(values)}")
    if meta.get("source_url"):
        out.append(f"- **Quelle:** {meta['source_url']} (abgerufen {meta.get('fetched_at', '?')})")

    if definition := get_child_value(schema, "definition", recursive=False):
        out += ["", "## Definition", "", definition]

    fields = [line for struktur in schema.findall(NAMESPACE + "struktur") for line in _fields(struktur)]
    if fields:
        out += ["", "## Feldstruktur", ""] + fields

    rules = schema.iter(NAMESPACE + "regel")
    rule_lines = []
    for rule in rules:
        if text := get_child_value(rule, "freitextRegel", recursive=False):
            rule_lines += [f"### `{get_node_identification(rule)}` — {get_child_value(rule, 'name', recursive=False)}", "", text, ""]
    if rule_lines:
        out += ["", "## Regeln", ""] + rule_lines

    return "\n".join(out) + "\n"

def convert_xdf_schemas(target_location: Path = TARGET_LOCATION) -> int:
    """ Converts every crawled schema to \\<target_location\\>\\<fim_id\\/\\<fim_id\\>.md. """

    out_dir = target_location
    out_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for meta_path in sorted((target_location).glob("*/meta.json")):
        meta = json.loads(meta_path.read_text("utf-8"))
        xdf = meta_path.parent / "schema.xdf.xml"
        if not xdf.exists():
            continue
        (out_dir / f"{meta['fim_id']}" / f"{meta['fim_id']}.md").write_text(to_markdown(xdf, meta), encoding="utf-8")
        written += 1
    return written

if __name__ == "__main__":
    print(f"Converted {convert_xdf_schemas()} schemas to markdown")
