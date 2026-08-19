import html, json, time

from dataclasses import dataclass, field as dc_field, asdict
from pathlib import Path
import xml.etree.ElementTree as ET

from .fim_connector.fim_api_extension import (NAMESPACE as X, get_child_value, get_id,
                                              get_translated_rules, get_version, get_werte,
                                              get_xdf_namespace, iter_rule_bearers,
                                              find_leistungsschluessel, get_leistung_texte)
from .rule_parser import parse_rule, parse_translation

# ---------------------------------------------------------------------
# XDF 3.0 → Antragsgraph
#
# Two relations over one set of nodes, which is why this is a graph and not a tree:
#
#   contains    the form structure — a group holds fields and further groups
#   condition   a rule — one field decides whether another is required, forbidden, …
#
# Condition edges run *across* the containment tree: a field sits in one place structurally
# but can be governed by a field from a completely different branch. Both are Edges with a
# `kind`, so cycles, ordering and rendering all work off one list.
#
# Nothing here decides anything a human did not write down. Rules come from FITKO's own
# translation where it exists and from the freitext grammar otherwise; what neither could
# read stays in the graph as certain=False instead of disappearing.

TARGET_LOCATION = Path(__file__).parent.parent.parent / "fim_data"

# Everything that knows how FIM stores things — ids, versions, code lists, rule-bearing
# elements, the translated-rules endpoint — lives in fim_connector.fim_api_extension. This
# module only assembles them into a graph.

# ---------------------------------------------------------------------
# The graph

@dataclass
class Node:
    """
        One element of the form — a group or a field.

        Identity is `path_id`, never `id`: baukasten groups are reused, so "Straßenanschrift"
        exists twice in one schema with the same id and the same child ids. Only the path says
        whether it is the company's address or the workplace's.
    """
    path_id: str                       # identity: dotted chain of enclosing ids
    id: str                            # bare FIM id, as rules and the API name it
    version: str
    kind: str                          # "group" | "field"
    label: str                         # bezeichnungEingabe — the question a citizen reads
    name: str = ""                     # administrative name, for the file and the Bescheid
    definition: str = ""
    hilfetext: str = ""
    feldart: str = ""                  # select | text | date | …
    datentyp: str = ""
    werte: list[dict] = dc_field(default_factory=list)   # allowed answers of a select field
    anzahl: str = ""                   # cardinality *at this position*, e.g. "1:1"
    required: bool = False
    bezug: list[str] = dc_field(default_factory=list)    # legal basis written on this element
    # The legal basis that *applies* — 13 % of fields carry none of their own and take it from
    # the nearest enclosing group, a few from the schema. Kept apart from `bezug` on purpose:
    # a skill that cites law must be able to say whether the citation stands on the field
    # itself or was inherited. `bezug_source` names where it came from.
    bezug_effective: list[str] = dc_field(default_factory=list)
    bezug_source: str = ""             # "self" | path_id of the ancestor | "schema" | ""
    path: list[str] = dc_field(default_factory=list)
    parent: str | None = None          # path_id of the enclosing group
    children: list[str] = dc_field(default_factory=list) # path_ids, in document order

@dataclass
class Edge:
    """
        Directed, from `parent` to `child`, both path_ids.

        kind="contains"  — parent holds child. The form structure.
        kind="condition" — parent decides about child. Everything from `operator` down
                           describes that decision and stays empty for contains edges.
    """
    parent: str | None
    child: str | None
    kind: str                                            # "contains" | "condition"
    # --- condition edges only ---
    operator: str | None = None
    values: list[str] = dc_field(default_factory=list)
    actions: list[str] = dc_field(default_factory=list)  # required | forbidden | show | …
    scope: list[str] | None = None                       # Bundesländer the rule is limited to
    rule_id: str | None = None
    text: str = ""                                       # the sentence, or the API's message
    bezug: list[str] = dc_field(default_factory=list)    # legal basis of the rule itself
    certain: bool = True
    origin: str = ""                                     # "api" | "freitext"
    condition: dict | bool | None = None                 # the untouched API condition tree
    # the ids as the *rule* named them; parent/child above are those resolved onto nodes.
    # They differ whenever a rule names an id that occurs at several places or not at all.
    source_id: str | None = None
    target_id: str | None = None
    context: list[str] = dc_field(default_factory=list)  # where the rule sat in the tree

    @property
    def resolved(self) -> bool:
        """ Both ends landed on a real node — a rule naming an unknown id has not. """
        return not (self.target_id and self.child is None)

