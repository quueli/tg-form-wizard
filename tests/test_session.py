import pytest


@pytest.fixture
def manager(tmp_path, monkeypatch):
    import data.session_manager as sm
    monkeypatch.setattr(sm, "SESSIONS_DIR", str(tmp_path / "sessions"))
    return sm.SessionManager()


def test_create_and_get_roundtrip(manager):
    sid = manager.create_session(user_id=42)
    session = manager.get_session(sid)
    assert session["user_id"] == 42
    assert "answers" in session


def test_update_merges_answers(manager):
    sid = manager.create_session(7)
    manager.update_session(sid, {"answers": {"category": "category_1"}})
    manager.update_session(sid, {"answers": {"group": "group_2"}})
    answers = manager.get_session(sid)["answers"]
    assert answers["category"] == "category_1"
    assert answers["group"] == "group_2"


def test_delete(manager):
    sid = manager.create_session(1)
    assert manager.delete_session(sid) is True
    assert manager.get_session(sid) is None
    assert manager.delete_session(sid) is False


def test_progress_grows_with_answers(manager):
    empty = manager.calculate_progress({})
    some = manager.calculate_progress({"segment": "segment_1", "category": "category_1"})
    assert empty == 0
    assert some > empty


def test_cleanup_removes_expired(manager, monkeypatch):
    import data.session_manager as sm
    sid = manager.create_session(5)
    monkeypatch.setattr(sm, "SESSION_LIFETIME", -1)
    manager.cleanup_expired_sessions()
    assert manager.get_session(sid) is None
