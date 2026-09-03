# Editorial revision plan: voice, cultural depth and AI-pattern removal

## Purpose

This plan describes a sequence of narrow editorial passes over `story/1-prologue.md` and the files in `story/2-entries/`. Its purpose is to address the following concerns without rewriting the book, changing its structure, altering the entry order, or reducing its essential warmth:

1. remove conspicuous AI-style rhetoric;
2. make Indigo Pepper's voice change credibly from 1938 to 1971, using authentic period phrasing and references;
3. prevent the Manaïari from reading as an idealised "noble indigenous society";
4. give Nangula agency beyond the role of mystical Black guide;
5. make blue stone's many uses feel coherent rather than conveniently invented;
6. distinguish Jamie's voice from Indigo's;
7. make the Manaïari population feel less anonymous;
8. resolve small plausibility problems;
9. present Japanese influence as part of Aizomea's inherited culture rather than suggesting that Aizomea secretly invented Japanese traditions.

The living canon supersedes several assumptions in the earlier quality report. In particular, entry 57's mid-sentence cut, entry 67's bracketed production notes and entry 66's dual date are deliberate or authorised devices, not faults. Entry 35's known copy error remains a copy-editing matter. None of the protected devices is to be "cleaned up" during these passes.

### Reference convention

An entry number always means the single file in `story/2-entries/` whose filename begins with that two-digit number. A shortened reference such as `entry 44:13` therefore means line 13 of `story/2-entries/44-how-dragons-die-T1.md`. Before editing, resolve the number to the full filename with the directory inventory; never infer a target from its title alone.

`workbench/canon-ledger.md` and this plan use the canonical 01–77 numbering. `workbench/entry-plan.md` is a historical working document and still uses the former numbering. The conversion is: old `01–21` stay `01–21`; old `21a` is canonical `22`; old `22–74` become canonical `23–75`; old `74a` is canonical `76`; old `75` is canonical `77`. Always confirm by title and filename, and never paste an old number into a new change log.

## Authority and maintenance protocol

The documents do not have equal status:

1. **`workbench/canon-ledger.md` is the authority for facts, mechanics, people, planted payoffs and protected language.** Nothing recorded there changes without an explicit author decision.
2. **`workbench/chronology.md` is the authority for every dateline and trip sequence.** If a date moves, change the chronology first, or in the same atomic edit as the manuscript and ledger.
3. **`workbench/entry-plan.md` is the authority for current editing telemetry:** entry shapes, ending types, voice notes, em-dash policy, deliberate interruptions and local de-ticking instructions. Consult it before opening each story file, while remembering that its entry numbers are historical.
4. **`workbench/world-lore-candidates.md` is non-canon.** It may suggest questions; it cannot justify a manuscript change.
5. This revision plan schedules work. It never silently overrules the four documents above.

Before every pass:

- read the canon ledger and chronology in full, not merely the relevant search results;
- read the relevant rows in `entry-plan.md`, resolve their canonical filenames and list all protected lines, entry shapes and payoffs that the pass might touch;
- label every intended intervention **non-canon prose**, **canon clarification** or **canon amendment**;
- prepare exact file and phrase anchors, because line numbers will drift after the first edit;
- present canon amendments as decisions for the author rather than treating recommendations in this plan as approval.

During and after every pass:

- a non-canon prose change may alter wording but not the fact that the wording establishes;
- a clarification must preserve every ledgered meaning and payoff;
- an approved canon amendment must update `canon-ledger.md` first or atomically with the story; update every source reference and planted payoff it affects;
- any approved change to a date, duration, age or trip order must update `chronology.md` first or atomically, then the canon ledger and story;
- no protected line, protected entry shape or authorised paradox may be changed without a separate, explicit author decision;
- re-read the whole edited entry and its immediate thematic neighbours, then re-run the relevant corpus searches;
- do not commit a story edit while the ledger or chronology describes a different world.

## Editing constraints

These constraints apply to every pass.

- Preserve all 77 entry subjects, the prologue frame, the five trips, the thematic ordering and the existing emotional arc.
- Do not delete or combine entries.
- Do not add new scenes merely to solve an editorial problem. A sentence, clause, name, remembered disagreement or concrete counterexample is normally enough.
- Preserve the central joke or image of each entry.
- Keep each entry within approximately 10 per cent of its present length unless explicitly agreed otherwise.
- Use British English.
- Treat the chronology's dates and trip tags as authoritative. Entry 66's T3–T5 dual-date form is authorised; its final River/Kai paragraph belongs to 1971. Its final presentation remains an open chronology decision, not a fault to repair casually.
- Do not make the world grim in order to make it credible. The objective is texture, limitation and disagreement, not misery.
- Do not replace one polished slogan with another. Prefer an observed fact, an imperfect recollection or a character action.
- Do not perform global prose replacements. Every flagged construction must be reconsidered in context.
- Read the entire entry before changing a flagged sentence. Many sentences carry a setup or payoff outside their own paragraph.
- Apply the em-dash and addendum rules in `entry-plan.md`: no parenthetical double dashes; target at most four genuine speech-rhythm dashes across the corpus; use `P.S.`, with occasional `Evening.` or `Next morning.`, rather than an editorial `Later` template.
- Keep a pass-specific change log containing file, stable phrase anchor, original problem, intervention, reason, canon class, ledger action, chronology action and protected-status check.
- Keep all research notes, decision dossiers, ledgers, change logs and other editorial artefacts under `workbench/`.
- Commit one approved pass at a time. Stage explicit paths only, inspect the staged diff, and never absorb unrelated working-tree changes into an editorial commit.

## Pass order and dependencies

| Pass | Concern | Why it occurs here |
|---|---|---|
| 1 | AI rhetoric and repeated prose machinery | Establishes a cleaner prose baseline. |
| 2 | Indigo's five-age voice, period phrasing and references | Rebuilds deliberate variation after formula removal. |
| 3 | Manaïari idealisation | Uses Pepper's newly differentiated degree of certainty. |
| 4 | Nangula's agency | Corrects her role before Jamie's narration is revised. |
| 5 | Blue stone coherence | Aligns presentation with existing mechanics; any changed fact is decision-gated. |
| 6 | Jamie's voice | Rewrites the frame and notes against the now-stable Pepper voice. |
| 7 | Named Manaïari continuity | Adds personal continuity after cultural claims are settled. |
| 8 | Plausibility | Presents local factual and institutional decisions without silently revising canon. |
| 9 | Japanese–Aizomean cultural relationship | Applies the agreed direction to the small number of affected passages. |
| 10 | Regression and read-aloud audit | Ensures later passes have not restored AI patterns or flattened voices. |

Each pass should be approved before the next begins. Changes discovered during one pass but belonging to another should be logged, not silently fixed.

---

# Pass 1 — Remove conspicuous AI rhetoric

## Objective

Make the prose feel selected and written rather than continuously optimised. Preserve wit and lyricism, but vary how observations arrive and how entries end.

This pass is not an attempt to make the writing rough or dull. It should remove repeated rhetorical machinery while protecting the genuinely distinctive images.

## 1A. Eradicate the `not X, but Y` construction

The target count after this pass is zero, including loose variants split across sentences. The replacement must express the underlying information directly, through sequence, comparison, action or uncertainty. This newer author instruction supersedes the earlier keeper note for `Justice is not a sword, but a thimble`; update the corresponding `entry-plan.md` row when that sentence is recast. It does **not** supersede the canon-ledger protection of the Prague egg sentence, which is a deliberately sanctioned, non-`but` negation-reframe.

Do not mechanically delete `not` or replace `but` with `rather`. That leaves the same rhetorical fingerprint.

### Strict inventory

