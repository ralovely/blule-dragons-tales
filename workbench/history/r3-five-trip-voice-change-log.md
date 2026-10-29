# R3 — Indigo's five-trip voice

**Author-approved for shipping: retained revisions in 21, 33 and 42 only.** The author said “Reviewed. Ship.” after the narrowed selection. [R3 thread](https://ampcode.com/threads/T-01a10e44-8803-767b-8337-0253cf41251d). The master owns tracker updates; remote delivery is confirmed in the thread after execution.

## Author selection after the walkthrough

The author explicitly requested withdrawing seven proposals and retaining three through the [walkthrough thread](https://ampcode.com/threads/T-01a1852f-0282-771d-ba4b-c369a859993f). That initial request authorised local revision only; the subsequent “Reviewed. Ship.” authorises committing and shipping this narrowed set and its record. No Reviewed marks are set by the agent.

| Disposition | Entries | Applied action |
|---|---|---|
| Retained | 21, 33, 42 | Existing R3 wording kept byte-for-byte: punctuality, fishing partnership, sustained claw-mark study. |
| Withdrawn | 01, 07, 13, 61, 65, 67, 70 | Restored complete files exactly from shipped R2, including all earlier author revisions. No alternative wording substituted. |

Only three manuscript files now differ from shipped R2. The initial ten-proposal record and sample assessment below are historical, not a description or endorsement of the current selection. In particular, the T1, T4 and T5 proposals are withdrawn; the earlier claims about their effect must not be read as findings about the current manuscript. R1/R2 text, references, source ledger/logs and the imported master tracker remain intact. The preview continues to compare shipped R2 with the working tree.

### Selection validation

- Re-read all three retained entries and all seven restored entries in full. The retained paragraphs, dates, stories and endings are unchanged from the initial R3 proposals; no further editorial adjustment was made.
- Assertions across all 79 manuscript files confirm that only 21/33/42 differ from shipped R2; the other 76 match it byte-for-byte. Pre-action fingerprints confirm the three retained files and every non-withdrawn manuscript file remain unchanged. All datelines and editor's notes match R2. The imported plan retains its pre-action hash. The initial post-restoration check found the review-state file unchanged and empty. A later check found valid review marks for 21 and 33 added externally during validation; these were left intact. The agent did not add, remove or overwrite any review marks.
- `git diff --check` passes. All 156 original/current API comparisons pass across the 78 selectable preview files; `/api/meta` identifies the R2 commit as its baseline. `amp orb services ensure` reports the preview running and responding HTTP 200.
- Inspected 2× rendered comparisons for 21/33/42 and the restored 01. The retained changes are legible, and 01 reports “No changes”. The inline diff clips part of 21's deleted wording; switching to the existing plain baseline view exposes both complete paragraphs without clipping. No preview tooling was changed.
- At selection review, preview remained available at https://t-03gzvqndyibx13muth7tkfvh9-p22553.onamp.dev/ and delivery was local and uncommitted. The master tracker was not edited.

### Final shipping validation

On the subsequent explicit shipping request, re-read all three retained entries in full and checked them against the authoritative references. No unintended edit, altered fact or contradiction was found. The final diff contains one revised paragraph in each entry. Assertions confirm all other 76 manuscript files match shipped R2 exactly, including the seven withdrawals, all R1/R2 wording and protected entries. Datelines, editor's notes and all final paragraphs remain unchanged. All 156 original/current preview API comparisons pass. Inspected fresh 2× plain-baseline comparisons for 21/33/42; all affected paragraphs are fully readable. `git diff --check` passes. Fetch found `origin/main` still at the R2 baseline before commit preparation. Only the three manuscript files and this record belong in the commit; preserve the imported coordination plan outside it. Rebase, final-byte verification, push and remote confirmation are reported in the thread after execution.

## Initial baseline and scope (5 October 2026)

Started from [shipped R0–R2](https://github.com/ralovely/blule-dragons-tales/commit/44143f7a4221802d3bab6ba24c1accf174e43f8d); fetch confirmed `origin/main` at the same commit. After confirming a clean worktree, downloaded `workbench/plans/editorial-revision-plan.md` from the live master. Its receipt SHA-256 is `b610f36c9925fc1077e3d01a32676219c94fa7055bcbe0058fe436d0b6cca0d1`. That file is imported coordination baseline, not R3 authorship; do not stage or ship its tracker with R3.

Read the whole prologue and 77 entries, the empty colophon, all three authoritative references, R1/R2 logs and the R2 source ledger before editing. The matrix's targets are diagnostic. Ten entries receive one changed paragraph each; the other 69 manuscript files, counting prologue and colophon, are byte-identical to baseline.

All interventions are wording-only proposals. No scene, measurement, relationship, dateline, mechanism or biography is added. No new conspicuous period expression, French insertion or age announcement is introduced. R2's sourced choices and unresolved claims remain as recorded; this pass makes no new historical-authenticity claim. Society, Nangula, material coherence and Jamie remain with their later owners.

## Initial proposals and phrase anchors (dispositions above supersede this list)

Word counts include datelines and use whitespace-separated tokens, as in the preview. Every entry remains within 10% of baseline length.

| Entry | Anchor and intervention | Rationale / retention | Words before → after |
|---|---|---|---|
| 01 · T1 | “Its edges are never the same” links the shifting outline to the stationary cliffs before explaining the mist | Follow the observer's discrimination in an accumulating sentence. Keep two failed sketches, the mapping joke, Cassius address and island-shape uncertainty. | 283 → 283 |
| 07 · T1 | “Tall as they are” and “Some of the ridges curve” gather short impressions into qualified observations | Longer syntax leads to the short “Probably a coincidence.” Keep the reviewed “not really”, measurements, abandoned binomial, Cassius's sketch ordering and floating-island description. | 427 → 422 |
| 13 · T2 | “The menu is a wonderful kind of madness” gives way to rice, cook, hand signal and dragon | Attend to the coordinated process without another first-arrival flourish. Keep the surgeon comparison, pulse, taste, French exclamation, berries, venom and pudding-bowl ending. No society claim is revised. | 328 → 307 |
| 33 · T2 frame | “The sea dragons herd fish” puts the working relationship first; the boat observation qualifies it | Explain what she can follow without pretending she sees the signal. Preserve sheepdog comparison, “Manners”, singing, current uncertainty, retrospective coastal familiarity and southern boat. | 552 → 533 |
| 21 · T3 | “I have tested this rigorously. Admirable, in principle. Infuriating when one is waiting.” | Let the experienced scientist become personally impatient rather than expound a philosophy. Retain the dusk correction, Manami's silent company, all stories, Sayo and the mayflies/mountains stinger. | 619 → 610 |
| 42 · T3 | “Weeks of sketching claw marks” leads with sustained work and unresolved judgement | Habit and stubborn curiosity, followed by a long catalogue and the unchanged disagreement with Manami. Preserve depth, repeated patterns, mural uncertainty and cave routines. | 412 → 409 |
| 65 · T4 | “Cendre studied the fireproofed thatch” moves the two children's responses ahead of the village's recognition | Her account notices her adult children first. Arrival nods remain retrospective; no event changes. R1's “over seven years” and “since I last saw it”, smell speculation and the Cassius measuring P.S. remain verbatim. | 212 → 213 |
| 67 · T4 | “River and I have learnt about the drying process” replaces the impersonal opening of the second paragraph | Mother and daughter participate in the same mistake before Cendre's dry, silent contrast. Keep the repeated hard-way joke, all quantities, the third shake and both production notes. | 208 → 210 |
| 61 · T5 | “It has followed me with the tune ever since”; “Ignoring it did nothing. Nor did shooing it.” | Economise on explanation and report failed remedies directly. Keep the extended medley anecdote: T5 need not become solemn or uniformly terse. Organ/flood, French lullaby, choir and sacrifice ending remain. | 137 → 127 |
| 70 · T5 frame | “After sunset, our only lights…” replaces the broad introductory declaration and brings the light to her own use | Familiar navigation rather than introducing the island again. Preserve light sources, faint craft glow, reading limit, nocturnal detail, full-moon behaviour, remembered fear and English sleep, and the entire River ending. | 340 → 317 |

## Initial deliberate retentions

All eight R2 entries (16/29/32/35/60/62/71/75) are unchanged, including Paris and the author's saved-up clothing coupons. All R1 wording survives; only an unrelated paragraph in 65 changes. Entry 66 is entirely unchanged: two separate dated excerpts, with “took to surfing”, no old journal carried between trips and no retrospective P.S.

Protected entries 23/49/74 and all of 77 remain untouched, as do 11/58's brief forms, 57's cut, the bird promise, every editor's note and all endings. Grief is already carried by 31's direct address and by the surrounding T3 life; no extra bereavement reminder is inserted. Physical limits and present company already work in 72/75/77. Scientific precision survives into the late trips. None of these qualities is assigned exclusively to an age.

## Initial unlabelled-sample editorial assessment

Read fifteen passages without titles, datelines or trip tags, shuffled with a fixed seed, plus a sixteenth unlabelled passage from 21 to include its revised punctuality paragraph. Compared their cadence and attention. These were selected by the editing agent, with the key available and the manuscript already familiar: **this was not an independent blind test**, nor an audio/read-aloud test. Samples differ in length; names, subject matter and one production note remained visible. No trip-identification accuracy is claimed.

| Trip | Sample key and anchors | Audible distinction and remaining weakness |
|---|---|---|
| T1 | A = 01 coastline; B = 07 opening; N = 36 future colleague and goat milk | A/B accumulate observations before a provisional conclusion; N supplies the argumentative scientist and English comparison. A could still belong to later fieldwork. The unchanged early fragments in 02 prevent “young” from meaning only long sentences. |
| T2 | L = 13 cooking; K = 33 fishing; G = 18 logistics opening | Declarative process, qualified access to evidence, and an organising explanation. More controlled than A/B, but L is not independently datable: topic does some of the work. This is the weakest trip boundary. |
| T3 | E = 21 amphitheatre and silent Manami; P = 21 punctuality; J = 42 claw marks; I = 31 Cassius ending | The broadest range: setting, irritated habit, sustained zoology, then personal address stripped of explanation. E alone has little age signature; J could be T2 without the accumulated relationship context. Grief stays intermittent rather than colouring every page. |
| T4 | O = 65 children at settlement; M = 67 drying; C = 69 departure | Cendre and River organise what the mother notices; she recognises similarities without directing their choices. M retains Indigo's own foolishness. Names and relationships strongly cue the period, so this is evidence of changed attention, not purely syntactic differentiation. |
| T5 | F = 61 hymn; H = 70 opening; D = 75 fog and tea | Failed remedies stated economically, familiar light put to use, then chosen company and acknowledged knees. D remains spacious and speculative. F could be Indigo at several ages; preserving the comic speaker is preferable to adding age signals. |

The movement is clearer across groups than in isolated sentences. The author should judge whether that restraint is sufficient, particularly T1/T2, whether 21 loses a valued philosophical joke, and whether 65's children-first ordering earns its small backward glance to arrival. These are editorial decisions, not failed validation checks.

## Initial validation and review surface

- Re-read all ten changed pieces in full after editing, and re-read their immediate thematic neighbours: 02/06/08/12/14/20/22/32/34/41/43/60/62/64/66/68/69/71. Rechecked changed paragraphs against the canon and their related payoffs. No canon amendment is proposed; references remain unchanged.
- Python assertions across 79 manuscript files passed: exactly the ten listed files change, exactly one paragraph per file; every dateline and editor's note matches baseline; all eight R2 entries, protected whole entries, brief pieces, 66, 65's R1 paragraphs/P.S. and 67's layout notes are retained. The single protected em dash count is unchanged. All final paragraphs are unchanged except the intentionally single-paragraph entry 61, whose ending is verbatim. Read the altered syntax for repeated formulas: T1's two longer clauses and T3's clipped irritation are local choices, not a new repeated template.
- Authoritative references, R1/R2 logs and source ledger are byte-identical to baseline. The imported master plan still matches its receipt hash. `git diff --check` passes.
- Started the existing preview with `amp orb services ensure`. Its baseline resolves to shipped R2, with 78 selectable files. All twenty original/current API comparisons match Git/disk. Review API returns an empty list in this fresh orb; no Reviewed marks were set or cleared. Historical R1/R2 approval is evidenced by their shipped commits/logs, not a copied local review-state file.
- Opened all ten comparisons in Chromium at 2× and inspected their captures. Every revised passage is visible and legible. Inspected 70 again after scrolling to its complete River ending. The existing inline diff concatenates some replacement words and makes 65's reordered paragraph look split; clean working text is legible. This is a preview limitation, not altered manuscript paragraph spacing. No preview code, save, revert or review control was changed.

At initial review, the live preview retained `main` versus the editable working tree. The earlier `.amp/in/artifacts/r3-voice-comparison.png` capture shows the now-withdrawn 61 proposal and is not evidence of the current selection. R3 remained local and uncommitted. No tracker update, push, merge or archive was performed.
