# Architecture

Robot Knowledge Engine is organized around evidence provenance and product versions.

```text
PDF / HTML / Excel / code / images
                |
        parsers and normalizers
                |
     versioned document metadata
          /          |          \
   vector index   lexical index  entity graph
          \          |          /
             fusion and reranking
                     |
        answer with evidence citations
                     |
       citation and conflict validation
```

## Design rules

1. Every extracted chunk retains its source, document date, section or page, content hash, product, and applicable hardware or firmware version.
2. Exact identifiers such as `R86-3`, `can_node_id`, and `921600` use lexical retrieval alongside embeddings.
3. Generated answers must be traceable to retrieved evidence. Conflicting sources are presented rather than silently resolved.
4. Local engineering files remain outside Git. The repository stores source definitions, parsers, tests, and reproducible download instructions.
5. The first case study is AgiBot Lingxi X1, while domain models remain vendor-neutral.

## Planned services

- FastAPI: source registry, ingestion jobs, retrieval, answers, and citations.
- PostgreSQL + pgvector: durable metadata, chunks, embeddings, and evaluation results.
- Redis: transient ingestion progress and task events.
- Worker: parsing, OCR, table extraction, embedding, and entity extraction.
- Web UI: document explorer, cited answers, version filters, and evaluation reports.
