import re
from dataclasses import dataclass, field as dc_field

"""
This file contains the grammar and parsing logic for the "freitextRegel" elements in FIM. 
It defines how to extract structured information from the free-text rules, including identifying targets, actions, conditions, and scopes. 
The parser handles various sentence structures and edge cases, ensuring that even unparseable sentences are represented as uncertain edges rather than being discarded.

The IDs carry type information (G for group, F for field) and are used to identify the elements affected by the rules.
Example:
    - ID: G60000086 Version: 2.1 Status: aktiv</xdf3:beschreibung><xdf3:definition>Angaben für die Adressierung im Inland, soweit es sich um die Anschrift eines Gebäudes handelt.</xdf3:definition>
    - ID: F60000243 Version: 1.2 Status: aktiv</xdf3:beschreibung><xdf3:bezug>XInneres.Meldeanschrift.strasse Version 8</xdf3:bezug>

What does not parse is not guessed. It comes back as Edge(certain=False).
"""

# A FIM id, optionally as a dotted path: F60000000243 or G00000002194.F60000000243.
# The leading letter carries the type (G group, F field), the digits are the number.
ID = r"[GF]\d{6,}(?:\.[GF]\d{6,})*"

# End of sentence: a period or exclamation mark, whitespace, then a capital. The lookbehind
# and lookahead are zero-width so the split consumes only the whitespace between sentences.
_SENTENCE = re.compile(r"(?<=[.!])\s+(?=[A-ZÄÖÜ])")
# Any quoted span. Opening and closing quotes are listed separately because the corpus mixes
# „…" , "…" and '…'. The 120-char ceiling keeps a stray unpaired quote from swallowing the
# rest of the rule.
_QUOTED = re.compile(r"[\"„'][^\"“”']{0,120}[\"“”']")

def _sentences(text: str) -> list[str]:
    """
        Sentence split that survives the legal-form lists.

        Codelist labels like "AG & Co. KG" carry a period followed by a capital, so a naive
        split cuts them in half and the fragments parse as nothing. Masking the quoted spans
        first was worth 224 of 486 failures on the corpus.
    """
    masked, spans = [], []

    def hide(match):
        spans.append(match.group(0))
        return f"\x00{len(spans) - 1}\x00"

    for sentence in _SENTENCE.split(_QUOTED.sub(hide, " ".join(text.split()))):
        masked.append(re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], sentence))
    return masked
_SCOPE = re.compile(r"^Für (?:das Land|die Länder)\s+([A-ZÄÖÜ]{2}(?:\s*,\s*[A-ZÄÖÜ]{2})*)\s+gilt[:.]?\s*",
                    re.I)
_SCOPE_RESET = re.compile(r"^Für alle anderen Länder gilt[:.]?\s*", re.I)
_CONDITION = re.compile(rf"\bwenn\b(?P<cond>.*?),?\s*\bdann\b(?P<then>.*)", re.I | re.S)
_OPERATOR = re.compile(r"(<>|&lt;&gt;|=|\bungleich\b|\bgleich\b|\bnicht leer\b|\bleer\b)", re.I)
_ID = re.compile(ID)
_VALUE = re.compile(r"(?P<code>\b\d{3,6}\b)?\s*[\"„'](?P<label>[^\"“”']{1,80})[\"“”']|\b(?P<bare>wahr|falsch)\b")

# checked in order — negations first, or "darf nicht befüllt sein" reads as "befüllt"
_ACTIONS = (
    ("hide",  r"deaktiviere|nicht angezeigt|ausgeblendet|aus(?:zu)?blenden|nicht sichtbar"),
    ("forbidden",    r"darf\s+(?:.*?\s+)?nicht\s+(?:.*?\s+)?bef[üu]llt|nicht bef[üu]llt (?:werden|sein)"),
    ("validation", r"muss\s+(?:zeitlich\s+)?(?:vor|nach)\b|validit[äa]t|plausib|gr[öo]ßer als|kleiner als"),
    # "darf nicht leer sein" is a requirement, not a prohibition — it lands here, not in
    # verboten, whose pattern needs an explicit "befüllt" to fire.
    ("required",     r"muss\s+(?:.*?\s+)?bef[üu]llt|pflichtangabe|pflichtfeld|zu bef[üu]llen"
                    r"|vor(?:zu)?bef[üu]llen|muss\s+(?:.*?\s+)?angegeben|nicht leer (?:sein|bleiben)"),
    # \b matters: "aktiviere" without it also fires inside "deaktiviere", which made 307
    # sentences claim to show and hide the same field at once. Same for negated visibility.
    ("show",    r"\baktiviere|ein(?:zu)?blenden|eingeblendet"
                    r"|(?<!nicht )angezeigt|(?<!nicht )sichtbar"),
)

