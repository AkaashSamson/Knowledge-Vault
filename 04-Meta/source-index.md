---
type: meta
title: Source Index
description: Master catalog of all original source files and their corresponding Markdown source records.
tags: [meta]
generated:
  by: antigravity/gemini-3.8-flash
  at: 2026-10-10T12:00:00Z
status: active
---

# Master Source Index

This index maintains a compact, navigable catalog of all source materials ingested into the vault. It strictly distinguishes original files stored under `01-Sources/files/` from their descriptive Markdown records stored under `01-Sources/records/`.

## Catalog

| Source Name | Original File Path | Source Record Path | Brief Description | Relevant Domains |
| Attention Is All You Need | [/01-Sources/files/Attention_is_all_you_need.pdf](/01-Sources/files/Attention_is_all_you_need.pdf) | [/01-Sources/records/Attention_is_all_you_need.md](/01-Sources/records/Attention_is_all_you_need.md) | Foundational paper introducing the Transformer architecture and self-attention mechanism | `deep-learning`, `nlp`, `llm` |

---

## Ingestion Protocol Reminder

When adding a new entry via `/ingest`:
1. Register the original file under `01-Sources/files/<filename>`.
2. Generate the descriptive Markdown record at `01-Sources/records/<filename>.md`.
3. Add a single concise row to the table above.
4. Do not copy full summaries into this table; link directly to the source record.
