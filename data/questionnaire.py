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
}

SIZES = {
    "size_1": "Size 1",
    "size_2": "Size 2",
    "size_3": "Size 3",
    "size_4": "Size 4",
}

DEFAULTS = {
    "segment": "segment_1",
    "item_a": "a1",
    "item_b": "b1",
    "size": "size_1",
}
