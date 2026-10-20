---
type: meta
title: Knowledge Vault Agent Guidelines
description: Operational rules, skill synchronization, and OKF validation requirements for AI agents.
tags: [meta]
---

# Knowledge Vault Agent Guidelines

## 1. Skill Synchronization (Mandatory)
The authoritative source for all vault skills is `04-Meta/skills/`.
Whenever any skill in `04-Meta/skills/` is created, updated, or deleted:
1. Run `bash 04-Meta/scripts/sync-skills.sh` to synchronize symlinks to `.agents/skills/` and `~/.gemini/config/skills/`.
2. Ensure both the local vault and the user's global Antigravity environment stay in sync.

## 2. OKF v0.2 Conformance & Validation
1. Every non-reserved Markdown file must contain valid YAML frontmatter with a non-empty `type:` field.
2. Before committing any changes, run the validator:
   ```bash
   python3 04-Meta/scripts/validate.py
   ```
3. Fix any reported validation errors or unapproved tag warnings before committing.

## 3. Tag Taxonomy Rule
1. Inspect `04-Meta/taxonomy.md` first.
2. Always reuse existing canonical tags.
3. **NEVER create or assign a new tag without asking the user for explicit permission first.**
4. If approved, add the new tag to `04-Meta/taxonomy.md`.

## 4. Output & Promotion Boundaries
1. Generated deliverables belong in `03-Outputs/`.
2. Never treat an output as implicit wiki knowledge.
3. Only promote content to `02-Wiki/` using `/promote-to-wiki` after receiving explicit user instruction.
