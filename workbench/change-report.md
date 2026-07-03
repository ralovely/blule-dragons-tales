# change-report.md — Aizomea refactor, first full pass

**Scope:** Prologue + all 75 entries edited as copies in `entries-v2/` (originals frozen in `entries/` as the "before"; compare in `preview.html`). Editing done in numeric order (author preference) applying each entry's trip voice from `entry-plan.md`.

## 1. §2 fingerprint patterns — before → after (corpus = entries-v2/*.md + prologue)

| Pattern | Baseline | Target | After |
|---|---|---|---|
| `the way (a\|an\|one\|old\|two)` similes | 23 | ≤ 9 | **9** |
| `as if` | 27 | ≤ 12 | **3** |
| `something close(r)? to` | 7 | ≤ 2 | **1** |
| `I can only describe / be described` | 4 | ≤ 1 | **1** (cave mural, 41 — the one sanctioned survivor) |
| `No x. No y.` paired fragments | 7 | ≤ 2 | **2** (41 folded; survivors: "No village. No walls." 54, "No alarms. No schedules." 69) |
| Sentence-initial `Nobody` | 20 | ≤ 8 | **8** (incl. protected "Nobody asks." 20) |
| `It is not …` negation-reframes | 11+ | ≤ 4 | recast/folded throughout; survivors are the excellent ones ("not a sword, but a thimble" 17; "not pottery / birth records" 36; the rock-was-not-a-rock reveal in the prologue) |
| Em-dashes (`---` / `—`) | 36 entries + 11 prologue | ≤ 4, lumpy | **0** punctuation em-dashes (prologue's 8 `---` are markdown section rules; "— Indy" signature sanctioned) |
| "magic" (banned word) | several | 0 | **0** |

Distribution is lumpy by design: most files now show zeroes; survivors cluster in a few.

## 2. Enumerated §9 fixes — status

| # | Fix | Status |
|---|---|---|
| 1 | Entry 15 broken "They are prolonged…" sentence | ✅ repaired |
| 2 | Entry 34 duplicate "six pages / professors wept" line | ✅ deduped (kept "wept, or resigned") |
| 3 | Entries 51 & 56 identical closer | ✅ 51 rewritten (ends on child's claim); 56's line kept (protected) |
| 4 | Anachronisms: soccer (34), brain freeze (62), power dynamics (55) | ✅ football / "the cold-ache" / "chain of command" |
| 5 | Entry 12 bird thread "Tomorrow." | ✅ kept (deliberate loose thread) |
| 6 | Entry 1 "brand new landmass" | ✅ recast ("No chart shows the place"; new-to-maps not new-in-age) |
| 7 | Prologue 1972 comma/em-dash | ✅ fixed (then de-em-dashed entirely) |
| 8 | South-of-France duplicate (3 & 41) | ✅ 3 → Côte Basque (author biographical root); 41 keeps the simile |
| 9 | "Built for someone taller" repeats (2,3,12,13) | ✅ first kept (2); 12 = self-aware running joke; 13 deleted |
| 10 | Economy contradiction (17 & 61 vs 10) | ✅ 17: strikethrough "~~merchants~~ men" (subtle, per author) |
| 11 | Entry 18 sleep/nod paradox | ✅ NO CHANGE (author decision; paradox preserved) |
| 12 | Entry 65 "second visit" | ✅ file retagged `T3-T4`→`T3-T5` (author-approved rename); phrase kept |
| 13 | Entry 47 scale contradiction | ✅ "dining table" → "the size of a bus" (keeps the whole-country-yet-small paradox, but big enough for the meadow/sapling/tenant; "bus" period-fine for 1955) |
| 14 | Entry 9 riding vs 18 carrying | ✅ NO CHANGE (author decision) |
| 15 | Untagged entries (14,15,24–27) | ✅ filename tags satisfy (author-confirmed) |
| 16 | Prologue estate location | ✅ estate English; mother's family Côte Basque (author amendment) |
| 17 | Prologue biography block trim | ✅ trimmed ~15%; "outlasted them all" deleted |
| 18 | Prologue River/Cendre death beats | ✅ River = birthday-cake memory (author direction); Cendre = the row of stones (pays off entry 9) |
| 19 | Prologue "take my hand" ending | ✅ replaced; ends on the compass/object (inherited-tic scene cut per author, shortened to 2 sentences) |
| 20 | Entries 1 & 2 tonal lurch | ✅ in-place default: 1's ending less breezy; 2's orienting opener (no layout swap) |
| 21 | Entry 9 colour-repetition seam | ✅ committed as deliberate journal-repetition w/ strike-throughs (author later dropped the Prague line entirely) |
| 22 | Entry 66 bracketed working notes | ⊘ N/A — author clarified (2026-06-15) these are the **author's own production/layout notes** ("[replace the intro with annotated illustrations?]", "[make a wet journal entry here]"), NOT Indigo's marginalia. Left in place for layout; no Jamie footnote. |

## 3. File / spread integrity

- **75 entry files present, unrenamed** except the one author-approved tag correction (`65-…-T3-T4.md` → `65-…-T3-T5.md`; numeric prefix unchanged, so order and position-keyed spread association intact).
- Topics and paintable moments per `index.md` unchanged — no merges, splits, or reorderings.
- **Length:** corpus 22,952 → 23,296 words (+1.5% overall). No entry moved more than ~±40%. Largest swings: 74 (+35%, tea-surrender + Nangula question), 66 (+18%, Jamie footnote), 64 (+17%, Tic B measuring-notice). Ultra-shorts (11, 22, 48, 57, 73) untouched.
- **Untouched entries (deliberate slack / protected):** 06, 08, 11*, 22*, 27, 38, 48*, 57*, 60, 61, 70, 71, 73*, 75† (* = protected; † = protected-substantially). 14 of 75 left identical — clean entries left clean so the edit distribution is itself lumpy.

## 4. Tic arcs (spot-checked)

- **A haberdashery:** peaks in T3 (17 thimble, 29 tears/mended, 36 kintsugi, 38), present T1/T2 (09, 12, 18 buttoned-fog), into T4/T5 (61 button, 74). 
- **B measure→doubt:** heavy T1 (01,02,04,07,09,10,19), thinning T2/T3, dies with the single T4 notice in **64** ("I seem to have stopped measuring things. Cassius would mind.").
- **C apologies:** 05 (anchor), 10 (river), 53 (cliff). [Weather-escalation beat tried in 67, removed — came from nowhere, author 2026-06-15. Tic carried fine by the three.]
- **D tea:** grievances 03/17/34 → **surrender in 74** ("I call it tea now, and mean it").
- **E French:** back-weighted; existing + 52 (le pauvre), 72 (une berceuse à deux voix).
- **F Nangula question:** attributed in 56 → **final UNATTRIBUTED use in 74** ("What is it *for*?") — the rereader's payoff.

## 5. Furniture added

Strike-throughs (visible thinking): 02, 09, 17 (~~merchants~~), 50 (~~nonsense~~ sense), 68 (~~It is my own.~~). · P.S. addenda: 04, 53, 64 (the measuring-notice, as an after-the-fact realisation). · N.B. measurements: 01, 02, 04, 09, 19, 34. · Editor's notes preserved (all original): 26, 28, 30, 31, 35, 52, 54.

## 6. Outstanding / for author review

- Big length swing flagged: **74** (+35%) — tea-surrender + Nangula question added to a short entry; still under ±40% but the most-changed short piece. Review against its illustration spread.
- Sketch-caption furniture is under-budget (only entry 08's existing captions) — deferred pending illustration placement, since captions must coordinate with art.
- Entry 69 ending: the envious-reflection coda was trimmed, then RESTORED (author 2026-06-15) — it's tied to the River/Kai thread and Indigo's deux-vies conflict, not generic profundity.
- Author has been reviewing per-entry live in the preview throughout.

## 7. Phase 5 verification (run 2026-06-14)

**§11.4 Ending-type audit.** Stinger family (ST+STj) = **17 of 75** (target ≤25 ✓); of these **10 are joke-stingers** (target ≥10 ✓). Pure JOKE endings ≈13 more. Spread is healthy: PF ≈12, IMG ≈14, Q 6, QUOTE 4, LOG 4, MT 2. No run of 3+ identical ending shapes. Adjacent same-family pairs differ in *shape* and so don't read as formula: 64 (poignant admission) → 65 (wet-grinning image); 66 (deadpan one-liner) → 67 (self-implicating domestic aside); 21 (grand) → 22 (dry, protected). Big emotional closers (68, 71, 72, 73, 75) preserved.

**§11.3 Voice swap.** Prologue past-tense:present = 62:14 (retrospective memoir); entries present-tense dominant (498 is/are across 75); untranslated French in 8 entry files, 0 in prologue. Jamie ≠ Indigo on tense, register, and furniture — trivially attributable.

**§11.5 Read-aloud / shape echo.** Corpus-wide repeated sentence-openings sit at normal English frequencies (≤0.2/entry), not clustered within a trip. Negation-reframe survivors ("It is not …" ×6, "This is not …" ×4) are ordinary syntax or the sanctioned keepers, not the epigram template.

**§11.6 Tic arcs.** B (measure→doubt) decays to its single T4 notice in 64 ✓; A (haberdashery) peaks T3 ✓; D (tea) surrenders in 74 ✓; E (French) back-weighted to T4–T5 ✓; F (Nangula question) attributed in 56 → unattributed in 74 ✓.

## 8. New entry (§7a): 74a-the-compass-T5.md — justification

One new entry (of the permitted 3–4; the only candidate that cleared all gates). **Gap served:** the Nangula rework (Tic F was shelved as canon-unsafe) left two needs — Indigo addressing Nangula directly (done lightly in 31) and the compass-succession beat the author requested: Indigo at 70, final trip, wondering who carries the compass after her, with the reader knowing it will be the unborn Jamie. Nothing in the existing 75 could host this without overloading protected 75. **Paintable moment:** the compass open on the desk at night, green-gold eye in lamplight, an old hand beside it. **No new facts:** the compass, its eye, and Nangula's years of waiting-to-choose are all prologue canon; River's manner of holding things echoes 75 without advancing River/Kai. **Voice:** T5 (present, spare, letter-mode). Final form (author-edited, **approved 2026-07-03**): two paragraphs, ~55 words, closing on the twin questions "How did you know? How will I know?" — the succession entirely in implication. Draft header removed by author.

## 8b. New entry (§7a): 21a-the-old-quarrel-T3.md — justification (draft)

The plan's #1 candidate slot: the "teeth" entry, where the island's benevolence is not guaranteed. Author direction (2026-07-04): explicit teeth — an actual dragon fight, north vs south — but vague and long ago, told through evidence only: claw-scars unlike hunters' work (contrast with 31), Manami's five words ("He went south once"), and one fused, singed knot in the Knotted Cord racks. No Manaïari harmed, southern mystery unresolved, no narration of the event itself. **Placement 21a:** immediately after the ceremony that teaches the reader what knots are, and immediately before protected 22 ("Manami and I disagreed today") — quarrel, then its comic domestic echo. **Ending rotation:** 21 ST → 21a Q (paired "Perhaps…") → 22 joke ✓. **Paintable:** the scarred dragon asleep among children, or the ugly knot. ~240 words, `STATUS: draft`.

## 9. Post-review verification (2026-07-03, after the author's full per-entry review)

**Planted-payoff walk — 13/13 threads intact end-to-end:** windowsill row (12→75, "I packed them all"); purple stone (35→trunk note; prologue's "purple crystals" game echo); Hana (03 baby→36 apprentice); River/Kai full chain (61→62→63→65→69→73→75 blue cloth→prologue "somewhere in these pages"); Cassius letters (01, 30 + "never stopped writing" note, 64 "Cassius would mind"); 56's protected cut + 54 pressed leaf + 52 Jamie-walked note; bird promise (12); Elder's nod (18)↔arrival (19); "(Editor's note: She did.)"↔Protection Act; teeth (28)↔1985; button origin; knick-knackery echo (42↔prologue); NEW compass chain (19 eye → 31 "your compass" → 74a succession).

**Voice-swap deep check — 10/10:** seven random Indigo paragraphs and three Jamie paragraphs, shuffled; every one trivially attributable (tense, person, register, furniture). The only sample needing even a beat of thought was a Jamie domestic memory, settled instantly by its child's-eye details.

**Structural-twin pass (same day):** "X is, [aside], Y" opener reduced to its two joke uses (35, 38); "I have spent/been…now" frame de-twinned (33 vs 18); not-figurative disclaimer triplet reduced (50 trimmed; 32, 62 differ); flight-entry purple patches trimmed (23 wink cut, 49 letters-simile cut); 28's essay opener relocated to an earned closing verdict (author); 14 rewritten as a scene-framed history (author-tuned: softened settler claim, Onseki/onsen made implicit).

**Result:** all acceptance criteria met on this pass. Remaining is author sign-off (review once, in the preview) and the deferred sketch-caption furniture (awaits illustration placement).
