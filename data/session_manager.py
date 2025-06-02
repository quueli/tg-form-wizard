import json
import os
import time

from .questionnaire import DEFAULTS

SESSION_LIFETIME = int(os.getenv("SESSION_LIFETIME", 86400))  # seconds, 1 day default
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
            "answers": {
                "segment": DEFAULTS["segment"],
                "item_a_include": [],
                "item_a_exclude": [],
                "item_b_include": [],
                "item_b_exclude": [],
                "item_c_include": [],
                "item_c_exclude": [],
            },
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

        for key, value in updates.items():
            if key != "answers":
                session[key] = value

        with open(self._get_file_path(session_id), "w") as f:
            json.dump(session, f)

        return True

    def delete_session(self, session_id: str) -> bool:
        try:
            os.remove(self._get_file_path(session_id))
            return True
        except FileNotFoundError:
            return False

    def cleanup_expired_sessions(self):
        now = time.time()
        for filename in os.listdir(SESSIONS_DIR):
            if filename.endswith(".json"):
                session_id = filename[:-5]
                session = self.get_session(session_id)
                if session and now - session["created_at"] > SESSION_LIFETIME:
                    self.delete_session(session_id)

    def get_user_sessions(self, user_id: int) -> list:
        sessions = []
        now = time.time()

        for filename in os.listdir(SESSIONS_DIR):
            if filename.endswith(".json"):
                session_id = filename[:-5]
                session = self.get_session(session_id)
                if session and session["user_id"] == user_id and now - session["created_at"] <= SESSION_LIFETIME:
                    sessions.append({
                        "id": session_id,
                        "created_at": session["created_at"],
                        "progress": self.calculate_progress(session["answers"]),
                    })

        return sessions

    def calculate_progress(self, answers: dict) -> int:
        total_steps = 19  # questions in the full flow
        filled_steps = sum(1 for key in answers if answers[key] not in ([], "", None))
        return int((filled_steps / total_steps) * 100)
