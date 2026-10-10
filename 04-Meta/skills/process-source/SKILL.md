---
name: process-source
description: Extract and integrate reusable knowledge from an ingested source into permanent wiki notes.
type: skill
---

# Process Source Skill (`/process-source`)

This workflow extracts modular, reusable concepts, topics, entities, and research questions from an ingested source into `02-Wiki/`.

## Workflow Steps

1. **Locate Source**:
   - Inspect the target Markdown source record in `01-Sources/records/` and original file in `01-Sources/files/`.
2. **Determine Scope & Incremental Slices**:
   - Support processing full documents, designated chapters/sections, or specific topic queries.
   - For large documents, process incrementally (e.g. one chapter or section at a time) to prevent hallucination and maintain quality.
3. **Check Processing History**:
   - Check the **Processing Log** in `01-Sources/records/<source>.md` to avoid duplicating work.
4. **Extract Reusable Knowledge**:
   - Avoid regurgitating paragraphs or writing chapter summaries.
   - Distill knowledge into atomic units fitting the **4 semantic types**:
     - `concept`: Mechanisms, definitions, algorithmic ideas, mental models.
     - `topic`: Broader maps linking multiple concepts.
     - `entity`: Systems, persons, software frameworks, institutions.
     - `question`: Open problems, research frontiers, conflicting interpretations.
5. **Check Existing Wiki Notes**:
   - Check `02-Wiki/` before creating a new note.
   - If a related note exists, update and enrich it rather than creating a duplicate.
6. **Apply Frontmatter, Links & Citations**:
   - Use the [Wiki Note Template](/04-Meta/templates/wiki-note.md).
   - In frontmatter, add `sources:` referencing the source record (`/01-Sources/records/<source>.md`).
   - Use footnote citations (`[^1]`) in the body for specific claims.
   - Link related concepts together using standard relative links.
7. **Taxonomy & Tags**:
   - Reuse existing tags from [04-Meta/taxonomy.md](/04-Meta/taxonomy.md).
   - **If a new tag is needed, ask the user for permission before applying it.**
8. **Concise Style**:
   - Keep note text concise, direct, and information-dense (can employ caveman brevity where appropriate).
9. **Update Processing Log**:
   - Update the Processing Log in `01-Sources/records/<source>.md` marking the processed sections.
10. **Validate & Git Commit**:
    - Validate YAML frontmatter, links, and citations.
    - Commit changes: `git commit -m "feat(wiki): extract <concept/topic> from <source>"`
    - Record entry in `04-Meta/logs/YYYY-MM/log.md`.
