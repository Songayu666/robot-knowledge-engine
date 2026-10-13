# Roadmap

## M0 — Public foundation

- Source manifest and version-aware domain models
- FastAPI health and source registry endpoints
- Local X1 source inventory without publishing private files
- CI, linting, tests, and container dependencies

## M1 — Evidence ingestion

- PDF and HTML parsing with page and section provenance
- Excel BOM and parameter table extraction
- Content hashing, deduplication, and ingestion jobs
- PostgreSQL schema and migrations

## M2 — Hybrid retrieval

- pgvector semantic retrieval
- exact keyword retrieval for identifiers and numeric parameters
- metadata filtering by product, hardware, firmware, date, and source authority
- reranking and retrieval evaluation

## M3 — Verifiable answers

- answer generation from retrieved evidence
- page, section, and source citations
- source conflict detection and insufficient-evidence refusal
- regression question set for X1

## M4 — Engineering intelligence

- diagrams, images, and video keyframes
- BOM-to-drawing-to-code entity links
- knowledge graph and cross-document navigation
- troubleshooting and assembly workflows

## M5 — Continuous knowledge maintenance

- official website and GitHub change detection
- version comparison and reindexing
- public benchmark reports and deployment hardening
