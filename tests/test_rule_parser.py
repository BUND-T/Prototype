from prototype.rule_parser import parse_rule

def test_two_branch_rule_yields_both_edges():
    """ The house style states both branches in one rule — both must become edges. """
    edges = parse_rule(
        'Wenn das Feld G60000000220.F60000000352 "Vertretung" = 001 "Nein", dann muss die '
        'Feldgruppe G00000001501.G00000000350.F00000000594 "Zahlung" befüllt sein. '
        'Wenn das Feld G60000000220.F60000000352 "Vertretung" <> 001 "Nein", dann darf die '
        'Feldgruppe G00000001501.G00000000350.F00000000594 "Zahlung" nicht befüllt sein.',
        rule_id="R00000001361")

    assert len(edges) == 2 and all(k.certain for k in edges)
    ja, nein = edges
    assert (ja.source, ja.operator, ja.target) == ("F60000000352", "=", "F00000000594")
    assert ja.actions == ["required"] and nein.actions == ["forbidden"] and nein.operator == "<>"
    assert ja.values == ["001 Nein"], ja.values
    assert ja.target == "F00000000594", "the dotted path names context; the leaf is the target"

def test_typed_actions_from_mutterschutz():
    """ S00000000371 states the action outright — aktiviere / deaktiviere, not just 'befüllt'. """
    edges = parse_rule(
        "WENN F17000009294 'Status der Frau' = 001 'schwanger', DANN aktiviere F17000009295 "
        "'Entbindungstermin' UND mache es zu einer Pflichtangabe. "
        "WENN F17000009294 'Status der Frau' = 002 'stillend', DANN deaktiviere F17000009295 "
        "'Entbindungstermin'.")

    # "aktiviere F…295 UND mache es zu einer Pflichtangabe" is two edges on the same target,
    # not one merged edge — merging them once produced "show and hide at the same time".
    assert [(k.target, k.actions) for k in edges] == [
        ("F17000009295", ["show"]),
        ("F17000009295", ["required"]),
        ("F17000009295", ["hide"]),
    ], [(k.target, k.actions) for k in edges]
    assert edges[1].target == "F17000009295", "'mache es zu…' refers back to the previous clause"
    assert all(k.source == "F17000009294" for k in edges)

def test_legal_form_labels_do_not_split_the_sentence():
    """ "AG & Co. KG" carries a period — splitting there produced 224 junk fragments. """
    edges = parse_rule(
        'Wenn das Feld F05000017001 "Rechtsform" = 111221 "AG & Co. KG", dann muss das Feld '
        'F05000017002 "Registernummer" befüllt werden.')

    assert len(edges) == 1 and edges[0].certain
    assert edges[0].target == "F05000017002" and edges[0].actions == ["required"]

def test_land_scope_applies_and_resets():
    """ Scope carries into the clause and 'für alle anderen Länder' clears it again. """
    edges = parse_rule(
        'Für die Länder NW, SL gilt: Die Datengruppe G05000017100 "Ausweis" muss befüllt werden. '
        'Für alle anderen Länder gilt: Die Datengruppe G05000017100 "Ausweis" darf nicht befüllt werden.')

    assert edges[0].scope == ["NW", "SL"] and edges[0].actions == ["required"]
    assert edges[1].scope is None and edges[1].actions == ["forbidden"]

def test_unparsed_sentence_is_kept_and_flagged():
    """ An edge we cannot read must stay visible, never be dropped. """
    edges = parse_rule("Die Mitgliedstaaten der EU sind alphabetisch sortiert: Belgien, Dänemark.")

    assert len(edges) == 1
    assert edges[0].certain is False and edges[0].actions == ["unclear"]
    assert "Mitgliedstaaten" in edges[0].text, "the original wording must survive for review"

if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("ok")
