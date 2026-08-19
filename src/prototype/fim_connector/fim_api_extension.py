import json, re
import xml.etree.ElementTree as ET
import urllib.error, urllib.parse, urllib.request
from functools import lru_cache
from pathlib import Path

"""
This file provides helper functions to extract information from the FIM .xml files.
Although the FIM portal API provides many functions to queury data for a given schema, it does for example not provide a function to get all the datagroups and fields for a schema.
This file provides functions to extract this information from the .xml files.
"""

BASE = "https://fimportal.de"
UA = "prototype/0.1 (Bund/t)" # User-Agent header for polite crawling
APPROVED = (5, 6) # freigabe_status values that indicate a schema is approved
NAMESPACE = "{urn:xoev-de:fim:standard:xdatenfelder_3.0.0}" # The namespace used in the XDF XML files. All elements are prefixed with this namespace.

# ----------------------------------------------------------------------------------------------------
# API calls to the FIM portal
# ----------------------------------------------------------------------------------------------------

def _GET(path: str):
    """ GET request of the form `https://fimportal.de/path` from the FIM portal API, returning JSON or raw text. """

    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA}) # HTTP request with polite User-Agent

    # returns response body as JSON or raw text
    with urllib.request.urlopen(req, timeout=180) as resp:
        body = resp.read()
    try:
        return json.loads(body)
    except json.JSONDecodeError as e:
        print(f"JSON decode error for {path}: {e}")
        return body.decode("utf-8", "replace")

def get_latest_schema_version(fim_id: str) -> str:
    """ Returns the latest version of a schema given its fim_id. """
    schemas = _GET(f"/api/v1/schemas/{fim_id}")

    latest_version = "0"
    for schema in schemas:
        # versions are of the form X.Y.Z, so we compare each number seperately begining from the first number. E.g. 0.10.1 < 1.0.0
        latest_version_tuple = tuple(map(int, latest_version.split(".")))
        version = schema.get("fim_version", "")
        version_tuple = tuple(map(int, version.split(".")))

        for i, version_prefix in enumerate(version_tuple):
            if int(version_prefix) > int(latest_version_tuple[i]):
                latest_version = version
                break

    return latest_version

def get_approved_schemas(call_limit: int = 100):
    """
        Returns all schemas that are approved (freigabe_status 5 or 6) and are the latest version in the form of an iterator object.
        Yield will not store the full list but instead will yield one schema at a time, allowing for efficient memory usage.

        Yields dicts with keys:
            fim_id, 
            fim_version, 
            name, 
            bezeichnung, 
            freigabe_status, 
            freigabe_status_label, 
            steckbrief_id, 
            xdf_version, 
            bezug, 
            letzte_aenderung.
    """

    query = "".join(f"freigabe_status={s}&" for s in APPROVED) + "is_latest=true"
    offset = 0
    while True:
        page = _GET(f"/api/v1/schemas?{query}&limit={call_limit}&offset={offset}")
        yield from page["items"] # yield each schema dict in the current page.

        offset += page["count"]  # increment offset for the next page
        if offset >= page["total_count"] or not page["count"]:
            return # stop iteration when all items have been yielded or if the current page is empty.

# ----------------------------------------------------------------------------------------------------
# Specific field extractions from XML file
# ----------------------------------------------------------------------------------------------------

def get_node_in_XML(file: Path, names: str | list[str]) -> ET.Element | None:
    """ 
        Returns the first node with the given name in the XML file. 
        If a list of names is provided, it will return the first node that matches the path of names in order.
        Returns None if no matching node is found.
    """

    namespaces = ""
    iterator = names if isinstance(names, list) else [names]
    for i, name in enumerate(iterator):
        namespaces += NAMESPACE + name + "/" if i < len(iterator) - 1 else NAMESPACE + name

    return ET.parse(file).getroot().find(namespaces)

def _path(child_name: str, recursive: bool) -> str:
    """ `.//` searches the whole subtree, no prefix means direct children only. """
    return (".//" if recursive else "") + NAMESPACE + child_name

def get_child_value(node: ET.Element, child_name: str, recursive: bool = True) -> str | None:
    """
        Returns the text value of the first matching child, or `None` if not found.
        `recursive=False` does not search recursively. Important when the child name is not unique but we want the direct child only.
    """
    child = node.find(_path(child_name, recursive))
    return (child.text or "").strip() if child is not None and child.text else None

def get_child_node(node: ET.Element, child_name: str, recursive: bool = True) -> ET.Element | None:
    """ Returns the first matching child node, or `None` if not found. See get_child_value. """
    return node.find(_path(child_name, recursive))

