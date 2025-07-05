# tg-form-wizard

a telegram bot that walks a person through a long questionnaire (19 steps in the original) and puts the answers into a google sheet. the real questions are replaced with a dummy set in data/questionnaire.py, swap that module and the rest works as is.

    pip install -r requirements.txt
    python -m examples.run_offline    # walks the cascade and writes an xlsx, no telegram needed
    pytest