| Location | Current construction or identifying phrase | Editorial treatment |
|---|---|---|
| `story/1-prologue.md:6` | `not where the story begins, but where I found it` | Begin with the house directly; let chronology emerge afterwards. |
| `story/1-prologue.md:50` | `not a knot for a rope, but a map` | Let Nangula identify the current-map positively or ask a less balanced question. |
| `story/1-prologue.md:56` | `not a letter or a map, but an object` | Name the carved dragon first; remove the suspense template. |
| `story/1-prologue.md:78` | `not for this book, but ... the reason` | State Jamie's boundary and motivation in two unequal sentences. |
| `story/1-prologue.md:98` | `not in order ... but as things struck her` | Describe Indigo's actual habit without negative contrast. |
| `story/2-entries/01-where-the-world-keeps-its-secrets-T1.md:3` | `not fiery ... but warm and ancient` | Describe the smell by its positive qualities. |
| `story/2-entries/02-first-days-T1.md:13` | `not one or two ... but hundreds` | Use the number and Pepper's overwhelmed reaction directly. |
| `story/2-entries/03-the-manaari-T1.md:13` | `not one of master and beast ... but of family` | Show the family relationship through one observed behaviour. |
| `story/2-entries/04-language-T1.md:13` | `not "the dragon left" but nearer to ...` | Explain the tense as a translation problem without the balanced correction. |
| `story/2-entries/07-underground-labyrinths-T1.md:3` | `not really following any geological pattern` | Give the specific geological contradiction Pepper observes. |
| `story/2-entries/09-the-blue-stones-kiss-T1.md:5` | `not only in the rock` | Start with its presence in ordinary objects. |
| `story/2-entries/17-the-matriarchs-T3.md:5` | `not a case to be won, but a tear to be mended` | Describe what disputants and mediators actually do. |
| `story/2-entries/17-the-matriarchs-T3.md:5` | `not to argue, but to do` | Move directly into the assigned shared task. |
| `story/2-entries/17-the-matriarchs-T3.md:6` | `not a sword, but a thimble` | Remove the summarising maxim; end on the ginger disagreement or another concrete detail. |
| `story/2-entries/20-not-all-dragons-T1.md:5` | `not really` after denying malice | Allow Pepper's uncertainty or discomfort to remain unresolved. |
| `story/2-entries/24-soaring-with-the-sky-T3.md:5` | `wasn't preparing to jump, not really` | Describe the waiting and the physical risk. |
| `story/2-entries/24-soaring-with-the-sky-T3.md:13` | `Not with a scream, but with ... Wheee` | Report the unexpected sound without a binary setup. |
| `story/2-entries/25-the-amulets-promise-T3.md:5` | `not in years, but in maturity` | State the criteria and who judges them. |
| `story/2-entries/32-dragons-outside-aizomea-T2.md:3` | `should not have surprised me, but it did` | Let the surprise emerge from Pepper's previous assumption and present observation. |
| `story/2-entries/33-the-sea-the-coast-T1-T2.md:9` | `not to the sea, but to the nearest dragon` | Describe the first fish being given to the dragon. |
| `story/2-entries/42-dragon-caves-T3.md:9` | `not grounds for eviction, but ... nudged` | Describe the actual sleeping-cave response. |

`story/2-entries/66-the-sea-the-surfers-T3-T5.md:7` contains a grammatical `not, but` pair (`The stocky, heavy ones are not, but they try`) rather than a rhetorical definition. It should still be recast because the requested rule is zero occurrences.

### Completion search

After editing, search the prologue and entries for:

```text
\bnot\b[^.!?;\n]{0,120}\bbut\b
\bnot only\b
\bnot merely\b
\bnot really\b
```

Every strict `not … but …` result must be zero. Do not create undocumented quotation exceptions.

## 1B. Recast binary correction pairs

The same AI rhythm often appears without the word `but`. These should be individually recast; they need not all be deleted, but no two nearby entries should use the same mechanism.

### High-priority inventory

| Location | Pattern |
|---|---|
| `story/1-prologue.md:48` | `The rock was not a rock. It was a dormant dragon egg.` **PROTECTED: the one sanctioned negation-reframe. Do not edit, re-flag or count it as a failure.** |
| `story/2-entries/04-...:11` | `You do not say ... You say ...` |
| `story/2-entries/05-...:11` | `not what the dragons express. It's what they withhold` |
| `story/2-entries/14-...:5` | `nothing to do with being clean` |
| `story/2-entries/20-...:11` | `They do not want to be hidden. They want to be left alone.` |
| `story/2-entries/33-...:5` | `Not at the sea. Past it.` |
| `story/2-entries/33-...:9` | `Not riding them. Working alongside them.` |
| `story/2-entries/33-...:13` | `Not sadder. Just older.` |
| `story/2-entries/34-...:3` | `there is no such thing as a dragon egg` |
| `story/2-entries/34-...:11` | `Except when they are not.` |
| `story/2-entries/37-...:3` | `They are not pottery. They are birth records.` |
| `story/2-entries/41-...:3` | `are not wise. They are simply old` |
| `story/2-entries/41-...:5` | `Not wisdom. Cunning` |
| `story/2-entries/45-...:7` | `Not with grief` |
| `story/2-entries/50-...:3` | `did not stop ... did not slow ... adjusted` |
| `story/2-entries/52-...:7` | `are not guiding anyone. They are afraid` |
| `story/2-entries/59-...:9` | `It was the nap. The nap was the important thing.` |
| `story/2-entries/63-...:3` | `This is not a metaphor or an anthropomorphism.` |
| `story/2-entries/68-...:5` | `Not out of cruelty. Hunger.` |
| `story/2-entries/70-...:3` | `the dark here is not empty. It is full` |
| `story/2-entries/70-...:9` | `The dark is not the enemy. It is the other half` |
| `story/2-entries/73-...:3` | `trying to be discreet. They are not good at it` |
| `story/2-entries/77-...:3` | `I am not entirely lying.` |

Preserve at most a very small number of ordinary negative statements where the negative itself is the fact. Remove the balanced revelation rhythm, with the protected Prague egg sentence as the single pre-authorised exception.

## 1C. Reduce concept-perfect endings

An entry does not always need to explain its own meaning. Review the final paragraph or sentence of the following entries first:

`01, 03, 04, 05, 09, 10, 17, 18, 21, 24, 29, 30, 32, 41, 43, 48, 50, 51, 52, 53, 57, 59, 60, 64, 66, 70, 75, 77`.

Use one of five ending modes, distributed irregularly:

1. a physical observation;
2. an unanswered scientific question;
3. a domestic interruption;
4. a plain factual note;
5. an emotional inference left unstated.

Avoid replacing existing endings with new aphorisms. In particular, inspect phrases such as:

- `A continent with no interest in being mapped` (`01`);
- `a living sentence, constantly being revised` (`04`);
- `a thread of blue that stitches a world together` (`09`);
- `Justice here is ... a thimble` (`17`);
- `They trade mayflies for mountains` (`21`) — **protected verbatim in its stinger slot; do not edit**;
- `a fence made of smiles` (`29`);
- `the guest book of a place` (`32`);
- `colour is biography` (`46`);
- `the best collection of nothing` (`57`);
- `the other half of the day` (`70`);
- `friendship ... stop performing` (`77`).

Some may remain because they are good. The test is cumulative: retain only the few whose loss would genuinely damage the book. The canon-ledger protection takes precedence over this diagnostic list: entry 57's cut, entries 23, 49 and 74 in full, entry 77 substantially as-is and all other protected lines are excluded unless the author makes a separate decision.

## 1D. Vary exposition joints

Corpus baseline:

- `I watched`: 20 occurrences;
- `I asked`: 19 occurrences;
- `Manami`: present in 40 of 77 entries;
- `no one` or `nobody`: 30 occurrences;
- `something`: 53 occurrences;
- `entire` or `entirely`: 38 occurrences;
- `slow` forms: 30 occurrences;
- `warm` forms: 26 occurrences;
- `faint` forms: 19 occurrences.

These are diagnostic counts, not automatic deletion targets.

Prioritise repeated joints:

- `it turns out` in `21` and `29`;
- `I have come to understand` in `48`;
- `I am beginning to ...` in `04`, `16` and `33`;
- `I find myself ...` in `09` and `20`;
- `I have decided ...` in `12`, `41` and `59`;
- consecutive `I think`, `I suspect` or `I wonder` where they create generic reflective voice;
- Manami laughing, shrugging or informing Pepper that she has asked the wrong question.

Possible alternatives include a dated observation, a contradiction in Pepper's notes, quoted local disagreement, a remembered earlier mistake, or an object whose use reveals the information.

