# Aizomea — Refinement Brief

*Start-of-session prompt for continued refinement work. The big anti-AI refactor is DONE (June–July 2026, ~130 commits); this brief is for whatever comes next. Read this file first, then the canon ledger.*

## The project

An illustrated book (300+ pages of art) set in the **Wyrmspan** universe: *the Land of Dragons* — Aizomea, a hidden living continent in the Pacific. The text is scaffolding for illustration; every entry hands the illustrator at least one paintable moment.

**The frame:** Jamie (present day, gender never specified) inherits a trunk from their grandmother, **Lady Indigo Pepper** (1901–1985), containing the journals of five secret trips to Aizomea — 1938, 1948, 1955–56, 1963, 1971. The book = Jamie's **prologue** (memoir) + **77 journal entries** curated from "thousands of pages" (this curation conceit is load-bearing: it explains uneven coverage, gaps, and consistent quality). Long-game threads: River (her daughter) falls for Kai the fisherman across 1963/1971 → Jamie, born 1972, is their child — **implied, never stated**. Nangula Sossusvlei passed the guardianship (and the compass) to Indigo; Indigo wonders who comes next; the reader knows.

## The text (canonical)

- `1-prologue.md` — Jamie's voice.
- `2-entries/` — 77 entries, numbered **01–77** in book order (thematic, NOT chronological), each opening with an italic period dateline ("*11th March 1938*"). Filenames carry trip tags (`-T1`…`-T5`, some dual).
- `0-timeline.md`, `3-colophon.md` — adjacent book parts, untouched by the refactor.

## Voice & tone — the heart of it

