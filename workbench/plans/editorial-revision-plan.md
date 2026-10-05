# Editorial revision master plan

Reconciled 5 October 2026 against the complete manuscript and the approved revision history. This replaces the former ten-pass execution script. The original pass numbers remain as cross-references, not an instruction to repeat completed work.

**Master thread:** [Editorial coordination](https://ampcode.com/threads/T-01a10d5e-807d-76f2-989b-2e2fa505ae1d). The author designated this as the overarching thread, with one child thread per work item. This file is the durable tracker; the master owns its status and dependency updates.

## Authority and baseline

- `manuscript/1-prologue.md` and `manuscript/2-entries/` contain the current reading text: a prologue and 77 thematically ordered entries. `manuscript/3-colophon.md` is empty; filling it is outside this revision.
- [Canon ledger](../../reference/canon-ledger.md): facts, mechanics, identities, payoffs and protected language.
- [Chronology](../../reference/chronology.md): applied datelines and trip windows; unresolved collisions are explicitly listed there. Applied does not mean every inference has been validated.
- [Timeline](../../reference/timeline.md): a navigational summary of those authorities, not a second set of dates or a proposed new entry order.
- [Historical entry plan](entry-plan.md): earlier shape, voice and tic experiments. It is useful context, not a current task list or authority over subsequent author review.
- [Pass 1 log](../history/pass-01-change-log.md) and [Pass 7 log](../history/pass-07-change-log.md): records of work at their respective dates, not guarantees about the present text.
- [World-lore candidates](../notes/world-lore-candidates.md): unapproved brainstorming. No candidate becomes canon by appearing in a brief.

The manuscript was author-reviewed after Pass 1. [The 20 September author-review commit](https://github.com/ralovely/blule-dragons-tales/commit/5c34892899c4e448c63dd62a01503e09f798d3f2) deliberately restored or revised numerous passages. Preserve that baseline. A historical search target is not permission to reverse an author choice. When the manuscript and ledger conflict, establish provenance, reconcile documented decisions, and ask about genuinely unresolved facts.

All new entry references use canonical 01–77 numbers and actual filenames. Historical conversion: old 01–21 unchanged; 21a → 22; old 22–74 → 23–75; 74a → 76; 75 → 77. Historical `story/` or root manuscript paths now resolve under `manuscript/`; old workbench canon/chronology paths now resolve under `reference/`.

## Settled work to preserve

| Earlier pass | Current state | Evidence and remaining boundary |
|---|---|---|
| 1 — rhetoric | Applied, then author-reviewed | The old zero-results report describes the pre-review pass. Current strict searches find `not really` in 07 and `not … but` in 32. These are review questions, not automatic regressions. Only the protected signature em dash remains. |
| 7 — residents | Approved scope applied, 4 October | Sayo 05/21; Sumi 17/66; Emi 35/37; Ren 52/73; Hana's motherhood in 73. See ledger and pass log. No obligation to fill the discarded candidate roster. |
| 9 — Japanese inheritance | Core revision applied, 20 September | Settlers brought gourd seeds and bathing customs; dragons already used heated pools. Kintsugi remains a comparison, with no Aizomean priority claim. No universal naming etymology has been established. |
| 8 — selected plausibility fixes | Applied, 21 September | Aizomea is an island; 53 retains Pepper's ~150-mile estimate and Jamie's ~100-mile correction. Trunk hidden since Indigo's death; Chestnut returns nearly a hundred years later; 59 explicitly recalls ten years earlier. [Commit](https://github.com/ralovely/blule-dragons-tales/commit/60fe0d08b3cc6e10fca7bcbc3cb64a39431fa5ec). |

Passes 2–6 remain partially prepared or outstanding, not completed. Pass 8 has a smaller residual scope. Pass 10 remains a final audit.

## Work tracker

States distinguish **queued**, **active**, **awaiting author decision**, **ready for review**, and **shipped**. A prepared dossier is not an approved decision; a child report is not an integrated or shipped change. Record the child link, evidence and delivery state when each item advances.

| ID | Work item | Dependency | Status / child thread |
|---|---|---|---|
| R0 | Reconcile plan and references | None | Author authorised shipment from master; six documentation files re-read; relative links and all 77 datelines checked; manuscript unchanged; remote confirmation recorded in master thread |
| R1 | Continuity decisions and narrow repairs | R0 shipped first | Author-reviewed and rechecked in [continuity child](https://ampcode.com/threads/T-01a10d72-5ce5-77ba-a8f8-d0ea8e4107a2): child reports all six Reviewed fingerprints match saved/API bytes, exact-change check passed after author revisions; author authorised shipment after R0; child owns delivery |
| R2 | Period-language research palette | R0 baseline available | Ready for author review: [research child](https://ampcode.com/threads/T-01a10d72-a110-726b-80a8-5c25a10d71d1) delivered a bounded palette, copied to master and read; four suspect expressions have earlier witnesses, other claims remain unresolved; no manuscript edits; uncommitted and unshipped |
| R3 | Indigo's five-trip voice (old Pass 2) | R1 resolved for affected passages; R2 palette reviewed | Queued |
| R4 | Manaïari social texture (old Pass 3) | R3 | Queued |
| R5 | Nangula's independent agency (old Pass 4) | R4; author decisions on new facts | Queued |
| R6 | Blue-stone inventory and coherence (old Pass 5) | R5 for manuscript edits; inventory may precede it | Queued |
| R7 | Remaining plausibility decisions (old Pass 8) | R6; coordinate legal wording with R8 | Queued |
| R8 | Jamie's distinct voice (old Pass 6) | R3–R7 settled for affected text | Queued |
| R9 | Regression, continuity and read-aloud audit (old Pass 10) | All accepted edits integrated | Queued |

Launch ready items rather than creating all child threads against an obsolete snapshot. Manuscript editing is sequential because passes share files. Independent research can overlap; its findings remain proposals until reviewed.

R1 and R2 were launched on 5 October with instructions to download all six reconciled documents directly from the master's live workspace. Their initial manuscript baseline is the remote default branch including the 4 October resident pass; the master has no manuscript changes. These imported documents are shared baseline, not child-authored work. The author subsequently authorised R0 shipment from the master, then R1 shipment from its child, superseding the earlier delivery restriction recorded below. R1 must preserve this current tracker and apply its reference delta over the imported R0 baseline. The dossiers remain child-owned and are not included in the six-file R0 shipment.

R1 review update: the author approved the other recommendations and replaced G with two distinct excerpts because Pepper does not carry old journals between trips. Entry 66 retains 18 April 1956 and adds 22 April 1971 for the second excerpt. During preview review, the author made 05 end at the permanent stain (no remembered question), removed the second elapsed-year count in 65, and changed 66 to “took to surfing” so the excerpt stands independently. Entry 62 remains unchanged; Chestnut's exact naming date is unspecified. The child reports no new continuity conflict, synchronised references and supersession recorded in `workbench/history/r1-continuity-change-log.md`. Its comparison across all 77 entries and prologue found only approved repairs and these author revisions; all six Reviewed fingerprints match saved bytes and API content. Rechecking made no manuscript edits. The author requested a double-check, not shipping. These changes remain local to the child; refresh the master's earlier proposal dossier and references before integration. [Author preview](https://t-03gzuht0rz9ifth7rwnu0brfm-p26928.onamp.dev/ "amp-portal"). No implementation files have been integrated here.

R2 follow-up: at the author's request for a couple of subtle WWII references, the child reports adding optional research on Make Do and Mend / clothes coupons (60 or 33) and the liberation of Paris on 25 August 1944 (32's 25 August 1948 dateline and Montmartre connection). The proposal is a domestic trace plus a brief public-event recollection, without invented wartime whereabouts, service or family experiences. These are research options, not authorised manuscript insertions. Re-download `workbench/notes/pepper-period-language-ledger.md` from R2 before integration: the master's copy predates this addition. The child reports documentation checks passed and manuscript unchanged; still uncommitted and unshipped.

## Child-thread and review workflow

1. The master briefs one item in `ralovely/blule-dragons-tales`, linking this plan and naming the exact scope, dependencies and protected material. Children do their own work, without creating further threads unless the author requests it.
2. Give each child the actual baseline. New orbs begin from the remote default branch, not this thread's local `main` or uncommitted files. Transfer unshipped documents or changes with Amp file-transfer tools, or start after the required changes have shipped. Record which baseline was used.
3. Read the ledger and chronology in full before editing; read each affected entry in full. Classify interventions as wording-only, canon clarification or canon amendment. New events, relationships, mechanics, dates and cultural explanations need an explicit author decision. Existing approval of editorial work is not approval of every possible new fact.
4. Each child owns its manuscript changes, necessary reference maintenance, validation and review surface in its own checkout. Keep a concise item log under `workbench/history/` containing decisions, affected phrase anchors, protections and unresolved questions. Research and decision dossiers belong under `workbench/notes/`.
5. Preserve a meaningful before/after preview until author approval. Use `amp orb services ensure`; reserve “Reviewed” marks for the author. Follow root `AGENTS.md` for validation and shipping. This plan grants no blanket push or merge permission.
6. Report back to the master with the child link, findings, decisions needed, files changed, validation evidence and actual delivery state. The master checks the evidence, records status here, and supplies the accepted baseline to the next child. Do not duplicate child implementation in the master checkout.

The earlier single `editorial/full-plan` branch and per-entry commit recipe are retired. Use reviewable item-scoped changes in each child; keep unrelated work separate. The overarching master stays available for coordination while child shipping follows the repository's archival workflow.

## Editorial constraints

- Keep the prologue frame, 77 subjects, five trips, thematic order and emotional arc. No new scenes or merged/deleted entries to solve a local problem.
- Preserve each entry's central image, joke or discovery. Aim to stay within roughly 10% of its starting length unless the author agrees otherwise.
- Use British English. Keep warmth, exuberance and deliberate unevenness; restraint is not a universal target.
- Preserve the ledger's protected language and devices: whole entries 23, 49 and 74; 77 substantially as-is; 57's unfinished final sentence; 67's layout notes; the bird promise; River/Kai's implicit relationship; the compass and keepsake payoffs. Preserve brief entry shapes, including 11 and 58.
- Keep established blue-stone, amulet, riding/carrying, gift-economy and unwritten-language facts unless their amendment is approved. Do not rationalise deliberate fantasy paradoxes away.
- Avoid introducing repetitive correction formulas, generated lists, moral endings and ornamental em dashes. Keep the protected `— Indy` signature. Use `P.S.` for genuine additions, with occasional `Evening.` or `Next morning.` where apt.
- Search counts diagnose clusters; they do not decide prose quality. Preserve author-reviewed language unless the current item earns and obtains a different decision. The protected Prague egg revelation is not a fault.
- After each change, re-read the whole entry and its thematic neighbours; inspect the affected manuscript in the preview and check relevant dates, protections and payoffs. Documentation-only work needs reference and link checks, not a manuscript preview.

## R1 — Continuity decisions and narrow repairs

Start with `workbench/notes/continuity-decision-dossier.md`: exact passages, competing facts, provenance, smallest wording option, date/canon option if needed, affected payoffs and recommendation. Separate a confirmed contradiction from an ambiguity. Do not move dates or create a literacy explanation merely to make the check pass.

Known questions:

| Anchor | Question to resolve |
|---|---|
| 05 / 09 | On 29 June 1938 Pepper learns why her fingers stain; on 20 July she still cannot account for it. Preserve the thematic mystery/reveal while making her dated knowledge coherent. |
| 73 / language ledger | Hana “reads” to her children, but Manaïari has no written form. Preserve Hana's motherhood and the dragon's nightly visit. Determine whether this is loose wording or a deliberate exception before changing it. |
| 60 | Dated 14 July 1948, about six weeks after arrival, yet one activity has continued “for months.” Determine whether a remembered observation or later addition is intended. |
| 62 | Both the initial exchange and apparent return past the stall occur “this morning.” Check whether the sequence needs clarification. |
| 64 | “Yesterday” and “this morning” lead into “by the end of the week.” Resolve the time of writing without disturbing the River/Manami ending. |
| 65 | “Gone eight years” versus departure in April 1956; the Hiccupper was seen in October 1955. Distinguish rounded time since that meeting from time away from Aizomea. |
| 66 | Body dated April 1956; River/Kai paragraph belongs to 1971. The dual-trip fact is settled; visible presentation remains undecided. |
| P / birthdays | Indigo is born 9 June 1901 but described as six at Chestnut's naming on 30 April 1907. Preserve the age-six story; seek a decision about the conflicting exact date. |

Inspect the applied chronology for related collisions, without expanding into a new plot or comprehensive plausibility rewrite. Completion: each confirmed collision is resolved consistently after the required decision, or explicitly remains blocked; manuscript and references agree; protected payoffs survive.

## R2 — Research period language before using it

Create `workbench/notes/pepper-period-language-ledger.md`. Research Indigo's cohort: an educated British woman born in 1901, with a French mother, scientific training and international travel. T5 should retain habits formed in 1915–1935, not adopt a younger generation's voice.

Prioritise dated private letters, diaries and field notes by comparable women; then contemporary institutional sources, broadcasts and historical dictionaries/corpora. Modern historical fiction, unsourced phrase lists and model recollection are not evidence. Short quotations support linguistic analysis, not wholesale imitation of a real writer.

For each candidate record expression/construction, meaning and tone, attested date, attributable source and locator, writer/background where known, register, suitable trips and restriction on use. Include uncertainty and rejected anachronisms. The palette must be reviewed before manuscript integration.

Research doubt and scientific caution, surprise, irritation, affection, notebook corrections, domestic/professional objects, travel, and plausible French usage. Favour syntax and collocation over conspicuous slang; no marker quota per entry. Source windows: T1 principally 1925–39; T2 1939–50; T3 1948–57; T4 1957–65; T5 1965–72 with cohort continuity.

Verify rather than presume wrong: `technically correct` (06), `public service` and `involuntary rotating art gallery` (60), `the window had closed` (62), `chain of command` (56), `supervisory` (63), `technically possible but not worth the bother` (66), emotional vocabulary (04/30), and `stop performing` (protected 77, report only). Check contractions as register, not a ban. Audit date-sensitive references to Oxford, Harley Street, the Muséum, the UN, medicines, transport and scientific terminology.

Completion: a modest usable palette with verified dates and source locators, supported recommendations, and an explicit list of unresolved claims. No manuscript edits in the research stage.

## R3 — Make Indigo age on the page

| Trip | Movement and attention | Main targets / comparators |
|---|---|---|
| T1, 1938–39 | Accumulating scientific sentences, measurements, English comparisons, uncertainty and self-correction | Targets 01/03/04/07/09/20/35/44/71; compare 02/19/36 |
| T2, 1948 | Controlled authority, systems, consequences, fewer first-arrival flourishes | Targets 13/33/60; check 59; compare 18/32 |
| T3, 1955–56 | Widest rhythm; habits, grief, relationships and stubbornly zoological detail | Targets 21/29/30/41/42/48/50/52/53; compare 23/31/49; preserve 57's cut |
| T4, 1963 | Mother watching adult children: Cendre organises and measures; River joins and belongs | Targets 62/63/65/67/68; compare 64/69 |
| T5, 1971 | Economy, physical limits, present company and departures; humour still possible | Targets 61/70 and 66's late paragraph; compare 45/72/74/75/76 and protected 77 |

The matrix guides differences, not uniform sentence lengths or forced tense changes. A date or age announcement is not voice work. Integrate only reviewed, sourced period language; usually at most one conspicuous marker in a short entry, two in a long one, and none where unnecessary. Preserve the author-reviewed humour and strong short entries.

Completion: compare at least three unlabelled passages per trip, recording which differences are audible and which remain weak. This is an editorial assessment, not a claim of an independent blind test unless one was actually conducted. Check mixed-trip cues, source every introduced dated expression, and inspect new cadence clusters.

## R4 — Give Manaïari society texture without making it grim

Primary targets: 03/04/10/13/14/17/21/25/29/30/33/37/53–56/62. Preserve the completed resident and cultural-inheritance work.

Limit Pepper's sample to the people and places she knows. Recognise healers, mediators and harbour authorities as institutions; show the costs of obligations, patience or disagreement. Let locals differ without adding cruelty or deprivation as proof of realism.

Preserve no money, no ownership-word, favours remembered but not counted, worthless gold, an unwritten language, and all amulet mechanics. Value need not mean price; oral disagreement need not mean a hidden script. Distinguish companionship from a universal cure in 30 and beautiful teeth from universal health in 29. Use Emi's existing opinion and Sayo's impatience before inventing further people.

Manami remains a friend with competence and humour, not an infallible spokesperson. Look for personal answers, disagreement and imperfect understanding. Protect 23's joke rather than using it as an instruction to make her always right elsewhere.

Completion: the sample limits and institutional roles are legible; several interpersonal or regional differences arise naturally; no new accounting, ownership grammar or literacy system has slipped in. New factual details are approved and ledgered.

## R5 — Give Nangula an independent life

Read all her passages together: P, 02/04/05/20/25/32/44/76. Preserve the professional research already implied, lifelong solo visits, English teaching, breadcrumbs, Prague paired eggs, carved device, scrolls, death in Namibia in 1935 and compass succession. Indigo and Nangula never discussed Aizomea; all island addresses are posthumous.

Propose a small number of concrete professional contributions, habits or substantive differences that make her purpose legible independently of Indigo. Added biography is an author decision, not a wording-only edit. Ground secrecy and succession in responsibility rather than timelessness and tests of a chosen heroine. Credit her scholarship without inventing authorship of the transfer mechanism.

Research the intended use of `Sossusvlei` as a family name before recommending any replacement; preserve it until a specific amendment is approved. Do not annex her to Aizomea by turning Pepper's grief in 44 into objective spiritual fact.

Completion: a reader can identify Nangula's own purpose, a contribution and a complementary difference; the chronology and secrecy remain intact. Coordinate the resulting prologue facts with R8.

## R6 — Make blue stone's uses cohere

Begin with `workbench/notes/blue-stone-decision-dossier.md`, one row per occurrence: exact claim, canon status, narrative function, proposed wording clarification and any requested amendment. Include P and 06/07/08/09/12/24–30/32/34/37/42/46/52/63/66/70/76 and find any others in the corpus.

The previous plan omitted an existing claim: **34 already says traces of blue stone make one egg variety lighter than air**. Inventory that claim; do not silently remove it or generalise it to all objects. The Prague humming egg is not a lump of blue stone. The ledger's reconciliation notes distinguish omissions from new approvals.

Use recurring descriptive families as editorial aids, not new physical laws: resonance/response; prepared craft material; long contact/incorporation; dragon-mediated behaviour. Keep permanent blue hands, domestic uses, glow/full moon, teeth perimeter, poultice and food, humming season, harvest-only riding and every amulet property. Preserve mystery while distinguishing observation, report and inference.

Completion: all occurrences inventoried; related uses share sensory/craft vocabulary; no property weakened without approval, no new universal mechanism invented, no use of `magic` to describe the stone in manuscript prose.

## R7 — Resolve the remaining plausibility questions

Create `workbench/notes/plausibility-decision-dossier.md` with current fact, smallest wording option, canon-changing option only if needed, evidence and dependent passages. Research should resolve a real distraction, not require the fantasy to operate as a technical manual.

Remaining targets: `Dragon Protection Act` as an international law in P; aerial/radio/satellite concealment beyond the maritime account in 18; hot-air glider launch in 24; implications of the unbreakable promise in 25; `Mouelleubleus` as a Manaïari term in 46. Economy/value belongs to R4, dating collisions to R1, floating-egg material to R6. Keep the already settled island scale and prologue elapsed-time wording.

Completion: selected options are approved, applied and reflected in references, or explicitly declined. A speculative concern does not itself require an explanatory sentence.

## R8 — Separate Jamie's prose from Indigo's

Work on P and the seven editor's notes in 27/29/31/32/36/53/55. Jamie reconstructs from family memory, journals, letters, objects and personal travel; Indigo observes in the field. Keep Jamie's domestic specificity and allow scepticism or irritation without flattening affection.

Preserve the information architecture and all protected prologue language: the building argument, paired-humming exchange, Prague egg revelation and complete note to Jamie. Preserve `She did.` in 32, the annual amulet glow, teeth, purple stone, Cassius correspondence, Jamie's island travel and green leaf. Entry 67's bracketed text belongs to production, not Jamie.

Completion: the two voices differ without names or date labels; Jamie's certainty has identifiable grounds; personal judgement appears alongside affection; no invented archive fact or family event has bypassed approval.

## R9 — Final audit against the accepted manuscript

- Re-read the whole prologue and all 77 entries, then the prologue beside T1, trip samples, society passages, every Nangula reference and the blue-stone inventory.
- Read entry endings consecutively and read aloud in groups of ten. Report whether read-aloud actually occurred; visual inspection is not equivalent.
- Compare every dateline/trip tag, character recurrence, material property and planted payoff with the reconciled references. Confirm protected text, short shapes, cut, layout notes and all seven editor's notes.
- Search correction formulas, repeated exposition joints, universal claims and adjective clusters. Compare with the author-reviewed baseline and item logs. Report retained author choices separately from new unwanted patterns; zero matches is not a substitute for editorial judgement.
- Check each newly introduced dated phrase against the reviewed source ledger; check each factual amendment against an explicit decision.
- Exercise the affected manuscript preview, preserve the before/after comparison for approval, and report actual validation and delivery state.

Acceptance: coherent chronology and canon; distinct but continuous voices; social variety; Nangula's agency; related blue-stone uses; inherited Japanese culture; preserved warmth, discoveries and emotional restraint. No fresh global rewrite at the audit stage. Route any unresolved issue to its owning item and keep it visible in this tracker.