class Graph:
    """
        Nodes plus both edge kinds, with the schema's metadata.

        Deliberately knows nothing about XML: collect_graph_data() is the XDF adapter, and a
        second adapter (PDF forms) can fill the same structure later.
    """

    def __init__(self, schema: dict | None = None):
        self.schema = schema or {}
        self.nodes: dict[str, Node] = {}     # keyed by path_id, insertion = document order
        self.edges: list[Edge] = []
        # the XZuFi side: what the applicant is told, as opposed to what they are asked.
        # Empty when no Leistung could be matched — see find_leistungsschluessel.
        self.leistung: dict = {}

    # --- building ---

    def add(self, node: Node) -> Node:
        """ Registers a node and links it to its parent with a contains edge. """
        self.nodes[node.path_id] = node
        if node.parent is not None:
            self.nodes[node.parent].children.append(node.path_id)
            self.edges.append(Edge(parent=node.parent, child=node.path_id, kind="contains"))
        return node

    def connect(self, edge: Edge) -> Edge:
        self.edges.append(edge)
        return edge

    # --- reading ---

    def of_kind(self, kind: str) -> list[Edge]:
        return [e for e in self.edges if e.kind == kind]

    def fields(self) -> list[Node]:
        """ Field nodes in document order — the things a citizen is actually asked. """
        return [n for n in self.nodes.values() if n.kind == "field"]

    def conditional(self) -> set[str]:
        """ path_ids that some certain rule makes situational. """
        return {e.child for e in self.edges
                if e.kind == "condition" and e.certain and e.parent and e.child}

    def cycles(self) -> list[list[str]]:
        """
            Cycles among certain condition edges — reported, never silently broken.

            A cycle means two fields condition each other. That is a modelling question for
            the Fachstelle, so the graph names it instead of picking an order.
        """
        neighbours: dict[str, set[str]] = {}
        for e in self.edges:
            if e.kind == "condition" and e.certain and e.parent and e.child:
                neighbours.setdefault(e.parent, set()).add(e.child)

        found, open_set, done = [], set(), set()

        def walk(node_id, path):
            if node_id in open_set:                   # back edge → the cycle is path from here
                found.append(path[path.index(node_id):] + [node_id])
                return
            if node_id in done:
                return
            open_set.add(node_id)
            for neighbour in sorted(neighbours.get(node_id, ())):
                walk(neighbour, path + [node_id])
            open_set.discard(node_id)
            done.add(node_id)

        for start in sorted(neighbours):
            walk(start, [])
        return found

    def ask_order(self) -> list[str]:
        """
            The order to ask the fields in: the schema's own document order.

            The XDF file is the authority here — it is how the Bundesredaktion laid the form
            out. Condition edges are checked against it by violations(), not used to reorder:
            silently rearranging questions would invent an order nobody wrote down.
        """
        return [n.path_id for n in self.fields()]

    def violations(self) -> list[tuple[str, str]]:
        """
            (deciding field, dependent field) pairs where the dependent is asked first.

            A copilot cannot evaluate a condition whose source is still unanswered, so every
            pair here is a place where document order and the rules disagree.
        """
        rank = {path_id: i for i, path_id in enumerate(self.ask_order())}
        return [(e.parent, e.child) for e in self.edges
                if e.kind == "condition" and e.certain and e.parent in rank and e.child in rank
                and rank[e.parent] > rank[e.child]]

    # --- output ---

    def statistics(self) -> dict:
        certain = [e for e in self.of_kind("condition") if e.certain]
        return {
            "nodes": len(self.nodes),
            "fields": sum(1 for n in self.nodes.values() if n.kind == "field"),
            "edges_contains": len(self.of_kind("contains")),
            "edges_condition": len(self.of_kind("condition")),
            "edges_certain": len(certain),
            "edges_unclear": len(self.of_kind("condition")) - len(certain),
            "edges_from_api": sum(1 for e in self.of_kind("condition") if e.origin == "api"),
            "edges_from_freitext": sum(1 for e in self.of_kind("condition")
                                       if e.origin == "freitext"),
            # a rule that names an id no node carries, or one that occurs at several places
            # and could not be pinned down by the rule's own position
            "edges_unresolved": sum(1 for e in certain if not e.resolved),
            "cycles": len(self.cycles()),
            "order_violations": len(self.violations()),
        }

    def to_dict(self) -> dict:
        """
            The graph.json payload — nodes and edges as lists, so document order survives.

            Self-contained on purpose: cycles and the mermaid rendering are materialised here
            rather than recomputed, so anything reading graph.json (the skill compiler, a
            copilot) needs the file and nothing else.
        """
        return {
            "schema": self.schema,
            "leistung": self.leistung,
            "statistics": self.statistics(),
            "ask_order": self.ask_order(),
            "cycles_detail": self.cycles(),
            "order_violations": self.violations(),
            "mermaid": self.to_mermaid(),
            "nodes": [asdict(n) for n in self.nodes.values()],
            "edges": [asdict(e) | {"resolved": e.resolved} for e in self.edges],
        }

    def to_mermaid(self, max_edges: int = 60) -> str:
        """
            Mermaid flowchart of the condition edges — contains edges would only add noise.

            Uncertain edges are drawn as yellow notes, matching the marking in the skill file;
            past `max_edges` the graph is truncated rather than rendered into a hairball.
        """
        label = {p: (n.label or n.id)[:38] for p, n in self.nodes.items()}
        style = {"required": "==>", "forbidden": "-.->", "hide": "-.->", "show": "-->"}

        lines, unclear, shown = ["flowchart TD"], [], 0
        for e in self.of_kind("condition"):
            if not e.certain:
                unclear.append(e)
                continue
            # no parent: unconditional. no child: a rule over several fields at once.
            if not e.parent or not e.child or shown >= max_edges:
                continue
            arrow = style.get(e.actions[0] if e.actions else "", "-->")
            value = ", ".join(e.values)[:28] or "?"
            text = f'{e.operator or "?"} {value} → {"+".join(e.actions)}'
            if e.scope:
                text += f' [{",".join(e.scope)}]'
            lines.append(f'  {_mermaid_id(e.parent)}["{label.get(e.parent, e.parent)}"] '
                         f'{arrow}|"{text}"| {_mermaid_id(e.child)}["{label.get(e.child, e.child)}"]')
            shown += 1

        for i, e in enumerate(unclear[:10]):
            lines.append(f'  unclear{i}["?: {e.text[:60]}"]:::unclear')
        if unclear:
            lines.append("  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000")
        return "\n".join(lines)