## 1E. Audit generated lists and similes

Review entries with three or more escalating examples: `17, 21, 24, 34, 35, 41, 43, 56, 60, 63`.

Do not remove their subjects. Where the list feels engineered, vary the weight of its components: one detailed example plus two fragments, an interrupted list, or one example Pepper cannot interpret.

Review animal and human analogies in `02, 03, 16, 38, 41, 42, 43, 46, 48, 56, 59, 63, 67, 73`. Preserve the most exact comparisons. Remove or literalise the ones that merely signal cuteness.

## 1F. Apply the handwritten-journal punctuation rule

Run the em-dash audit from `entry-plan.md` as part of this pass, because em-dash-heavy parenthetical rhythm is one of the identified AI cues.

- Remove every double-dash parenthetical (`--- x ---`) and every ornamental parenthetical em dash.
- Prefer a comma, semicolon, colon, parentheses or a full stop according to Indigo's trip voice.
- Permit at most four single dashes in the entire corpus, only where spoken or interrupted rhythm genuinely requires one.
- Use `P.S.` for an addendum, varied sparingly with `Evening.` or `Next morning.`; do not create a repeated `Later` template.
- Record every surviving dash in the pass log with its reason.

## Pass 1 completion test

- Zero strict `not X, but Y` constructions. The protected Prague egg sentence remains the sole sanctioned negation-reframe and is excluded from the close-substitute count.
- Every em dash is either removed or one of at most four individually justified speech-rhythm exceptions; no double-dash parenthetical survives.
- No more than one concept-perfect aphoristic ending in any group of five consecutive entries.
- No two consecutive entries use the same setup–misinterpretation–correction–moral structure.
- Every retained simile contributes physical information, period character or a uniquely funny image.
- The prose still sounds lively when read aloud; it should not sound deliberately de-polished.

---

# Pass 2 — Make Indigo age on the page

## Objective

Make a reader identify the approximate trip from an undated paragraph. Achieve this through sentence movement, certainty, observational priorities and relationships—not through conspicuous reminders of her age.

Period authenticity is part of this objective. Indigo should sound like an educated British woman born in 1901, with a French mother, scientific training and years of international travel. She should not sound like a contemporary writer wearing vintage accessories.

## Voice matrix

| Trip | Sentence behaviour | Attention | Knowledge stance | Humour |
|---|---|---|---|---|
| T1, 1938, 36–37 | longer, accumulating, occasional N.B. and self-correction | measurement, taxonomy, England, proof | hedged; competing hypotheses | nervous, self-deprecating |
| T2, 1948, 47 | controlled declaratives, fewer flourishes | systems, consequences, protection | earned authority with acknowledged gaps | drier and less performative |
| T3, 1955–56, 53–54 | widest rhythm; long thought beside abrupt observation | meaning, grief, habit, relationships | confident enough to leave mysteries alone | driest and most idiosyncratic |
| T4, 1963, 62 | lighter, scene-led, more `we` | Cendre and River noticing the world | experienced guide and observant mother | anecdotal, often carried by the children |
| T5, 1971, 69–70 | short, spare, concrete; silence allowed | knees, hands, weather, small leave-takings | little need to classify | gentle, rarely escalating |

## Entry inventory

### T1: strengthen the arriving scientist

Primary targets: `01, 03, 04, 07, 09, 20, 35, 44, 71`.

- `01`: retain uncertainty; reduce the mature, summative statements about faith and reality.
- `03`: frame social conclusions as provisional observations from her first weeks, especially leadership, gender and health.
- `04`: she reaches remarkably sophisticated linguistic conclusions by day twenty-eight. Add uncertainty, competing translations or evidence that Manami disputes her grammar.
- `07`: replace vague modern phrasing (`a bit otherworldly`, `not really following`) with the particular geological conflict her training recognises.
- `09`: keep measurements and failed terminology; reduce later-trip lyric certainty.
- `20`: late T1 can be more confident, but Pepper should remain uneasy about translating Manami's explanation of the southern dragons.
- `35`: keep professorial references and family longing; correct the one lapse into catalogue voice if Pass 1 has not already done so.
- `44`: principal mismatch. Add the scientist's uncertainty, source distinctions and fresh grief for Nangula. Reduce the composed authority associated with older Pepper.
- `71`: retain its emotional simplicity; a small concrete festival detail can anchor the abstraction if needed.

Use `02, 19` and `36` as T1 exemplars.

### T2: establish the returner's authority

Primary targets: `13, 33, 60`; check mixed-trip `59`.

- `13`: `Mon Dieu, the food!` and the succession of marvels sound closer to T1. Let her know the meal customs and notice what has changed since 1938.
- `33`: maintain its steadiness, but separate remembered first-trip surprise from present knowledge.
- `60`: the staged public-service guide is energetic and performative. Give it the controlled observational authority of 1948 and remove modern listicle cadence.
- `59`: ensure retrospective phrases such as `the first time` clearly refer to 1938 rather than appearing to happen in 1948.

Use `18` and `32` as T2 exemplars.

### T3: protect variation without making it the universal voice

Primary targets: `21, 29, 30, 41, 42, 48, 50, 52, 53, 57`.

- Remove remaining early-trip comparisons where they function only as jokes, particularly Harley Street in `29` and London in `30`.
- Let knowledge appear in accumulated detail instead of explanatory authority.
- Preserve abrupt private fragments in `23, 31, 49` as exemplars.
- Do not turn every mystery into philosophy. Some T3 entries should remain stubbornly zoological or petty.
- Keep Cassius present through habits and absent address, not through repeated explanatory editor's notes.

Use `23, 31, 48, 49` and `53` as T3 exemplars.

### T4: let the children carry the wonder

Primary targets: `62, 63, 65, 67, 68`; check `64` and `69` as exemplars.

- Replace some `I watched` framing with the family's collective position or with Pepper watching Cendre and River react.
- Cendre and River must not become interchangeable reaction devices. Cendre organises, measures and withholds; River moves, joins, talks and belongs.
- Pepper should explain less than she did in T3 because her children supply the entry's discovery.
- Preserve `64` and `69`, which already achieve the intended voice with very little text.

### T5: slow the line

Primary targets: `61, 70`, plus the 1971 paragraph in the authorised dual-date entry `66`.

- `61`: keep the choir, but shorten the escalation and let seventy-year-old Pepper's response be less busy.
- `70`: reduce general exposition about night. Keep the present house, River's absence and what Pepper hears now.
- `77`: **protected substantially as-is and the canonical T5 model.** Use it as a comparator, not a routine editing target. Any proposed change must preserve the blue cloth, the windowsill-object payoff and its present restraint, and requires author approval before implementation.
- The 1971 surfing material should use River and Kai rather than repeat the full ethnography of surfing.

Use `45, 72, 74, 75` and `76` as T5 exemplars.

## Period phrasing and reference research

### Principle

Research Indigo's **generation**, not merely the year of each entry. A seventy-year-old in 1971 does not automatically adopt 1971 youth slang; much of her idiom would have formed between roughly 1915 and 1935. Later language may enter through professional life, politics, her children or ordinary linguistic change, but it should not replace her underlying verbal habits.

The objective is quiet authentication. Period language should usually pass unnoticed while making contemporary phrasing feel slightly less available.

### Required research artefact

Before editing for period language, create `workbench/pepper-period-language-ledger.md`. Every phrase or reference approved for possible use should record:

| Field | Requirement |
|---|---|
| Expression or construction | The phrase, syntax or characteristic usage—not merely an isolated word. |
| Meaning and tone | Formal, amused, irritated, affectionate, scientific, doubtful, private, and so forth. |
| Attested date | Exact year where possible; otherwise a documented range. |
| Source and speaker | Diary, letter, interview or other primary source, including the writer's age and background where known. |
| Register | Written diary, private letter, published prose, speech, journalism or institutional language. |
| Suitable trip or trips | T1–T5, based on Indigo's age and the expression's circulation. |
| Use restriction | Why it fits Indigo and how often it may appear. |

Do not place researched expressions directly into the manuscript until the ledger has been reviewed. The ledger is a palette, not a quota.

### Source hierarchy

Research should favour primary sources that resemble Indigo's likely language environment:

