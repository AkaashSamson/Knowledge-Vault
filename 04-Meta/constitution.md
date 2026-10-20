---
type: meta
title: Knowledge Vault Constitution
description: Authoritative operating manual, architectural principles, metadata standards, and agent execution policies.
tags: [meta]
generated:
  by: antigravity/gemini-3.8-flash
  at: 2026-10-10T12:00:00Z
status: active
---

# Knowledge Vault Constitution

This document defines the architectural rules, data standards, and operational boundaries for this personal, AI-native Knowledge Vault. Human authors and AI agents must comply with these guidelines.

---

## 1. Vision & Architecture

The Knowledge Vault is a long-lived, multi-domain knowledge corpus inspired by Andrej Karpathy's LLM Wiki concept. It operates inside an Obsidian-compatible Markdown repository under Git version control.

### Core Principles
1. **Unified Cross-Domain Graph**: All subjects (computer science, AI, physics, theology, music theory, history, etc.) live in a single vault. Knowledge connects across disciplines through standard relative Markdown links and tags.
2. **Role-Based, Flat Layout**: Directory structures reflect functional roles (what a file does), not arbitrary subject silos.
3. **Strict Separation of Sources vs. Knowledge**: Raw source files are preserved immutably; structured source records catalogue them; wiki notes synthesize reusable insights.
4. **Agent-Friendly & Human-Navigable**: Formatted for seamless reading in Obsidian and deterministic parsing by AI agents.

---

## 2. Directory Roles

```text
Knowledge-Vault/
├── 00-Inbox/          # Staging area for raw materials awaiting ingestion or triage.
├── 01-Sources/
│   ├── files/         # Original, unmodified source files (PDFs, EPUBs, HTML, TXT, etc.).
│   └── records/       # Markdown source records describing each original source.
├── 02-Wiki/           # Permanent, reusable, flat knowledge notes.
├── 03-Outputs/        # Generated deliverables (articles, presentations, reports, scripts).
├── 04-Meta/           # Governance, taxonomy, source index, templates, logs, and skills.
└── 05-Bundles/        # Imported third-party Open Knowledge Format (OKF) bundles.
```

### Specific Directory Rules
- `00-Inbox/`: Temporary staging area. Notes do not stay here permanently.
- `01-Sources/files/`: Stores original source files. Filenames are preserved.
- `01-Sources/records/`: Stores Markdown records using the source filename + `.md`.
- `02-Wiki/`: Kept flat by default (no subject folders). No `02-Wiki/index.md` exists to avoid redundant indexes.
- `03-Outputs/`: Deliverables organized into `articles/`, `presentations/`, `reports/`, and `scripts/`.
- `04-Meta/`: Administrative core. Houses `constitution.md`, `taxonomy.md`, `source-index.md`, `templates/`, `logs/`, and agent `skills/`.
- `05-Bundles/`: Modular home for importing external OKF v0.2 knowledge bundles without polluting local wiki notes.

---

## 3. Document Standards & OKF v0.2 Conformance

The vault strictly implements **Open Knowledge Format (OKF) v0.2**:

1. **YAML Frontmatter**: All non-reserved Markdown files begin with a valid YAML frontmatter block delimited by `---`.
2. **Mandatory `type`**: Every frontmatter block contains a non-empty `type:` key.
3. **Reserved Filenames**:
   - `index.md`: Reserved for progressive disclosure / directory listings. Root `index.md` carries `okf_version: "0.2"`. No other frontmatter is allowed on index files.
   - `log.md`: Reserved for chronological changelogs (no frontmatter).
4. **Lifecycle & Provenance Fields**:
   - `generated`: Contains `{ by: "<actor>", at: "<ISO-8601-UTC>" }`.
   - `status`: One of `draft`, `active`, or `archived`.
   - `sources`: Array of source records consulted, specifying `id:`, `resource:`, and `title:`.
   - `verified`: Optional confirmation event list `{ by: "<actor>", at: "<ISO-8601-UTC>" }`.

---

## 4. Semantic Wiki Note Conventions

All permanent notes in `02-Wiki/` must be assigned one of the **four semantic types**:

