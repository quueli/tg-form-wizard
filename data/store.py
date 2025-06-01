import time

from .questionnaire import DEFAULTS

_sessions = {}


def create_session(user_id: int) -> str:
    session_id = f"{user_id}_{int(time.time())}"
    _sessions[session_id] = {
        "user_id": user_id,
        "created_at": time.time(),
        "answers": {"segment": DEFAULTS["segment"]},
    }
    return session_id


def get_session(session_id: str):
    return _sessions.get(session_id)


def update_session(session_id: str, answers: dict) -> bool:
    session = _sessions.get(session_id)
    if not session:
        return False

    session["answers"].update(answers)
    return True


def delete_session(session_id: str) -> bool:
    return _sessions.pop(session_id, None) is not None