def _mermaid_id(path_id: str) -> str:
    """ Dots separate mermaid syntax, so a path_id has to be flattened for a node name. """
    return path_id.replace(".", "_")

# ---------------------------------------------------------------------
# XDF adapter

def _walk(element, graph: Graph, parent: str | None = None, path: tuple[str, ...] = ()):
    """
        Depth-first over struktur/enthaelt, adding one Node per group or field.

        `anzahl` sits on the <struktur> wrapper, not on the element: cardinality belongs to the
        *position*, so the same baukasten group is mandatory in one place and optional in
        another. That is also why it is read from the wrapper here and not from the element.
    """
    for wrapper in element.findall(X + "struktur"):
        anzahl = get_child_value(wrapper, "anzahl", recursive=False) or ""
        for enthaelt in wrapper.findall(X + "enthaelt"):
            for child in enthaelt:
                eid = get_id(child)
                if not eid:
                    continue
                path_id = ".".join(path + (eid,))
                graph.add(Node(
                    path_id=path_id, id=eid, version=get_version(child),
                    kind="group" if child.tag.split("}")[-1].endswith("gruppe") else "field",
                    # bezeichnungEingabe is already phrased as a question ("In welcher Art
                    # Beschäftigungsverhältnis steht die Frau?"); `name` is the file-keeping
                    # term and only stands in when the citizen-facing one is missing
                    label=(get_child_value(child, "bezeichnungEingabe", recursive=False)
                           or get_child_value(child, "name", recursive=False) or ""),
                    name=get_child_value(child, "name", recursive=False) or "",
                    definition=get_child_value(child, "definition", recursive=False) or "",
                    hilfetext=get_child_value(child, "hilfetextEingabe", recursive=False) or "",
                    feldart=get_child_value(child, "feldart", recursive=False) or "",
                    datentyp=get_child_value(child, "datentyp", recursive=False) or "",
                    werte=get_werte(child), anzahl=anzahl, required=anzahl.startswith("1"),
                    bezug=[b.text.strip() for b in child.findall(X + "bezug") if b.text],
                    path=list(path), parent=parent))
                _walk(child, graph, parent=path_id, path=path + (eid,))

