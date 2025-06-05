from datetime import datetime

from data import questionnaire as q

COLUMNS = [
    ("segment", q.SEGMENTS),
    ("category", q.CATEGORIES),
    ("group", q.GROUPS),
    ("item_a", q.ITEMS["a"]),
    ("priority", q.PRIORITIES),
    ("track", q.TRACKS),
    ("option_final", q.OPTIONS_FINAL),
    ("notes", None),
]

HEADER = [key.replace("_", " ") for key, _ in COLUMNS]


def _label(value, lookup):
    if value is None or value == []:
        return ""
    if isinstance(value, (list, tuple)):
        return ", ".join(_label(v, lookup) for v in value)
    if lookup is not None:
        return lookup.get(value, str(value))
    return str(value)


def answers_to_row(answers: dict) -> list:
    return [_label(answers.get(key), lookup) for key, lookup in COLUMNS]


def append_xlsx(path: str, answers: dict) -> None:
    from openpyxl import Workbook, load_workbook

    try:
        wb = load_workbook(path)
        ws = wb.active
    except FileNotFoundError:
        wb = Workbook()
        ws = wb.active
        ws.title = "responses"
        ws.append(["timestamp", *HEADER])

    ws.append([datetime.now().isoformat(timespec="seconds"), *answers_to_row(answers)])
    wb.save(path)
