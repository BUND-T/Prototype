from prototype.graph import Graph, Edge, collect_graph_data
from prototype.skill import build_skill

# Same baukasten group under two parents — the case that made SKILL.md list every address
# field twice under one heading, and that makes a bare id useless as a key.
XDF = """<?xml version='1.0' encoding='utf-8'?>
<xdf3:xdatenfelder.stammdatenschema.0102 xmlns:xdf3="urn:xoev-de:fim:standard:xdatenfelder_3.0.0">
 <xdf3:stammdatenschema>
  <xdf3:identifikation><xdf3:id>S00000000371</xdf3:id><xdf3:version>1.0.0</xdf3:version></xdf3:identifikation>
  <xdf3:name>Kurz</xdf3:name><xdf3:bezeichnung>Testantrag</xdf3:bezeichnung>
  <xdf3:bezug>&#167; 28 MuSchG</xdf3:bezug>
  <xdf3:regel>
   <xdf3:identifikation><xdf3:id>R00000002566</xdf3:id><xdf3:version>1.0.0</xdf3:version></xdf3:identifikation>
   <xdf3:name>Status</xdf3:name>
   <xdf3:freitextRegel>WENN F17000009294 'Status' = 001 'schwanger', DANN aktiviere F17000009295 'Termin' UND mache es zu einer Pflichtangabe.
Die Mitgliedstaaten sind alphabetisch sortiert: Belgien.</xdf3:freitextRegel>
  </xdf3:regel>
  <xdf3:struktur><xdf3:anzahl>1:1</xdf3:anzahl><xdf3:enthaelt>
   <xdf3:datenfeldgruppe>
    <xdf3:identifikation><xdf3:id>G00000002191</xdf3:id><xdf3:version>1.0.0</xdf3:version></xdf3:identifikation>
    <xdf3:name>Unternehmen</xdf3:name>
    <xdf3:struktur><xdf3:anzahl>1:1</xdf3:anzahl><xdf3:enthaelt>
     <xdf3:datenfeldgruppe>
      <xdf3:identifikation><xdf3:id>G60000000086</xdf3:id><xdf3:version>2.1.0</xdf3:version></xdf3:identifikation>
      <xdf3:name>Strassenanschrift</xdf3:name>
      <xdf3:struktur><xdf3:anzahl>1:1</xdf3:anzahl><xdf3:enthaelt>
       <xdf3:datenfeld>
        <xdf3:identifikation><xdf3:id>F60000000243</xdf3:id><xdf3:version>1.2.0</xdf3:version></xdf3:identifikation>
        <xdf3:bezeichnungEingabe>Strasse</xdf3:bezeichnungEingabe>
        <xdf3:feldart>select</xdf3:feldart>
        <xdf3:werte><xdf3:wert><xdf3:code>001</xdf3:code><xdf3:name>Hauptstrasse</xdf3:name></xdf3:wert></xdf3:werte>
       </xdf3:datenfeld>
      </xdf3:enthaelt></xdf3:struktur>
     </xdf3:datenfeldgruppe>
    </xdf3:enthaelt></xdf3:struktur>
   </xdf3:datenfeldgruppe>
  </xdf3:enthaelt></xdf3:struktur>
  <xdf3:struktur><xdf3:anzahl>0:1</xdf3:anzahl><xdf3:enthaelt>
   <xdf3:datenfeldgruppe>
    <xdf3:identifikation><xdf3:id>G00000002194</xdf3:id><xdf3:version>1.0.0</xdf3:version></xdf3:identifikation>
    <xdf3:name>Beschaeftigungsort</xdf3:name>
    <xdf3:struktur><xdf3:anzahl>0:1</xdf3:anzahl><xdf3:enthaelt>
     <xdf3:datenfeldgruppe>
      <xdf3:identifikation><xdf3:id>G60000000086</xdf3:id><xdf3:version>2.1.0</xdf3:version></xdf3:identifikation>
      <xdf3:name>Strassenanschrift</xdf3:name>
      <xdf3:regel>
       <xdf3:identifikation><xdf3:id>R60000000023</xdf3:id><xdf3:version>2.0.0</xdf3:version></xdf3:identifikation>
       <xdf3:name>StrasseHier</xdf3:name>
       <xdf3:freitextRegel>Wenn F60000000243 "Strasse" nicht leer, dann muss F60000000243 "Strasse" befüllt werden.</xdf3:freitextRegel>
      </xdf3:regel>
      <xdf3:struktur><xdf3:anzahl>0:1</xdf3:anzahl><xdf3:enthaelt>
       <xdf3:datenfeld>
        <xdf3:identifikation><xdf3:id>F60000000243</xdf3:id><xdf3:version>1.2.0</xdf3:version></xdf3:identifikation>
        <xdf3:bezeichnungEingabe>Strasse</xdf3:bezeichnungEingabe>
       </xdf3:datenfeld>
      </xdf3:enthaelt></xdf3:struktur>
     </xdf3:datenfeldgruppe>
    </xdf3:enthaelt></xdf3:struktur>
   </xdf3:datenfeldgruppe>
  </xdf3:enthaelt></xdf3:struktur>
 </xdf3:stammdatenschema>
</xdf3:xdatenfelder.stammdatenschema.0102>"""

