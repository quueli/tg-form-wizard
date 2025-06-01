from data import constraints as c


def test_groups_filtered_by_category():
    groups = c.get_available_groups("category_1")
    assert groups == ["group_1", "group_2", "group_3"]
    assert "group_5" not in c.get_available_groups("category_3")


def test_items_filtered_by_group():
    assert c.get_available_items("a", "group_2") == ["a1", "a2", "a3"]
    assert c.get_available_items("bad", "group_2") == []


def test_tracks_depend_on_priority():
    assert c.get_available_tracks("priority_1") == ["track_1", "track_2"]
    assert c.get_available_options("priority_1", "track_1") == ["option_1", "option_2"]


def test_reset_clears_downstream():
    answers = {
        "segment": "segment_1",
        "category": "category_1",
        "group": "group_2",
        "item_a": "a3",
        "level": "level_2",
    }
    out = c.reset_dependent_answers("category", answers)
    assert "group" not in out
    assert out.get("item_a") == "a1"
    assert out.get("level") == "level_1"
    assert out["category"] == "category_1"


def test_flags_are_radio_in_a_group():
    selected = c.validate_flag_selection([], "flag_1")
    assert selected == ["flag_1"]
    selected = c.validate_flag_selection(selected, "flag_2")
    assert "flag_1" not in selected
    assert "flag_2" in selected


def test_size_dropped_when_a1_b1_excluded():
    excluded = {"a1": "exclude"}
    assert c.should_include_size(excluded, {"b1": "exclude"}) is False
    assert c.should_include_size({"a2": "include"}, {}) is True
