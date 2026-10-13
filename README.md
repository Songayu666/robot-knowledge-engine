# Robot Knowledge Engine

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

An evidence-grounded, version-aware knowledge engine for robot manuals, engineering documents, and source code.

The first case study uses AgiBot Lingxi X1 materials to build answers that preserve document provenance, product versions, exact engineering identifiers, and source conflicts. The engine is vendor-neutral and is intended to grow into a reusable robot engineering knowledge platform.

## Why this project

Engineering questions often span manuals, BOM spreadsheets, drawings, configuration files, and source code. A useful assistant must retrieve exact identifiers as well as semantic matches, distinguish hardware and firmware versions, and show evidence for every technical conclusion.

The planned retrieval path combines:

- semantic vector search;
- exact lexical search for model numbers, parameters, and error codes;
- product and version metadata filters;
- entity relationships across BOMs, drawings, manuals, and code;
- reranking, citation validation, and conflict detection.

## Current milestone

The repository currently provides:

- a FastAPI service with health and source registry endpoints;
- version-aware source and document metadata models;
- an initial official X1 source manifest;
- a privacy-safe local document inventory tool;
- PostgreSQL/pgvector and Redis service definitions;
- tests, linting, CI, architecture, roadmap, and data policy.

## Quick start

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
cp .env.example .env
uv sync --extra dev
uv run uvicorn robot_knowledge_engine.api.main:app --reload
```

Open <http://127.0.0.1:8000/docs>. Run quality checks with:

```bash
uv run ruff check .
uv run ruff format --check .
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run pytest
```

To inspect a local document collection without publishing filenames:

```bash
uv run python scripts/inventory_local_sources.py \
  /home/zhongde/agibot_ws/智元灵犀X1_20250307
```

## Local data

Large or restricted documents are intentionally excluded from Git. Configure their location in `.env`:

```dotenv
RKE_LOCAL_X1_ROOT=/home/zhongde/agibot_ws/智元灵犀X1_20250307
```

See [Architecture](docs/ARCHITECTURE.md), [Roadmap](docs/ROADMAP.md), and [Data policy](docs/DATA_POLICY.md).

## License

Source code is licensed under Apache License 2.0. Third-party documents and datasets retain their original rights and licenses.
