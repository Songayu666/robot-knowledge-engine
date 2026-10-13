"""Version-aware source and document metadata models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from enum import StrEnum
from typing import Any


class SourceKind(StrEnum):
    WEB = "web"
    GITHUB = "github"
    LOCAL = "local"


@dataclass(frozen=True, slots=True)
class SourceRecord:
    source_id: str
    name: str
    kind: SourceKind
    location: str
    official: bool
    product: str | None = None
    document_type: str | None = None
    published_at: date | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class DocumentMetadata:
    document_id: str
    source_id: str
    title: str
    product: str | None = None
    hardware_version: str | None = None
    firmware_version: str | None = None
    page: int | None = None
    section: str | None = None
    source_url: str | None = None
    content_hash: str | None = None
    ingested_at: datetime = field(default_factory=lambda: datetime.now(UTC))
