import json

from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------
# Antragsgraph → SKILL.md
#
# Der Skill beschreibt den Antrag, er entscheidet ihn nicht. Jede Bedingung steht als Regel
# mit FIM-ID und Rechtsgrundlage im Text, und die verbindliche Fassung ist graph.json —
# das Sprachmodell übersetzt nur zwischen Alltagssprache und Feldwert.
#
# Regeln, die der Parser nicht lesen konnte, werden nicht weggelassen, sondern gelb markiert
# im Abschnitt "Ungeklärt" ausgewiesen. Ein Copilot, der eine Bedingung nicht kennt, muss das
# sagen können, statt sie zu erfinden.

TARGET_LOCATION = Path(__file__).parent.parent.parent / "fim_data"

# rule_parser action names → the German wording that goes into the skill text. The parser
# works with short English tags, the copilot reads prose; this table is the only place that
# translates between the two. Unknown tags fall through unchanged (see ACTION_TEXT.get below),
# so a new action shows up verbatim instead of disappearing from the table.
ACTION_TEXT = {
    "required": "muss ausgefüllt werden",
    "forbidden": "darf nicht ausgefüllt werden",
    "show": "wird gezeigt",
    "hide": "entfällt",
    "validation": "wird geprüft",
    "unclear": "ungeklärt",
}

def _condition(edge: dict, names: dict) -> str:
    """
        The "wenn …" half of one edge as a German sentence.

        The edge stores the condition in three separate pieces (source id, operator, values),
        which is what the graph needs but not what a reader needs. Each operator gets the
        phrasing that reads naturally in German — "leer" wants "ist", "else" wants no value
        at all — so the branches below are wording, not logic.

        Arguments:
            edge:  one entry from graph["edges"] (see rule_parser.Edge).
            names: field id → display name, used to avoid printing bare FIM ids.

        Returns:
            A sentence fragment such as: wenn „Rechtsform" gleich „01 GmbH" ist
    """
    # names.get(..., source): an id the schema does not define stays visible as an id rather
    # than turning into an empty quote — a missing field must not read like a nameless one.
    source = names.get(edge["parent"], edge["parent"])
    if edge["operator"] == "else":
        # the parser's catch-all branch ("alle anderen Ausprägungen der Codeliste"): it has no
        # values by definition, so naming one would be an invention
        return f'in allen anderen Fällen von „{source}"'
    if edge["operator"] in ("leer", "nicht leer"):
        # presence checks carry their own verb, "gleich leer" would be wrong German
        return f'wenn „{source}" {edge["operator"]} ist'
    # a condition whose values the parser could not read still describes *that* the field
    # decides — "einem beliebigen Wert" says the trigger is unknown instead of dropping the row
    values = " oder ".join(f'„{w}"' for w in edge["values"]) or "einem beliebigen Wert"
    # unknown operator → printed as it stands; no operator at all → the neutral "gesetzt auf"
    comparison = {"=": "gleich", "<>": "ungleich"}.get(edge["operator"], edge["operator"] or "gesetzt auf")
    return f'wenn „{source}" {comparison} {values} ist'