1. private diaries and letters by British women born approximately 1885–1910;
2. diaries, letters, field notes and memoirs by women scientists, naturalists, archaeologists, physicians, travellers and expedition members;
3. correspondence by Oxford-educated women and by British women with sustained French or international connections;
4. dated BBC broadcasts, oral-history recordings and interviews for spoken cadence;
5. contemporary British newspapers, scientific journals, travel writing, advertisements and institutional documents for objects, public references and professional vocabulary;
6. dictionaries and historical corpora to verify earliest use, frequency and register.

Modern historical fiction is not evidence. General web lists of "old British sayings" are not evidence. Search-engine date claims and language-model recollection must be verified against a dated source.

When using published primary sources, collect short examples for linguistic analysis; do not imitate one real writer's voice wholesale.

### Research categories

Build a modest bank for each of the following:

- doubt, hypothesis and scientific caution;
- surprise and disbelief;
- approval, admiration and delight;
- irritation, fatigue and physical discomfort;
- mild oaths and private exclamations;
- affectionate references to Cassius, Cendre and River;
- transitions used in notebooks and field observations;
- ways of correcting an earlier note;
- descriptions of something fashionable, modern, badly designed or socially improper;
- period names for clothing, luggage, drawing materials, medicines, meals, household objects and transport;
- scientific institutions, practices and professional frustrations;
- everyday reference points that change between 1938, 1948, 1955, 1963 and 1971;
- French expressions plausibly retained from Indigo's mother, with accurate register and spelling.

References should reveal character as well as date. A comparison to a ration book, wireless broadcast, railway refreshment room, post-war building material or particular scientific instrument is useful only when Indigo would naturally think of it.

### Trip-specific research windows

| Trip | Primary source window | Particular emphasis |
|---|---|---|
| T1 — 1938 | principally 1925–1939 | interwar scientific training, Oxford habits, travel logistics, class expectations, pre-war domestic comparisons |
| T2 — 1948 | principally 1939–1950 | wartime and post-war material reality, rationing, reconstruction, institutional authority, changed assumptions |
| T3 — 1955–56 | principally 1948–1957 | mature private prose, bereavement, established professional language, dry middle-aged humour |
| T4 — 1963 | principally 1957–1965 | adult children, changing travel and technology, maternal observation, awareness of a younger generation's speech |
| T5 — 1971 | principally 1965–1972, anchored in her earlier cohort | ageing, physical economy, later conservation language, retained interwar idiom beside selective newer usage |

The windows guide research; they are not hard publication cut-offs. An expression attested earlier can remain in an older speaker's vocabulary.

### Integration rules

- Prefer syntax, collocation and habitual turns of phrase over conspicuous slang.
- Use period-specific markers sparsely: normally no more than one clearly dated expression or reference in a short entry and two in a long entry.
- Do not force a marker into every entry. A convincing cohort voice depends on consistency of thought as much as vocabulary.
- Avoid stock costume language such as `jolly good`, `old bean`, `spiffing`, `crikey`, indiscriminate `rather`, or constant `my dear` unless a primary source and Indigo's context justify it.
- Do not make T1 a caricature of aristocratic Englishness or T5 a caricature of old age.
- Preserve existing French only when its wording and emotional register are plausible for a bilingual daughter rather than decorative Frenchness.
- Favour references Indigo could have encountered directly. Do not use a famous person, book, discovery or consumer object merely to timestamp a paragraph.
- Avoid explaining references inside the journal. If a term would be opaque to the intended audience, context should carry it or the term should not be used.
- Do not replace an AI-sounding sentence with a conspicuously quaint sentence. Period language must still pass all Pass 1 tests.

### Existing language requiring verification

This is a checking list, not a presumption that each phrase is wrong:

- `technically correct` and the conversational cadence around it in `06`;
- `public service` and the staged guide format in `60`;
- `involuntary rotating art gallery` in `60`;
- `the window had closed` in `62`;
- `chain of command` in `56`;
- `supervisory` as a comic description in `63`;
- `technically possible but not worth the bother` in `66`;
- `friendship ... stop performing` in `77`;
- modern therapeutic language surrounding emotional suffering in `30`;
- contemporary-sounding universal formulations in `04`, especially around owning sadness;
- the balance of contractions such as `don't`, `isn't`, `I've` and `I'm` in supposedly private written entries across all five trips;
- terminology for psychology, conservation, geology, biology, aviation and international law wherever it carries a date-sensitive claim.

### Reference audit

Existing references to Oxford, Harley Street, London, the Côte Basque, Saint-Jean-de-Luz, the Muséum National d'Histoire Naturelle, the United Nations, Japanese settlement, dentists, aspirin, trains, municipal pools, rockets and other real-world anchors should be logged by entry and checked for:

1. availability by that date;
2. phrasing current to Indigo's generation;
3. likelihood that Indigo personally knew it;
4. whether it differentiates the trip or simply decorates the prose;
5. cumulative frequency, so that early England comparisons diminish naturally rather than vanishing by rule.

### Period-language completion test

- Every newly introduced period expression has a dated, attributable source in the ledger.
- No passage depends on stereotyped vintage slang for authenticity.
- T1, T2 and T3 show credible linguistic continuity rather than three unrelated period costumes.
- T4 and T5 allow newer references without making Indigo sound like someone born decades later.
- At least half of the authenticity gains come from syntax, professional vocabulary, objects or habits rather than idioms.
- A modern reader can understand each entry without a glossary.
- A final search confirms that period edits introduced no banned AI constructions from Pass 1.

## Pass 2 completion test

- Blind-test at least three unlabelled passages from each trip; trip identity should be reasonably inferable.
- T1 and T5 must never be mistaken for each other.
- T2 must no longer read as a small appendix to T3.
- T4 entries must distinguish Cendre's and River's ways of seeing.
- No sentence announces Pepper's age merely to prove the voice pass occurred.
- Every trip attribution and retrospective cue agrees with `chronology.md`, including the T3–T5 and other dual-date entries.

---

# Pass 3 — Give the Manaïari a credible, non-utopian society

## Objective

Preserve the warmth, parity and ecological intelligence of Manaïari life while showing that Pepper is observing one region, through friends, during selected visits. Replace universal claims with situated knowledge and reveal the costs or limits of communal systems.

## Governing approach

Use four small techniques:

1. **Limit the sample.** Prefer `in this village`, `among the families I know`, `so far`, or a named person's practice to claims about all Manaïari.
2. **Name the institution accurately.** A society can lack judges and currency without lacking arbitration, obligation, healers or governance.
3. **Show a cost.** Communal exchange may create remembered obligations; consensus may be slow; mediation may produce a truce rather than affection.
4. **Let locals disagree.** Manami's account need not be final. Another person can use a different word, dislike a custom or remember an event differently.

Do not add cruelty, poverty or misogyny merely as proof of realism.

## Target inventory

