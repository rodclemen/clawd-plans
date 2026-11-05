# Brief: Dungeon Crawler Clawd, phase 6 polish pass (shared by all helpers)

You are polishing a finished universe in Clawd Clash, a macOS app that shows AI coding sessions as pixel-art
characters ("Clawds": a blocky orange critter on four legs, in costume) on a desktop strip, a window and a full-screen
screen saver. The universe is a Dungeon Crawler Carl parody, "Dungeon Crawler Clawd", Swift, folder
`Sources/App/Universes/DungeonCrawlerClawd/`, prefix `Crawl`. Everything is drawn; this pass fixes the known weak
spots before the docs and trailer are rendered from this art. Your prompt lists your files and your weak spots.

## Your worktree
Agent worktrees start from `main`, not the universe branch. Before anything else, in your worktree run
`git reset --hard 4b7109d` and check `git log -1` shows "a W that doesn't read as H". Never check out another branch in
the main repo folder, and never work there.

## Read first
- `clawdify_guide.md`: "House style", "Look and style", and "The polish pass".
- The plan: `~/Documents/- CODE -/clawd-plans/in-progress/dungeon-crawler-clawd.md`: the Cast and Places tables for what
  your characters and places should look like, Transitions for the trips, and the Status sections for the owner's calls.
- The head of `Tools/Preview/main.swift` for the Preview commands. Names can clash with other universes: use `crawl:`
  in front (`crawl:rory`).

## Hard rules (the owner is strict about these)
- Edit ONLY your assigned files. If a fix needs a change anywhere else, leave it and say so in your report. Never touch
  core or engine files, CHANGELOG.md, or another helper's files. Engine-wide issues are reported, not worked around.
- Change only what the weak spot needs. Keep function names, signatures, ids, weapons, colours and behaviour otherwise.
- Clawd has FOUR legs that read as four: never merge or drop them, even on dark trousers or in a redesign.
- Few big clean shapes. If a detail won't read at 1x, make it bigger or drop it; don't add fine noise.
- Outlines are cut at the 72x52 frame edge: keep solid art inside it. After any character change run
  `build/preview edges <out.txt> "Dungeon Crawler Clawd"`; everything listed for your characters must be on purpose.
- Pixel art only, no smooth gradients or glossy effects. Must read on a DARK desktop: no dark-on-dark.
- Every top-level name is `private` or starts with `crawl` (types `Crawl…`). Never name anything `crawler…`.
- No em dashes anywhere (code, comments, strings, commit messages). Pun names say "clawd", never a bare "claw".
- Never run a plain `./build.sh`: it installs into /Applications and launches the app, and wipes build/.

## Owner's decisions: do NOT undo these
- Donut: mostly brown fur, ginger saddle, brown tail, cream ruff and muzzle. Mongo: blue-grey hide, pink only as
  plumage. Prepotente stands alone, no Bianca under him. No busy multi-colour coats.
- Harbinger and Astrid both red. Shi Maria is a spider with a granny head, as drawn. Li Jun has no prayer beads. Small
  fry keep their signatures. HEM keeps the shared fist shake.
- Tserendolgor's flamethrower and tank. Eva's four swords (two on her back, two at her sash). Quan Ch pale cyan. Zhang's
  rocks grey-brown stone. The Hydra's heads take turns; Judge Lucian on top, bigger, in a wig. Circus trapezes hang from
  a cable between the poles. The Hunting Grounds lava sits in a crater summit.
- Chaco's signature runs off the left edge on purpose.
- The wheel is a game-show drum on its side, not a round face. Do not change trip odds, the stairwell's floor table or
  Ping's dot colours: those wait for the owner.

## Build and check (in your worktree)
- Characters and places: `Tools/Preview/build.sh`, then the `cast`, `fight`, `drills`, `magic`, `place`, `rides` and
  `edges` commands. A build takes 4 to 7 minutes with others running, so batch your changes between builds.
- Trips: `zsh Tools/Transitions/build.sh`, then `build/transitions <out> <from> <to>` (`SHEET_ONLY=1` skips the clips),
  `FRAMES="<n>-<case>:0.1,0.3,0.5" build/transitions <out> <from> <to>` for chosen moments, `W=960 H=224 ART=1 …` for the
  window's strip. Keys run `1-collapse` to `12-emberusFire`, in `CrawlWipe`'s order. Check both sizes, and a bright pair
  and a dark pair of places (crawlHumpTown, crawlStudio; crawlCorridor, crawlTemple).
- Places: check BOTH the window strip and the screen saver sizes.
- Render every "before" FIRST, before you edit anything.
- `QUICK=1 Tools/CheckUniverse/check.sh DungeonCrawlerClawd` must stay clean apart from the "hand-off scope" line.
- Look at every render yourself (Read the PNG; crop and upscale with python PIL). For anything that moves, look at
  several frames or a short GIF. A fix only counts if you can see it at the size it's used.

## Before and after (the owner's approval gate)
Save to `~/Desktop/dungeon-crawler-clawd-phase-6/<your group>/`, never into build/. One PNG per fixed thing, named after
it (`Li Jun.png`): BEFORE on the left, AFTER on the right, each labelled, nearest-neighbour enlarged, the whole character
or place in frame, on a dark background. One character per image, never cropped tight: the owner has read tight crops
and mixed images as art bugs. Trips: the moment that changed, before and after, plus a GIF of the after.

## Finish
- One commit per file in your worktree: Conventional Commits, scope `crawl`, e.g. `fix(crawl): Li Jun stops being a red
  blob`, with a body saying what changed. NEVER add Co-Authored-By or any Claude or AI attribution line.
- Report back, short: commit hashes and branch, what you fixed, what you could NOT fix and why, anything for the owner to
  decide, any engine request, and anything else in your files that looks weak.