@dataclass
class Edge:
    """
        One directed edge: source decides, target is affected, actions say how.

        actions is a list because a single clause can carry several — "DANN aktiviere F…
        UND mache es zu einer Pflichtangabe" is two effects on one target, and collapsing
        them to one would silently drop the mandatory-ness.
    """
    target: str | None            # None only for cross-field rules that affect no single field
    actions: list[str]
    source: str | None = None
    operator: str | None = None
    values: list[str] = dc_field(default_factory=list)
    mentioned: list[str] = dc_field(default_factory=list)  # every id named in the clause
    scope: list[str] | None = None          # Bundesländer this clause is scoped to
    rule_id: str | None = None
    text: str = ""
    certain: bool = True
    # "api" when FITKO's own translation produced this edge, "freitext" when the grammar
    # below did. Both are certain, but only one of them is authoritative — a reader has to
    # be able to tell which, so this is not folded into `certain`.
    origin: str = "freitext"
    # the untouched condition tree of an API rule. source/operator/values are a flattened
    # view for display; anything the flattener cannot express (xor, or across two different
    # fields) survives here rather than being lost.
    condition: dict | bool | None = None

    def key(self):
        return (self.source, self.operator, tuple(self.values), self.target,
                tuple(self.actions), tuple(self.scope or ()))

def _leaf(dotted: str) -> str:
    """ G1.G2.F3 names a path; the last segment is the element the rule talks about. """
    return dotted.split(".")[-1]

# ---------------------------------------------------------------------
# translated-rules (API) → edges
#
# FITKO translates part of the corpus itself and serves the result under
# /api/v1/translated-rules: effect, target, a condition tree and a ready German message.
# That translation is authoritative, so it wins wherever it exists — the grammar above only
# has to run for the elements the API answers with 404.

_EFFECT = {"require": "required", "forbid": "forbidden", "valid": "validation"}

# what `not` does to an already flattened operator. Anything missing here cannot be negated
# flatly — see _flatten, which then gives up rather than returning a half statement.
_INVERSE = {"=": "<>", "<>": "=", "leer": "nicht leer", "nicht leer": "leer"}

def _literal(value) -> str:
    """ JSON literal → the same spelling the freitext grammar produces, so both agree. """
    if isinstance(value, bool):
        return "wahr" if value else "falsch"     # matches the _VALUE "bare" group
    return str(value)

def _identifier(node) -> str | None:
    """ {"identifier": "self.G1.F2"} → "F2"; anything else → None. """
    if isinstance(node, dict) and set(node) == {"identifier"}:
        return _leaf(str(node["identifier"]).removeprefix("self."))
    return None

def _flatten(condition) -> tuple[str | None, str | None, list[str]]:
    """
        Condition tree → the flat (source, operator, values) an Edge carries.

        Only the shapes that actually occur are handled; everything else returns an empty
        triple, which means "not expressible flatly". The caller keeps the original tree in
        Edge.condition, so returning nothing here loses no information — it only means the
        table view falls back to the API's own message.

        Arguments:
            condition: the `condition` value of one translated rule.

        Returns:
            (source id or None, operator or None, list of values).
    """
    if condition is True or condition is None:
        return None, None, []                       # rule applies unconditionally
    if ident := _identifier(condition):
        # a bare boolean field: "… muss angegeben werden, wenn die Abfrage bejaht wird"
        return ident, "=", ["wahr"]
    if not isinstance(condition, dict) or len(condition) != 1:
        return None, None, []

    (operator, operand), = condition.items()
    if operator == "not":
        # negation wraps a single condition — invert its operator instead of nesting.
        # An operator that has no inverse here would silently produce (source, None): the
        # source without the relation is worse than nothing, so drop the whole triple.
        source, inner, values = _flatten(operand)
        inverted = _INVERSE.get(inner) if inner else None
        return (source, inverted, values) if inverted else (None, None, [])
    if operator == "is_empty":
        # the API's presence check — the freitext grammar already produces these two
        # operators from "wenn F… leer ist", so both extractions end up speaking one language
        return (_identifier(operand), "leer", []) if _identifier(operand) else (None, None, [])
    if operator in ("equal", "not_equal") and isinstance(operand, list) and len(operand) == 2:
        left, right = operand
        if ident := _identifier(left):
            return ident, "=" if operator == "equal" else "<>", [_literal(right)]
        return None, None, []                       # literal = literal, or field = field
    if operator == "or" and isinstance(operand, list):
        parts = [_flatten(p) for p in operand]
        sources, operators = {p[0] for p in parts}, {p[1] for p in parts}
        # "= 001 oder = 002" on one field is a value list; an OR across two different fields
        # is a genuine disjunction and must not be squashed into one source
        if len(sources) == 1 and len(operators) == 1 and None not in sources:
            return parts[0][0], parts[0][1], [v for p in parts for v in p[2]]
    # `and` is deliberately absent: it joins conditions on *different* fields ("F1 leer UND
    # F2 leer"), and a flat edge has room for exactly one source. On a single field it would
    # be contradictory anyway. Same for xor and nested combinations — all keep their tree.
    return None, None, []