def build_skill(graph: dict) -> str:
    """
        Renders one Antragsgraph as the text of a SKILL.md.

        The document has a fixed order — frontmatter, header data, working instructions, cycle
        warning, fields, conditions, unclear rules, mermaid graph — and is assembled as a list
        of lines that is joined once at the end. That keeps the sections readable as blocks and
        makes an empty section (no unclear rules, no cycles) a matter of not appending.

        Nothing here decides anything about the Antrag: every statement is a rendering of what
        build_graph already put into the graph.

        Arguments:
            graph: the dict written by graph.build_graph.

        Returns:
            The complete markdown text, ready to be written to SKILL.md.
    """
    head = graph["schema"]
    # id → display name once, up front: names are needed in four sections below, and falling
    # back to the id keeps a nameless element addressable instead of blank
    names = {k["path_id"]: (k["label"] or k["id"]) for k in graph["nodes"]}
    stats = graph["statistics"]

    # the graph keeps parsed and unparsed rules in one list, the document must not: certain
    # edges become the binding table, unclear ones the yellow "please decide this" section
    # only condition edges belong here — the contains edges are the form structure and are
    # already expressed by the field headings below
    conditions = [k for k in graph["edges"] if k["kind"] == "condition"]
    certain = [k for k in conditions if k["certain"]]
    unclear = [k for k in conditions if not k["certain"]]
    # targets of a *conditional* edge — an edge with a source. Unconditional edges ("Die Gruppe
    # muss befüllt werden") apply always, so they say nothing about a field being situational.
    conditional = {k["child"] for k in certain if k["parent"] and k["child"]}

    # YAML frontmatter first: name and description are what a skill host reads to decide
    # whether this skill applies at all, so both are derived from the FIM head data
    lines = [
        "---",
        f'name: antrag-{head["fim_id"].lower()}',
        f'description: Führt Antragstellende durch „{head["bezeichnung"]}" '
        f'(FIM {head["fim_id"]} {head["fim_version"]}). Fragt nur, was in der jeweiligen '
        f'Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.',
        "---",
        "",
        f'# {head["bezeichnung"]}',
        "",
        # provenance block: which schema, which version, how ripe, on what legal basis, and
        # when it was compiled. A skill without this cannot be checked against its source.
        f'- **FIM-ID:** `{head["fim_id"]} {head["fim_version"]}` · **Reifegrad:** {head["freigabe_status_label"] or "unbekannt"}',
        f'- **Rechtsgrundlagen:** {"; ".join(head["bezug"]) or "keine angegeben"}',
        f'- **Kompiliert:** {head["compiled_at"]} aus {head["source_url"] or "FIM"}',
        f'- **Umfang:** {stats["fields"]} Felder, {stats["edges_certain"]} gesicherte Bedingungen,'
        f' {stats["edges_unclear"]} ungeklärt',
        "",
        # the four rules that keep the model on the translator role: without them a language
        # model happily infers a condition it did not read, which is exactly the failure this
        # whole pipeline exists to prevent
        "## Verbindliche Arbeitsweise",
        "",
        "1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis"
        " fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.",
        "2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage"
        " die amtliche Formulierung und die Rechtsgrundlage.",
        "3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten"
        " nicht erfüllt ist, entfallen — frage sie nicht ab.",
        "4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln\" enthält"
        " Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern"
        " verweise auf die zuständige Stelle.",
        "",
    ]

    # cycles are recomputed rather than read from stats["cycles"], because the warning needs
    # one concrete example path, not just a count. A cycle is not an error to be broken here —
    # it means two fields condition each other, and a human has to look at it.
    if cycle_list := graph.get("cycles_detail") or []:
        lines += ["> **Achtung:** Der Graph enthält "
                   f'{len(cycle_list)} Abhängigkeitszyklus(se), z. B. {" → ".join(cycle_list[0])}. '
                   "Diese Felder können sich gegenseitig bedingen — bei Widersprüchen an die "
                   "Fachstelle verweisen.", ""]

    # The XZuFi block: prepared answers to everything the applicant asks that is not a field
    # value. Rendered only when the join to the Leistung was confirmed against the legal basis
    # — texts from the wrong Leistung would state wrong Fristen and Gebühren with the same
    # confidence as the field rules, which is the one failure mode this file must not have.
    if (leistung := graph.get("leistung") or {}).get("join") == "bestaetigt":
        lines += ["## Antworten zur Leistung", "",
                  f'_Quelle: LeiKa {leistung["leistungsschluessel"]}, bundesweiter Stammtext'
                  f' · Zuordnung geprüft über {leistung["evidence"]}._', ""]
        for schluessel, ueberschrift in (("voraussetzungen", "Wer darf den Antrag stellen?"),
                                         ("unterlagen", "Welche Unterlagen werden gebraucht?"),
                                         ("verfahrensablauf", "Wie läuft das Verfahren ab?"),
                                         ("zustaendige_stelle", "Wer ist zuständig?"),
                                         ("hinweise", "Besonderheiten"),
                                         ("volltext", "Ausführliche Beschreibung")):
            if text := (leistung.get("texte") or {}).get(schluessel):
                lines += [f"### {ueberschrift}", "", text, ""]
        for schluessel, ueberschrift in (("frist", "Frist"), ("kosten", "Kosten"),
                                         ("bearbeitungsdauer", "Bearbeitungsdauer")):
            if wert := leistung.get(schluessel):
                lines.append(f'- **{ueberschrift}:** `{wert}`')
        if leistung.get("laendertexte"):
            # not inlined: which one applies depends on the applicant's Bundesland, and that
            # is the portal's decision — this compiler only lists what exists
            lines += ["", f'_Für {len(leistung["laendertexte"])} Länder gibt es abweichende'
                      " Fassungen mit eigenen Fristen und Zuständigkeiten. Bei Fragen dazu auf"
                      " die zuständige Stelle des jeweiligen Landes verweisen._", ""]
        lines.append("")
    elif (leistung := graph.get("leistung") or {}).get("leistungsschluessel"):
        lines += ["> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet"
                  f' werden ({leistung.get("evidence")}). Zu Fristen, Kosten, Unterlagen und'
                  " Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle"
                  " verweisen.", ""]

    lines += ["## Felder", ""]
    # group by full path, not by the bare group id: reused baukasten groups like
    # "Straßenanschrift" sit at several places and would otherwise collapse into one
    # heading listing every field twice
    by_group: dict[tuple, list[dict]] = defaultdict(list)
    for k in graph["nodes"]:
        if k["kind"] == "field":
            by_group[tuple(k["path"])].append(k)

    for path, fields in by_group.items():
        # the heading spells out the whole nesting ("Betrieb › Straßenanschrift"), so a reused
        # group is distinguishable by where it sits; the bare id of the innermost group is
        # appended for anyone who wants to look it up in the XDF
        # `path` holds bare ids, `names` is keyed by path_id — so every ancestor is looked up
        # under its own cumulative prefix. Using the bare id here would print the same label
        # for both instances of a reused group, which is exactly what the path prevents.
        title = " › ".join(names.get(".".join(path[:i + 1]), group_id)
                           for i, group_id in enumerate(path)) or "Ohne Gruppe"
        lines.append(f'### {title}' + (f' (`{path[-1]}`)' if path else ""))
        lines.append("")
        for field in fields:
            # two independent properties on one line: "Pflicht/optional" comes from the XDF
            # cardinality (anzahl 1..), "conditional" from a rule pointing at this field.
            # A field can be Pflicht *and* conditional — mandatory once its condition holds.
            marker = "Pflicht" if field["required"] else "optional"
            if field["path_id"] in conditional:
                marker += ", conditional"
            # the bare id is what a reader looks up in FIM; path_id is the internal key
            lines.append(f'- **{field["label"]}** (`{field["id"]}`) — {marker}')
            if field["bezug_effective"]:
                # "(geerbt)" matters: it says the paragraph stands on the enclosing group, not
                # on this field. A copilot citing law must not claim more precision than exists.
                geerbt = "" if field["bezug_source"] == "self" else " _(geerbt)_"
                lines.append(f'  - Rechtsgrundlage: {"; ".join(field["bezug_effective"])}{geerbt}')
            if field["hilfetext"]:
                # the official help text, verbatim — it is the wording the applicant is
                # entitled to hear, so it is quoted rather than paraphrased
                lines.append(f'  - Hilfe: {field["hilfetext"]}')
        lines.append("")

    # one row per conditional edge: condition → affected field → effect → rule id. The rule id
    # is what makes a row checkable against the FIM source, which is why "?" is printed rather
    # than the column being left out.
    lines += ["## Bedingungen", "", "| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |",
              "|---|---|---|---|---|"]
    for edge in certain:
        if not edge["parent"]:
            continue    # unconditional edge: the "Bedingung" column would be empty, and the
                        # cardinality in the field list already says the field is mandatory
        # several actions on one target stay joined ("wird gezeigt und muss ausgefüllt werden"):
        # dropping one would lose the mandatory-ness the parser deliberately kept apart
        actions: list[str] = edge["actions"]
        effect = " und ".join(ACTION_TEXT.get(a, a) for a in actions)
        # a rule scoped to single Bundesländer must never read as generally applicable
        scope = f' _(nur {", ".join(edge["scope"])})_' if edge["scope"] else ""
        # a cross-field rule constrains a set, not one field — say so instead of naming one
        field = f'„{names.get(edge["child"], edge["child"])}"' if edge["child"] else "_mehrere Felder_"
        # the rule's own paragraph where it has one — that is the norm making *this condition*
        # apply, which is more precise than the affected field's. Empty stays empty rather than
        # falling back to the field's, which would attribute the condition to the wrong norm.
        bezug = "; ".join(edge["bezug"]) or "—"
        lines.append(f'| {_condition(edge, names)}{scope} | {field} '
                      f'| {effect} | {bezug} | `{edge["rule_id"] or "?"}` |')
    lines.append("")

    # only written when something is actually unclear — an always-present but empty section
    # would train the reader to skip it
    if unclear:
        lines += [
            "## Ungeklärte Regeln",
            "",
            "Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine"
            " Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine"
            " menschliche Entscheidung:",
            "",
        ]
        for edge in unclear:
            # the original sentence, untouched and marked yellow: the parser failed on it, so
            # any rewording here would be guesswork on top of an unread rule
            lines.append(f'- <mark>{edge["text"]}</mark> — Regel `{edge["rule_id"] or "?"}`')
        lines.append("")

    # the mermaid picture closes the document — it is an overview, not the source of truth,
    # and to_mermaid truncates past 60 edges rather than rendering an unreadable hairball
    lines += ["## Abhängigkeitsgraph", "", "```mermaid", graph["mermaid"], "```", ""]
    return "\n".join(lines)