def _inherit_bezug(graph: Graph):
    """
        Fills bezug_effective on every node: its own, else the nearest ancestor's, else the
        schema's.

        Measured on the corpus: 87 % of fields carry their own <bezug>, 13 % take a group's,
        6 fall through to the schema — none end up without one. bezug_source records which of
        the three it was, so a citation can always be traced back to where it is written.
    """
    for node in graph.nodes.values():
        if node.bezug:
            node.bezug_effective, node.bezug_source = list(node.bezug), "self"
            continue
        ancestor = graph.nodes.get(node.parent) if node.parent else None
        while ancestor is not None:
            if ancestor.bezug:
                node.bezug_effective, node.bezug_source = list(ancestor.bezug), ancestor.path_id
                break
            ancestor = graph.nodes.get(ancestor.parent) if ancestor.parent else None
        else:
            if schema_bezug := graph.schema.get("bezug"):
                node.bezug_effective, node.bezug_source = list(schema_bezug), "schema"

def _rule_bezug(element) -> dict[str, list[str]]:
    """
        R… id → the <bezug> written on that rule, for the rules of one element.

        155 of the 2390 rules in the corpus name their own legal basis, which is more precise
        than the field's: it is the paragraph that makes *this condition* apply.
    """
    out = {}
    for rule in element.findall(X + "regel"):
        if bezug := [b.text.strip() for b in rule.findall(X + "bezug") if b.text]:
            out[get_id(rule)] = bezug
    return out

def _resolver(graph: Graph):
    """
        Builds `resolve(bare_id, context) -> path_id | None` for this graph.

        Rules name elements by bare id, and baukasten reuse makes bare ids ambiguous (49 % of
        edges in the corpus without this). Where the rule sits in the tree says which instance
        it means: an address rule under the workplace is about *that* address. What stays
        ambiguous returns None instead of picking one.
    """
    by_id: dict[str, list[Node]] = {}
    for node in graph.nodes.values():
        by_id.setdefault(node.id, []).append(node)

    def resolve(bare_id: str, context: list[str]) -> str | None:
        candidates = by_id.get(bare_id, [])
        if len(candidates) == 1:
            return candidates[0].path_id
        for depth in range(len(context), 0, -1):        # nearest enclosing scope wins
            prefix = ".".join(context[:depth])
            narrower = [c for c in candidates
                        if c.path_id == prefix or c.path_id.startswith(prefix + ".")]
            if len(narrower) == 1:
                return narrower[0].path_id
        return None

    return resolve

def _conditions(schema, graph: Graph, use_api: bool = True):
    """
        Adds one condition edge per rule statement.

        Per rule-bearing element the API translation wins where it exists; the freitext
        grammar runs only for the elements the API answers with 404.
    """
    resolve = _resolver(graph)
    for element, path in iter_rule_bearers(schema):
        eid = get_id(element)
        translated = get_translated_rules(eid, get_version(element)) if use_api and eid else None
        if translated is not None:
            # the API returns no R… ids of its own, so the bearing element is the reference
            parsed = parse_translation(translated, rule_id=eid)
        else:
            parsed = []
            for rule in element.findall(X + "regel"):
                if text := get_child_value(rule, "freitextRegel", recursive=False):
                    parsed += parse_rule(html.unescape(text), get_id(rule))

        # a freitext edge knows its R… id, so it gets exactly the rule's own bezug. An API
        # edge is keyed by the bearing element, so it can only be attributed when the element's
        # rules agree on one — otherwise the citation would be guesswork.
        bezug_by_rule = _rule_bezug(element)
        distinct = {tuple(b) for b in bezug_by_rule.values()}
        element_bezug = list(distinct.pop()) if len(distinct) == 1 else []

        for edge in parsed:
            graph.connect(Edge(
                bezug=bezug_by_rule.get(edge.rule_id or "", element_bezug),
                parent=resolve(edge.source, list(path)) if edge.source else None,
                child=resolve(edge.target, list(path)) if edge.target else None,
                kind="condition",
                operator=edge.operator, values=edge.values, actions=edge.actions,
                scope=edge.scope, rule_id=edge.rule_id, text=edge.text,
                certain=edge.certain, origin=edge.origin, condition=edge.condition,
                source_id=edge.source, target_id=edge.target, context=list(path)))