| Entry | Problematic claim | Minimal direction |
|---|---|---|
| `03` | Everyone is tall, broad, perfectly toothed and healthy; women hold settled authority; men check with women; no fences; a single defining trait. | Make Pepper's limited first-month sample explicit. Replace sex-wide behaviour with observed roles. Distinguish unfenced land from unclaimed use. Remove the claim that no one looks unwell. |
| `04` | No word for ownership; grammar conveniently embodies ideal emotional philosophy. | **Preserve the canon fact that there is no word for `own/possess`.** Make Pepper's translation incomplete by showing how temporary use, care, boundaries or responsibility are expressed without smuggling ownership back into the grammar. Let Manami challenge one of Pepper's profound readings. |
| `10` | No money; everything happens easily; fairness apparently needs no enforcement. | **Preserve no money, no ownership-word, worthless gold and favours remembered but not tracked.** Pepper may mistake the absence of currency for the absence of value, scarcity or social memory; do not introduce accounts, prices or score-keeping. |
| `13` | Meals solve almost anything; food culture approaches universal genius. | Attribute the belief to Manami or the local settlement. Include one issue a meal merely postpones. |
| `14` | The island's oldest institution is presented as socially effortless. | Preserve the baths while acknowledging etiquette, access or regional variation. Japanese inheritance is handled in Pass 9. |
| `17` | No courts; every dispute is a tear; honey cakes dissolve conflict; history has no writing. | Present mending women as mediators, not the absence of governance. The tree dispute can end in a working agreement. **Preserve the canon fact that the language has no written form:** variation may come through oral accounts, cords, scars, objects or differing tapestry readings, not a newly invented written archive. Preserve the merchant strikethrough unless separately approved. |
| `21` | The village speaks with one voice through ritual. | Allow different knot-keepers or families to interpret knot forms differently. One brief qualification is sufficient. |
| `25` | Elders and dragons flawlessly recognise maturity; lost amulets always return; vows cannot be broken. | These apparent conveniences are **currently canon facts**: readiness rather than age, an unbreakable promise and the eventual return of a lost amulet. Improve social texture through differing judgements about readiness or the inconvenience of a very late return, without weakening those mechanics. Any change to the mechanics requires a canon amendment in Pass 5. |
| `29` | Perfect teeth expand into the claim that no one aches, limps or coughs. | Keep the blue-stone toothpaste, luminous teeth, perimeter-fence behaviour and dragon dental comedy. Qualify only Pepper's extrapolation from those facts to universal human health. |
| `30` | No doctors or appointments; the right people know everything; companionship reliably repairs all mental suffering. | Name healers and their specialities. Let the wrist remain an unusually good outcome. Present companionship as care, never as a universal cure. Preserve blue stone as an ingredient of the poultice unless the canon is explicitly amended. |
| `33` | Children literally swim before walking; the sea is simply their garden; people have collectively chosen not to join the world. | Attribute these to coastal families and Pepper's impression. Retain the strong coastal identity without making it species-wide. |
| `37` | A single craft is trusted to three people and embodies centuries without social complication. | This is mostly credible; use it to show apprenticeship, disagreement or responsibility rather than perfection. |
| `53–56`; use `57` only as a comparator | Twelve villages differ visually, but Manaïari society appears socially identical everywhere. | Add one or two small regional differences in custom, terminology or attitude without adding new scenes. Entry 57 and its mid-sentence cut are protected. |
| `62` | A valuable pebble and what Pepper calls barter appear beside her early claim that gold is worthless. | Use this as a correction of her equation of money with value. Reframe the exchange as gift, favour, enthusiasm or situational reciprocity consistent with favours being remembered but not tracked. Do not introduce prices, accounts or an ownership vocabulary. |

## Manami audit

Manami should remain central, but she cannot always be the calm, correct representative of her people.

Across her 40 entry appearances:

- retain her competence and dry humour;
- identify at least three moments where her answer is personal rather than culturally definitive;
- identify at least two subjects on which someone else disagrees with her;
- let her misunderstand Pepper once without turning it into a symmetrical joke;
- preserve entries `23`, `45`, `64` and `75` as strong evidence of a relationship beyond exposition.

## Pass 3 completion test

- No global claim about health, harmony, ownership, gender or governance rests on one observation.
- The no-money, no-ownership-word gift economy remains intact while value, scarcity, boundaries and remembered favours become legible.
- The language remains unwritten; tapestries, cords, oral accounts and material traces may disagree without becoming a covert script.
- Healers, mediators, elders and harbour authorities are recognised as institutions even if they are informal.
- At least three regional or interpersonal differences exist among Manaïari practices.
- The society remains enviable in some respects without becoming morally or practically infallible.

---

# Pass 4 — Give Nangula an independent life and agency

## Objective

Keep Nangula mysterious because Jamie never met her, while removing the pattern in which an enigmatic African woman exists to test, choose and spiritually authorise a white British heroine.

Mystery should come from incomplete records and necessary secrecy, not from racialised timelessness or oracular behaviour.

## Core direction

Nangula should read as:

- a senior dracologist and field operator with her own programme of work;
- an active professional counterpart who chose what information to share for practical and ethical reasons, while **never discussing Aizomea with Indigo**;
- someone who argued with Indigo, made errors and had preferences unrelated to guiding her;
- the author or co-author of knowledge Indigo later uses;
- a person whose succession plan was deliberate, not a posthumous magical coronation.

The existing silence is not a blank to fill with retroactive conversations. Nangula died before T1; all Indigo's direct addresses to her are posthumous. Strengthen agency through her independent research, ordinary professional encounters outside Aizomea, authored scrolls, practical habits and Indigo's remembered disagreements about dragons or method. The sideways meetings and breadcrumb gifts are canon and may be contextualised, not replaced.

## Reference inventory

| Location | Current function | Revision direction |
|---|---|---|
| `story/1-prologue.md:40–42` | Introduced as the second person who shaped Indigo; tall, patient, ancient-seeming, a lifelong solo visitor. | Preserve her lifelong solo relationship with Aizomea. Add profession, purpose or a concrete working habit. Consider recasting the centuries comparison so age and racialised timelessness do not do all the character work. |
| `story/1-prologue.md:44–48` | Appears after a failed lecture and solves the lonely egg through one cryptic sentence. | Preserve the meeting and egg. Make the knowledge visibly earned from her own research. Give Indigo something useful to contribute so the relationship begins as unequal colleagues, not seer and supplicant. |
| `story/1-prologue.md:50` | Appears in far-flung cities, asks sideways questions and leaves breadcrumb gifts. | Preserve the canonical meetings and breadcrumbs. Add signs that the meetings belonged to a recognisable professional relationship: correspondence, shared conferences, exchanged specimens or arguments about dragon research **outside Aizomea**. Establish why direct disclosure remained impossible. |
| `story/1-prologue.md:52` | Had known all along; waited for the right person; selected Indigo after years of tests. | Reduce chosen-one overtones without removing the canonical passing of guardianship. Ground Nangula's judgement in demonstrated discretion and complementary expertise. Evidence of other collaborators is possible only if it does not imply other Aizomea visitors and is added to the ledger. |
| `story/1-prologue.md:56–58` | Her death activates the carved dragon and transfers her life's work. | Keep the device, paired hum and transfer. Credit the scrolls explicitly as scholarship. A claim that Nangula designed the mechanism with dragons would be new canon and therefore needs a separate author decision and ledger amendment; do not insert it merely because this plan suggests it. |
| `story/1-prologue.md:62` | Indigo travels using Nangula's scrolls. | State that Indigo is continuing or testing Nangula's work. Avoid making the predecessor disappear once the adventure begins. |
| `entry 02:11` | Nangula's name functions as a password that settles Indigo's acceptance. | Show what the name means locally: trust earned, a promise made, or a debt remembered. Acceptance can remain conditional. |
| `entry 04:7` | Nangula taught Manami English. | Keep. This is useful evidence of ordinary labour and reciprocal exchange; consider adding what Manami taught Nangula. |
| `entry 05:9` | Pepper assumes Nangula was better at silence and nearly everything else. | Replace vague idealisation with a specific remembered skill, failure or disagreement. |
| `entry 20:3` | Nangula always asked the better question. | Give the actual kind of question she asked or recall a time her question was wrong. |
| `entry 25:5` | Nangula is good at keeping things close. | Connect secrecy to an explicit responsibility rather than innate mysteriousness. |
| `entry 32:9` | Nangula researched for decades and `never once let slip` the origin. | Preserve the secrecy exactly in meaning. Let Indigo understand or contest its ethical burden and explicitly credit one classification, route or protective practice to Nangula. Preserve `(Editor's note: She did.)` and `like bark over a nail` verbatim. |
| `entry 44:13` | Indigo imagines part of Nangula absorbed into Aizomea three years after her death in Namibia. | Preserve the posthumous grief and exact anniversary logic. If recast, keep Namibia and avoid spiritually annexing her to the island; do not make her physically present or available for dialogue. |
| `entry 76:3` | Direct address to Nangula and inheritance question. | Preserve. It is powerful once succession has been framed as responsibility rather than selection by destiny. |

## Cultural check

Confirm deliberately whether `Sossusvlei` is intended as Nangula's family name. It is strongly associated with a Namibian geographic location and may read as an exotic place-name assigned to a person. It is currently a canon anchor. Do not change it automatically: a replacement requires research, an explicit author decision, a canon-ledger update and a complete reference search.

## Pass 4 completion test

