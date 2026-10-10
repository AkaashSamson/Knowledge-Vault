---
name: query
description: Answer user inquiries using the vault's strict evidence hierarchy (Wiki -> Sources -> External Web Search) without altering wiki notes.
type: skill
---

# Query Skill (`/query`)

This workflow answers questions using the best available evidence while strictly maintaining read-only boundaries on permanent wiki notes.

## Evidence Hierarchy

When investigating an inquiry, follow this exact order:

1. **Vault Wiki (`02-Wiki/`)**:
   - Search existing permanent notes first.
   - If concepts are found, cite them directly.
2. **Source Records & Files (`01-Sources/`)**:
   - Follow notes' underlying source references. Reference only the wiki note unless the source details are missing or not mentioned in the wiki note.
   - If wiki knowledge is incomplete, consult relevant source records (`01-Sources/records/`) or raw files (`01-Sources/files/`).
3. **External Web Research**:
   - If vault evidence is insufficient or absent, consult external sources via web search.
   - **Mandatory Disclosure**: When generating an answer relying on web articles or blog posts, prepend a clear disclaimer:
     > **Disclaimer**: This response was generated using external web articles and blog posts because existing vault coverage was insufficient.
   - **Recommendation**: Separately suggest authoritative textbooks, research papers, or primary sources that the user can ingest into the vault to enable deeper future responses.

## Response & Output Rules

- **Read-Only**: Answering a query never creates or alters notes in `02-Wiki/`.
- **Grounded Citations**: Ground every factual statement in the consulted notes or documents using standard links.
- **Deliverable Generation**:
  - When the user requests a formal deliverable (report, article, presentation deck, or script), generate it in `03-Outputs/` organized under the corresponding subfolder (`articles/`, `presentations/`, `reports/`, or `scripts/`).
  - Use the [Output Template](/04-Meta/templates/output.md).
  - Marp presentations must always reside in `03-Outputs/presentations/`, never in `02-Wiki/`.
