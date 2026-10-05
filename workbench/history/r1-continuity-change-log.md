# R1 — continuity decisions and narrow repairs

Author selections in [the R1 thread](https://ampcode.com/threads/T-01a10d72-5ce5-77ba-a8f8-d0ea8e4107a2), 5 October 2026: approve the dossier's other recommendations; replace G with two excerpts together in entry 66, each with a full date. Pepper would not carry old journals between trips, so no P.S.; the author also declined Jamie intervention.

## Initial implementation (author revisions recorded below)

| Decision / phrase anchor | Applied change | Class and protections |
|---|---|---|
| A · 05, “The faint blue has deepened” | The question about its source becomes remembered uncertainty | Knowledge-state clarification; no date or material property changes. 09 and Sayo's author-edited parenthesis untouched. |
| B · 73, “as she reads” | “as she tells her children stories” | Oral-storytelling clarification; reading simile, Hana/Ren households, waiting dragon and lullaby intact. No literacy fact invented. |
| C · 60, “for months” | “for weeks” | Approved duration narrowing; 14 July 1948 and 59's later reference unchanged. |
| D · 62 | No change | Both encounters fit one morning. |
| E · 64, “Yesterday” / “this morning” | “Last week” / “the next morning” | Approved relative-time repair; completed week precedes composition. River/Manami ending unchanged. |
| F · 65, “gone eight years” | Over seven years away; nearly eight since seeing the Hiccupper | Distinguishes absence from meeting interval. Birthday dateline, restored speculation and measuring P.S. untouched. |
| G · 66, “River, on her second visit” | Separate excerpt introduced by `*22nd April 1971*` | Author-approved two-excerpt form and full-date instruction; agent-selected day, not an exact date discovered in the source. One week after 15 April return, before later T5 domestic scenes. Original 18 April 1956 dateline and both prose blocks untouched; no P.S., Jamie note, new scene or new numbered piece. |
| H · ledger Chestnut naming | Age six; exact date unspecified | Approved retirement of conflicting reference-only precision. Prologue and Indigo's birthday untouched. |

The second surfing date is the only added dateline. No existing dateline, trip window, birthday, filename or entry number moves. The collection remains 77 numbered pieces; chronology lists 66 under both periods. The three living references are synchronised. Historical plans and Pass 1/7 logs are not rewritten to pretend earlier wording never existed.

## Imported baseline versus R1 work

Manuscript comparison baseline: [4 October resident-pass record](https://github.com/ralovely/blule-dragons-tales/commit/472435f9ecefa286c2d00a90f4128a2839f6fb6d), local `main` at implementation. The preview compared that committed manuscript with the editable working tree through author review.

The six master documents were imported before R1. Their receipt hashes remain in the [dossier](../notes/continuity-decision-dossier.md). R1 changes only `reference/canon-ledger.md`, `reference/chronology.md` and `reference/timeline.md` on top of that import. The imported workbench documents were left untouched during R1; integration then retained their shipped R0 versions, including the master's newer tracker. R1 also owns the six manuscript edits, dossier and this log. The imported R0 changes are separate from the R1 amendments in Git history.

## Initial preview validation

- Re-read all six changed entries in full, their relevant neighbours, and the updated references. Reviewed the R1-only reference changes against the imported baseline.
- Exact-replacement check across all 77 entries plus the prologue passed: only the six approved manuscript changes exist; all original datelines and all other text are byte-identical to the baseline. In particular, both surfing prose blocks, protected whole entries, prologue, seven editor's notes, production notes, Sayo's parenthesis, River/Manami ending and the Cassius P.S. survive unchanged.
- Checked the added date lies after T5 arrival and before the next selected entry; ledger, chronology and timeline agree. Local document links resolve. The three unedited imported workbench files still match their receipt hashes.
- `git diff --check` passed. The preview API's six before/after pairs match Git and disk respectively. The preview loaded all 78 manuscript files (prologue plus 77 pieces), reported the six edited entries as changed, and retained zero Reviewed marks.
- Inspected 2× Chromium captures of all six affected preview comparisons. The second full dateline is legible above the unchanged River/Kai excerpt; the five wording repairs are readable. Existing diff panes can have different scroll positions and concatenate adjacent deleted/inserted words; current-text panes are clear. No preview tooling was changed.

## Author review and revalidation

The author reviewed all six changed entries and edited three. Their saved wording supersedes the initial implementation above:

- **05:** removed the remembered question altogether. The entry ends “The faint blue has deepened since I arrived; it does not wash off.” This retains the stain and avoids claiming ignorance after June's discovery, without giving its cause ahead of 09 in thematic reading order.
- **65:** removed “in the nearly eight years”; the second paragraph now says “It has, since I last saw it, grown considerably and learned some control.” The earlier “over seven years” absence remains accurate. The almost-eight-year meeting interval still follows from the dates but no longer needs stating in the prose.
- **66:** changed “took to it” to “took to surfing”, allowing the short excerpt to stand independently. Both dates and the remaining surfing prose, including the River/Kai ending, are unchanged.

Re-read these three entries in full and rechecked their continuity against the established dates and payoffs. No further manuscript correction was needed or made. Updated the living reference summaries to match the reviewed wording; the original dossier recommendations remain historical evidence.

Revalidation passed: the prologue and all 77 entries match the baseline plus the selected R1 changes and exactly these three author revisions. Original dates and all other prose are preserved. All six Reviewed hashes match current file bytes, and the preview API serves those same bytes. `git diff --check` passes. No review marks were changed by the agent.

## Shipping integration

The author requested Ship and authorised R0 first, then R1. Integrated on top of [shipped R0](https://github.com/ralovely/blule-dragons-tales/commit/2f043f7cc7d9009c6d09039111f64dc1d4781d47), applying only the R1 reference delta against the fingerprinted imported baseline. The three R0 references matched that baseline exactly. The shipped master tracker, historical entry plan and Pass 1 log are unchanged by R1.

Final integrated checks passed: all six manuscript files match their author-review hashes and pre-integration bytes; the other 72 manuscript files are unchanged; all original datelines survive, with only 66's approved second date added. The three references match the reviewed R1 state. The preview API serves the same bytes and retains all six author review marks. Re-read the six changed entries and inspected the final surfing excerpt in the preview: the separate full date and author's “took to surfing” wording are legible, with the River/Kai ending intact. `git diff --check` passes.

**Delivery at commit preparation:** author-reviewed, revalidated and authorised for publication on top of R0. Push and remote verification are reported in the R1 thread after execution; the master owns its tracker update.
