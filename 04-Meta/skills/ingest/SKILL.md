---
name: ingest
description: Ingest a new source into the vault by archiving the raw file, generating an OKF-compliant source record, and updating the source index.
type: skill
---

# Ingest Skill (`/ingest`)

This workflow registers an external source into the vault. It creates a structured source record without generating wiki notes prematurely.

## Workflow Steps

1. **Inspect & De-duplicate**:
   - Determine the source file type and metadata.
   - Check `01-Sources/files/` and [04-Meta/source-index.md](/04-Meta/source-index.md) to ensure the source has not already been ingested.
2. **Archive the Original File**:
   - Save or copy the original file into `01-Sources/files/<filename>`.
   - Preserve original filenames and extensions.
3. **Generate Source Record**:
   - Create `01-Sources/records/<filename>.md` using the [Source Record Template](/04-Meta/templates/source-record.md).
   - Set YAML frontmatter:
     - `type: source-record`
     - `title`: Formal source title
     - `resource`: `/01-Sources/files/<filename>`
     - `author`: Author or creator
     - `published_date`: Original publication date
     - `tags`: Selected from [04-Meta/taxonomy.md](/04-Meta/taxonomy.md). **If a new tag is needed, ask the user for permission before applying it.**
     - `generated: { by: "antigravity/<model>", at: "<ISO-8601-UTC>" }`
     - `status: active`
   - Include an overview, table of contents / chapter breakdown, and candidate concepts for future extraction.
4. **Update Catalog**:
   - Add a row for the new source in [04-Meta/source-index.md](/04-Meta/source-index.md) with name, file path, record path, brief summary, and domain tags.
5. **Validate**:
   - Verify all paths, markdown links, and YAML frontmatter.
6. **Git Commit**:
   - Review `git status` and `git diff`.
   - Commit changes: `git commit -m "feat(source): ingest <filename>"`
   - Record entry in `04-Meta/logs/YYYY-MM/log.md`.
