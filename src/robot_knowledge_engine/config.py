"""Environment-backed application settings."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    environment: str = "development"
    log_level: str = "INFO"
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    source_manifest: Path = Path("configs/sources.example.yaml")
    local_x1_root: Path | None = None

    @classmethod
    def from_env(cls) -> Settings:
        local_root = os.getenv("RKE_LOCAL_X1_ROOT")
        return cls(
            environment=os.getenv("RKE_ENVIRONMENT", "development"),
            log_level=os.getenv("RKE_LOG_LEVEL", "INFO"),
            api_host=os.getenv("RKE_API_HOST", "127.0.0.1"),
            api_port=int(os.getenv("RKE_API_PORT", "8000")),
            source_manifest=Path(
                os.getenv("RKE_SOURCE_MANIFEST", "configs/sources.example.yaml")
            ),
            local_x1_root=Path(local_root).expanduser() if local_root else None,
        )