def parse_translation(rules: list[dict], rule_id: str | None = None) -> list[Edge]:
    """
        FITKO's machine-readable rules → Edges, one per translated rule.

        `target` may be absent: a rule like "mindestens eines der Felder … muss wahr sein"
        constrains a set of fields, not one. Such an edge keeps target=None instead of being
        dropped or having a target invented for it.

        Arguments:
            rules:   the JSON list from /api/v1/translated-rules/<id>/<version>.
            rule_id: the element the rules hang off — the API returns no R… ids of its own.

        Returns:
            One Edge per rule, all with origin="api" and certain=True.
    """
    out = []
    for rule in rules:
        effect = str(rule.get("effect") or "")
        target = rule.get("target")
        source, operator, values = _flatten(rule.get("condition"))
        out.append(Edge(
            target=_leaf(str(target).removeprefix("self.")) if target else None,
            # unknown effects keep their API name rather than being mapped to something wrong
            actions=[_EFFECT.get(effect, effect or "unclear")],
            source=source, operator=operator, values=values,
            mentioned=[i for i in (source, _leaf(str(target).removeprefix("self."))
                                   if target else None) if i],
            rule_id=rule_id,
            # the API ships its own German sentence — better than anything we would render
            text=rule.get("message", ""),
            certain=True, origin="api", condition=rule.get("condition")))
    return out

def _values(text: str) -> list[str]:
    out = []
    for m in _VALUE.finditer(text):
        if m.group("bare"):
            out.append(m.group("bare").lower())
        else:
            out.append(f'{m.group("code")} {m.group("label")}'.strip() if m.group("code")
                       else m.group("label"))
    return out

def _actions(text: str) -> list[str]:
    return [name for name, pattern in _ACTIONS if re.search(pattern, text, re.I)]

_AND = re.compile(r"\s+UND\s+|\s+und\s+(?=(?:aktiviere|deaktiviere|mache|blende|zeige|muss|darf))")
_ELSE_VALUE = re.compile(r"alle anderen|jede andere|sonst\b|übrige", re.I)

def _sentence(sentence: str, rule_id: str | None, scope: list[str] | None) -> list[Edge]:
    """
        One sentence can hold several effects on different targets:

            DANN aktiviere F…295 UND mache es zu einer Pflichtangabe UND deaktiviere F…296

        Splitting on UND keeps them apart — merging them produced a single edge that claimed
        to show and hide at once. A clause without an id ("mache es zu einer Pflichtangabe")
        refers back to the target of the clause before it.
    """
    cond = _CONDITION.search(sentence)
    if cond:
        condition, consequence = cond.group("cond"), cond.group("then")
    else:
        condition, consequence = "", sentence               # unconditional: "Die Gruppe X muss befüllt werden."

    sources = _ID.findall(condition)
    op = _OPERATOR.search(condition)
    operator = {"&lt;&gt;": "<>", "ungleich": "<>", "gleich": "="}.get(
        (op.group(1).lower() if op else ""), op.group(1).lower() if op else None)
    # values live after the operator — before it sits the source field's own label
    values = _values(condition[op.end():]) if (condition and op) else []
    if condition and not values and _ELSE_VALUE.search(condition):
        operator = "else"                        # "= alle anderen Ausprägungen der Codeliste"

    edges, last = [], None
    for clause in _AND.split(consequence):
        actions = _actions(clause)
        if not actions:
            continue
        ids = _ID.findall(clause)
        target = _leaf(ids[0]) if ids else last
        if not target:
            continue
        last = target
        edges.append(Edge(target=target, actions=actions,
                            source=_leaf(sources[0]) if sources else None,
                            operator=operator, values=values, mentioned=[_leaf(i) for i in ids],
                            scope=scope, rule_id=rule_id, text=sentence.strip()))
    return edges

def parse_rule(text: str, rule_id: str | None = None) -> list[Edge]:
    """
        Splits one freitextRegel into its sentences and turns each into an edge.

        A rule almost always states both branches ("Wenn = X, dann muss …; wenn <> X, dann
        darf nicht …"), so one rule normally yields two edges. Sentences that do not parse
        come back as certain=False rather than being dropped — a silently missing edge is
        worse than a visibly uncertain one.
    """
    edges, scope, last_target = [], None, None
    for sentence in _sentences(text):
        if not sentence.strip():
            continue
        # `scope` carries across sentences, so the match objects need names of their own
        if scoped := _SCOPE.match(sentence):
            scope = [land.strip() for land in scoped.group(1).split(",")]
            sentence = sentence[scoped.end():]
        elif reset := _SCOPE_RESET.match(sentence):
            scope = None
            sentence = sentence[reset.end():]
        if not sentence.strip():
            continue

        new_edges = _sentence(sentence, rule_id, scope)
        # "Für alle anderen Länder wird das Feld nicht angezeigt." names no id — it means the
        # element the previous sentence just talked about.
        if not new_edges and last_target and not _ID.search(sentence) and (actions := _actions(sentence)):
            new_edges = [Edge(target=last_target, actions=actions, scope=scope,
                         rule_id=rule_id, text=sentence.strip())]
        if new_edges:
            last_target = new_edges[-1].target
            edges += new_edges
        else:
            edges.append(Edge(target="?", actions=["unclear"], rule_id=rule_id,
                                text=sentence.strip(), scope=scope, certain=False))
    return edges
