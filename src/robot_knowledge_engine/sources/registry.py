"""Load version-aware source definitions from YAML."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

import yaml

from robot_knowledge_engine.domain import SourceKind, SourceRecord


class SourceManifestError(ValueError):
    """Raised when a source manifest is missing or malformed."""


def _parse_date(value: Any) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError as exc:
        raise SourceManifestError(f"Invalid published_at date: {value}") from exc


def load_sources(path: Path) -> list[SourceRecord]:
    if not path.is_file():
        raise SourceManifestError(f"Source manifest not found: {path}")

    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rows = payload.get("sources")
    if not isinstance(rows, list):
        raise SourceManifestError("Manifest must contain a 'sources' list")

    records: list[SourceRecord] = []
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise SourceManifestError(f"Source at index {index} must be a mapping")
        try:
            source_id = str(row["id"])
            if source_id in seen:
                raise SourceManifestError(f"Duplicate source id: {source_id}")
            seen.add(source_id)
            known = {
                "id",
                "name",
                "kind",
                "location",
                "official",
                "product",
                "document_type",
                "published_at",
            }
            records.append(
                SourceRecord(
                    source_id=source_id,
                    name=str(row["name"]),
                    kind=SourceKind(str(row["kind"])),
                    location=str(row["location"]),
                    official=bool(row["official"]),
                    product=row.get("product"),
                    document_type=row.get("document_type"),
                    published_at=_parse_date(row.get("published_at")),
                    metadata={
                        key: value for key, value in row.items() if key not in known
                    },
                )
            )
        except KeyError as exc:
            raise SourceManifestError(
                f"Source at index {index} is missing {exc.args[0]}"
            ) from exc
        except ValueError as exc:
            if isinstance(exc, SourceManifestError):
                raise
            raise SourceManifestError(
                f"Source at index {index} has invalid kind: {row.get('kind')}"
            ) from exc
    return records
