# python -m examples.run_offline
import tempfile
from pathlib import Path

from data import constraints as c
from data import questionnaire as q
from services.export import XlsxSheetWriter, answers_to_row


def walk() -> dict:
    answers: dict = {}

    answers["segment"] = next(iter(q.SEGMENTS))
    answers["category"] = "category_1"

    groups = c.get_available_groups(answers["category"])
    answers["group"] = groups[0]

    items_a = c.get_available_items("a", answers["group"])
    answers["item_a_include"] = items_a[:1]
    answers["item_a_exclude"] = items_a[1:2]

    answers["priority"] = "priority_1"
    answers["track"] = c.get_available_tracks(answers["priority"])[0]
    answers["option_final"] = c.get_available_options(answers["priority"], answers["track"])[0]
    answers["notes"] = "sample run"
    return answers


def main():
    answers = walk()
    print("answers:")
    for k, v in answers.items():
        print(f"  {k}: {v}")

    print("\nrow:")
    print("  " + " | ".join(x for x in answers_to_row(answers) if x))

    out = Path(tempfile.gettempdir()) / "tg_form_wizard_demo.xlsx"
    writer = XlsxSheetWriter(str(out))
    writer.append_answers(answers)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
