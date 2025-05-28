from .questionnaire import CATEGORY_GROUP_MAP, ITEM_GROUP_MAP


def get_available_groups(category_key: str) -> list:
    if not category_key:
        return []

    return CATEGORY_GROUP_MAP.get(category_key, [])


def get_available_items(item_type: str, group_key: str) -> list:
    if item_type not in ITEM_GROUP_MAP:
        return []

    available = []
    for item_key, groups in ITEM_GROUP_MAP[item_type].items():
        if groups.get(group_key):
            available.append(item_key)

    return available
