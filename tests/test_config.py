from pathlib import Path

from robot_knowledge_engine.config import Settings


def test_settings_read_local_source_root(monkeypatch) -> None:
    monkeypatch.setenv("RKE_LOCAL_X1_ROOT", "/tmp/x1")
    settings = Settings.from_env()
    assert settings.local_x1_root == Path("/tmp/x1")