def _graph(tmp_path):
    """
        The test schema as a Graph — deliberately offline.

        use_api=False keeps the freitext grammar in charge: the ids below are real ones, so a
        live translated-rules lookup would silently replace the rules this file is testing.
    """
    src = tmp_path / "schema.xdf.xml"
    src.write_text(XDF, encoding="utf-8")
    return collect_graph_data(src, {"freigabe_status_label": "fachlich freigegeben (gold)"},
                              use_api=False)

# --- structure -------------------------------------------------------

def test_reused_group_gets_distinct_paths(tmp_path):
    """ G60000000086 sits under two parents — same id, two nodes, two paths. """
    g = _graph(tmp_path)
    addresses = [n for n in g.nodes.values() if n.id == "G60000000086"]
    assert {n.path_id for n in addresses} == {
        "G00000002191.G60000000086", "G00000002194.G60000000086"}

def test_cardinality_belongs_to_the_position(tmp_path):
    """ The same group is mandatory under the company and optional under the workplace. """
    g = _graph(tmp_path)
    assert g.nodes["G00000002191.G60000000086"].required
    assert not g.nodes["G00000002194.G60000000086"].required

def test_children_are_recorded_in_document_order(tmp_path):
    """ A node at the bottom simply has no children — `children` says it, no extra class. """
    g = _graph(tmp_path)
    assert g.nodes["G00000002191.G60000000086.F60000000243"].children == []
    assert g.nodes["G00000002191.G60000000086"].children == [
        "G00000002191.G60000000086.F60000000243"]

def test_contains_edges_mirror_the_tree(tmp_path):
    """ Every node except the top-level ones is the child of exactly one contains edge. """
    g = _graph(tmp_path)
    contains = g.of_kind("contains")
    assert len(contains) == sum(1 for n in g.nodes.values() if n.parent is not None)
    assert len({e.child for e in contains}) == len(contains), "a node has one parent"
    assert ("G00000002191", "G00000002191.G60000000086") in [(e.parent, e.child) for e in contains]

def test_code_list_survives_into_the_node(tmp_path):
    """ The allowed answers exist only in the XDF export — the JSON API never serves them. """
    g = _graph(tmp_path)
    assert g.nodes["G00000002191.G60000000086.F60000000243"].werte == [
        {"code": "001", "name": "Hauptstrasse"}]

# --- rules -----------------------------------------------------------

def test_rule_position_resolves_the_duplicated_id(tmp_path):
    """
        F60000000243 exists twice; the rule sits inside the Beschaeftigungsort address, so
        that is the instance it means. Without this the corpus had 49 % ambiguous edges.
    """
    g = _graph(tmp_path)
    street = [e for e in g.of_kind("condition") if e.target_id == "F60000000243"]
    assert street, "the rule nested in the second address must produce an edge"
    assert all(e.child == "G00000002194.G60000000086.F60000000243" for e in street)
    assert all(e.context[:1] == ["G00000002194"] for e in street)
    assert all(e.resolved for e in street)