- A reader can state what Nangula wanted independently of Indigo.
- At least one piece of knowledge remains explicitly Nangula's contribution.
- Indigo and Nangula have at least one substantive disagreement or complementary difference.
- The phrases `right person`, `waiting`, `testing` and timeless/centuries imagery no longer form her defining pattern; the canonical breadcrumbs remain but gain professional context.
- Her death transfers responsibility; it does not magically prove Indigo was chosen.
- No passage implies that Nangula and Indigo discussed Aizomea, travelled there together or corresponded about it.
- The Prague pair-humming line, compass chain, death date, solo-visiting history and all posthumous addresses retain their canon meanings.

---

# Pass 5 — Make blue stone feel coherent rather than convenient

## Objective

Reduce the "magical Swiss Army knife" impression without casually deleting the book's signature images. Coherence can come from presentation, recurrence and categories of use; it does not require a hard-science system or a large rewrite.

## Canon gate

This pass begins with a decision dossier, not a manuscript edit. The canon ledger presently requires all of the following meanings to survive:

- the stone hums, and the Prague eggs hum in pairs;
- its source is the floating islands, and harvesting it is the only accepted reason a human rides a dragon;
- harvesting permanently stains the hands blue;
- it is valuable, non-rare and hard-won, with respect rather than reverence;
- it appears in pendants, thimbles, cooking pots, tools, glowing-wall mortar, poultice, toothpaste, pigment, ice cream and gourd voices;
- it glows at night and more brightly at full moon;
- nesting dragons' luminous teeth form a perimeter fence;
- the humming season re-tunes the world and keeps the floating islands afloat;
- an amulet promise cannot be broken, readiness is not determined by age, fire-and-ice forging destroys most stones, and a lost amulet always returns;
- the prose never calls it `magic`.

No item in that list may be weakened into folklore, coincidence or error simply to satisfy this pass. If the author chooses to change one, record the decision in `canon-ledger.md` before or with the affected entries and audit every payoff. The default, low-change route is to keep them all and make their relationships legible.

## Preferred low-change coherence model

Use four descriptive families. These are editorial categories, not new laws of physics:

1. **Resonance and response:** humming eggs, sounding gourds, the compass's call, annual amulet glow and the island-wide chord.
2. **Prepared material:** powder, pigment, paste, mortar, inlay, tools, cookware, culinary preparation and poultice. Different crafts can use the same substance differently without each use being announced as a fresh supernatural power.
3. **Long contact and incorporation:** permanent blue hands, glowing teeth, colour in scales, seams and structures that carry the mineral over time.
4. **Dragon-mediated exceptions:** riding to harvest, the return of lost amulets, the teeth perimeter and any behaviour whose agent is plausibly a dragon rather than the mineral acting alone.

Do not force all four into a scientific explanation. Reuse a few observable signatures—faint vibration, cool weight, blue residue, moonlit glow, preparation by skilled hands—so later appearances feel like applications of a known material. Let Pepper distinguish measurement, inference, report and mystery.

An optional `energy retention` or `mineral bonding` explanation would itself be new canon. It may be proposed in the decision dossier, but it is not authorised by this plan and must not be inserted without approval.

## Functional inventory

### Foundation and resonance

- `06`: preserve blue dust changing the gourds' voices; connect its handling or vibration to the established stone rather than explaining a new power.
- `07` and `09`: preserve the floating-island source, harvest-only riding rule, women riders, song, permanent staining and hard-won value. Use `09` as the principal empirical description.
- `27`: preserve the canonical fact that the humming season re-tunes the world and keeps the islands afloat. Pepper may be uncertain about mechanism, not about deleting the event from the world.
- `32` and `76`: preserve the compass chain and its probable response to the call across oceans. Do not confuse the Prague egg with blue stone.

### Domestic and crafted material

- `12`: preserve tools, cooking pots, glowing mortar, pigment and poultice. The editorial task is to avoid presenting the catalogue as a sequence of miracles.
- `24`, `26`, `37` and `66`: clarify craft language only where material form is genuinely confusing. Any new alloy, resin or treatment rule is a canon amendment, not an invisible copy-edit.
- `42`, `52` and `70`: make glow descriptions compatible in intensity and context while preserving night glow and the stronger full-moon effect.
- `63`: preserve blue stone's culinary use in the ice cream. Its purpose may remain peculiar; do not turn safety or flavour chemistry into an unrecorded new fact.

### Body, care and dragons

- `08` and `46`: leave biological incorporation unexplained unless the manuscript makes a contradictory causal claim.
- `29`: preserve toothpaste, luminous teeth and the perimeter fence. The fence may be described as dragon behaviour involving blue-stone teeth; do not demote it to superstition without a canon decision.
- `30`: preserve blue stone in the poultice. It is permissible to make Pepper less certain which part of the treatment aided her unusually quick recovery, provided the poultice fact survives.
- `34`: floating eggs need not become a blue-stone mechanism. Avoid inventing a connection merely to make the system look tidy.
- `25–27`: preserve every amulet property. Social variation belongs in who is judged ready, how people live with promises and what a delayed return costs; it does not belong in quietly making the promise breakable.

## Decision dossier before editing

Create `workbench/blue-stone-decision-dossier.md` containing one row per reference, its exact canon meaning, present narrative function, apparent power category, proposed wording-only clarification and whether a canon amendment is actually requested. Group repeated manifestations so the author can see whether the problem is the number of properties or merely the way each is introduced.

If no canon amendments are approved, this pass is limited to wording, ordering within existing paragraphs and calibrated Pepper uncertainty. If an amendment is approved, update the ledger and every dependent reference in the same pass.

## Pass 5 completion test

- Every blue-stone occurrence is inventoried and maps to a recurring descriptive family or a clearly dragon-mediated exception.
- Every blue-stone and amulet meaning currently required by the ledger survives unless its specific amendment was approved and recorded.
- Later entries reuse established sensory and craft vocabulary instead of unveiling a new property each time.
- Pepper distinguishes what she measured, inferred, was told and still cannot explain.
- No manuscript occurrence calls the stone `magic`.
- The stone remains useful, domestic, extraordinary and visually abundant, but no longer feels as though a new ability was invented for the needs of one entry.

---

# Pass 6 — Separate Jamie's prose from Indigo's

## Objective

Make the prologue and editor's notes recognisably Jamie's work while preserving family warmth and the metafictional frame.

## Proposed distinction

| Indigo | Jamie |
|---|---|
| field observation | archival reconstruction |
| sensory and biological comparison | domestic memory and documentary detail |
| scientific uncertainty | uncertainty about family motives and omissions |
| French phrases and English self-mockery | contemporary, plainer English |
| discovers meaning in a present scene | compares conflicting journals, letters, objects and memories |
| often lyric | more direct, occasionally sceptical |

Jamie may be a good writer. She should simply be good in a different way.

## Prologue targets

- Reduce Pepper-like aphorisms and inversions in paragraphs around lines `6, 32, 42, 50, 70, 78, 86, 92, 98`.
- Treat line references only as search anchors. The phrases `won an argument with a building`, `The rock was not a rock. It was a dormant dragon egg.`, the paired-humming exchange and the full `Jamie. If you are reading this…` note are protected. Build Jamie's distinction around them; do not revise them.
- Keep Jamie strongest when remembering tangible domestic facts: sandwiches, bannister, books, birthday cake on the kitchen floor.
- Add one or two signs of archival work where the prologue currently claims certainty: conflicting dates, a conclusion drawn from letters, something Indigo never explained.
- Let Jamie disagree with or feel irritated by Indigo once. Affection without resistance makes Jamie sound like a curator of legend rather than a granddaughter.
- Preserve the meta-frame and the amount of context. The pass changes narrative texture, not information architecture.
- Avoid giving Jamie Pepper's fondness for universal closing statements.

## Editor's-note inventory