def write_skill(graph: dict, target: Path) -> Path:
    """
        Writes the rendered skill to `target`, creating the folder if needed.

        Explicit utf-8: the text is full of German umlauts and typographic quotes, and on
        Windows the default encoding is not utf-8.

        Arguments:
            graph:  the dict from graph.build_graph.
            target: the SKILL.md path to write.

        Returns:
            The path written, so callers can log or chain on it.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_skill(graph), encoding="utf-8")
    return target

def compile_skill(fim_id: str, corpus: Path = TARGET_LOCATION) -> Path:
    """
        Turns one already-compiled graph into its skill file.

        Reads <corpus>/<fim_id>/graph.json (written by graph.compile_schema) and writes
        SKILL.md beside it. graph.json is all it needs — the mermaid diagram and the cycle
        list are compiled into that file, so this step never touches the XDF again.

        Arguments:
            fim_id: the FIM id of the schema, e.g. "S00000000371".
            corpus: root of the harvested data; defaults to the repo's fim_data.

        Returns:
            The path of the written SKILL.md.
    """
    graph = json.loads((corpus / fim_id / "graph.json").read_text("utf-8"))
    return write_skill(graph, corpus / fim_id / "SKILL.md")

def compile_all(corpus: Path = TARGET_LOCATION, use_api: bool = True) -> dict:
    """
        Compiles every harvested schema: graph.json, graph.mmd and SKILL.md per folder.

        Arguments:
            corpus:  root of the harvested data.
            use_api: False skips translated-rules — much faster, but the freitext grammar
                     then has to read every rule on its own.

        Returns:
            Counts of what was written, plus the schemas that failed with their reason.
    """
    # imported here, not at module level: build_skill deliberately works off graph.json alone,
    # and only this batch entry point needs the compiler that produces it
    from .graph import compile_schema

    written, failed = 0, []
    for source in sorted(p.parent for p in corpus.glob("*/schema.xdf.xml")):
        try:
            compile_schema(source.name, corpus, use_api=use_api)
            compile_skill(source.name, corpus)
            written += 1
        except Exception as e:                    # one broken schema must not stop the corpus
            failed.append((source.name, f"{type(e).__name__}: {e}"))
    return {"geschrieben": written, "fehlgeschlagen": failed}

if __name__ == "__main__":
    print(compile_all())
