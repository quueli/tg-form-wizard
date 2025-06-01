import json
import os
import time

from .questionnaire import DEFAULTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SESSIONS_DIR = os.path.join(BASE_DIR, "sessions")


class SessionManager:
    def __init__(self):
        if not os.path.exists(SESSIONS_DIR):
            os.makedirs(SESSIONS_DIR)

    def _get_file_path(self, session_id: str) -> str:
        return os.path.join(SESSIONS_DIR, f"{session_id}.json")

    def create_session(self, user_id: int) -> str:
        session_id = f"{user_id}_{int(time.time())}"
        session_data = {
            "user_id": user_id,
            "created_at": time.time(),
            "answers": {"segment": DEFAULTS["segment"]},
        }

        with open(self._get_file_path(session_id), "w") as f:
            json.dump(session_data, f)

        return session_id

    def get_session(self, session_id: str) -> dict:
        try:
            with open(self._get_file_path(session_id), "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def update_session(self, session_id: str, updates: dict) -> bool:
        session = self.get_session(session_id)
        if not session:
            return False

        if "answers" in updates:
            session["answers"].update(updates["answers"])

        with open(self._get_file_path(session_id), "w") as f:
            json.dump(session, f)

        return True

    def delete_session(self, session_id: str) -> bool:
        try:
            os.remove(self._get_file_path(session_id))
            return True
        except FileNotFoundError:
            return False
