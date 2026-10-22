---
name: clawd-slayer
description: "Clawd Slayer (Buffy) universe: built, released in 3.7.0 on 2026-10-18; decisions and lessons"
metadata:
  node_type: memory
  type: project
  originSessionId: be19b5c9-e9f0-4576-b0b5-ea68d1892e1a
  modified: 2026-10-17T15:43:59.668Z
---

Clawd Slayer (Buffy the Vampire Slayer parody) is built on branch `buffy` in clawd-clash, raw value 7 (6 is Clawd of the Rings). Working plan: `CLAWD-SLAYER-PLAN.md` at the repo root (same as clawd-plans `in-progress/buffy.md`); delete it before merging.

- 2026-10-17: taken over from the clawd-plans session's worktree; main (3.6.0 and later) merged in (d90632b), keeping all Slayer work. Helpers renamed `sl…` → `slayer…` for the PR guard.
- **Decision 2026-10-17:** build it the current way (not after the universe-modules refactor); port it with the others later.
- Phase 1 (skeleton: Buffy, Willow, Old Master, library) done. Phase 2 (core ensemble, ~32 characters + 7 places) started 2026-10-17 with parallel helpers, one new file per batch (SlayerHeroes2/3, SlayerVillains2/3/4, SlayerScenes2).
- Phase 2 approved 2026-10-17 (with fixes: Ozz stake + wolf claws, Jenny casts a touch from the glowing Orb, Dark Willow 3 bolts). Phase 3 (48 characters + 12 places) started the same day with nine helpers: SlayerHeroes4-6, SlayerVillains5-9, SlayerScenes3-4; the character audit follows.
- Phases 3 to 5 and the polish pass done 2026-10-18 (all 84 characters, 20 places, rides, Tabula Rasa, habits, drills, 13 trips; polish merged after user review). Next: phase 6 (README, docs sheets, trailer, showcase repo, cask, release as 3.7.0), which needs the user's OK since it's public.
- 2026-10-18: phase 6 done. Trailer approved (title tilted 20°, R fixed), buffy fast-forwarded into main and pushed (a6b47e9), CHANGELOG is `## 3.7.0`, plan moved to clawd-plans `done/clawd-slayer.md`. Showcase repo github.com/rodclemen/clawd-slayer created and 3.7.0 released the same day (the user ran both: the auto-mode classifier blocks repo creation and release.sh, so hand those over as `!` commands). No clawd-slayer cask: only the three original universes have casks.
- Polish review lesson: helpers' comparison PNGs were cropped too tightly and some mixed two characters in one image; the user read those as art bugs. Check comparison images before showing them.
- Each phase is shown to the user before the next. Releasing it bumps to 3.7.0 ([[version-rule]]); check new art with `build/preview edges` ([[outline-frame-rule]]).
