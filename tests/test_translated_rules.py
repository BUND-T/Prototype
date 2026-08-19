"""
    translated-rules (API) → Edge.

    All offline: the payloads below are verbatim responses from
    /api/v1/translated-rules, so the flattener is tested without a network call.
"""

from prototype.rule_parser import parse_translation, _flatten


def test_equal_becomes_a_conditional_edge():
    """ The common case: one field's value decides another field. """
    edge, = parse_translation([{
        "effect": "require",
        "target": "self.F17000009298",
        "message": "Das Feld … muss angegeben werden, wenn 'Beschäftigungsverhältnis' den Wert '999' hat.",
        "condition": {"equal": [{"identifier": "self.F00000003391"}, "999"]},
    }], rule_id="G00000002193")

    assert edge.target == "F17000009298"        # "self." stripped
    assert edge.source == "F00000003391"
    assert edge.operator == "=" and edge.values == ["999"]
    assert edge.actions == ["required"]         # API "require" → our vocabulary
    assert edge.origin == "api" and edge.certain
    assert edge.text.startswith("Das Feld")     # the API's own wording is kept


def test_negation_is_inverted_not_nested():
    """ not(equal) is the same statement as not_equal — the flat edge must say so. """
    edge, = parse_translation([{
        "effect": "forbid", "target": "self.F05000016256",
        "message": "…", "condition": {"not": {"equal": [{"identifier": "self.F05000016255"}, "001"]}},
    }])
    assert edge.operator == "<>" and edge.values == ["001"]
    assert edge.actions == ["forbidden"]


def test_bare_identifier_is_a_yes_no_field():
    """ condition = the field itself means "wenn die Abfrage bejaht wird". """
    edge, = parse_translation([{
        "effect": "require", "target": "self.G60000000220",
        "message": "…", "condition": {"identifier": "self.F00000003327"},
    }])
    assert (edge.source, edge.operator, edge.values) == ("F00000003327", "=", ["wahr"])


def test_is_empty_maps_onto_the_operators_the_grammar_already_uses():
    """
        Both extractions must speak one language: "leer"/"nicht leer" is what parse_rule
        produces from "wenn F… leer ist", so the API's is_empty has to land on the same words.
    """
    assert _flatten({"is_empty": {"identifier": "F60000000231"}}) == ("F60000000231", "leer", [])
    assert _flatten({"not": {"is_empty": {"identifier": "F60000000231"}}}) \
        == ("F60000000231", "nicht leer", [])


def test_negation_of_an_unflattenable_condition_keeps_nothing():
    """
        The trap: without an inverse the old code returned (source, None) — a field named as
        the condition, with the relation silently dropped. Half a statement is worse than none.
    """
    assert _flatten({"not": {"xor": [{"identifier": "F1"}, {"identifier": "F2"}]}}) \
        == (None, None, [])


def test_and_is_not_squashed_into_one_source():
    """ "F1 leer UND F2 leer" has two sources; a flat edge has room for one. """
    condition = {"and": [{"is_empty": {"identifier": "F1"}},
                         {"is_empty": {"identifier": "F2"}}]}
    assert _flatten(condition) == (None, None, [])

    edge, = parse_translation([{"effect": "valid", "message": "…", "condition": condition}])
    assert edge.condition == condition           # the tree survives the flattener giving up


def test_or_over_one_field_collapses_into_a_value_list():
    assert _flatten({"or": [
        {"equal": [{"identifier": "F1"}, "001"]},
        {"equal": [{"identifier": "F1"}, "002"]},
    ]}) == ("F1", "=", ["001", "002"])


def test_or_across_two_fields_is_not_squashed():
    """
        The dangerous case: flattening this would claim F1 alone decides. It must stay
        unflattened — and the raw tree has to survive on the edge.
    """
    condition = {"or": [
        {"equal": [{"identifier": "F1"}, True]},
        {"equal": [{"identifier": "F2"}, True]},
    ]}
    assert _flatten(condition) == (None, None, [])

    edge, = parse_translation([{"effect": "valid", "message": "Mindestens eines der Felder …",
                                "condition": condition}])
    assert edge.target is None                  # no single field is affected
    assert edge.source is None                  # nothing invented
    assert edge.condition == condition           # nothing lost either
    assert edge.actions == ["validation"] and edge.certain


def test_unconditional_rule_has_no_source():
    edge, = parse_translation([{"effect": "forbid", "target": "self.F05000019538",
                                "message": "… darf nicht angezeigt werden.", "condition": True}])
    assert edge.source is None and edge.values == []
    assert edge.target == "F05000019538"


def test_booleans_use_the_same_words_as_the_freitext_parser():
    """ The grammar yields "wahr"/"falsch" from prose; the API yields JSON true/false. """
    _, operator, values = _flatten({"equal": [{"identifier": "F1"}, True]})
    assert (operator, values) == ("=", ["wahr"])


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