def get_node_identification(node: ET.Element) -> str:
    """
        The identification of a node as `id v<version>`, or `?` when it carries none.
    """
    identification = get_child_node(node, "identifikation", recursive=False)
    if identification is None:
        return "?"
    return (f"{get_child_value(identification, 'id', recursive=False) or ''} "
            f"v{get_child_value(identification, 'version', recursive=False) or ''}")

def get_id(element: ET.Element) -> str:
    """ The bare FIM id — how rules and the API address an element. `""` when it has none. """
    identification = get_child_node(element, "identifikation", recursive=False)
    return "" if identification is None else (get_child_value(identification, "id", recursive=False) or "")

def get_version(element: ET.Element) -> str:
    """ The element's *own* version, which is not the schema's — the API needs it to match. """
    identification = get_child_node(element, "identifikation", recursive=False)
    return "" if identification is None else (get_child_value(identification, "version", recursive=False) or "")

def get_xdf_namespace(root: ET.Element) -> str:
    """ The XDF namespace of a parsed file, e.g. `…xdatenfelder_3.0.0`, or `""`. """
    return root.tag.split("}")[0].lstrip("{") if "}" in root.tag else ""

def get_werte(element: ET.Element) -> list[dict]:
    """
        The inline code list of a select field: `[{"code": "001", "name": "Arbeitnehmerin"}, …]`.

        This is the one thing the JSON API does not serve — `/api/v1/fields/…` reports
        `feldart: select` but never the options. They exist only in the XDF export.
    """
    werte = get_child_node(element, "werte", recursive=False)
    if werte is None:
        return []
    return [{"code": get_child_value(w, "code", recursive=False) or "",
             "name": get_child_value(w, "name", recursive=False) or ""} for w in werte]

def iter_rule_bearers(element: ET.Element, path: tuple[str, ...] = ()):
    """
        Yields `(element, path)` for every element carrying <regel> children, depth-first.

        Yielding the bearing element rather than the single <regel> is what makes the API
        usable: /api/v1/translated-rules is addressed per element, not per rule. The path is
        what later tells two instances of a reused baukasten group apart.
    """
    if element.findall(NAMESPACE + "regel"):
        yield element, path
    for wrapper in element.findall(NAMESPACE + "struktur"):
        for enthaelt in wrapper.findall(NAMESPACE + "enthaelt"):
            for child in enthaelt:
                if eid := get_id(child):
                    yield from iter_rule_bearers(child, path + (eid,))

