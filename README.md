# tg-form-wizard

![ci](https://github.com/quueli/tg-form-wizard/actions/workflows/ci.yml/badge.svg)

a telegram bot that walks a person through a long questionnaire (19 steps in the original) and puts the answers into a google sheet. the real questions are replaced with a dummy set in data/questionnaire.py, swap that module and the rest works as is.

the part that took actual thought: steps depend on each other. which groups you see depends on the category, which items on the group, which final options on the track. data/constraints.py answers "given what's chosen so far, what is still valid", and going back to an earlier step wipes everything downstream so you cant end up with stale answers. some steps are multi-select where every option is include / exclude / not set.

every answer is written to a per-session json file right away, so a bot restart doesnt lose someone in the middle of step 14.

## run

    pip install -r requirements.txt
    python -m examples.run_offline    # walks the cascade and writes an xlsx, no telegram needed
    pytest

for the actual bot put BOT_TOKEN in .env and `python bot.py`. export goes to xlsx by default, EXPORT_BACKEND=sheets plus a service account json switches it to google sheets.