def _attach_leistung(graph: Graph):
    """
        Adds the XZuFi texts of the Leistung this schema belongs to.

        Best effort by construction: the join is not modelled in FIM, so it is established
        heuristically and verified against the legal basis. An unconfirmed match keeps the
        key and the verdict but no texts — a wrong Frist or Gebühr, stated as confidently as
        the field rules, would break exactly the promise this pipeline exists to keep.
    """
    treffer = find_leistungsschluessel(graph.schema.get("bezeichnung") or "",
                                       graph.schema.get("bezug") or [])
    graph.leistung = dict(treffer)
    if treffer["join"] != "bestaetigt" or not treffer["leistungsschluessel"]:
        return
    try:
        graph.leistung |= get_leistung_texte(treffer["leistungsschluessel"])
    except Exception as e:                        # the graph itself must not depend on XZuFi
        graph.leistung["evidence"] += f" · Texte nicht abrufbar: {type(e).__name__}"

def collect_graph_data(xdf_path: Path, meta: dict | None = None, use_api: bool = True,
                       with_leistung: bool = True) -> Graph:
    """
        Reads one XDF 3.0 file into a Graph.

        Arguments:
            xdf_path: a schema.xdf.xml as the FIM API delivers it.
            meta:     the harvest metadata beside it, for Reifegrad and source URL.
            use_api:  False keeps everything local — for tests and offline runs.

        Returns:
            The Graph: nodes in document order, contains edges from the structure,
            condition edges from the rules.
    """
    root = ET.parse(xdf_path).getroot()
    # XDF 2.0 uses a different namespace, has no <freitextRegel> and models values through
    # <praezisierung>. Every findall below would return nothing, so an unsupported file has
    # to fail loudly instead of producing an empty graph that looks compiled.
    if (found := get_xdf_namespace(root)) and not found.startswith("urn:xoev-de:fim:standard:xdatenfelder_3"):
        raise ValueError(f"{xdf_path.name}: XDF-Namespace {found} wird nicht unterstützt, "
                         "der Compiler liest XDatenfelder 3.x")

    schema = root.find(X + "stammdatenschema")
    if schema is None:
        raise ValueError(f"no <stammdatenschema> in {xdf_path} — expected an XDF 3.0 schema")

    meta = meta or {}
    graph = Graph({
        "fim_id": get_id(schema),
        "fim_version": get_version(schema),
        "bezeichnung": (get_child_value(schema, "bezeichnung", recursive=False)
                        or get_child_value(schema, "name", recursive=False) or ""),
        "definition": get_child_value(schema, "definition", recursive=False) or "",
        "freigabe_status_label": meta.get("freigabe_status_label"),
        "bezug": [b.text.strip() for b in schema.findall(X + "bezug") if b.text],
        "source_url": meta.get("source_url"),
        "compiled_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    })
    _walk(schema, graph)
    _inherit_bezug(graph)          # needs the whole tree, so it runs after _walk
    _conditions(schema, graph, use_api=use_api)
    if use_api and with_leistung:
        _attach_leistung(graph)
    return graph

# ---------------------------------------------------------------------
# Files

def write_graph(graph: Graph, target: Path) -> Path:
    """ Writes graph.json. utf-8 explicitly — the labels are full of umlauts. """
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(graph.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    return target

def compile_schema(fim_id: str, corpus: Path = TARGET_LOCATION, use_api: bool = True) -> Graph:
    """
        Compiles one harvested schema into graph.json and graph.mmd beside its source.

        Everything for one schema stays in one folder — the XDF it came from, the metadata,
        the graph and the diagram. The mermaid file is a copy of what graph.json already
        carries, written out separately so it can be rendered without unpacking the JSON.

        Arguments:
            fim_id:  the FIM id, i.e. the folder name under `corpus`.
            corpus:  root of the harvested data.
            use_api: False skips translated-rules and uses the freitext grammar throughout.

        Returns:
            The compiled Graph.
    """
    source = corpus / fim_id
    meta_path = source / "meta.json"
    meta = json.loads(meta_path.read_text("utf-8")) if meta_path.exists() else {}
    graph = collect_graph_data(source / "schema.xdf.xml", meta, use_api=use_api)
    write_graph(graph, source / "graph.json")
    (source / "graph.mmd").write_text(graph.to_mermaid(), encoding="utf-8")
    return graph
