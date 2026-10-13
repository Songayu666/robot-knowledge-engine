from pathlib import Path

import pytest

from robot_knowledge_engine.domain import SourceKind
from robot_knowledge_engine.sources import SourceManifestError, load_sources


def test_example_manifest_is_valid() -> None:
    sources = load_sources(Path("configs/sources.example.yaml"))
    assert len(sources) >= 8
    assert all(source.product == "AgiBot Lingxi X1" for source in sources)
    assert any(source.kind is SourceKind.GITHUB for source in sources)


def test_duplicate_source_ids_are_rejected(tmp_path: Path) -> None:
    manifest = tmp_path / "sources.yaml"
    manifest.write_text(
        """
sources:
  - id: duplicate
    name: One
    kind: web
    location: https://example.com/1
    official: true
  - id: duplicate
    name: Two
    kind: web
    location: https://example.com/2
    official: true
""".strip(),
        encoding="utf-8",
    )
    with pytest.raises(SourceManifestError, match="Duplicate source id"):
        load_sources(manifest)
