# R5 — Nangula's work before and beyond Indy

30 October 2026. Author-reviewed; shipment subsequently authorised with “ship”. The initial wording proposals below were approved, then judged too lightweight by the author. The follow-ups record the subsequently approved research purpose, contribution and final wording; they supersede the initial no-new-facts recommendation and validation scope. Historical local-delivery statements below describe their respective review stages, not the final shipping authority. [R5 thread](https://ampcode.com/threads/T-01a18c78-380a-731f-9162-c0f0a5b9c807).

## Baseline and reading

Fetched `origin/main`; both it and local `main` resolve to shipped R4 commit `21d628345712ae669e2ff489c450022f450a7733`. Initial worktree clean. R0–R4 are shipped despite the stale, master-owned tracker; it is not edited here. Preserve R3's retained 21/33/42 and R4's 29/30; 17's withdrawn change is not revived.

Read the R5 brief, canon ledger and chronology in full, timeline, Wyrmspan compatibility guidance and source row 133, tone-research direction and assessment. Read P and 02/04/05/20/25/32/44/76 together in full. A case-insensitive manuscript search for Nangula/Sossusvlei found no additional named occurrences. Related context read: 01/03/06/18/19/24/26/31/33/43/45/75/77. R1's 05 ending and the author-approved 76 questions remain untouched.

## Diagnosis and three local proposals

Nangula already has an independent profession, lasting relationships and a complementary way of thinking. The problem is emphasis, not an empty biography. Her introduction makes her a mysterious guide before readers encounter the explicit decades of cataloguing in 32. The proposed repair uses those existing facts rather than inventing a project or anecdote.

| Proposal | Exact anchor / change | Classification, evidence and tradeoff |
|---|---|---|
| A — P: bring her profession forward | Add “She had spent decades cataloguing dragons outside Aizomea” to her introduction, joining it to the existing lifelong solo visits | Wording-only redistribution of the explicit fact in 32: “You spent decades at it before me, Nangula”. Makes her purpose legible before her help to Indy. Adds no publication, discovery, institutional role or research method. Slightly fuller introductory sentence; keeps the patient walking image verbatim. |
| B — P: continuity of work, not an examination | “She had been waiting for the right person… the years of sideways questions were her way of making sure” → “She had kept Aizomea secret through decades of work; now she had chosen Indy to carry that work on.” | Interpretive wording clarification of existing secrecy, choice, life's work and guardianship, not a new event or biography. Author judgment required: it shifts emphasis from testing a successor to entrusting work. Does not explain why she chose Indy, impose an oath, attribute the mechanism to her or erase 76's uncertainty. The walking-for-centuries simile stays a simile, not evidence of supernatural longevity. |
| C — 04: give the teaching an active subject | “Manami speaks English, learnt from Nangula over her many visits” → “Nangula taught Manami English over her many visits” | Wording-only: ledger §2 and 04 already establish the teaching. A concrete contribution to another person's life, made before Pepper arrived. Does not claim Nangula taught anyone else, prepared Manami for Indy, transcribed Manaïari or invented a literacy system. Preserves Pepper's confession and the complete fish joke. |

Together: purpose = cataloguing dragons over decades; contributions = scholarship preserved in scrolls and English taught to Manami; complementary difference = Nangula's patient silence and unexpected questions versus Pepper's fierce concentration, noisy thinking and accumulating notes. The difference is already enacted in P/05/20; no new habit or invented argument is needed. Keep 20's “would have” as a posthumous imagining, not a recollected island conversation.

## Name research: keep Sossusvlei

The most direct source of intended fictional usage is the author's supplied [Wyrmspan CSV](../../reference/32fafdfa-wyrmspan_dragon_facts.csv), Wyrmspan ID **133**, physical line 134, **SOSSUSVLEI WYVERN**:

> This wyvern was named posthumously for the nineteenth-century dracologist Nangula Sossusvlei, who still holds the record for cataloging the most dragon species in history.

Read under the [author's source guidance](../../reference/wyrmspan-dragon-facts.md): early canon is a compatibility constraint, not an instruction to insert every fact. This directly establishes the supplied two-part personal name and commemorative species-name connection; it is not a mistaken place-name substitution by this manuscript. It does **not** establish a real Namibian naming tradition, language, ethnicity, inherited surname genealogy or cultural explanation. No such claim is made or researched here; none is needed to recommend retaining the intended fictional name. No replacement proposed.

The source's record-holder status and posthumously named wyvern are **not inserted**. Adding either would be a manuscript canon clarification/amendment for explicit author selection and reference coordination, not a wording-only repair. A new specific research finding, publication, teaching episode, personal habit or relationship would likewise require a decision; none is proposed as necessary. The existing cataloguing fact is sufficient, without a superlative or an invented catalogue excerpt.

## Author decisions and deliberate retentions

1. Accept, revise or reject A/C's emphasis changes independently.
2. Accept, revise or reject B's responsibility/continuation framing. It is the substantive interpretive choice, not a factual correction. Recommendation: accept without further explanation of the selection criteria.
3. Recommendation: no new biography or cultural explanation, no name amendment, and no import of the source's record or commemorative species at this stage. If the author wants a more specific professional achievement, choose it explicitly before drafting it as fact.

P's scholarly scrolls already belong to Nangula; neither she nor Indigo is named as the maker of the carved object, compass or dragon-triggered transfer. All remain unexplained. Prague's paired eggs, its revelation, breadcrumbs and meetings, secret sketches, death in 1935, wooden carving, jewel-toned dragon and succession are unchanged. 44 remains byte-identical: death in a bed in Namibia, three years earlier, and “I think” twice. Pepper's grief does not establish spiritual geography. No Aizomea conversation is added before her death. No chronology or general dragon rule changes. 76 is byte-identical, including both mirrored questions; the heir remains unannounced.

R8 handoff if these proposals are approved: only the two P paragraphs change; Jamie's sources remain journals, letters and family stories already named there. No new archive item or degree of documentary certainty is invented. Canon ledger and chronology remain unchanged because no new fact is proposed; the author must approve B's interpretation rather than treating this note as canon.

## Validation and review surface

- Re-read both changed pieces in full after editing, checked all named occurrences and related passages against the ledger, chronology and source. This is an editorial assessment, not an independent reader test or a claim that new biography has been approved.
- Inline Python comparison across all **79 manuscript files**: exactly P/04 differ; the other 77 match fetched `origin/main` byte-for-byte, including R3's 21/33/42, R4's 29/30, restored 17, 44 and 76. Datelines and paragraph counts unchanged. P: **1979 → 1976** whitespace-separated words; 04: **806 → 804**, comfortably within 10%.
- `git diff --check` passed. All **156 original/current API responses** across 78 selectable pieces match Git/disk. Preview meta resolves `main` to the R4 commit above. Review API is empty; no review, save or revert control was used.
- `amp orb services ensure` initially timed out waiting for its portal proxy. Service inspection showed preview running; rerunning ensure succeeded: **HTTP 200**, no repository tooling change required.
- Opened plain-baseline comparisons at 2× in Chromium. Inspected final screenshots: P shows both changed paragraphs in full alongside the unchanged paired eggs and carved-device/scrolls account; 04 shows the complete teaching paragraph and intact fish joke. Browser DOM confirms Reviewed unchecked. No UI implementation changed, so no interaction recording was needed.
- Final captures: `.amp/in/artifacts/r5-prologue-comparison.png`, `.amp/in/artifacts/r5-04-comparison.png`.

Exact review portal: https://t-03h5784c6xoj97rywz4tewv7r-p23399.onamp.dev/

Delivery state: two locally modified manuscript pieces and this new supporting record only. No authoritative reference or tracker change, commit, push, merge or deployment. Before/after remains shipped local `main` versus working tree; author approval is outstanding.

## Author follow-up — substantive purpose and contribution

The author approved the initial changes but found them too lightweight. Three further suggestions were presented explicitly as new-fact proposals. The author accepted (1) Nangula's investigation of which stories describe the same animals; accepted (2) the identification example, changing **coasts to continents** for greater drama; and liked (3) the premise of a difference in willingness to conclude, but rejected its wording. This is author approval of the new facts in 1/2, not blanket permission to invent supporting biography.

Applied locally:

- P replaces the initial generic cataloguing insertion with: “Nangula had spent decades trying to discover which of the world's dragon stories belonged to the same animals. Indy followed rumours towards a creature; Nangula followed a creature through the rumours.” The lifelong visits and patient-walking image follow unchanged.
- 32 adds: “Your notes put the same dragon on three different continents. I had given it three separate entries. In my defence, so had everyone else.” Placed in the existing catalogue paragraph, before the mythology and guest-book image. No continents, animal, journey dates or identification technique are invented. The example is an approved fictional contribution, not an externally researched historical claim. It remains compatible with Wyrmspan ID 133's cataloguing scholar and 32's existing centuries-long roaming dragons; it does not import the record-holder superlative or name a species.
- The approved new facts are recorded in the canon ledger's People section. Chronology and timeline need no change. Original 04 and succession wording remain as approved.

Suggestion 3 remains **outside the manuscript and ledger**, pending wording approval. Two possible replacements for the rejected six-month/book-sending formulation:

> “You cannot be certain yet,” Nangula would say. “No,” Indy would agree, and go anyway.

Or, with the difference less weighted towards Nangula being right:

> Nangula wanted another observation. Indy wanted to leave while there was still daylight. They were both right often enough to be irritating.

Recommendation: the second. It gives caution a practical cost, makes expedition initiative useful too, and allows affectionate irritation without a new named incident. These are proposals for remembered exchanges or habitual behaviour, not recovered quotations from established letters. No such archive claim has been inserted.

Re-read the complete revised P and 32, and rechecked the research facts against existing chronology, secrecy, prologue protections, the cataloguing source and the guest-book/protection payoffs. Inspected fresh 2× plain-baseline captures of both affected states: `.amp/in/artifacts/r5-prologue-research.png` and `.amp/in/artifacts/r5-32-continents.png`. Both new passages are fully readable; Prague, the carved-device/scrolls account and 32's “She did.” remain intact. The original 04 capture remains current. Preview still compares against shipped R4, not against the earlier R5 draft; Reviewed marks remain reserved for the author. Latest validation results and delivery state are reported in this thread after execution.

Follow-up validation passed: only P/04/32 differ across all 79 manuscript files; datelines and paragraph counts match baseline; exactly the two intended P paragraphs differ, and removing the precise approved 32 insertion restores that entry byte-for-byte. All 156 API comparisons match Git/disk. Word counts: P 1979→1998; 04 806→804; 32 428→452, all within 10%. `git diff --check` and supporting-record link checks pass. The review API now contains an author-set mark for 04; it was left untouched. Local delivery consists of those three manuscript pieces, the canon-ledger addition and this record, still uncommitted and unshipped. Proposal 3 still needs a wording decision.

## Final wording decision — follow the tracks

The author preferred B but noted that “leave while there was still daylight” could mean going home. Approved replacement: “Nangula wanted another observation. Indy wanted to follow the tracks before the rain came. They were both right often enough to be irritating.” Added as a short paragraph after the sideways meetings and before the succession paragraph in P. No claim of a shared island expedition, named incident or additional date is made. The canon ledger records the approved habitual contrast. The rejected daylight and dialogue alternatives above are historical only; no R5 wording decision remains outstanding.

Re-read the complete prologue after insertion and the revised reference paragraph. Checked the new material against the earlier research/Prague passages, existing secrecy, 05's patience contrast, 32's scholarly contribution and protected 44/76 payoffs. `amp orb services ensure` returns HTTP 200 at the same portal. Fresh 2× screenshot `.amp/in/artifacts/r5-prologue-fieldwork.png` was inspected: full new paragraph readable between the intended neighbours, Prague and scrolls intact, no clipping.

Final validation: only P/04/32 differ across 79 manuscript files; all datelines preserved. Removing the exact new paragraph leaves only the two previously approved P paragraph changes. All 156 original/current preview responses match Git/disk; `git diff --check` passes. P now 1979→2021 words (04 806→804; 32 428→452), all within 10%. Only 04 is author-marked Reviewed; no agent-set review marks. All approved R5 material is applied locally with supporting references; no commit, push or shipment has occurred.

## Placement revision — attach the contrast to her research

The author found the standalone paragraph interrupted the breadcrumb thread and was unattached to an action. Removed it from between the meetings and their explanation. In the introductory research paragraph, replaced the overlapping “Indy followed rumours… Nangula followed a creature…” contrast with: “On a dragon's trail, she wanted another observation. Indy wanted to follow the tracks before the rain came. They were both right often enough to be irritating.” The research question now supplies its subject, and the trail supplies the situation for “another observation”; no new expedition, evidence type or dated event is added. The ledger's approved habitual contrast still applies without amendment. This placement is a local revision for author review, not a claim that author satisfaction has been independently verified.

Re-read the prologue in full and inspected `.amp/in/artifacts/r5-prologue-integrated.png` at 2×. The contrast is readable within the introduction, and breadcrumbs now lead directly to “Nangula had known all along.” Earlier fieldwork captures show superseded placement. Before/after remains shipped R4 versus current working tree; no review marks, commits or shipping actions taken.

The author subsequently asked to retain “Indy followed rumours towards a creature; Nangula followed a creature through the rumours.” Restored it immediately after the research question, retaining the concrete trail/observation contrast alongside it. No return to the rejected standalone placement. Re-read the complete prologue, confirmed preview bytes match disk and `git diff --check` passes, and inspected a fresh 2× comparison privately. The author requested no more screenshots in replies; visual verification continues without displaying them. Still local, uncommitted and unshipped; no new facts or reference amendment needed for this restoration.

## Preview diff repair — author requested

The restored sentence took the whole-text word comparison over its 4,000,000-cell guard (1979 × 2025 tokens = 4,007,475). The old fallback presented the entire prologue as deleted/added despite only two changed paragraphs. Reproduced with the real prologue using the actual inline diff functions: no unchanged operations, one whole-file hunk. Git and both API versions confirmed no hidden manuscript changes or line-ending conversion.

At the author's request, changed only the diff implementation in `preview/index.html`: remove matching token prefixes/suffixes before allocating the bounded comparison table; if still too large, anchor on unique matching lines in order and word-diff the intervening blocks. The cell limit remains in force; only an oversized unalignable block falls back to delete/add, not automatically the entire manuscript. No new dependency or service configuration.

Validation: the scratch regression check fails on the old source and passes on the fix. Ten scenarios cover the real prologue, far-apart edits in a 2400-line document, a long single paragraph, identical long text, boundary insertion/deletion, whitespace, empty inputs and entirely replaced large text. Each checks reconstruction and reverting all hunks with their returned ranges. Another 250 seeded mixed-edit cases pass reconstruction/revert checks. In Chromium, the actual prologue reports two hunks, 11035 unchanged characters and first change offset 4416 instead of a whole-file replacement. Inspected the default and changed-region renders privately. Tested the actual single-change Revert and Undo controls with non-GET fetches intercepted: the first change alone reverts, the second remains, and Undo restores the exact original editor bytes. No test write reached the manuscript server and no author review mark was changed. Scratch scripts and inspection captures are removed after validation; screenshots are not included in replies at the author's request. Fix remains local/uncommitted with the R5 work.

## Final author review and shipping validation

The author joined “She was from Namibia and had spent decades…” and joined the observation/tracks sentences with a semicolon in the preview; both edits are preserved. P/04/32 are all marked Reviewed with fingerprints matching current saved content. The author then authorised shipment with “ship”. No manuscript edits were made during shipping preparation.

Re-read P/04/32 in full, inspected their final diffs and checked against the canon ledger, chronology and preserved source constraints. Only P's introduction and work-succession paragraph, 04's teaching attribution and 32's identification example differ from shipped R4. Protected Prague wording, scroll/device mechanism, 44's grief, 76's questions, R3/R4 choices, all datelines and other manuscript files remain unchanged. The ledger records only the approved research and habitual contrast.

Fresh shipping checks pass: old preview source reproduces whole-prologue replacement, fixed source gives two localised hunks; ten large-text/boundary scenarios and 250 seeded reconstruction/revert cases pass. All 156 API comparisons match Git/disk, all 78 selectable pieces reconstruct both versions correctly, and all three review fingerprints match. `git diff --check` passes. Inspected fresh final rendered comparisons privately for P/04/32; changed passages readable, including the author's final punctuation and 32's protected “She did.” The earlier browser Revert/Undo validation remains applicable because the preview code has not changed since. No author review marks were changed by the agent.

Fetched `origin/main` remains at shipped R4 baseline before committing. Preview repair and R5 editorial work will be separate scoped commits; final rebase, push and remote confirmation are reported in the thread after execution.
