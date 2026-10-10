---
name: promote-to-wiki
description: Promote verified, reusable knowledge from an approved generated output into the permanent wiki.
type: skill
---

# Promote to Wiki Skill (`/promote-to-wiki`)

This workflow extracts permanent, reusable insights from generated deliverables in `03-Outputs/` and integrates them into `02-Wiki/`.

## Critical Prerequisite: Explicit User Approval

**Generating an output NEVER implies permission to alter the wiki.**
This workflow MUST ONLY be initiated when the user explicitly instructs the agent to promote an output (e.g., *"Promote the findings in 03-Outputs/reports/distributed-consensus.md to the wiki"*).

## Workflow Steps

1. **Confirm Output & Scope**:
   - Verify the user's explicit approval for the target artifact in `03-Outputs/`.
2. **Identify Reusable Insights**:
   - Extract timeless, modular concepts, entity definitions, and open questions from the artifact.
   - Ignore deliverable-specific narrative fluff, formatting, or slide mechanics.
3. **Verify Claims & Provenance**:
   - Trace factual claims back to the primary source records or verified citations present in the output.
   - Do not promote unsourced inferences without clearly labeling them as hypotheses (`type: question` or explicit disclaimers).
4. **De-duplicate & Synthesize**:
   - Search `02-Wiki/` for existing notes.
   - If an existing note covers the concept, enrich it with the new findings and citations.
   - If novel, create a new note adhering to the [Wiki Note Template](/04-Meta/templates/wiki-note.md).
5. **Apply OKF Frontmatter & Citations**:
   - Ensure the note carries the appropriate semantic `type` (`concept`, `topic`, `entity`, `question`).
   - Populate `sources:` pointing to the underlying source records (or note the promoted deliverable as a secondary provenance source).
   - Add footnote citations for claim attribution.
6. **Tagging Policy**:
   - Consult [04-Meta/taxonomy.md](/04-Meta/taxonomy.md).
   - Reuse existing tags. **If a new tag is required, ask the user for permission before adding it.**
7. **Mark Output Metadata**:
   - Update the frontmatter in the deliverable note in `03-Outputs/`: set `promoted_to_wiki: true`.
8. **Validate & Git Commit**:
   - Run validation on all modified and newly created notes.
   - Review `git status` and `git diff`.
   - Commit changes: `git commit -m "feat(wiki): promote insights from <deliverable>"`
   - Record entry in `04-Meta/logs/YYYY-MM/log.md`.
