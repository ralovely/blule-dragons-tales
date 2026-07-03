# Aizomea Refactor — Plan, Task List & Style Guide for the Editing Agent

**Inputs:** `1-prologue.md` (Jamie's frame narrative) and an `entries/` directory containing **one file per journal entry** (75 files, tagged [T1]–[T5] for the five trips: 1938, 1948, 1955, 1963, 1971).

**Repository conventions (Claude Code):**
- **Discover the filename convention first** (likely a numeric prefix encoding entry order) and never rename existing files — spread associations and order depend on them.
- **Create `index.md` in Phase 0:** the authoritative ordered manifest (filename → entry number → trip tag → topic → paintable moment → word count). This *is* the topic-anchor table of §2; all other planning files key on filename.
- **Edit files in place; use git as the safety net.** Commit at the end of each phase and each batch (§11) with messages like `T1 batch 1/2: entries 01–08 — de-tick + tic placement`. Never mix mechanical fixes and voice rewrites in one commit; reviewability of diffs is part of the deliverable.
- **New entries (§7a) are new files** named to slot between neighbours without renumbering anything (e.g., `23a-…` between `23-…` and `24-…`), registered in `index.md`, and clearly marked `STATUS: draft — author approval pending` at the top of the file.
- Working files (`canon-ledger.md`, `index.md`, `entry-plan.md`, `change-report.md`, `queries-for-author.md`) live in a `workbench/` directory, not in `entries/`.
- The per-file layout is an advantage: greps and word counts run per entry for free, and §11 verification numbers must be reported **per file and as totals**.

**Mission, in priority order:**
1. Remove the AI prose fingerprint so the text reads as unmistakably human-written.
2. Preserve and **reinforce** the two voices: Lady Indigo Pepper (journals) and Jamie (prologue).
3. Keep **every world fact intact** — dates, names, creatures, mechanics, geography — except the enumerated fixes in §9.
4. Differentiate the *structure* of the prologue (memoir) from the entries (field journal).
5. Give Lady P. a small kit of personal tics that **evolve across the five trips**.

**One honest caveat to hold while working:** no edit can guarantee a "not AI" verdict from a detector, and that is not the goal. The goal is reader perception: eliminate the recognisable 2024-model house style (template sentences, uniform architecture, aphoristic closers) and replace it with idiosyncratic, unevenly distributed, period-correct human texture. Humans repeat themselves too — but their repetitions are personal, lumpy, and lexical, not structural and uniform. That is the standard.

---

## 1. Non-negotiables

- **The 75 existing entries keep their order and their topics.** Illustration spreads are already associated with entries, so no merging, splitting, deleting, or reordering. Every entry keeps its subject, its trip tag, and its primary illustration anchor (the paintable moment). Within that, length is flexible: actual layout has not begun, so entries may grow or shrink where the rewrite genuinely benefits — but the illustration anchor must stay paintable and central, and an entry should not change so much in scale that its associated art no longer fits its weight (a one-spread vignette shouldn't become a four-page essay, or vice versa). When in doubt about a large length change, log it in `queries-for-author.md`.
- **Up to 3–4 new entries may be added, but only if they earn their place** (criteria and candidates in §7a). New entries get no pre-associated illustration, so each must hand the illustrator an obvious paintable moment. Default to zero; add only where the book gains something the existing 75 cannot provide.
- **Never change a fact** outside §9. If a sentence must be rewritten, its factual payload survives verbatim in meaning.
- **Never delete a joke that lands.** Rephrase around it. Protected lines are listed in §10.
- **Never replace one template with another.** The classic failure mode: you strip "It is not X. It is Y." and unconsciously converge on a new uniform pattern ("X, which is to say Y"). After every batch of 10 entries, self-audit for new repetitions you have introduced.
- **Do not modernise Indigo or period-ify Jamie.** The vocabulary gap between them is a feature (§8).
- **Do not "improve" everything.** Human journals contain slack: plain sentences, mild redundancy, observations that go nowhere. Leave some. Polish is the enemy here.
- **Preserve all Editor's Notes** exactly in function (they are Jamie's voice intruding on Indigo's pages); you may retune their wording to Jamie's voice bible (§5).
- **British English throughout** (learnt, whilst, colour, grey). Indigo only.

---

## 2. Phase 0 — Canon ledger (do this before touching any prose)

Build `canon-ledger.md` by extracting from both files:

1. **Chronology:** every date, age, trip duration, and "X years ago/since" statement. Known-good anchors: Indigo born ~1901; meets Lady Chestnut ~1907; Nangula dies 1935; trips 1938, 1948, 1955, 1963, 1971; Cassius dies 1954; Dragon Protection Act 1972; Jamie born 1972; Indigo dies 1985 aged 84; Jamie finds the trunk ~20 years before "now".
2. **People:** Indigo, Jamie, Nangula, Cassius, Cendre, River, Kai, Manami, Hana, every named villager, every named dragon.
3. **World mechanics:** the compass (dragon's eye, look-through navigation), the blue stone and stained fingertips, the hum-in-pairs eggs, the riding rule (blue-stone harvest only), amulets, the gift economy, the southern coast, arrival-by-sleep, the lantern keepers, the walking dragon, dream-fishing, sky-calligraphy.
4. **Planted payoffs (must survive):** windowsill objects (12 → 75); purple stone (35 → trunk); Hana baby → apprentice (3 → 36); River/Kai thread (61 → 62 → 65 → 69 → 73 → blue cloth in 75 → prologue arithmetic); "She never stopped writing to him" covering the post-1954 Cassius letters; entry 56's deliberate mid-sentence cut; the bird promise in 12 (deliberate loose thread — keep).
5. **Topic-anchor table:** built as `workbench/index.md` (see repository conventions): one row per file recording filename, entry number, trip tag, topic (one sentence), primary paintable moment, and current word count. Topics and paintable moments are the contract with the illustration spreads; word counts are recorded as a reference baseline (flag any rewrite that moves an entry more than ~±40%, not as a violation but for author review).
6. **Tic inventory with counts.** Run across `entries/*.md` plus the prologue (e.g., `grep -c 'It is not' entries/*.md`); record per-file and total baselines → targets. Per-file counts matter: they are how you verify *lumpy* distribution (§2 closing rule) rather than even sanding — a healthy result has zeroes in most files and clusters in a few, not a 0.3 average everywhere:

| Pattern (grep) | Baseline | Target |
|---|---|---|
| `the way (a\|an\|one\|old\|two)` similes | 23 | ≤ 9 |
| `It is not` reframes (incl. variants "X is not A; it is B") | 11+ | ≤ 4 |
| `No [a-z]+\. No [a-z]+\.` paired fragments | 7 | ≤ 2 |
| `as if` | 27 | ≤ 12 |
| `something close(r)? to` | 7 | ≤ 2 |
| `I can only describe` | 4 | ≤ 1 |
| `quiet*` as intensifier | 19 | ≤ 8 |
| Sentence-initial `Nobody` | 20 | ≤ 8 |
| Aphoristic stinger endings | ~60 of 75 entries | ≤ 25 of 75 |
| Comic triple (exactly three escalating examples) | majority of entries | ≤ 30 entries |

Deletions must be **uneven**: do not reduce each pattern by a fixed ratio per entry. Cluster survivors. A human leans on a phrase three times in one fortnight of entries and then not for a decade.

---

## 3. The fingerprint — what exactly to remove

For each item: the pattern, why it reads as AI, and the replacement strategy.

**3.1 The negation-reframe epigram** ("It is not magic. It is logistics."). Replace by: stating the positive observation directly; or letting the contrast live in *content* across two sentences of different shapes; or cutting the first half entirely. Keep ≤4, and keep only the funny ones, never two in the same trip's entries.

**3.2 The "the way X does Y" simile.** Keep the nine best (protected: the librarian shushing, the sheepdog farmer, the south-of-France grandmothers — pick one of the two duplicated south-of-France uses). All other similes must be replaced from **Indigo's personal domains** (§4.3), not from generic animal/domestic stock. Delete rather than swap where the sentence survives without it.

**3.3 The paired/triadic fragment cadence** ("No ceremony. No permission."). Keep ≤2. Elsewhere, fold into ordinary syntax ("They ask no permission and hold no ceremony for it") or cut.

**3.4 The stinger ending.** The single most important fix. Of 75 entries, no more than 25 may end on an aphorism or emotional one-liner. The rest end per the ending-type system in §7. The prologue's section breaks get the same treatment.

**3.5 The comic triple.** Vary example counts: one example, two, four, a list of seven, none. Sometimes the second example should be a failure ("I had a third example but a hatchling ate the page" — sparingly; once).

**3.6 Intensifier palette.** "quiet/soft/gentle/small" as default adjectives. Replace with specific sensory detail or nothing. "Quiet awe" → describe what she did with her hands.

**3.7 Uniform paragraph mass.** Many entries are four paragraphs of near-equal length. Break this: single-sentence paragraphs, one long unbroken paragraph when she's excited, interrupted entries.

**3.8 Hedging stock:** "something close to", "I can only describe as", "in a way that". A field scientist of 1938 hedges differently: "I am not certain", "I may be wrong about this", "I shall have to look again."

---

## 4. Voice bible — Lady Indigo Pepper (entries)

**4.1 Core register (all trips):** dry, precise, self-deprecating, curious before frightened, English understatement over a French ember. She is a trained biologist who was laughed at by her department and has decided to find it funny. She is never twee. She is occasionally, briefly, devastated — and covers it with an observation about tea or buttons.

**4.2 What the journal *is*:** a working field journal, not an essay collection. It should contain journal furniture, distributed unevenly:
- Datelines and fragments of weather (T1 mostly — a young scientist's discipline).
- "Later —" addenda appended after the entry was "finished".
- Entries that stop because life intruded ("Manami is calling. The fog is doing the thing again.").
- Lists: supplies, words learnt in Manaïari, things lost (entry 11 is already this — it's the model).
- Sketch captions: "[written beneath a drawing: …]" — 4–6 instances, coordinated with illustration placement.
- Self-corrections: a struck-through word rendered as ~~strikethrough~~, 5–8 instances total ("It was ~~dreadful~~ beautiful."). Never typos, never fake errors — *visible thinking*, which is the most human texture there is and one models essentially never produce.
- Underlining (render as italics) for words she distrusts: "the village does not have a *leader*."

**4.3 The Pepper tic kit** — invented personal tics, each with an arc across T1→T5. Budgets are for the whole book; distribution must be lumpy.

**Tic A — Haberdashery and mending.** Her metaphor home-domain: buttons, hems, darning, thimbles, seams. Rooted in canon (the button she offered Lady Chestnut at age six; the kintsugi eggs; the mending theme). Examples: "the valley was buttoned shut with fog"; "a friendship worn at the elbows"; "the argument needed hemming, not winning." Arc: occasional in T1, peak in T3, by T5 it is simply how she sees ("Everything here is mended. Nothing here is new."). Budget: 12–15. This becomes *her* recognisable repetition — the human kind.

**Tic B — Measure, then doubt.** T1: she counts and measures compulsively (the existing "seventeen plant species" is canon), appends "N.B." notes, attempts Latin binomials and abandons them mid-word. T2–T3: the measurements thin out. T4: gone — and she notices, **once**: "I did not measure it. I seem to have stopped measuring things. Cassius would mind." Budget: heavy in T1 (8–10 instances), then decaying. This decay is itself the strongest "a human planned this" signal in the book.

**Tic C — Apologising to objects.** Already canon (the rocks). Formalise: 4–6 instances, escalating absurdity once (she apologises to the weather).

**Tic D — Tea jurisprudence.** Already canon. Keep 3–4 grievances; allow one full surrender in T4 or T5 (she has gone native; the local brew wins; she is quietly ashamed).

**Tic E — French slippage that increases with age.** T1: French only at emotional peaks. T3: the odd mid-sentence article. T5: casual code-switching, untranslated. (Older bilinguals drift toward the childhood tongue; readers feel this even if they can't name it.) Keep existing instances (*Mon Dieu*, *Mes petits monstres*, *Deux vies*, *C'est beau*) and add ~6 more, back-weighted to T4–T5.

**Tic F — The Nangula question.** After 1935 (so from T1 onward), Indigo inherits the habit of the sideways question and sometimes attributes it: "Nangula would have asked the better question." / "What is it *for*? (Her question, not mine. It is always her question.)" Budget: 5–7, fading slightly by T5 as the habit becomes hers without attribution — the final unattributed use in T5 should be noticeable to a rereader.

**4.4 Voice evolution by trip** (sentence mechanics, not just content):
- **T1 (1938, age 37):** longest sentences, semicolons, scientific scaffolding, occasional breathless run-ons when amazed, exclamation marks permitted (≤5), measurements, N.B.s.
- **T2 (1948, 47):** the war is never mentioned but the prose is sparer; fewer flourishes; first hems and buttons settling in.
- **T3 (1955, 54; Cassius newly dead):** letters-to-Cassius cadence; second-person intrusions; the mending metaphors peak; sentences mid-length and steady.
- **T4 (1963, 62; children present):** shorter sentences; watching more than doing; parental noticing; measurement habit confirmed dead.
- **T5 (1971, 70):** fragments earn their place here and only here as a default; white space; French; present tense; few adjectives. Entry 75 is already the model — protect it and tune the rest of T5 toward it.

---

## 5. Voice bible — Jamie (prologue + editor's notes)

Jamie is writing **memoir** in the present day: a different instrument entirely.

- **Mechanics:** flowing complete sentences; past tense braided with present-day reflection; modern vocabulary *allowed* (this contrast does differentiation work for free); long paragraphs; parenthetical asides; no comic triples; **no stingers** — Jamie's sections end on an image, an object, or a plain fact.
- **Jamie's own tics (small kit, distinct from Indigo's):**
  - *The archivist's habit:* grounding claims in physical evidence from the trunk. "There is a photograph of this. It is on my desk as I write." 3–5 instances.
  - *The hedge of love:* "I like to think…" / "I have decided to believe…" — 2–3 instances. Jamie inherits Indigo's wit but holds it differently: tentative where she was certain.
  - Jamie **never** uses haberdashery metaphors, never measures-then-doubts, never apologises to objects — except once, deliberately, in the final lines (Jamie catches themself doing an Indy thing and notes it). That single inheritance moment replaces the current "take my hand" ending.
- **Editor's notes:** retune to archivist register. "(Editor's note: She did.)" is protected verbatim. Entry 66's in-text bracketed working notes must be converted from Indigo's marginalia into Jamie's editor-voice footnote (the frame requires Jamie to have *processed* the pages, not left raw to-dos).

---

## 6. Structural differentiation — memoir vs field journal

| Dimension | Prologue (Jamie) | Entries (Indigo) |
|---|---|---|
| Tense | Past, with present-day frame | Present and near-past, immediate |
| Sentence default | Long, subordinate, complete | Variable; fragments legal (T5 default) |
| Paragraphs | Long, even | Lumpy: 1 line to 1 page |
| Furniture | Photographs, objects, dates recalled | Weather, lists, addenda, sketches, strike-throughs |
| Endings | Image / object / fact | Per §7 ending system |
| Humour | Wry, retrospective | Live, situational, deadpan |
| Reader address | Sparing, warm | Never (she writes for herself, Cassius, Nangula) |

If a paragraph could be moved between the two files without anyone noticing, it fails. Spot-test this during verification (§11).

---

## 7. Entry shape & ending system

Before editing prose, produce `entry-plan.md`: a 75-row table assigning each entry a **shape** and an **ending type**. Constraints: no two consecutive entries share an ending type; shapes distributed unevenly across trips per §4.4. Shape changes may now alter entry length (§1), but every entry's topic and paintable moment stay fixed.

**Shapes:** standard scene; ultra-short (≤6 lines); list/inventory; interrupted; addendum-led ("Later —" carries the point); letter-cadence to Cassius or Nangula (mostly T3); sketch-caption-led; single unbroken excited paragraph. The five existing ultra-shorts (11, 22, 48, 57, 73) are protected as-is and must not be lengthened. Up to ~4 additional entries may be *trimmed toward* ultra-short where the entry's best material is one image and the rest is padding — log each such conversion for author review, since its illustration spread may have been scoped to the longer text.

## 7a. New entries (up to 3–4, default zero)

A new entry must pass all four gates: (1) it serves a documented gap in this plan, not general abundance; (2) it carries one obvious, central paintable moment, since it has no pre-associated illustration; (3) it fits the trip voice of wherever it's placed (§4.4) and is inserted *between* existing entries as a new file (insertion-safe filename, e.g. `23a-…`; never renumber neighbours); (4) it introduces **no new world facts** beyond elaborating established canon — new texture, not new mechanics. Each addition ships with a one-paragraph justification in `change-report.md`, carries `STATUS: draft — author approval pending` at the top of its file, and is registered in `index.md`.

**Candidate slots, in priority order (pick at most 3–4):**
1. **A teeth entry** — the strongest gap (§ tone rebalance, fix list context): one entry where the island's benevolence is *not* guaranteed. Best well: the southern coast, written as dread-at-a-distance (Indigo gets nearer than anyone should, is turned back — by whom or what stays unclear). T2 or T3. Paintable moment: the empty boats, or the border itself.
2. **A second teeth-adjacent entry** only if entry 1 of this list lands short: e.g., the night something goes wrong in the village (a hatching that fails, handled with the book's restraint). T4 candidate.
3. **An ultra-short T2 entry** — T2 (1948) is the thinnest trip and its sparer post-war voice (§4.4) is currently more told than shown; a six-line entry in that register would do disproportionate voice-evolution work. Paintable moment required all the same.
4. **A letter-shaped entry** in T3 addressed to Cassius outright (the cadence exists; one fully committed instance would anchor it), doubling as quiet grief work. Paintable moment: what she describes *for* him.

Do **not** add: a birds entry (the loose thread in 12 is protected), anything resolving the southern mystery, anything advancing River/Kai beyond existing beats (that thread's restraint is its engine).

**Ending types (≥8 in rotation):** plain fact; mid-thought stop; logistics/domestic note ("Supper now."); unanswered question; the joke with no moral; quotation of someone else's words; sensory image; aphorism/stinger (≤25 total, and at least 10 of those should be jokes rather than profundities). The big emotional entries (68, 71, 72, 73, 75) keep their weight — they will hit harder once the other sixty entries stop competing for profundity.

---

## 8. Period language rules

- **Indigo's hard vocabulary cutoff:** nothing first attested after her trip's year, and prefer pre-1930 idiom throughout. When unsure of a word's vintage, replace with a plainly old alternative rather than researching forever.
- **Banned (found in current text):** "brain freeze" (62), "power dynamics" (55), "soccer" (34 → "football"). 
- **Sweep targets:** psychology/management jargon (dynamics, processing, validate, boundaries-as-metaphor), internet comic timing ("It is fooling absolutely no one" — rephrase to period deadpan: "It deceives no one, least of all the goat"), Americanisms.
- **Jamie:** modern vocabulary permitted and mild anachronism-by-contrast encouraged; Jamie may say "soccer"… but is presumably British, so still wouldn't. Use judgement.
- Units imperial; pre-decimal money references if any arise; "wireless" not "radio set" debates need not be entered — when in doubt, omit technology.

---

## 9. Enumerated mandatory fixes (the *only* permitted fact/content changes)

1. Entry 15: repair the broken sentence ("…I will say only that They are prolonged…").
2. Entry 34: delete one of the duplicated "six pages of notes / professors would have wept" lines (keep "wept, or resigned").
3. Entries 51 & 56: identical closing line ("I think about it more than I should") — rewrite one ending entirely (56's cut-off device is protected; change 51).
4. Anachronisms per §8.
5. Entry 12 "birds… Tomorrow." — keep as deliberate loose thread; do not add a bird entry.
6. Entry 1: "brand new landmass" → clarify "new to her/the world's maps", not new in age.
7. Prologue: fix the 1972 comma/em-dash mismatch.
8. South-of-France comparison duplicated (3 & 41): keep one, vary the other within Tic A's domain.
9. "Built for someone taller" repeated as-new in 2, 3, 12, 13: keep first occurrence; make one later occurrence a self-aware running joke; delete the rest.
10. Economy contradiction: entries 17 & 61 vs entry 10 — soften "merchant/wares/valuable" vocabulary **or** (preferred) add one Indigo sentence noticing the contradiction and being bothered by it as a scientist.
11. Entry 18 ("asleep, yet I remember the nod"): **no change — author decision.** The contradiction is deliberate whimsy: memory works strangely under the island's magic, and the unexplained paradox is the point. The agent must not rationalise, resolve, or lampshade it further. Treat the existing line as protected in spirit; rephrase only if the de-tick pass requires it, preserving the paradox intact.
12. Entry 65: retag or rephrase "second visit" to sit in T5 (River's visits are 1963 and 1971).
13. Entry 47: resolve the scale contradiction (vast meadow-back vs "dining table") — pick vast; adjust the dining-table line to a different comic comparison.
14. Entry 9 riding rule vs entry 18 carrying: **no change — author decision.** Riding and being carried are distinct acts in this world; entry 9's rule governs riding only, and in entry 18 the carrying *is* the point of the rite. There is no contradiction to fix and no disambiguation needed.
15. Untagged entries (14, 15, 24–27): add trip tags consistent with content (production metadata).
16. Prologue Brittany/estate: resolve location. Recommended: the **estate is English** (Lady Chestnut's woods, Jamie's childhood, the trunk); Brittany belongs to the mother's family. Adjust the "winters in Brittany" sentence accordingly.
17. Prologue: trim the biography block (Oxford/parents paragraphs) by 15–20%; convert summary to one scene-detail per claim where kept; delete or rebuild "The men in her field dismissed her. She outlasted them all."
18. Prologue: give River's and Cendre's deaths one beat of physical texture each (an object, a detail from the trunk) — two sentences, no melodrama.
19. Prologue: replace "Now, take my hand…" ending per §5 (Jamie's single inherited-tic moment). Keep the "knick-knackeries" echo.
20. Entries 1 & 2 tonal lurch: the originally recommended swap is now **layout-affecting — author decision required, do not perform unilaterally**. Default in-place alternative: soften the lurch by retuning entry 1's ending (less breezy, a first note of unease) and entry 2's opening (one orienting sentence), keeping both entries in position and within their length bands.
21. Entry 9: merge the two drafts (the "I keep coming back to the colour… written about it three times" passage) — either commit to it as deliberate journal-repetition (then shape it so it reads chosen) or cut the seam.
22. Entry 66: convert bracketed working notes to Jamie's editorial footnote (§5).

Anything else that looks like an error: **log it, don't fix it.** Output `queries-for-author.md`.

---

## 10. Protected lines (keep verbatim)

"won an argument with a building" · "(Editor's note: She did.)" · "They only hum in pairs. … I have its sister." · "A woman must draw the line somewhere." · "I hate them, gently." · "None of them left. The tales do not say what happened to them. Nobody asks." · "like bark over a nail" · the mayflies/mountains line (it may keep its stinger slot) · entry 22 in full · entry 48 in full · entry 73 in full · entry 75 substantially as-is · the entry-56 cut at "The walls are covered in" · "It ate the sign." · the blue cloth in 75 · "Jamie. If you are reading this…" note in full.

---

## 11. Workflow & verification

**Phase 0:** Canon ledger + `index.md` manifest + tic inventory (§2), all in `workbench/`. Commit.
**Phase 1:** `workbench/entry-plan.md` — one row per file: shape, ending type (§7), trip voice notes (§4.4), tic placements (lumpy distribution by design). Commit.
**Phase 2:** Prologue rewrite (§5, fixes 7, 16–19), edited in place. Commit.
**Phase 3:** Entries in trip order T1→T5 (voice evolution must be felt while writing), one file at a time, committed in batches of 10–15 files; after each batch, self-audit the batch's files for newly introduced repetitions (§1) *and* grep the batch for the §2 patterns before committing.
**Phase 4:** Remaining §9 fixes; cross-file pass for the planted payoffs (§2.4); draft any §7a new-entry files (`STATUS: draft`). Commit separately from Phase 3 work.
**Phase 5:** Verification:
1. Re-run all §2 greps across `entries/*.md` + prologue; every target met; report per-file and total numbers, confirming clustered (not uniform) distribution.
2. **Spread integrity:** all 75 original files present, unrenamed, original trip tags; diff `index.md` — every topic and paintable moment intact; list any entry whose length moved more than ~±40% and any ultra-short conversions, flagged for author review against its illustration spread. New entry files (≤4) listed separately with justifications, placement, and `STATUS: draft` headers intact.
3. **Fact diff:** walk the canon ledger against the edited files; zero unauthorised changes. (Use `git diff` per file against the Phase 0 commit for anything suspicious.)
3. **Voice swap test:** extract 5 random paragraphs from each file, shuffle; they must be trivially attributable. If any paragraph is ambiguous, revise it.
4. **Ending audit:** list all 75 ending types; confirm quotas and no consecutive repeats.
5. **Read-aloud pass** (or closest equivalent): flag any sentence whose *shape* you have read earlier in the same trip.
6. **Tic arc check:** confirm Tic B decays, Tic A peaks at T3, Tic E back-weights, Tic F's final use is unattributed.
7. Output `change-report.md`: counts before/after, all §9 fixes confirmed, queries log.

**Acceptance criteria:** all §2 targets met with clustered per-file distribution · all 22 §9 items resolved as written (11 and 14 are explicit no-change decisions; fix 20 only with author sign-off) · all protected lines intact · canon diff clean · **all 75 original files present and unrenamed with topics and paintable moments intact per `index.md`; new entry files ≤4, each passing all §7a gates and marked `STATUS: draft`** · voice swap test passes · prologue and entries structurally distinct per §6 table · strike-throughs, addenda, and sketch captions present · clean per-phase git history · no new uniform pattern detectable on a full read.

---

## 12. Failure modes to watch for

- **Template swapping** (§1) — the cardinal sin.
- **Over-correction into blandness:** if you delete every flourish, you kill the voice. The budget targets are floors of character, not just ceilings of repetition — the nine surviving similes and four surviving reframes should be *excellent*.
- **Even sanding:** reducing every pattern uniformly per entry recreates statistical flatness. Cluster.
- **Twee drift:** when rewriting whimsy, the gravitational pull is toward cute. Indigo's comedy is deadpan, dry, and slightly cruel to herself. If a rewritten line could appear in a greeting card, cut it.
- **Fact mutation through paraphrase:** "nearly a year" becoming "almost a year" is fine; becoming "a year" is not. When a sentence carries a number, a date, or a rule, copy that payload exactly.
- **Per-file myopia:** the one risk the file-per-entry structure adds. Editing entries in isolation is how the original fingerprint happened — each file locally fine, globally uniform. Cross-file properties (tic arcs, ending-type rotation, planted payoffs, lumpy distribution) live only in `workbench/` files and in greps across `entries/*.md`; consult `entry-plan.md` before opening each file and re-grep after each batch. No entry is finished until its *neighbours* have been checked for ending-type collisions.
- **Spread mismatch:** length is flexible, but each existing entry has an illustration spread scoped to roughly its current weight. Big swings (a vignette ballooning, a centrepiece shrinking) and ultra-short conversions are review items, not silent choices. New entries must arrive with their paintable moment front and centre — an entry the illustrator can't anchor is a layout problem wearing a literary costume.
- **Earning-its-place inflation:** the 3–4 new-entry budget is a ceiling, not a quota. If only one candidate truly clears the §7a gates, add one. Padding the count is the same disease as padding the prose.
- **Forgetting the illustrations:** entries are scaffolding for art across 300+ pages. Never trade a concrete visual image for an abstraction; every entry should still hand an illustrator at least one paintable moment — the same one recorded in the topic-anchor table.
- **Polishing the slack out:** if v2 reads *better* than v1 in every single sentence, you have failed the brief. It should read warmer, lumpier, and more alive — which is different from better-polished.
