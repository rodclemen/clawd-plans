# Brief: Dungeon Crawler Clawd, phase 5 transitions (shared by all helpers)

You are building part of phase 5 of a new universe in Clawd Clash, a macOS app that shows AI coding sessions as
pixel-art characters ("Clawds": a blocky orange critter on four legs, in costume) on a desktop strip, a window and a
full-screen screen saver. The universe is a Dungeon Crawler Carl parody, "Dungeon Crawler Clawd", Swift, folder
`Sources/App/Universes/DungeonCrawlerClawd/`, prefix `Crawl`. All 95 characters, 20 places and the mechanics are done.
Phase 5 is the transitions ("trips") the window and the screen saver play when the scene moves from one place to
another. The wiring already exists on branch `dungeon-crawler-clawd` (commit f0661af): `CrawlTrips.swift` (the
`CrawlWipe` kinds, durations, owners, `pick`, `draw`, the shared helpers and the `CrawlArt` canvas),
`CrawlSystemCaption.swift` (the System box that ends every trip, already done) and twelve stand-in files
`Crawl<Name>Trip.swift`, each a plain crossfade. You replace THREE stand-ins with the real drawing.

## Your worktree
Agent worktrees start from `main`, not from the universe branch. Before anything else, in your worktree run
`git reset --hard f0661af` and check `git log -1` shows "the twelve trips as stand-ins" and your files exist.

## Read first
- `clawdify_guide.md` (repo root): "House style", and what it says about transitions.
- The plan: `~/Documents/- CODE -/clawd-plans/in-progress/dungeon-crawler-clawd.md`, section "Transitions
  (`CrawlTrip`, 12)": your trips' rows, the Style line, and the "Places (20)" table for what each place looks like.
- `CrawlTrips.swift` and `CrawlSystemCaption.swift` in full: the canvas (`CrawlArt`: about 160 art pixels tall,
  `wide` for the window's strip), `span`, `ease`, `mix`, `wash`, `crossfade`, `art.runs` to clip a place to a shape.
- Models to match in structure, quality and comment voice: `Universes/Eternia/Eternia*Trip.swift` (start with
  EterniaPortalTrip, EterniaJawbridgeTrip, EterniaGreyskullTrip) and `Universes/Slayer/Slayer*Trip.swift`
  (SlayerHellmouthTrip, SlayerTitlesTrip). `Universes/ClawdOfTheRings/RingsTrips.swift` shows `crewShown` in use.
- `CrawlKit.swift`: `crawlText` / `crawlTextWidth` (the System's 3×5 block letters, `scale:` for bigger). Use them for
  ALL lettering. `CrawlAchievement.swift`'s `crawlDrawSystemBox` for the System box look (navy, bright blue frame,
  soft blue glow, gold heading).

## Hard rules (the owner is strict about these)
- Write ONLY your three assigned files. If you truly need a change elsewhere (a helper in CrawlTrips.swift, a duration),
  say so in your report instead of making it. Never touch core files.
- Every top-level name is `private` or starts with `crawl` (types `Crawl…`). Never name anything `crawler…`.
- Keep each file's function names and signatures as the stand-in has them (`draw<Name>`, and `<name>CrewShown` where
  the stand-in has one).
- No em dashes anywhere (code, comments, strings). Pun names say "clawd", never a bare "claw". Clawd has four legs.
- Pixel art only, on the `CrawlArt` grid, never smooth gradients or glossy effects; nothing so fine it won't read in
  the window's strip (about 480×112 art pixels at 2 screen pixels each). Must read on a DARK desktop: no dark-on-dark.
- Old and new places only via `ctx.drawShot` (scaled or clipped is fine), so the window's info list stays sharp.
- Every frame from k = 0 to 1 must be clean: k = 0 looks like the old place, k = 1 exactly the new place (the System
  box follows on top; leave its corner, top-left, free of anything that fights it near the end).
- `crewShown` (only where your file has one): the crew are drawn by the engine on top of the scene; return less than 1
  while the floor is gone under them (fade them as they drop), 1 again once they've landed in the new place.
- Doc comments in the voice of the existing trip files: what it looks like and what happens, step by step, with the
  timings (`k` ranges).

## Build and check (in your worktree)
- `zsh Tools/Transitions/build.sh` (a minute or two), then:
  - `build/transitions <out> crawlCorridor crawlStudio` renders a key-frame sheet plus a clip of every trip;
    `SHEET_ONLY=1` skips the clips.
  - `FRAMES="<n>-<case>:0.1,0.3,0.5" build/transitions <out> <from> <to>` writes chosen moments full size (keys are
    `1-collapse` … `12-emberusFire`, from `CrawlWipe`'s order).
  - `W=960 H=224 ART=1 …` renders the window's strip as drawn. Check both sizes.
  - Try a bright pair and a dark pair of places (e.g. crawlHumpTown, crawlStudio; crawlCorridor, crawlTemple).
- `QUICK=1 Tools/CheckUniverse/check.sh DungeonCrawlerClawd` must stay clean apart from the "hand-off scope" line
  (CHANGELOG.md).
- Never run a plain `./build.sh`: it installs into /Applications and launches the app.
- Look at every render yourself (Read the PNG; crop and upscale with python PIL) and fix what doesn't read. Make a short
  GIF of each trip (frames plus PIL) and look at it too.
- Save review renders and GIFs to `~/Desktop/dungeon-crawler-clawd-phase-5/<trip>/` (never into build/).

## Finish
- One commit per trip file in your worktree: Conventional Commits, scope `crawl` (e.g. `feat(crawl): the Hole trip,
  Donut's pit`), with a body saying what happens. NEVER add Co-Authored-By or any Claude or AI attribution line.
- Report back: the commit hashes and branch, what each trip does, anything you were unsure of, anything weak you'd flag
  for the polish pass, and any change you needed outside your files. Keep it short.
