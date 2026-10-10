---
type: meta
title: Knowledge Vault Tag Taxonomy
description: Master human-readable and agent-governed reference for all tags used across the vault.
tags: [meta, taxonomy]
generated:
  by: antigravity/gemini-3.8-flash
  at: 2026-10-10T12:00:00Z
status: active
---

# Knowledge Vault Tag Taxonomy

This document is the authoritative reference for tags within the vault. Tags provide cross-domain discovery and conceptual categorization without fragmenting notes into domain-specific folder hierarchies.

## Tag Policy & Governance Rules

1. **Check First**: Agents and human authors must inspect this taxonomy before assigning tags to any note or source record.
2. **Reuse Existing**: Always reuse an established tag whenever it reasonably covers the topic. Avoid creating synonyms (e.g. use `operating-systems`, do not introduce `os` or `operating_sys`).
3. **Explicit User Permission Required**: **An agent must never invent or assign a new tag without asking the user for permission first.**
4. **Update on Approval**: When the user approves a new tag, the agent must immediately add it to this file with a short description and domain grouping.
5. **Format**: All tags must be kebab-case (lowercase words joined by hyphens, e.g., `machine-learning`).

---

## Canonical Domains & Tags

### Computer Science & Systems
- `computer-science`: General theoretical and applied computer science principles.
- `operating-systems`: OS architecture, kernels, processes, concurrency, memory management, and virtualization.
- `system-design`: Distributed architectures, scalability, resilience, APIs, and storage systems.
- `software-engineering`: Design patterns, programming languages, refactoring, testing, and lifecycle methodologies.
- `distributed-systems`: Consensus, RPC, replication, partitioning, and network protocols.

### Artificial Intelligence & Machine Learning
- `artificial-intelligence`: Broad AI concepts, heuristics, agents, and reasoning.
- `machine-learning`: Statistical learning, optimization, evaluation metrics, and algorithms.
- `deep-learning`: Neural network architectures, backpropagation, attention mechanisms, and training dynamics.
- `llm`: Large language models, prompting, inference, context windows, fine-tuning, and LLM architectures.
- `nlp`: Natural language processing, tokenization, embeddings, and semantic parsing.

### Sciences & Mathematics
- `physics`: Classical mechanics, electromagnetism, thermodynamics, quantum mechanics, and relativity.
- `mathematics`: Linear algebra, calculus, discrete math, probability, and logic.

### Humanities, Arts & History
- `music-theory`: Harmony, rhythm, scales, composition, counterpoint, and acoustics.
- `theology`: Systematic theology, doctrine, and church history.
- `biblical-studies`: Exegesis, hermeneutics, textual analysis, and historical context.
- `history`: Broad historical analysis, historiography, and eras.
- `industrial-revolution`: Technological, economic, and societal developments of industrial eras.
- `storytelling`: Narrative structures, character development, worldbuilding, and communication.

### Administrative & Vault Structure
- `meta`: Vault governance, constitutions, workflows, and infrastructure.
- `taxonomy`: Tag management and schema definitions.
- `template`: Note and deliverable scaffolding.
