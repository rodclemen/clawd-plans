---
name: universe-modules-refactor
description: "The universes-as-modules refactor (clawd-plans/universe-modules.md): started 2026-10-18 on branch universe-modules"
metadata:
  node_type: memory
  type: project
  originSessionId: be19b5c9-e9f0-4576-b0b5-ea68d1892e1a
  modified: 2026-10-18T11:12:16.833Z
---

The user chose the full refactor (not just the Settings checkboxes) on 2026-10-18, so new universes become one folder and users can tick which universes they use. Plan: clawd-plans `universe-modules.md` (updated: eight universes 0–7, Slayer is ported in phase 2, open questions settled with the recommended answers). Branch `universe-modules` in clawd-clash, off main after 3.7.0.

- Progress 2026-10-18: phases 0–2 done plus the Universe struct (dbd7ef7 … 1ad1d1f). Every universe has <Prefix>Facts.swift (enums, UniverseFacts, `static let key = Universe(number:)`, UniverseEntry) and <Prefix>Universe.swift (UniverseModule: theme, places, hem, preview, transitions, rides, drills, quirks, shootOuts, compactionLook, regeneration, placeCaption, prompts, meditation, poseStyle, moonwalkers, swingLine). registeredUniverses (Shared/UniverseFacts.swift) and registeredModules (UniverseModule.swift) are hand lists until phase 3. Next: phase 3 (universe.conf/NUMBERS/universes.sh, tools via registry, RenderPromo split, release.sh).
- Progress 2026-10-19: phase 3 done (README docs via module.docs, showcases in Promo/<Prefix>Showcase.swift, RenderPromo split into Tools/RenderPromo/Kit/ + Promo/<Prefix>Reel.swift behind PromoReel, all byte-identical); phase 5 done (Tools/CheckUniverse/check.sh, QUICK=1 for fast; BASE=universe-modules for scope); phase 6 done (Settings → Universes, Universe.removed, state.json `removed`, saver feed `removed`). Left: phase 4 (template, new-universe.sh, guards), a prefix/naming cleanup that check-universe lists (~170 unprefixed names, Marvelous file names, Clawdberg using Files' drawDressShoes), then phase 7 (guide). The branch has not merged main's art since 7439657.
- 2026-10-19 later: ALL phases done on universe-modules (4 template + new-universe.sh + guards, 5 check-universe, 6 Settings → Universes, 7 guide rewrite with "When a universe is complete", naming cleanup: check.sh --all has no ✗). Main merged in; main vs refactor render identically (180 sheets, only the random cantina band and the eagle-clock fix differ). Waiting for the owner's OK to merge into main; owner chose to wait for the merge rather than a test build.
- Run baselines from a detached snapshot worktree (`git worktree add --detach … HEAD` + `git diff | git apply`) so the main tree stays editable; never stash during a baseline run.
- Test technique: live overlay checks via a copy of build/Clawd Clash.app with CFBundleIdentifier com.rodclemen.clawdclash.refactortest, ad-hoc codesigned, run with --playground=… --missing-time and CLAWD_SHOT frames; delete its defaults afterwards. A loose binary outside the bundle gets SIGKILLed. Don't edit sources while a baseline run compiles.
- Phase 0 tools: `Tools/Baseline/baseline.sh <dir>` (QUICK=1 skips storyboards; MOON=new forced) and `compare.sh <a> <b>`; `build/preview ids <out.txt>` dumps every id, place, adoption and magic variant. Every later commit must compare identical.
- The user asked whether it saves resources: it doesn't (same disk, RAM, CPU); it's for maintainability and contributors.

**Why:** faster universe additions (including by other contributors) and universe selection.
**How to apply:** one universe per commit in phase 2, baseline compare after each; checkboxes are phase 6. Links: [[clawd-slayer]], [[version-rule]].