def test_rule_naming_an_absent_field_stays_unresolved(tmp_path):
    """ F17000009295 is named by a rule but is not in this schema — say so, do not guess. """
    g = _graph(tmp_path)
    orphan = [e for e in g.of_kind("condition") if e.target_id == "F17000009295"]
    assert orphan and all(e.child is None and not e.resolved for e in orphan)
    assert g.statistics()["edges_unresolved"] == len(orphan)

def test_unreadable_rule_is_kept_as_uncertain(tmp_path):
    g = _graph(tmp_path)
    assert g.statistics()["edges_unclear"] == 1
    assert all(e.origin == "freitext" for e in g.of_kind("condition"))

def test_cycle_detection_reports_a_loop():
    g = Graph()
    g.edges = [Edge(parent="A", child="B", kind="condition"),
               Edge(parent="B", child="A", kind="condition")]
    assert g.cycles(), "a two-node loop must be reported"

def test_contains_edges_never_count_as_cycles():
    """ The tree has no cycles, but only because cycles() ignores contains edges. """
    g = Graph()
    g.edges = [Edge(parent="A", child="B", kind="contains"),
               Edge(parent="B", child="A", kind="contains")]
    assert g.cycles() == []

def test_legal_basis_is_inherited_but_stays_marked(tmp_path):
    """
        87 % of fields carry their own <bezug>, the rest take a group's. Both end up in
        bezug_effective, and bezug_source says which — a citation must be traceable.
    """
    g = _graph(tmp_path)
    street = g.nodes["G00000002191.G60000000086.F60000000243"]
    assert street.bezug == [], "the test field carries none of its own"
    assert street.bezug_effective == ["§ 28 MuSchG"]
    assert street.bezug_source == "schema"

def test_rule_keeps_its_own_legal_basis(tmp_path):
    """ A rule naming a paragraph is more precise than the field it affects. """
    g = _graph(tmp_path)
    assert all(e.bezug == [] for e in g.of_kind("condition")), "no <bezug> on these rules"

# --- order -----------------------------------------------------------

def test_ask_order_is_document_order_of_the_fields(tmp_path):
    g = _graph(tmp_path)
    assert g.ask_order() == ["G00000002191.G60000000086.F60000000243",
                             "G00000002194.G60000000086.F60000000243"]
    assert all(g.nodes[p].kind == "field" for p in g.ask_order()), "groups are not questions"

def test_violations_are_reported_not_silently_reordered(tmp_path):
    """ A rule whose source is asked after its target is a finding, not something to fix. """
    g = _graph(tmp_path)
    assert g.violations() == []
    a, b = g.ask_order()
    g.connect(Edge(parent=b, child=a, kind="condition"))    # later field decides an earlier one
    assert g.violations() == [(b, a)]
    assert g.ask_order() == [a, b], "the order itself stays untouched"

# --- skill -----------------------------------------------------------

def test_unreadable_rule_survives_into_the_skill(tmp_path):
    """ The sentence the parser could not read must reach the reader, marked. """
    skill = build_skill(_graph(tmp_path).to_dict())
    assert skill.startswith("---\nname: antrag-s00000000371")
    assert "## Ungeklärte Regeln" in skill
    assert "<mark>Die Mitgliedstaaten" in skill, "unreadable rules are shown, never dropped"
    assert "§ 28 MuSchG" in skill and "fachlich freigegeben (gold)" in skill

def test_skill_lists_reused_group_once_per_position(tmp_path):
    """ Two headings, one per position — not one heading with the fields listed twice. """
    skill = build_skill(_graph(tmp_path).to_dict())
    assert "### Unternehmen › Strassenanschrift" in skill
    assert "### Beschaeftigungsort › Strassenanschrift" in skill

def test_skill_shows_no_contains_edges_in_the_condition_table(tmp_path):
    """ The condition table is about rules; structure is already in the field headings. """
    skill = build_skill(_graph(tmp_path).to_dict())
    table = [line for line in skill.splitlines() if line.startswith("| wenn")]
    assert table and len(table) == 1, table

if __name__ == "__main__":
    import pathlib, tempfile
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(pathlib.Path(tempfile.mkdtemp())) if fn.__code__.co_argcount else fn()
    print("ok")
