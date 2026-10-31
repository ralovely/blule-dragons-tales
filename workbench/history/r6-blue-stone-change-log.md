# R6 — blue-stone inventory and distributed wonder

31 October 2026. [R6 child](https://ampcode.com/threads/T-01a18fe9-eb00-7703-87b7-03bdb06895f6). **Author-reviewed and approved; shipping authorised.**

**Latest state:** the author confirmed **“All changes reviewed”** after applying the final 12 and expanded 30, then requested **“ship.”** All six changed pieces (07/08/12/29/30/34) are marked Reviewed; **32 stays unchanged and dragon-spit is rejected.** Canon ledger and dossier reflect the final approvals. See the final sections for validation and shipping authorisation; earlier sections describe then-current drafts.

## Initial scope and decision — superseded by author follow-up

The [decision dossier](../notes/blue-stone-decision-dossier.md) inventories explicit claims, linked objects and indirect echoes, separating existing canon from interpretation and from anything a future amendment would need to decide. It precedes the manuscript proposal. All named R6 pieces and the rest of P/01–77 were read in full. The starting checkout was clean at shipped R5 **2754ee92a93ff2f6999b2c5e0d4545d1ce8eb4f4** after fetching `origin/main`; separately shipped preview fix **7b70cb4** is included. No older coordinating-thread baseline was used.

Only manuscript proposal: **07, final paragraph, “a familiar reverence” → “a familiar respect”.** This aligns the airborne-quarry description with the approved respect-not-reverence framing. It does not dismiss the islands' wonder, alter the harvest rite or remove the milk offerings. Author acceptance, revision or rejection remains outstanding. No canon amendment is requested or implemented.

Deliberately retained: 34's causal assertion that blue-stone traces make one egg kind lighter than air; heavy raw samples; permanent hands; everyday pots/thimbles/tools/pigment; beetle shells; all glow/full-moon and dental-perimeter properties; poultice and food; humming season and allergy; harvest-only riding; every amulet property, its readiness rite and distant annual glow. The Prague egg remains an egg, and the compass's relationship to the stone remains Pepper's inference. No new mechanism or compulsory explanation is added.

The existing sensory and craft vocabulary is already coherent enough. Differences between contexts are not contradictions requiring a universal law. The dossier records why no repairs are proposed for raw weight versus floating shells, fragility versus tools, sky-source versus underground cave deposits, permanent versus surface colour, or different light levels.

## Executed validation

- Re-read the changed 07 in full and neighbours 06/08 after editing; checked it beside 09's harvest and 27's care/offerings. Re-read supporting records. No date, property, scene, joke, protected phrase or ending was changed.
- Inline Python comparison of **all 79 manuscript files** against fetched `origin/main`: **only 07 differs**, and its bytes equal the baseline with the exact single substitution. All other 78 files match byte-for-byte. All datelines match; 07 remains **427 → 427 words**.
- That exact-file comparison preserves R3's 21/33/42, R4's 29/30 and restored 17, R5's final P/04/32 and every protected whole piece/payoff. Authoritative references, tracker and preview implementation remain untouched.
- Checked **156 quoted inventory anchors** against shipped manuscript wording, including the floating-shell causal sentence. The classification does not treat an omitted ledger detail as permission to weaken it. Corpus search finds **no occurrence of `magic` in manuscript prose**.
- **All 156 original/current preview API responses** (78 selectable pieces) match Git/disk. Preview metadata confirms baseline `main` resolves to the shipped R5 head above. Review API is empty and stayed empty; no save, revert or review control was invoked.
- `amp orb services ensure` first timed out on portal-proxy readiness. Inspected the service, confirmed it running, and reran ensure successfully. No tooling/configuration change was needed.
- In Chromium at **2×**, opened 07 and inspected both word-diff and plain-baseline comparisons privately. Initial top-of-entry captures did not include the change; scrolled the actual panes and inspected replacement captures. Both final captures show the complete last paragraph and sunset ending without clipping, “reverence” versus “respect”, and the review toggle off. DOM confirms exactly one removed word and one added word, and Reviewed false. No UI implementation or interaction behaviour changed, so no interaction recording was needed. Inspection captures are temporary and removed; no screenshots are included in replies at the author's request.
- `git diff --check` and local supporting-record link checks pass. These are preservation/render checks, not a claim of author preference or a blind reader test.

## Review and delivery

Exact live portal: https://t-03h5cg8xixdrc8nq895x8171y-p23639.onamp.dev/

Select **07 · underground labyrinths**. The original is shipped R5 and the working text contains the single proposal; the before/after remains meaningful until approval. Reviewed marks belong to the author.

Local changes: 07 plus the new dossier and this log. No reference maintenance was necessary for a wording-only alignment with an already approved fact. No tracker rewrite, commit, push, merge, shipment or deployment. The next author decision is whether to accept the one-word proposal; no physical-law decision is required to complete this inventory.

## Author-directed trial — fewer explanatory jobs

The author clarified that canon is being created and can change in service of stories, including through other artefacts or mechanisms. The recommendation was to retain the material's sensory/craft identity, let living creatures have wonders of their own, keep medicine with practitioners and leaves, and distinguish the existing crafted amulets and inherited compass rather than invent another catch-all substance. “Let’s try” authorised this local draft.

Applied precisely:

- **08:** delete “The shells are infused with blue stone.” Pulsing beetles at dusk and both other captions remain.
- **12:** “blue stone poultice” → “leaf poultice”. Everyday treatment, aspirin comparison, pigment and bird promise remain.
- **29:** delete the sentence beginning “Over years, the blue stone bonds to the enamel”. Preserve dental practice/provenance, inspector, examined intact teeth, blue smile, glowing perimeter, daily line and full-set note. This revises the explanation, not the observed dental outcome or R4's observational limits.
- **30:** “crushed leaves and blue stone dust” → “crushed leaves”. Bone-setter, ice dragon, nine days, coordinated practitioners and spiritual care remain exactly as shipped.
- **32:** delete “I think your compass works on the same principle.” Separate the existing eye/north/looking sentences as their own paragraph. Keep the call as Manaïari belief and retain R5's complete contribution paragraph, liberation recollection, scars and “She did.” No replacement explanation.
- **34:** delete “The shell contains traces of blue stone, enough to make it lighter than air.” Every behaviour and anecdote stays, including strings, years outside the house and the kicking third egg. This is an author-directed canon attribution change, not an unnoticed removal of a protected claim.
- **25–27:** unchanged. The existing dragon-working/carving scene already supplies a distinct amulet origin; an added explanatory sentence would do the opposite of this pass's purpose. All amulet properties and humming-season descriptions remain.
- Earlier **07** respect proposal remains in the same before/after comparison; it is peripheral to this substantive trial.

Synchronised `reference/canon-ledger.md` only where needed: label the author-directed trial; remove the medical use and compass inference; record the now-unexplained beetles/eggs and retained dental outcomes; distinguish amulet objects from ordinary utensils; update the compass payoff anchor whose “your compass” wording was removed from 32. The original baseline inventory remains as provenance, with its later trial changes explicitly recorded. No chronology, tracker, source CSV or preview-code change.

### Trial validation and review

- Re-read all six newly changed pieces in full and their thematic neighbours 07/09/11/13/24–28/31/33/35, plus related source/ledger material. The short 08 caption reads as an observation, the float/kick anecdote is intact, and the care scenes no longer name the mineral. Wyrmspan 51/75/187/226 impose no conflicting material explanation; no source trait was imported.
- Inline Python applies the exact agreed replacements to shipped R5 and compares **all 79 manuscript files**: exactly 07/08/12/29/30/32/34 differ, with no additional changes. The other **72 files** match byte-for-byte, including P/04, 17, 21/33/42, 25–27, 37, 63/66/70/76 and protected whole pieces. R4's 29/30 and R5's 32 survive except for the precise authorised R6 edits above.
- All datelines unchanged. Word counts: 07 **427→427**; 08 **79→72**; 12 **598→597**; 29 **461→438**; 30 **357→353**; 32 **452→443**; 34 **394→380**. Every change is within 10%; no scenes or discoveries cut.
- All **156 original/current preview API responses** match shipped Git/disk. Baseline remains shipped R5; no agent-set save/review/revert. Reviewed API stays empty. No use of `magic` in manuscript prose.
- `amp orb services ensure` confirms **HTTP 200**, same exact portal above. Privately inspected fresh **2×** word-diff captures of all six new affected entries: each changed passage readable and unclipped, retained images/outcomes visible, and the compass paragraph break clear. 07's earlier inspected comparison remains unchanged. Browser DOM confirms one localised change per entry and Reviewed off. No UI implementation/behaviour change, so no interaction recording needed. Inspection captures are removed and not included in replies.
- `git diff --check`, exact baseline inventory-anchor checks and local links pass. Re-read changed reference passages and supporting records. These checks establish preservation and a usable review surface; author judgment of the prose remains open.

**Current delivery:** seven locally modified manuscript pieces, the synchronised canon-ledger trial and the two new R6 supporting records. Uncommitted and unshipped; no push, merge or deployment. The preview still compares the whole trial against shipped R5, not against an intermediate draft. Review 08/12/29/30/32/34; 07 remains available too. No further canon decision is blocking this trial; the author can now judge the actual wording.

### Author follow-up — 12 needs more comic strangeness

The author found “leaf poultice” too normal and not funny enough. Replaced it with **“dragon-spit poultice”** for review, preserving every other byte of 12's shipped wording. The aspirin comparison now normalises something peculiar rather than a familiar herbal remedy. This proposes a new ingredient, not a universal healing rule; exact wording and ingredient await author acceptance. Entry 30's crushed leaves stay as drafted. Ledger trial note and dossier updated to distinguish this proposal from the earlier leaf version.

Re-read 12 in full and neighbours 11/13, the healing scene in 30, tone guidance, and relevant source/ledger material. Source saliva rows 92/176/187 do not establish this remedy or contradict a particular prepared poultice. Exact-replacement validation passes for 12 and confirms 30 unchanged from its previous trial. Preview current API matches disk; service responds HTTP 200; fresh 2× comparison privately inspected with the complete remedy paragraph readable and unclipped. The preview reports one change for 12. `git diff --check` passes. No save/revert/review action invoked; review API now lists 07 and 08, which were left untouched. Private capture removed. Same review portal, still local and uncommitted; no push or shipping.

### Author decisions — retain 32; poultice discussion continues

The author keeps 32: the passage develops the compass rather than adding another use of blue stone. On inspection the author had already restored the manuscript; `git show HEAD:manuscript/2-entries/32-dragons-outside-aizomea-T2.md | cmp - manuscript/2-entries/32-dragons-outside-aizomea-T2.md` confirms byte identity with shipped R5. No manuscript edit was needed. Retain the original paragraphing, Manaïari belief and Pepper's “I think” inference. Ledger and dossier now reflect the explicit decision rather than the withdrawn proposal.

The dragon-spit version was rejected for the harvesting implication and potion-making register. The author amended 12 to the unspecified poultice with the smell line; it was left untouched. Further sensory description, inquiry and comic retreat belong in 30. The latest mushroom wording remains only a conversational proposal, not implemented or canon. Entry 30 still has crushed leaves. The ledger's stale dragon-spit trial description is corrected without approving any replacement ingredient.

Current delivery: six modified manuscript entries (07/08/12/29/30/34), ledger and two supporting records. Only reference/supporting records changed in this follow-up. Local, uncommitted and unshipped; no new manuscript or preview change and no review controls used.

### Final author approval and validation

The author said **“All changes reviewed.”** The preview review API lists exactly 07/08/12/29/30/34, matching all changed manuscript entries. The author applied the final 30 description: brown-green and stringy, boiled cabbage and wet wool, tiny mushrooms growing in it, and Pepper changing her question halfway through the ingredient answer. The final 12 keeps the smell joke and otherwise leaves composition unspecified. 32 remains shipped R5 verbatim. No further manuscript edits were made by the agent; the canon ledger and dossier now record the approved final state, not interim alternatives.

Final checks: **79 manuscript files compared** with shipped R5; exactly six differ, the other **73 byte-identical**. All datelines unchanged; **156 original/current preview API responses** match Git/disk; the six review marks match the final contents. An initial scratch date check mistakenly matched whole italic captions; narrowed it to actual dated headings and reran successfully. 30 is **357→387 words**, within 10%. Re-read final 30 in full alongside the previously read 12 and related material. Privately inspected fresh **2×** final comparisons of 12/30: full changed paragraphs readable and unclipped, including smell/aspirin in 12 and mushrooms/question change in 30. Inspection captures removed. Service responds **HTTP 200** at the same portal. `git diff --check` passes. No agent save/revert/review operations.

At completion of author review, delivery remained **local, uncommitted and unshipped**: six reviewed manuscript changes, the synchronised canon ledger, and the dossier/change log. No tracker rewrite, commit, push, merge or deployment had occurred. Exact live portal: https://t-03h5cg8xixdrc8nq895x8171y-p23639.onamp.dev/

### Shipping authorisation

The author subsequently requested **“ship.”** Re-read all six final manuscript pieces in full, inspected the final scoped diff and fetched `origin/main`, still at shipped R5. No new manuscript or canon decision is introduced by shipping. Prior private preview inspections cover the unchanged approved final text; the shipping pass rechecks file/API preservation, reviewed contents, datelines and whitespace before committing. Only the six manuscript pieces, canon ledger and these two supporting records belong to the shipment. The master tracker remains untouched.