**Indigo (entries):** a working field journal. Dry, precise, self-deprecating; curious before frightened; English understatement over a French ember; never twee — her comedy is deadpan and slightly cruel to herself. Briefly devastated, then covers with an observation about tea or buttons. Voice ages across trips: T1 long sentences, semicolons, measurements, N.B.s, day-counts; T2 sparer; T3 letter-cadence (to dead Cassius), mending metaphors peak; T4 shorter, parental watching, measuring habit dead (noticed once, entry 65's P.S.); T5 fragments, white space, French, present tense — entry 77 is the model. Personal tics (haberdashery metaphors, apologising to objects, tea jurisprudence → surrender in 75, French slippage increasing with age) — lumpy, not evenly spread.

**Jamie (prologue + editor's notes):** memoir. Long complete sentences, past tense braided with present reflection, modern vocabulary fine, parenthetical asides, **no stingers** — sections end on an image, object, or plain fact. Tics: grounding claims in trunk evidence; "I like to think… / I have decided to…". Never uses Indigo's tics.

**Style rules (author-set, hard):**
- **Every addition must earn its place locally** — a line justifies itself by voice, joke, fact, or hook, never by "texture" or a tic budget. Prefer no addition over a flat one.
- **State the telling detail, then stop.** Never explain the mechanic. Prefer *showing* furniture (strikethroughs `~~word~~` = visible thinking; italics for distrusted words; "P.S." addenda — never "Later") over explanatory sentences.
- **De-tick never removes meaning.** "As if"/"the way"/reflective closers that carry a specific idea are keepers (budget be damned).
- **No em-dashes** (`---`/`—`). Comma, semicolon, colon, parentheses, full stop. Sole survivor: the "— Indy" signature in the protected note.
- **No meta:** Indigo never refers to "entries," counts of them, or the book. **Knowledge chronology:** she can't know a thing before she learns it (the island's name arrives ~day 12; people before she meets them, etc.).
- **Dragons are beasts too.** Teeth stay off-page, told through evidence (entry 22's scars and singed knot; entry 33's returned boat). Never resolve the southern mystery.
- **Blue stone:** valuable, non-rare, hard-won; *respect, not reverence*; **never the word "magic."**
- **Nangula died in 1935 and never discussed Aizomea with Indigo** — address to her is posthumous only (32, 76).
- British English (learnt, whilst, colour); nothing anachronistic to each trip's year ("the cold-ache," not brain freeze).
- Subtle beats spelled-out; a wondering ("How will I know?") beats a statement.

**Accepted quirks — do NOT "fix":** the Manami-delivers-the-payoff pattern (~15 entries; she's the interpreter, it's character); the three one-word quote-cappers ("Dinner." / "Manners." / "Democracy."); entry 25 as the one scene-less notebook-note; entries 06/28 lean on their predecessors (a layout adjacency note, not a text problem); 14 entries left untouched as deliberate slack. Protected lines are listed in the ledger §5 — verbatim, always.

## Reference files

| File | What it is |
|---|---|
| `workbench/canon-ledger.md` | **THE LIVING CANON BIBLE** — chronology (trips, dates, voyage out), people, birthdays/death-days (§2b, with silent dateline alignments), world mechanics, planted payoffs, protected lines, trip rosters. Uses the canonical 01–77 numbering. Change canon here first. |
| `workbench/chronology.md` | Per-entry dating table — **source of truth for all datelines**; change a date here first, then re-stamp the entry. |
| `workbench/world-lore-candidates.md` | 20 major world-history facts (bounties→extinctions→institutions→law) for the prologue's graphical timeline — **pending author review**; #13 flags a deliberate liberty with the game's Steely Fae fact. |
| `workbench/queries-for-author.md` | Decision log (author rulings; append new ones). |
| `../agent-resources/wyrmspan_dragon_facts.csv` | The game's 262 dragon facts — **canon, but not actively reused**; dracologist guilds, the DPA's clauses, the Sossusvlei wyvern live here. World premise (author liberty): dragons well known but *rare* — like whales, not pigeons. |
| `workbench/entry-plan.md`, `index.md`, `change-report.md`, `aizomea-refactor-plan.md` | Historical refactor apparatus — **all use OLD entry numbers**; old→new mapping at the bottom of `index.md` (21a→22, old 22–74→+1, 74a→76, old 75→77). Tic inventory is appended to entry-plan. |
| `workbench/quality-report.md` | Outside review from another session — author said **ignore**. |
| `workbench/preview.html` + `preview-server.py` + `preview-files.json` | The side-by-side review app — **archived/broken** (points at deleted `entries/`+`entries-v2/` dirs). To revive for future passes: repoint at `2-entries/` and use `git show` for the "before" pane. |

## Working conventions

- **Git is the safety net.** Commit every change, small and single-purpose; end commit messages with `Co-Authored-By:` the agent line. The author edits files directly between turns — check `git status` before assuming tree state, and fold author edits into commits with attribution in the message.
- **Author reviews everything.** When the author asks a *question*, answer it — don't change text until asked. When the author says a change "feels wrong," the diagnosis usually generalises; look for the principle.
- New entries carry `STATUS: draft — author approval pending` until the author removes it. (Note: after the renumbering, inserting a new entry means renumbering again — an author decision.)
- Length guardrail: flag any entry moving beyond ~±40% of its size (illustration spreads are scoped to weight).

## Open threads

1. **World-lore review** → pick keepers from `world-lore-candidates.md`, settle the #13 liberty, promote to a new canon-ledger "world history" section, then design the prologue timeline.
2. **Canon-enrichment exercise** — author has flagged a future session on lore and enriching the canon ledger (beyond the timeline).
3. **Sketch captions** — 4–6 across the book, deferred to illustration layout, each must be individually good (no quota-filling).
4. **Alignment voicing** — the birthday/anniversary resonances (§2b) are currently silent in the datelines; decide entry-by-entry if any get a spoken beat (the silent ones are arguably strongest).
5. **Layout notes** — keep 27/28 and 05/06 adjacent (dependent openers); entry 22's illustration may show the scarred dragon drawn from his unscarred side; entry 45's spread can take the ascent or the garden.
6. **Available, unused:** the Date Line "two Tuesdays" dating joke (T1 voyage); River's unwritten 38th-birthday day (7 Aug 1971, between entries 70 and 75).
