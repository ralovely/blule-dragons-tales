# R2 — period-language wording pass

5 October 2026. **All eight revisions author-reviewed; shipment authorised by “Good. SHip”.** The sections below preserve the sequence of proposals, review and correction, not outstanding approval requests.

## Authority and baseline

The author first commissioned research, then asked for all R2 changes to be implemented after pulling the other threads' work. The request favours a few audible period turns, not decorative archaism. The illustrative “mayhaps” is not used. After reviewing the six wording changes, the author requested the missing clothes-coupon reference and anything else omitted. Two historical references are now added for review; dragons' non-involvement in the war still needs no explanation.

Implementation starts from [author-reviewed R1 on main](https://github.com/ralovely/blule-dragons-tales/commit/b2676d97f65c08730a527e6ef3fff4dbff0f7fcc). The earlier six imported master documents were preserved separately in the named stash recorded in the [research ledger](../notes/pepper-period-language-ledger.md). They are not R2 changes and must not be restored over the shipped references.

## Six applications

Source S1 below is Freya Stark, *Letters from Syria* (1942), [primary correspondence in OCR](https://archive.org/stream/FreyaStarkLettersFromSyria/Freya%20Stark%20Letters%20from%20Syria_djvu.txt). Dates are letter dates. These witnesses establish availability, not first use or compulsory imitation. The surrounding manuscript sentences are newly composed, not quotations from Stark.

| Entry | Before → proposed | Evidence and editorial reason |
|---|---|---|
| 16, T3 | “Gerald update. He…” → “As for Gerald, he…” | S1, letter 43 to her mother, 8 February 1928, p. 61: “As for the dancing…”. A familiar letter's transition rather than a bulletin heading. Still ordinary modern English; the point is cadence. The fish experiment and unanswered resentment are unchanged. |
| 29, T3 | “genuinely cross” → “much vexed” | S1, same letter, p. 61: “I was much vexed”. A deliberately prim response to the unfair excellence of dragon teeth. The original “cross” was already plausible; this is stronger period colouring, not an error correction. |
| 35, T1 | “epic kick” → “terrific kick” | S1, letter 15 to Mrs Jeyes, 22 December 1927, p. 26: swords “whirled round their heads at terrific speed”. Attests physical intensity, not this exact noun pairing. The kick still drives the same rebound joke. No finding that “epic” is historically impossible. |
| 62, T4 | “The window had closed.” → “I was to have no more.” | A plain statement of the existing refusal, replacing a metaphor whose figurative dating remains unresolved. S1, letter 95 to her mother, 11 May 1928, opening paragraph: “we thought we were to have a grey day for a change” supplies a dated grammatical comparator for “was/were to have”, not the exact sentence or its denied-permission sense. The new line is not presented as an attested historical idiom. Both market visits remain in the same morning, as R1 settled. |
| 71, T1 | “I sat in the middle of it and realised…” → “I sat among them, and it was borne in upon me that…” | S1, letter 43, 8 February 1928, p. 61. The realisation presses on her while surrounded by company. A single conspicuous turn in a short entry; Manami's response and the contrast between home and visiting remain intact. |
| 75, T5 | “I have caught myself wondering whether I could take some home, and whether…” → “I should like to take some home. I wonder whether…” | S1, letter 12 to her mother, 9 December 1927, p. 22: “I should like to paint our cargo…”. A retained early habit in an older woman's plainer admission. Slightly more direct desire replaces self-observation; uncertainty about the taste at home stays. This is the principal tonal choice for author review, not new travel or packing action. |

No quota was imposed across the five trips. The initial wording pass left T2 alone; the follow-up below restores its two historical references. R3's fuller age-and-voice differentiation remains separate. No French was added solely to advertise parentage. Scientific uncertainty and domestic/professional specificity already present are retained rather than supplemented with invented measurements.

## Follow-up: two omitted historical references

The agent wrongly interpreted the author's emphasis on diction as shelving historical references. The author had rejected only the dragon-war explanation. On being asked about the omission, the author authorised the coupons reference and anything else left out, and requested resetting review status for edited entries.

- **60 (14 July 1948):** after the dragon admires its laundry nest, add “One of my shirts was in it. I had not spent clothes coupons to line a dragon's nest.” This is a small extension of the existing incident, not a new wartime story. The Ministry of Information's 1943 *Make Do and Mend* film supplies period coupon language; [IWM's transcript and historical introduction](https://www.iwm.org.uk/history/second-world-war/home-front/rationing/make-do-and-mend-1943) distinguish the primary film from the institutional account dating clothes rationing to June 1941–1949. No coupon quantity, purchase date or wartime location is invented. R1's “for weeks” remains intact.
- **32 (25 August 1948):** add the opening notebook aside “Four years today since Paris was liberated. I have been thinking of Montmartre.” The [25 August 1944 Hôtel de Ville speech](https://www.charles-de-gaulle.org/wp-content/uploads/2017/03/Discours-de-lHotel-de-Ville-de-Paris.pdf), opening “Paris libéré” sequence, supplies the dated public event; the manuscript already supplies the anniversary dateline and childhood connection. The aside makes no claim that she witnessed liberation, heard a particular broadcast or had family under occupation. It is separated from the hunting paragraph; “like bark over a nail” and “She did.” remain unchanged.

Both sources were re-read for this follow-up. These are newly composed lines, not quotations. The stronger personal stake in the stolen laundry and the anniversary thought are the small additions now awaiting author judgement. The other unused palette expressions were alternatives, not omitted commitments; no further insertion is required solely to use the research.

## Retentions and limits

- Retain “technically correct” (06), “public service” (60), “chain of command” (56) and “supervisory” (63): the research ledger records earlier witnesses in 1909, 1927, 1951 and 1948 respectively. Their use in these jokes remains an editorial judgement.
- Leave the rotating-gallery metaphor, the tea/bother formulation, emotional-language questions and protected “stop performing” untouched. Their exact historical claims remain unresolved, not disproved.
- Oxford's exact headcount/department wording, Harley Street dentistry specifically, the Muséum programme and travel details remain unverified at that level of specificity. The international “Act” question remains R7's responsibility.
- Most private-language evidence is early Stark correspondence, edited for publication and read in OCR. This is not a balanced corpus of all five decades; continued use in 1971 is a character judgement.

## Initial six-entry validation

- Re-read all six changed entries in full, plus related Gerald, hatching, tea, River and farewell passages; checked current canon, chronology and timeline. No new event, relationship, date, scientific mechanism or wartime experience is proposed.
- `git diff --check` passed. A Python assertion check found exactly six changed manuscript files, no changes to references, master tracker or preview code, and identical datelines and editor's notes. All other manuscript files, including R1 repairs and protected entries, remain identical to the pulled baseline.
- Word counts, including datelines: 16, 368→369; 29, 487→487; 35, 544→544; 62, 263→265; 71, 77→80; 75, 217→214. All remain within 10% of baseline length.
- Started the existing preview with `amp orb services ensure`. For each affected file, checked `/api/original/` against Git and `/api/current/` against disk. All twelve comparisons passed.
- Opened all six entries in the browser and inspected rendered comparisons, including scrolled captures of the offscreen edits in 29 and 62. Changed text is legible in both panes. Each entry reports one change; Reviewed remains unchecked. No save, revert or review action was taken. A partly clipped first line at a scrolled pane boundary is existing preview behaviour, not a manuscript defect.

The author subsequently reviewed these six revisions. Their text and review records are preserved during the historical-reference follow-up. The preview continues to compare main with the local revisions. Passing checks does not imply shipping approval.

## Follow-up validation

Re-read 32 and 60 in full and checked the historical dates against the sources above. Preview original/current API responses match Git/disk; datelines are unchanged. Word counts: 32, 415→428; 60, 437→455. Both additions remain below 10% growth. Inspected both rendered comparisons, including the scrolled laundry passage; additions are legible. Explicitly cleared review status through the preview API for 32 and 60 and confirmed both controls are unchecked. The six existing review records remain identical and their current content fingerprints still match. `git diff --check` passed. The two new additions await author review; no shipping action was taken.

### Author wording feedback on 60

The author found “I had not spent clothes coupons to line a dragon's nest” obscure. Replaced it with “I had saved up my clothing coupons to buy that shirt. Now a dragon was sitting on it.” This makes the coupon-funded purchase and the indignity separate, concrete thoughts. The earlier wording above is historical, not the current proposal. Entry 32 is now marked reviewed by the author; only 60 is reopened, with all seven other review records preserved. No other manuscript text changed in this adjustment.

## Final approval and shipping checks

The author approved the clarified coupon passage and requested shipping. All eight manuscript files match their author-reviewed content fingerprints. Final checks passed: `git diff --check`, sixteen original/current preview API comparisons, unchanged datelines and editor's notes, and less than 10% length change per entry. Every revised passage was visually inspected in the preview, including the final coupon wording. The final fetch found local main equal to origin/main before the R2 commit, so no rebase was needed. Only the eight manuscript entries and these two R2 documents are included; the master tracker, canon, preview code and imported-baseline stash remain untouched. Research limitations above remain limitations, not claims resolved by author approval.
