# Ways of working

- **Edit with context.** Read the whole piece before changing a passage. Keep each editorial pass focused on its agreed purpose; flag unrelated opportunities separately.
- **Distinguish proposals from decisions.** Consult the relevant authoritative documents in `reference/`. Treat scratchpads and historical plans as working material, not permission to change the manuscript. Ask when instructions conflict. Keep affected references in sync with approved changes.
- **Keep supporting material separate.** Put plans, exploratory notes, research, and editorial records in the appropriate `workbench/` directory. Create them when useful, rather than documenting every small edit. Keep story facts and creative direction out of this file.
- **Make changes reviewable.** Keep revisions narrowly scoped and preserve a meaningful before/after comparison in the preview until author approval. Reserve its “Reviewed” marks for the author. Start the preview with `amp orb services ensure` in an Amp orb.

## Validation and shipping

- Re-read each changed piece in full. Check for unintended edits, contradictions with authoritative references, and effects on related passages. Inspect affected manuscript pieces in the preview.
- For preview or tooling changes, run relevant checks and exercise the affected reading, comparison, editing, saving, or review controls.
- Report what was checked and what still needs author judgment. Editorial preferences are not validation failures.
- Pressing **Ship** counts as author approval; individual “Reviewed” marks are not required. If a required validation check fails or cannot be completed, stop and report the blocker. Do not merge or push to `main` until it is resolved. Revalidate after rebasing if the final changes differ.
- After successful shipping, confirm the remote contains the shipped commit, report the result, and archive the Amp thread. Leave the thread open if shipping is blocked or fails.
