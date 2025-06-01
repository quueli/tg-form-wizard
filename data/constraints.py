from .questionnaire import (
    CATEGORY_GROUP_MAP,
    DEFAULTS,
    DISABLED,
    ITEM_GROUP_MAP,
    ITEM_VARIANT_MAP,
)


def get_available_groups(category_key: str) -> list:
    if not category_key:
        return []

    available = CATEGORY_GROUP_MAP.get(category_key, [])
    disabled_groups = DISABLED.get("group", [])
    return [g for g in available if g not in disabled_groups]


def get_available_items_c(variant_key: str, group_key: str) -> list:
    available = []
    for item_key, variants in ITEM_VARIANT_MAP.items():
        if variant_key in variants and variants[variant_key]:
            if group_key in ITEM_GROUP_MAP["c"].get(item_key, {}):
                available.append(item_key)
    return available


def get_available_items(item_type: str, group_key: str) -> list:
    if item_type not in ("a", "b", "c"):
        return []

    available = []
    item_options = ITEM_GROUP_MAP[item_type]

    for item_key, groups in item_options.items():
        if group_key in groups and groups[group_key]:
            available.append(item_key)

    disabled_items = DISABLED.get("items", {}).get(item_type, [])
    return [i for i in available if i not in disabled_items]


def should_include_size(item_a_choices: dict, item_b_choices: dict) -> bool:
    a1_excluded = any(item == "a1" and status == "exclude" for item, status in item_a_choices.items())
    b1_excluded = any(item == "b1" and status == "exclude" for item, status in item_b_choices.items())
    return not (a1_excluded and b1_excluded)


def get_available_levels(group_key: str) -> list:
    from data.questionnaire import LEVEL_GROUP_MAP, LEVELS

    available = []
    for level_key in LEVELS.keys():
        if group_key in LEVEL_GROUP_MAP.get(level_key, {}):
            available.append(level_key)

    if not available:
        available = list(LEVELS.keys())

    return available


def get_available_tracks(priority_key: str) -> list:
    from data.questionnaire import PRIORITY_TRACK_MAP, TRACKS

    if priority_key in PRIORITY_TRACK_MAP:
        return PRIORITY_TRACK_MAP[priority_key]

    return list(TRACKS.keys())


def get_available_options(priority_key: str, track_key: str) -> list:
    from data.questionnaire import OPTIONS_FINAL, TRACK_OPTION_MAP

    if track_key in TRACK_OPTION_MAP:
        return TRACK_OPTION_MAP[track_key]

    return list(OPTIONS_FINAL.keys())


def reset_dependent_answers(current_state: str, answers: dict) -> dict:
    # changing an answer invalidates everything picked after it
    reset_map = {
        "segment": ["category", "group", "variant", "item_a", "item_b", "item_c",
                    "size", "level", "priority", "track", "option_final"],
        "category": ["group", "item_a", "item_b", "item_c", "size", "level"],
        "group": ["item_a", "item_b", "item_c", "size", "level", "tags"],
        "variant": ["item_c"],
        "priority": ["track", "option_final"],
        "track": ["option_final"],
    }

    for state in reset_map.get(current_state, []):
        if state in answers:
            if state in DEFAULTS:
                answers[state] = DEFAULTS[state]
            else:
                del answers[state]

    return answers


def validate_flag_selection(selected_flags: list, new_flag: str) -> list:
    from data.questionnaire import FLAG_GROUPS

    new_flag_group = None
    for group_key, flags in FLAG_GROUPS.items():
        if new_flag in flags:
            new_flag_group = group_key
            break

    if not new_flag_group:
        if new_flag in selected_flags:
            selected_flags.remove(new_flag)
        else:
            selected_flags.append(new_flag)
        return selected_flags

    group_flags = FLAG_GROUPS[new_flag_group]
    selected_flags = [f for f in selected_flags if f not in group_flags]

    if new_flag not in selected_flags:
        selected_flags.append(new_flag)

    return selected_flags


def get_flag_groups() -> dict:
    from data.questionnaire import FLAG_GROUPS
    return dict(FLAG_GROUPS)
