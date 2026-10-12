---
type: meta
title: Knowledge Vault
description: Personal, AI-native knowledge vault conforming to Open Knowledge Format (OKF) v0.2.
tags: [meta]
---

# Knowledge Vault

A personal, AI-native knowledge vault inspired by Andrej Karpathy's LLM Wiki concept, built to conform with **Open Knowledge Format (OKF) v0.2**.

The vault unifies multiple domains (Computer Science, Artificial Intelligence, Physics, Mathematics, Music Theory, Theology, History, and Storytelling) in a single Obsidian-compatible Markdown repository under Git version control.

---

## Architecture & Directory Structure

Folders reflect functional roles rather than academic subject silos:

```text
Knowledge-Vault/
├── 00-Inbox/          # Staging area for raw materials awaiting ingestion or triage
├── 01-Sources/
│   ├── files/         # Original, unmodified source files (PDFs, EPUBs, HTML, etc.)
│   └── records/       # Markdown source records describing each source
├── 02-Wiki/           # Permanent, reusable, flat knowledge notes
├── 03-Outputs/        # Generated deliverables (articles, presentations, reports, scripts)
├── 04-Meta/           # Governance, taxonomy, source index, templates, logs, and skills
│   ├── constitution.md
│   ├── taxonomy.md
│   ├── source-index.md
│   ├── templates/
│   ├── logs/
│   ├── skills/
│   └── scripts/
└── 05-Bundles/        # External, modular OKF v0.2 knowledge bundles
```

---

## Core Principles

1. **One Vault, Multiple Domains**: Cross-domain synthesis through standard relative Markdown links and tags.
2. **Strict Separation of Sources vs. Knowledge**: Raw files remain untouched in `01-Sources/files/`; structured metadata records live in `01-Sources/records/`; synthesized concepts live in `02-Wiki/`.
3. **Four Semantic Note Types**: All permanent wiki notes belong to one of four types:
   - `concept`: Modular ideas, mechanisms, algorithms, definitions.
   - `topic`: Broader theme maps linking related concepts.
   - `entity`: Identifiable persons, organizations, systems, frameworks.
   - `question`: Open problems, research frontiers, active inquiries.
4. **Governed Tag Taxonomy**: Tags are managed via [04-Meta/taxonomy.md](/04-Meta/taxonomy.md). Agents must ask explicit user permission before introducing new tags.
5. **Output Boundary**: Generated artifacts in `03-Outputs/` do not automatically enter the wiki. Promotion requires explicit user approval.

---

## Agent Skills

The vault is operated by four core agent workflows:

- **`/ingest`**: Archives raw files, extracts metadata, and creates source records.
- **`/query`**: Answers inquiries following evidence hierarchy (`Wiki` $\rightarrow$ `Sources` $\rightarrow$ `Web Search`) without mutating wiki notes.
- **`/process-source`**: Incrementally extracts reusable concepts and topics from an ingested source.
- **`/promote-to-wiki`**: Distills approved deliverables into permanent wiki notes.

---

## Validation

Verify OKF v0.2 conformance, frontmatter schemas, link integrity, and taxonomy rules:

```bash
python3 04-Meta/scripts/validate.py
```
