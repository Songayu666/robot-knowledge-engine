"""FastAPI application entry point."""

from __future__ import annotations

from fastapi import FastAPI

from robot_knowledge_engine import __version__
from robot_knowledge_engine.config import Settings
from robot_knowledge_engine.sources import SourceManifestError, load_sources


def create_app(settings: Settings | None = None) -> FastAPI:
    active_settings = settings or Settings.from_env()
    app = FastAPI(
        title="Robot Knowledge Engine",
        version=__version__,
        description=(
            "Evidence-grounded, version-aware knowledge API for robot manuals, "
            "engineering documents, and source code."
        ),
    )

    @app.get("/health", tags=["system"])
    def health() -> dict[str, str]:
        return {"status": "ok", "version": __version__}

    @app.get("/api/v1/sources", tags=["sources"])
    def list_sources() -> dict[str, object]:
        try:
            sources = load_sources(active_settings.source_manifest)
        except SourceManifestError as exc:
            return {"count": 0, "sources": [], "warning": str(exc)}
        return {
            "count": len(sources),
            "sources": [
                {
                    "id": source.source_id,
                    "name": source.name,
                    "kind": source.kind.value,
                    "official": source.official,
                    "product": source.product,
                    "published_at": (
                        source.published_at.isoformat() if source.published_at else None
                    ),
                }
                for source in sources
            ],
        }

    return app


app = create_app()
