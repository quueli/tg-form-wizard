# sample config, the real one comes from the client's catalogue
SEGMENTS = {
    "segment_1": "Segment 1",
    "segment_2": "Segment 2",
}

CATEGORIES = {
    "category_1": "Category 1",
    "category_2": "Category 2",
    "category_3": "Category 3",
    "category_4": "Category 4",
}

CATEGORY_GROUP_MAP = {
    "category_1": ["group_1", "group_2", "group_3"],
    "category_2": ["group_2", "group_3", "group_4"],
    "category_3": ["group_1", "group_4", "group_5"],
    "category_4": ["group_3", "group_5"],
}

GROUPS = {
    "group_1": "Group 1",
    "group_2": "Group 2",
    "group_3": "Group 3",
    "group_4": "Group 4",
    "group_5": "Group 5",
}

VARIANTS = {
    "variant_1": "Variant 1",
    "variant_2": "Variant 2",
    "variant_3": "Variant 3",
    "variant_4": "Variant 4",
}

ITEMS = {
    "a": {
        "a1": "Option A1",
        "a2": "Option A2",
        "a3": "Option A3",
        "a4": "Option A4",
        "a5": "Option A5",
        "a6": "Option A6",
    },
    "b": {
        "b1": "Option B1",
        "b2": "Option B2",
        "b3": "Option B3",
        "b4": "Option B4",
        "b5": "Option B5",
    },
    "c": {
        "c1": "Option C1",
        "c2": "Option C2",
        "c3": "Option C3",
        "c4": "Option C4",
    },
}

ITEM_GROUP_MAP = {
    "a": {
        "a1": {"group_1": True, "group_2": True, "group_3": True, "group_4": True, "group_5": True},
        "a2": {"group_1": True, "group_2": True},
        "a3": {"group_2": True, "group_3": True},
        "a4": {"group_3": True, "group_4": True},
        "a5": {"group_4": True, "group_5": True},
        "a6": {"group_1": True, "group_5": True},
    },
    "b": {
        "b1": {"group_1": True, "group_2": True, "group_3": True, "group_4": True, "group_5": True},
        "b2": {"group_1": True, "group_2": True},
        "b3": {"group_2": True, "group_3": True, "group_4": True},
        "b4": {"group_4": True, "group_5": True},
        "b5": {"group_1": True, "group_5": True},
    },
    "c": {
        "c1": {"group_1": True, "group_2": True, "group_3": True, "group_4": True, "group_5": True},
        "c2": {"group_1": True, "group_3": True, "group_5": True},
        "c3": {"group_2": True, "group_4": True},
        "c4": {"group_1": True, "group_2": True, "group_3": True, "group_4": True, "group_5": True},
    },
}

# item_c narrows by variant on top of the group filter
ITEM_VARIANT_MAP = {
    "c1": {"variant_1": True, "variant_2": True, "variant_3": True, "variant_4": True},
    "c2": {"variant_1": True, "variant_4": True},
    "c3": {"variant_2": True, "variant_3": True},
    "c4": {"variant_1": True},
}

SIZES = {
    "size_1": "Size 1",
    "size_2": "Size 2",
    "size_3": "Size 3",
    "size_4": "Size 4",
}

LEVELS = {
    "level_1": "Level 1",
    "level_2": "Level 2",
    "level_3": "Level 3",
    "level_4": "Level 4",
}

LEVEL_GROUP_MAP = {
    "level_1": {"group_1": True, "group_2": True, "group_3": True, "group_4": True, "group_5": True},
    "level_2": {"group_1": True, "group_2": True},
    "level_3": {"group_2": True, "group_3": True, "group_4": True},
    "level_4": {"group_4": True, "group_5": True},
}

SPEEDS = {
    "speed_1": "Speed 1",
    "speed_2": "Speed 2",
    "speed_3": "Speed 3",
}

TAGS = {
    "tag_1": "Tag 1",
    "tag_2": "Tag 2",
    "tag_3": "Tag 3",
    "tag_4": "Tag 4",
    "tag_5": "Tag 5",
    "tag_6": "Tag 6",
}

TAG_GROUP_MAP = {
    "tag_1": {"group_1": True, "group_2": True, "group_3": True, "group_4": True, "group_5": True},
    "tag_2": {"group_1": True, "group_2": True},
    "tag_3": {"group_2": True, "group_3": True},
    "tag_4": {"group_3": True, "group_4": True},
    "tag_5": {"group_4": True, "group_5": True},
    "tag_6": {"group_1": True, "group_5": True},
}

PRIORITIES = {
    "priority_1": "Priority 1",
    "priority_2": "Priority 2",
    "priority_3": "Priority 3",
}

TRACKS = {
    "track_1": "Track 1",
    "track_2": "Track 2",
    "track_3": "Track 3",
    "track_4": "Track 4",
    "track_5": "Track 5",
    "track_6": "Track 6",
}

PRIORITY_TRACK_MAP = {
    "priority_1": ["track_1", "track_2"],
    "priority_2": ["track_3", "track_4", "track_5"],
    "priority_3": ["track_5", "track_6"],
}

OPTIONS_FINAL = {
    "option_1": "Option 1",
    "option_2": "Option 2",
    "option_3": "Option 3",
    "option_4": "Option 4",
    "option_5": "Option 5",
    "option_6": "Option 6",
    "option_7": "Option 7",
    "option_8": "Option 8",
    "option_9": "Option 9",
    "option_10": "Option 10",
    "option_11": "Option 11",
    "option_12": "Option 12",
}

TRACK_OPTION_MAP = {
    "track_1": ["option_1", "option_2"],
    "track_2": ["option_2", "option_3", "option_4"],
    "track_3": ["option_4", "option_5"],
    "track_4": ["option_5", "option_6", "option_7", "option_8"],
    "track_5": ["option_8", "option_9", "option_10"],
    "track_6": ["option_10", "option_11", "option_12"],
}

FLAGS = {
    "flag_1": "Flag 1",
    "flag_2": "Flag 2",
    "flag_3": "Flag 3",
    "flag_4": "Flag 4",
    "flag_5": "Flag 5",
    "flag_6": "Flag 6",
    "flag_7": "Flag 7",
    "flag_8": "Flag 8",
}

# flags in one group are mutually exclusive, picking one drops the rest
FLAG_GROUPS = {
    "zone_1": ["flag_1", "flag_2"],
    "zone_2": ["flag_3", "flag_4", "flag_5"],
}

CUSTOMER_TYPES = {
    "type_1": "Type 1",
    "type_2": "Type 2",
    "type_3": "Type 3",
    "type_4": "Type 4",
}

DISABLED = {
    "segment": ["segment_2"],
    "category": ["category_4"],
    "group": ["group_5"],
    "items": {"a": [], "b": [], "c": []},
}

DEFAULTS = {
    "segment": "segment_1",
    "item_a": "a1",
    "item_b": "b1",
    "item_c": "c1",
    "size": "size_1",
    "level": "level_1",
    "speed": "speed_1",
    "priority": "priority_1",
    "flags": [],
    "customer_type": "type_1",
}