| Entry | Current note type | Direction |
|---|---|---|
| `27` | Amulet-in-trunk confirmation | Preserve its function and the annual-glow payoff. Jamie may give a precise observation or date without weakening the canon mechanic. |
| `29` | Comic biographical confirmation | Make it archival and concise, or let Jamie's humour differ from Pepper's. |
| `31` | Emotional clarification about Cassius | Keep factual directness. Consider whether `She never stopped writing to him` is evidence or Jamie's conclusion. |
| `32` | `She did.` punch line | **Protected verbatim. Keep the wink and differentiate Jamie through surrounding notes and prologue prose instead.** |
| `36` | Object found in trunk | Keep as plain evidence; this is naturally Jamie's register. |
| `53` | Jamie's travel correction and size estimate | Important for Jamie's authority, but coordinate with the island/continent decision in Pass 8. |
| `55` | Impossibly green leaf | Record its condition without imitating Pepper's enchanted tone. |

All seven editor's notes—`27, 29, 31, 32, 36, 53, 55`—must retain their function as Jamie intruding on Indigo's pages. Entry 67's bracketed text is production/layout instruction and remains untouched; it is not an editor's note to restyle.

## Pass 6 completion test

- A paragraph stripped of names can still be identified as Jamie or Indigo.
- Jamie's claims are sourced from memory, archive or her own travel rather than omniscient certainty.
- Jamie has one clear emotional disagreement with Indigo.
- Editor's notes do more than deliver punch lines or confirm that magical keepsakes were real.
- Jamie remains appealing and capable; difference must not mean flatness.
- Every protected prologue line and planted payoff survives verbatim or substantially as specified by the canon ledger.

---

# Pass 7 — Turn selected anonymous roles into recurring people

## Objective

Make Aizomea feel inhabited by a community rather than staffed by unnamed examples, using a very small recurring cast. Do not name every passer-by.

Anonymity is appropriate in early T1, before Pepper speaks the language. It becomes less credible during T3, after years of friendship and repeated visits.

## Existing anchors

- **Manami:** Pepper's principal friend and guide; currently overburdened with exposition.
- **Hana:** Manami's daughter, a child in `03` and a young craftswoman in `37`.
- **Kai:** canonically the young fisherman in `62`, the dawn surfer in `66` and River's dinner companion in `74`. The implication that he is Jamie's father must never be stated or advanced.

## Proposed small roster

Before editing, expand the people section of `workbench/canon-ledger.md`, or create a subsidiary `workbench/character-ledger.md` explicitly governed by it, containing name, approximate birth year, settlement, work, family relationship, first appearance and later appearances. Use culturally coherent names; do not invent them ad hoc in separate entries.

The canon ledger already fixes several unnamed identities and their allowed recurrence, including the harbour master in `17` and `66`, the knot-keeper in `21` and `22`, and Kai in `62`, `66` and `74`. Do not merge a different anonymous role into one of these people, move an appearance, or add a name without treating it as a canon amendment. Agree the small roster first; update the ledger before or with the story.

Add no more than five or six recurring Manaïari beyond Manami, Hana and Kai. Candidate continuity roles:

| Character slot | Candidate entries | Purpose |
|---|---|---|
| Senior Listener | `05, 21, 30, 44` | Moves dragon communication and care away from Manami. |
| Harbour master | `17, 66`; optionally `33` only after approval | Preserve the fixed identity and give the coastal system a persistent human face. A new `33` appearance is a ledgered canon amendment. |
| Knot-keeper | `21`, with a later brief recurrence | Represents memory work without becoming an exposition oracle. |
| Healer or bone-setter | `30`, possibly recalled in `65` or T5 | Makes medicine an actual profession and supports Pass 3. |
| Egg repairer | `35, 37` | Can mentor Hana and connect hatching to family record. |
| Kai | `62, 66, 74` only by default | Preserve the existing River/Kai chain without making the parentage implication more explicit. Any additional appearance needs a payoff audit and author approval. |

## High-value anonymous references

Prioritise names in T3 and later:

- Listener and patient dragon in `05`;
- harbour master, mending woman and stonemason in `17`;
- teenage musician, boy, fisherman, knot-keeper and Listener in `21`;
- carver in `26`;
- healers in `30`;
- coastal fisherman or harbour master in `33`;
- hatching elder and egg workers in `35–37`;
- recurring elders in `41–45` where appropriate;
- child informant in `52`;
- residents encountered during `53–56`; entry `57` remains protected;
- young fisherman in `62` if he is Kai.

Do not name anonymous children or one-off villagers solely to increase a count. A name should create recognition, social difference or later payoff.

## Pass 7 completion test

- By T3, Pepper knows several residents without asking Manami to interpret everything.
- At least four non-Manami Manaïari recur in more than one entry.
- No new character has incompatible ages, locations or occupations.
- Each recurring person has one quality or opinion unrelated to their narrative job.
- Early T1 still feels socially unfamiliar.
- Every newly named or merged identity is recorded in the canon ledger, and every fixed unnamed identity remains consistent with its existing source references.

---

# Pass 8 — Resolve small plausibility and terminology concerns

## Objective

Remove distractions that invite arithmetic, institutional or geographical objections. Do not over-explain the fantasy.

This is a decision pass. Most items below are already canon anchors, so diagnosis alone does not authorise a "plausible" replacement. Prepare `workbench/plausibility-decision-dossier.md` with the current canon, the smallest wording-only option, any canon-changing option and all downstream references. Implement only the author's selections; update `chronology.md` first for time or scale decisions and `canon-ledger.md` first or atomically for every changed fact.

## Decision and change inventory

| Location | Concern | Required decision or direction |
|---|---|---|
| `story/1-prologue.md:70` | `Dragon Protection Act`, described as international law near the United Nations. | The Act and 1972 date are canon. Offer a wording-only distinction between a domestic Act and an international instrument, or an explicit rename; a rename requires ledger and payoff updates. Keep Pepper's political achievement and `She did.` payoff. |
| `story/1-prologue.md:86` | Trunk `sealed away for generations`. | Check against the fixed ~2005 discovery and family chronology. Prefer a wording correction that does not move dates; if a date moves, update chronology first. |
| `story/1-prologue.md:92` | Childhood dragon reappears `more than a hundred years later`. | Lady Chestnut being 100+ by ~2005 is canon. Resolve the wording or narration-date arithmetic without making the dragon younger; any narration-date decision belongs in chronology and the ledger. |
| Prologue, `01`, `07`, `18`, `20`, `32`, `33`, `53`, `57`, `75`, `77` | Aizomea alternates among continent, island and landmass. | Current canon calls it a continent while recording its crossing distances. Decide whether the terms describe geological category, ordinary speech or scale. A change to size or category is a canon amendment and must be propagated; protected entries `57` and `77` are not edited merely for terminology. |
| `entry 53:5–7` | Twenty days across, Pepper's 150-mile estimate and Jamie's 100-mile correction sit uneasily beside `sixth continent`. | The distances and Jamie's correction are canon. Prefer clarifying what was measured or how `continent` is used. Increasing scale or making distance non-Euclidean changes canon and requires chronology and ledger amendments. |
| `entry 18` and T5 context | Maritime concealment is explained; aircraft, radio and later satellite observation are not. | Any aerial, radio or image-distortion mechanism is new canon. Offer the smallest optional line and record its consequences; do not insert it as if already established. Preserve all existing fog, sentinel, sleep and Ship-Shifter mechanics. |
| `entry 24` | Hot-air geysers launch human gliders vertically. | Decide whether this is dragon/geothermal fantasy or ordinary physics. One observational caveat is enough. |
| `entry 25` | Literally unbreakable promises create major legal and ethical consequences. | Unbreakability is canon. Explore consequences or edge cases without making it belief, sensation or mere social obligation. Weakening it requires an explicit canon amendment and full amulet audit. |
| `entry 46` | `Mouelleubleus` appears French while presented as a Manaïari word. | The term is canon. A Pepper nickname, bilingual rendering or etymology would add canon; replacing it also changes canon. Present options and record the chosen one. |
| `entry 59` | A 1948 entry recounts `the first time` without immediately marking it as past-trip memory. | Add a light retrospective cue if still ambiguous after Pass 2. |
| `entry 62` versus `10` | Valuable exchange versus an apparently value-free society. | Preserve the gift economy: no money, no ownership-word, favours remembered but not tracked. Let Pepper correct her misunderstanding of value without introducing barter accounts or prices. |

Optional fact-checks before final copy-edit:

