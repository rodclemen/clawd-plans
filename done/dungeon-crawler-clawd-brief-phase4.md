# Brief: Dungeon Crawler Clawd, phase 4 mechanics (shared by all helpers)

You are building part of phase 4 of a new universe in Clawd Clash, a macOS app that shows AI coding sessions as
pixel-art characters ("Clawds": a blocky orange critter on four legs, in costume) on a desktop strip, a window and a
full-screen screen saver. The universe is a Dungeon Crawler Carl parody, "Dungeon Crawler Clawd", Swift, folder
`Sources/App/Universes/DungeonCrawlerClawd/`, prefix `Crawl`. All 95 characters and 20 places are drawn. The wiring
for phase 4 already exists on branch `dungeon-crawler-clawd` (the phase 4 stand-ins commit): four stand-in files,
already hooked into `CrawlUniverse.swift`, `CrawlRoster.swift` and `CrawlFacts.swift`. You fill in ONE of them.

## Your worktree
Agent worktrees start from `main`, not from the universe branch. Before anything else, in your worktree run
`git reset --hard <STAND-IN COMMIT>` (given in your task) and check `git log -1` shows the stand-ins commit and that
your file exists as a stand-in.

## Read first
- `clawdify_guide.md` (repo root): "House style", "Verification, every phase", and whatever it says about your part
  (rides, compaction, quirks/habits, drills).
- The plan: `/Volumes/8TB/- CODE -/clawd app/clawd-plans/in-progress/dungeon-crawler-clawd.md`, section "Mechanics that
  make it its own universe" (your item), "Cast" for who's who, and the "Status" sections (owner's decisions; the
  latest wins). The plan predates the module layout: where it names `Overlay.swift`, `Habits.swift` or
  `Drills.swift`, do it through the module's hooks instead (below). Never edit core files for this universe.
- Your hook in `Sources/App/Universes/UniverseModule.swift` and the newest universes doing the same thing, to match
  their structure and comment voice:
  - rides: `Sources/App/Theme.swift` (`struct Ride`), `Universes/Eternia/EterniaRides.swift`,
    `Universes/Slayer/SlayerRides.swift` (vehicles that drive in), the shared ride kit `Sources/App/Rides.swift`;
  - compaction: `CompactionLook` in UniverseModule.swift, `Universes/ClawdFiles/FilesMissingTime.swift`,
    `Universes/StevieClawdberg/ClawdbergOutaTime.swift`;
  - habits: `StageQuirks` in UniverseModule.swift, `Universes/Eternia/EterniaHabits.swift`,
    `Universes/StevieClawdberg/ClawdbergQuirks.swift`;
  - drills: `BespokeDrill` (grep `Sources/App/Drills.swift`), `Universes/Eternia/EterniaDrills.swift`,
    `Universes/ClawdFiles/FilesDrills.swift`.
- The universe's own art for the characters you use (`Art/CrawlHeroes*.swift`, `Art/CrawlVillains*.swift`) and the
  shared helpers in `CrawlKit.swift` (`crawlText`/`crawlTextWidth`: the System's block letters, `crawlBar`,
  `crawlReach`).

## Hard rules (the owner is strict about these)
- Write ONLY your assigned file. If you truly need a one-line change elsewhere in the folder (say, a signature hook
  in an art file), say so in your report instead of making it. Never touch core files outside the folder.
- Every top-level name is `private` or starts with `crawl` (types `Crawl…`). Never name anything `crawler…`.
- Clawd always has FOUR legs. Characters keep the books' names exactly as the plan gives them.
- No em dashes anywhere (code, comments, strings). Pun names say "clawd", never a bare "claw".
- Effects must read on a DARK desktop: no dark-on-dark. Text in the System's style uses `crawlText`.
- Doc comments in the voice of the existing files: what it looks like and what happens, step by step.

## Build and check (in your worktree)
- `zsh Tools/Preview/build.sh` (4 to 7 minutes when several helpers build at once; long timeout), then Preview's
  commands (run `build/preview` with no args for usage; `rides` and `drills` exist, read `Tools/Preview/main.swift`).
  There's no command for compaction looks or habits: to see yours, add a temporary command or scratch code to
  Preview in your worktree to render frames of it, and leave it out of your commit (say in the report how you did it). Names that clash with other universes need `crawl:` in front.
- `QUICK=1 Tools/CheckUniverse/check.sh DungeonCrawlerClawd` must stay clean apart from the expected "size" warning
  and the "hand-off scope" line (the branch also changed three core fight files on purpose).
- Never run a plain `./build.sh`: it installs into /Applications and launches the app. If you want the app compiled,
  `./build.sh --release 4.3.0` builds into build/ only.
- Look at every render yourself (Read the PNG; crop and upscale with python PIL) and fix what doesn't read. For
  anything that moves, also make a short GIF (frames plus PIL).
- Save review renders to `~/Desktop/dungeon-crawler-clawd-phase-4/<your-file>/` (never into build/).

## Finish
- Commit in your worktree: Conventional Commits, scope `crawl`, with a body saying what's in it. NEVER add
  Co-Authored-By or any Claude or AI attribution line.
- Report back: commit hash and branch, what you built, anything you were unsure of, anything weak you'd flag for the
  polish pass, and any change you needed outside your file. Keep it short.