| Type | Definition |
| :--- | :--- |
| `concept` | A reusable idea, principle, mechanism, algorithm, definition, or mental model. |
| `topic` | A broad theme or domain map that synthesizes and links multiple related concepts. |
| `entity` | An identifiable person, organization, system, software project, or concrete work. |
| `question` | An open inquiry, unresolved research topic, or hypothesized problem space. |

### Note Content Guidelines
- **Reusable Synthesis**: Notes must synthesize modular knowledge, not dump passive quotes.
- **Footnote Citations**: Every factual claim must be backed by a Markdown footnote keyed to an entry in the note's `sources:` frontmatter (e.g. `[^1]`).
- **Epistemic Clarity**: Clearly distinguish settled empirical facts from working hypotheses, extrapolations, or interpretations.
- **Link Richness**: Actively cross-link related wiki concepts using standard relative Markdown links (e.g. `[Virtual Memory](/02-Wiki/virtual-memory.md)`).

---

## 5. Taxonomy Management

Tagging is strictly managed via [04-Meta/taxonomy.md](/04-Meta/taxonomy.md):
1. **Search Before Tagging**: Check `04-Meta/taxonomy.md` first.
2. **Reuse Existing**: Always pick established canonical tags.
3. **User Approval Mandatory**: **The agent must never invent or assign a new tag without explicitly requesting and receiving user approval.**
4. **Immediate Update**: Once a tag is approved, record it in `04-Meta/taxonomy.md` under its respective domain.

---

## 6. Output & Promotion Boundaries

Deliverables created in `03-Outputs/` (such as research reports or Marp presentation decks) are task artifacts, **not** permanent wiki knowledge.
- Marp slide decks must **never** be placed in `02-Wiki/`.
- Generating an output does **never** imply permission to alter the wiki.
- Only the `/promote-to-wiki` workflow may extract reusable knowledge into `02-Wiki/`, and **only after the user provides explicit approval**.

---

## 7. Core Agent Workflows

The vault operates through four primary skills located in `04-Meta/skills/`:

1. **`/ingest`**:
   - Inspects file type, checks for duplicate sources.
   - Moves/registers original file in `01-Sources/files/`.
   - Creates metadata source record in `01-Sources/records/<filename>.md`.
   - Reuses taxonomy tags.
   - Updates `04-Meta/source-index.md`.
2. **`/query`**:
   - Answers inquiries using evidence hierarchy: (1) `02-Wiki/` $\rightarrow$ (2) `01-Sources/` $\rightarrow$ (3) External Web Search.
   - Read-only by default (never alters wiki notes merely to answer a query).
   - Clearly discloses if external blogs or web pages were used; suggests reputable papers/books to ingest.
3. **`/process-source`**:
   - Extracts reusable modular knowledge from an ingested source (chapter-by-chapter or by topic).
   - Generates or updates notes in `02-Wiki/` using the 4 semantic types.
   - Cites source records with footnotes.
   - Adheres to concise language.
4. **`/promote-to-wiki`**:
   - Triggered only upon explicit user approval of an output in `03-Outputs/`.
   - Distills verified, reusable insights into `02-Wiki/`.
   - Cross-links and verifies claims against primary source records.

---

## 8. Git & Change Discipline

All modifications made by an agent must be version-controlled:
1. Inspect `git status` before touching files.
2. Make only changes strictly requested by the current task.
3. Never stage or commit unrelated user modifications.
4. Run validation checks before committing.
5. Create atomic, meaningful commits following Conventional Commits format (`feat:`, `docs:`, `fix:`, `chore:`).
6. Record significant updates in `04-Meta/logs/YYYY-MM/log.md`.

---

## 9. Skill Maintenance & Synchronization

1. **Authoritative Source**: The canonical definition of each agent skill lives in `04-Meta/skills/<skill-name>/SKILL.md`.
2. **Antigravity Discovery**: Antigravity discovers slash-command skills from `.agents/skills/` (workspace) and `~/.gemini/config/skills/` (global).
3. **Mandatory Sync**: Whenever a skill file in `04-Meta/skills/` is modified, run `04-Meta/scripts/sync-skills.sh` to keep all links and files synchronized with the Antigravity discovery paths.