- Oxford biology and women's participation during Indigo's study period;
- the institutional language appropriate to a 1972 international dragon-protection agreement;
- period use of selected scientific and colloquial expressions;
- Pacific geography if any fixed bearings survive the final text.

## Pass 8 completion test

- `island`, `continent` and `landmass` reflect one deliberate canon rather than interchangeable usage.
- Jamie's age and the prologue's elapsed times can be calculated without contradiction.
- The protection agreement has credible institutional terminology.
- The chosen fantasy mechanism answers the most distracting concealment questions without attempting to simulate a technical manual.
- Later observations are allowed to correct Pepper's early interpretations.
- Every changed fact is represented consistently in the chronology and canon ledger; any unselected option remains only in the dossier.

---

# Pass 9 — Reframe Japanese influence as inherited and reciprocal

## Objective

Treat Aizomea's human culture as descended partly from Japanese settlers who brought knowledge with them, then developed distinct local forms in relationship with dragons. Do not imply that recognisable Japanese traditions were secretly invented in Aizomea and exported back to Japan.

The author has selected the broad direction: inherited, dual culture rather than secret Aizomean origin. Before editing the three passages, record that transmission model in `canon-ledger.md` and reconcile the 5th–6th-century settlement note in `chronology.md`. The exact claims about who arrived, what they brought and what later changed still need to be phrased narrowly enough that this small correction does not invent an unnecessary migration history.

## Reference inventory

| Location | Current direction | Revised direction |
|---|---|---|
| `entry 06:5` | Japanese settlers brought gourd seeds. | Keep. This already presents transmission in the respectful direction. Consider whether the instrument form also combines inherited and dragon-derived practice. |
| `entry 14:7–9` | A man of Japanese descent leaves Aizomea and takes bath-house culture home, implying an Aizomean origin for Japanese bathing etiquette. | Reverse the history. Settlers recognised the dragon pools through bathing traditions they already carried; generations of shared use produced an Aizomean variation. Remove the claim that Japan received the custom from Aizomea. |
| `entry 37:11` | `It reminds me of kintsugi. I wonder which came first.` | State or imply that descendants adapted an inherited repair philosophy to dragon eggshell and blue-stone resin. The local craft remains distinctive without claiming priority. |
| Manami, Hana and other names | Japanese-derived names exist beside a distinct Manaïari language. | Treat them as evidence of the agreed dual inheritance, then record the exact linguistic explanation in the canon ledger or its governed character ledger. Do not make every name share one origin by default. |

## Cultural model to establish

- Settlers arrived with languages, bathing practices, crops, crafts and memories.
- Isolation and exchange with dragons changed those practices over many generations.
- Manaïari culture is neither frozen historical Japan nor the hidden source of Japan.
- Similarity can indicate descent, parallel adaptation or continuing dual identity.
- Pepper must distinguish evidence from her delight in speculative origin stories.

## Pass 9 completion test

- No real Japanese tradition is attributed to Aizomea without explicit fictional-world justification and deliberate approval.
- The Manaïari are allowed cultural ancestry rather than appearing to have emerged as a timeless ecological ideal.
- Japanese inheritance is visible in more than exotic names, food and aesthetic motifs.
- Local adaptations remain original and illustration-worthy.
- The canon ledger and chronology state the same direction of cultural transmission as entries `06`, `14` and `37`.

---

# Pass 10 — Regression, collision and read-aloud audit

## Objective

Check the collection after all targeted passes without beginning a new stylistic rewrite.

## Automated checks

1. Search again for all strict and loose `not X, but Y` constructions.
2. Search for newly introduced `rather than`, `instead`, `not this. That`, and `isn't X. It's Y` substitutes.
3. Recount `I watched`, `I asked`, `Manami`, `no one`, `nobody`, `always`, `never`, `entirely`, `something`, `warm`, `faint` and `slow`. Counts need not be low; clusters should be inspected.
4. Search all blue-stone references and label each against the canon properties.
5. Search every Nangula reference and confirm that professional agency survives.
6. Search new character names against the character ledger.
7. Compare every manuscript dateline and trip tag with `workbench/chronology.md`; confirm that mixed-trip excerpts follow the authorised treatment.
8. Check every newly introduced period phrase or reference against `workbench/pepper-period-language-ledger.md`.
9. Search for every verbatim protected line in `workbench/canon-ledger.md`; confirm protected entries, cuts, bracketed production notes and planted payoffs by manual inspection.
10. Diff the final story facts against the canon ledger section by section: chronology, people, mechanics, payoffs and protected language.
11. Inspect `git diff --cached` before each commit and confirm that only the approved pass, its change log and the ledger/chronology maintenance it requires are staged.

## Human editorial checks

- Read the prologue followed immediately by one T1 entry. Jamie and Indigo should not sound interchangeable.
- Read one representative entry from each trip without looking at its date.
- Read entries `03, 04, 10, 17, 25, 30` consecutively to test whether Manaïari society remains varied and credible.
- Read entries `06, 07, 09, 12, 25–30, 34, 37, 42, 46, 52, 63, 66, 70` as one blue-stone dossier.
- Read all Nangula passages in isolation as if she were the protagonist of her own unwritten book. Her choices should form a coherent life.
- Read the last sentence of every entry consecutively. If they resemble a collection of quotations, the AI-ending pattern remains.
- Read the manuscript aloud in groups of ten entries. Repeated cadence is easier to hear than to see.

## Final acceptance criteria

- No structural changes have been introduced.
- Every entry retains its main image, discovery, joke or emotional purpose.
- No `not X, but Y` construction survives.
- Indigo's trip voice is identifiable from prose, not merely from date or subject.
- Period texture comes from verified syntax, usage, objects and references rather than stock vintage slang.
- Jamie has a distinct documentary and familial voice.
- The Manaïari possess institutions, disagreements, obligations and named individuals without losing their warmth.
- Nangula has independent purpose, scholarship and deliberate agency.
- Blue stone's many canon uses read as related material, craft, biological or dragon-mediated manifestations rather than unrelated conveniences.
- Japanese influence is inherited and transformed, never erased by a secret-origin claim.
- New prose does not exceed the original density of aphorisms, similes or tidy moral conclusions.
- `canon-ledger.md`, `chronology.md`, the governed character/period ledgers and the story contain no contradictory version of a fact.
- Every canon or date change can be traced to an explicit author decision in the pass log.
- All editorial artefacts produced by these passes live under `workbench/`.

## Suggested change-log format for each pass

| File + stable phrase anchor | Original issue | Intervention | Canon class | Ledger action | Chronology action | Protected status | Intended effect | Cross-pass risk |
|---|---|---|---|---|---|---|---|---|
| `story/2-entries/xx-...md` + short phrase | Brief diagnosis | recast / qualify / name / fact-align / voice | non-canon / clarification / amendment | none / section updated | none / row updated first | clear / protected decision ID | One sentence | Later pass to recheck |

The log should record decisions, not merely changed files. This will make later AI-assisted passes less likely to undo earlier judgement.

## Preview and commit workflow

The workbench preview compares the live `main` branch with the working tree. From the repository root (`story/`), run:

```sh
python3 workbench/preview-server.py 8765
```

Then open `http://127.0.0.1:8765/preview.html`. The left pane follows `main`; the right pane reads and autosaves the corresponding file in `2-entries/`. A commit made on `main` therefore makes the panes converge without a restart, while commits made on an editorial branch remain visible against `main`. The file list is generated dynamically, so renumbering or moving the old `entries`/`entries-v2` directories no longer breaks it. An optional second argument selects a different comparison branch or ref, for example:

```sh
python3 workbench/preview-server.py 8765 another-branch
```

Operational rules:

- leave the server running across edits and commits; its baseline follows the selected branch automatically;
- use the preview to assess wording, rhythm and word-count changes, not as the sole place to manage canon;
- the editor deliberately writes only existing files in `2-entries/`; it cannot create entries or update ledgers;
- when a preview edit changes canon or time, make the corresponding ledger or chronology edit before committing;
- after review, stage explicit files, inspect `git diff --cached`, run the pass checks and commit the approved pass as one coherent unit;
- leave unrelated pre-existing modifications and deletions unstaged.