@lru_cache(maxsize=None)
def get_translated_rules(fim_id: str, fim_version: str) -> list[dict] | None:
    """
        FITKO's machine-readable rules for one element, or `None` when there are none.

        A 404 is the documented answer for "not translated yet" and is not an error — it is
        the signal to fall back to the freitext grammar. Cached because baukasten groups are
        shared: the same group is otherwise asked for once per schema that embeds it.

        Arguments:
            fim_id, fim_version: the rule-bearing element, *not* the schema.

        Returns:
            The list of translated rules, or None if the API has no translation.
    """
    try:
        return _GET(f"/api/v1/translated-rules/{fim_id}/{fim_version}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise
    except (urllib.error.URLError, TimeoutError) as e:
        # a transient network problem must not silently read as "no rules": the freitext
        # fallback still runs, and origin="freitext" on the edge shows which one was used
        print(f"  translated-rules {fim_id} v{fim_version} nicht erreichbar: {e}")
        return None

# ----------------------------------------------------------------------------------------------------
# XZuFi: the Leistung behind a schema
#
# XDatenfelder says *what* is asked. XZuFi says why, which documents, how long, what it costs and
# who is responsible — written by the Redaktion in citizen-facing language. The two are not linked
# in the API (see find_leistungsschluessel), so the join has to be established and verified here.
# ----------------------------------------------------------------------------------------------------

XZUFI = "{http://xoev.de/schemata/xzufi/2_2_0}"

# urn:de:xzufi:codeliste:leistungstextmodulleika, version 20240216, fetched from XRepository.
# Kept as a table rather than downloaded at runtime: 16 entries that change once every few years
# are not worth a network dependency in the compile path.
LEIKA_TEXTMODUL = {
    "02": "leistungsbezeichnung", "03": "leistungsname", "05": "kurztext", "06": "volltext",
    "07": "handlungsgrundlagen", "08": "unterlagen", "09": "voraussetzungen",
    "11": "verfahrensablauf", "14": "formulare", "15": "weiterfuehrende_informationen",
    "16": "hinweise", "18": "urheber", "22": "zustaendige_stelle", "23": "ansprechpunkt",
    "24": "teaser", "25": "rechtsbehelf",
}

_LEIKA_ID = re.compile(r"\((\d{14})\)")          # "… erstellt: … (99006053006000)."
_PARAGRAF = re.compile(r"§+\s*(\d+[a-z]?)")
_GESETZ = re.compile(r"\b([A-ZÄÖÜ][A-Za-zÄÖÜäöüß]{2,}G|[A-ZÄÖÜ]{2,}[a-zäöüß]*V)\b")

def _normen(texte) -> tuple[set, set]:
    """
        Paragraph numbers and law abbreviations out of free-form legal references.

        The two sides spell the same norm differently — the schema writes "§ 28 (1) MuSchG
        v. 12.12.2019", the Leistung "§ 28 Absatz 1 und 2 Gesetz zum Schutz von Müttern …
        (Mutterschutzgesetz -MuschG)". Comparing the raw strings finds nothing; comparing
        paragraph numbers and the abbreviation (case-folded) finds the overlap.
    """
    blob = " ".join(texte or [])
    return set(_PARAGRAF.findall(blob)), {g.lower() for g in _GESETZ.findall(blob)}

def find_leistungsschluessel(bezeichnung: str, bezug: list[str]) -> dict:
    """
        The LeiKa key of the Leistung a schema belongs to, with a verdict on the match.

        There is no structured link: a schema's `steckbrief_id` points at the placeholder
        "Default-Dokumentsteckbrief", and `relation` and `datenschemata` are empty throughout.
        What does exist is the *Dokumentsteckbrief*, whose description names the LeiKa id in
        plain text. That gives a candidate, which is then checked against the legal basis —
        both sides carry it, and a Leistung about a different subject will not share it.

        Arguments:
            bezeichnung: the schema's title, used for the full-text search.
            bezug:       the schema's legal references, used to verify the candidate.

        Returns:
            {"leistungsschluessel", "join", "evidence"} — `join` is "bestaetigt",
            "unbestaetigt" (found, but the legal basis does not corroborate it) or "keiner".
    """
    leer = {"leistungsschluessel": None, "join": "keiner", "evidence": ""}
    if not bezeichnung:
        return leer
    try:
        treffer = _GET(f"/api/v1/document-profiles?fts_query={urllib.parse.quote(bezeichnung)}&limit=5")
    except (urllib.error.URLError, TimeoutError):
        return leer

    for item in treffer.get("items", []):
        try:
            profil = _GET(f"/api/v1/document-profiles/{item['fim_id']}/{item['fim_version']}")
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            continue
        profil = profil[0] if isinstance(profil, list) else profil
        gefunden = _LEIKA_ID.search(profil.get("beschreibung") or "")
        if not gefunden:
            continue
        schluessel = gefunden.group(1)
        try:
            steckbrief = _GET(f"/api/v1/leistung-steckbriefe/{schluessel}")
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            return {"leistungsschluessel": schluessel, "join": "unbestaetigt",
                    "evidence": "Leistungssteckbrief nicht abrufbar"}
        steckbrief = steckbrief[0] if isinstance(steckbrief, list) else steckbrief
        rechts = steckbrief.get("rechtsgrundlagen")
        paragrafen, gesetze = _normen(bezug)
        p2, g2 = _normen([rechts] if isinstance(rechts, str) else rechts)
        if (paragrafen & p2) and (gesetze & g2):
            return {"leistungsschluessel": schluessel, "join": "bestaetigt",
                    "evidence": f"§ {', '.join(sorted(paragrafen & p2))} · {', '.join(sorted(gesetze & g2))}"}
        return {"leistungsschluessel": schluessel, "join": "unbestaetigt",
                "evidence": f"Rechtsgrundlage stimmt nicht überein ({item['fim_id']})"}
    return leer

def get_leistung_texte(leistungsschluessel: str, sprache: str = "de") -> dict:
    """
        The citizen-facing texts of one Leistung, keyed by what they answer.

        Reads the federal LeiKa Stammtext — the nationwide wording. Länder maintain their own
        versions; those are listed under "laendertexte" as references rather than inlined,
        because which one applies depends on the applicant's Bundesland, and that is decided
        by the portal, not by this compiler.

        The text modules live only in the XZuFi XML, not in the JSON: `modulText` carries a
        LeiKa code (see LEIKA_TEXTMODUL), Fristen/Kosten/Bearbeitungsdauer are modules of
        their own. Every module holds one <inhalt> per language.

        Arguments:
            leistungsschluessel: the 14-digit LeiKa key.
            sprache:             languageCode prefix to keep, "de" by default.

        Returns:
            {"leistungsbezeichnung", "rechtsgrundlagen", "texte": {…}, "frist": …,
             "kosten": …, "bearbeitungsdauer": …, "laendertexte": [...]} — missing modules
            are simply absent, never invented.
    """
    treffer = _GET(f"/api/v1/leistung-stammtexte?leistungsschluessel={leistungsschluessel}&limit=30")
    bund = next((i for i in treffer.get("items", []) if i.get("source") == "leika"), None)
    if bund is None:
        return {}

    voll = _GET(f"/api/v1/leistung-stammtexte/{bund['redaktion_id']}/{bund['leistung_id']}/leika")
    voll = voll[0] if isinstance(voll, list) else voll
    xml = _GET(f"/api/v1/leistung-stammtexte/{bund['redaktion_id']}/{bund['leistung_id']}/leika/xzufi")
    root = ET.fromstring(xml if isinstance(xml, bytes) else str(xml).encode("utf-8"))
    tag = lambda e: e.tag.split("}")[-1]

    def inhalt(modul) -> str:
        """ The <inhalt> in the wanted language — modules carry every translation at once. """
        for kind in modul.iter():
            if tag(kind) == "inhalt" and (kind.get("languageCode") or "").startswith(sprache):
                return (kind.text or "").strip()
        return ""

    texte, module = {}, {}
    for modul in root.iter():
        if tag(modul) == "modulText":
            code = next((c.text for c in modul.iter() if tag(c) == "code"), "")
            if (name := LEIKA_TEXTMODUL.get(code or "")) and (text := inhalt(modul)):
                texte[name] = text
        elif tag(modul) in ("modulFrist", "modulKosten", "modulBearbeitungsdauer"):
            # these are structured, not prose: a Fristtyp code plus a duration, an amount, …
            # Only what is actually there is read out; the typ code stays a code because
            # resolving it would mean pulling yet another codelist for one label.
            werte = {tag(c): (c.text or "").strip() for c in modul.iter()
                     if tag(c) in ("dauer", "einheit", "betrag", "waehrung") and c.text}
            typ = next((c.text for c in modul.iter()
                        if tag(c) == "code" and (c.text or "").strip().isdigit()), None)
            module[tag(modul)] = ({"typ": typ} | werte) if (typ or werte) else None

    return {
        "leistungsbezeichnung": voll.get("leistungsbezeichnung"),
        "leistungsbezeichnung_2": voll.get("leistungsbezeichnung_2"),
        "rechtsgrundlagen": voll.get("rechtsgrundlagen"),
        "texte": texte,
        "frist": module.get("modulFrist"),
        "kosten": module.get("modulKosten"),
        "bearbeitungsdauer": module.get("modulBearbeitungsdauer"),
        # references only — the portal knows the Bundesland and picks from these
        "laendertexte": [{"redaktion_id": t.get("redaktion_id"), "leistung_id": t.get("leistung_id"),
                          "source": t.get("source"), "title": t.get("title")}
                         for t in treffer.get("items", []) if t.get("source") != "leika"],
    }

def get_all_datenfeldgruppen(file: Path) -> dict[str, dict[str, ET.Element]] | None:
    """ Returns a dict with all datenfeldgruppen IDs and their tree nodes. """
    root = ET.parse(file).getroot()
    datenfeldgruppen = root.findall(".//" + NAMESPACE + "datenfeldgruppe")

    res = dict()
    for node in datenfeldgruppen:
        ident_node = get_child_node(node, "identifikation", recursive=False)
        if ident_node is not None:
            id_value = get_child_value(ident_node, "id", recursive=False)
            version_value = get_child_value(ident_node, "version", recursive=False)
            if id_value is not None:
                res[id_value] = {"node": node, "version": version_value}

    return res if res else None

def get_all_datenfelder(file: Path) -> dict[str, dict[str, ET.Element]] | None:
    """ Returns a dict with all datenfelder IDs and their tree nodes. """
    root = ET.parse(file).getroot()
    datenfelder = root.findall(".//" + NAMESPACE + "datenfeld")

    res = dict()
    for node in datenfelder:
        ident_node = get_child_node(node, "identifikation", recursive=False)
        if ident_node is not None:
            id_value = get_child_value(ident_node, "id", recursive=False)
            version_value = get_child_value(ident_node, "version", recursive=False)
            if id_value is not None:
                res[id_value] = {"node": node, "version": version_value}

    return res if res else None

def rules_of(xdf: str) -> list[str]:
    """ Every free-text rule in an XDF 3.0 export, in document order. """
    RULE = re.compile(r"<xdf3:freitextRegel>(.*?)</xdf3:freitextRegel>", re.S)

    return [r.strip() for r in RULE.findall(xdf)]

if __name__ == "__main__":
    filepath = Path(__file__).parent.parent.parent.parent / "fim_data" / "S00000000371/schema.xdf.xml"
    node = get_node_in_XML(filepath, ["stammdatenschema", "struktur", "enthaelt"])
    print(get_child_value(node, "id") if node is not None else "Node not found")

    # print(get_all_datenfelder(filepath))

