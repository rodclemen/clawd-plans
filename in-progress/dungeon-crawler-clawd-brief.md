# Brief: Dungeon Crawler Clawd, phase 3 art (shared by all helpers)

You are drawing part of phase 3 of a new universe in Clawd Clash, a macOS app that shows AI coding sessions as
pixel-art characters ("Clawds": a blocky orange critter on four legs, in costume) fighting on a desktop strip and a
full-screen screen saver. The universe is a Dungeon Crawler Carl parody, "Dungeon Crawler Clawd", Swift, folder
`Sources/App/Universes/DungeonCrawlerClawd/`, prefix `Crawl`. The enum cases, homes, nemeses, place keys and wiring
already exist on branch `dungeon-crawler-clawd` (the phase 3 stand-ins commit); you only fill in ONE file.

## Your worktree
Agent worktrees start from `main`, not from the universe branch. Before anything else, in your worktree:
`git fetch origin` is not needed (same repo); run `git reset --hard <STAND-IN COMMIT>` (given in your task) and check
`git log -1` shows the stand-ins commit and that your file exists as an empty stand-in.

## Read first
- `clawdify_guide.md` (repo root) sections "Look and style" (Characters, Places), "House style", "Verification,
  every phase".
- The plan: `/Volumes/8TB/- CODE -/clawd app/clawd-plans/in-progress/dungeon-crawler-clawd.md`: "Cast" (the weapon
  table, Motion, `bulk`, `armoured`), your rows of the Heroes/Villains tables or the Places table, "Homes", the
  "Weak spots to expect" list and the "Status" sections' weak spots (mistakes not to repeat).
- Phases 1 and 2, the bar to match (same style, same comment voice): `Art/CrawlHeroes1-3.swift`,
  `Art/CrawlVillains1-3.swift`, `Places/CrawlScenes1-3.swift`, `CrawlKit.swift` (shared helpers: `crawlReach`,
  `crawlBar`, `crawlPunch`, `crawlTalons`, `crawlText`, `crawlTextWidth`), `CrawlHem.swift`. Read the files nearest
  your group and match them.
- `Sources/App/Persona.swift` (Persona fields; argument order matters), `Sources/App/Pose.swift`, and the shared body
  helpers (grep for `drawBody`, `drawLegs`, `Look`). Look at other universes' art for how fly / hover / bulk / blaster /
  thrown / ice / notes / waves / rings / spell / touch / fire / arrow characters are done.

## Hard rules (the owner is strict about these)
- Write ONLY your assigned file. Do not touch any other file (Facts, Roster, Kit, other art). If you need a helper,
  make it `private` in your file.
- Every top-level name is `private` or starts with `crawl`. Never name anything `crawler…` (Star Clawds has locals
  with that name).
- Places: members you add to `extension Scenes` start with `crawl` too (`Scenes.crawlSeattle`,
  `Scenes.crawlSeattleLife`); each `Place` uses the `Location` constant already declared in CrawlRoster.swift, and has a
  still, a moving layer and the plan's tall-canvas extras for the screen saver. Big landmarks are drawn LARGE and in
  double units (see the phase 2 scenes), and must still fit the window strip (about 56 units above the ground).
- Clawd always has FOUR legs (x 19, 23, 31, 35). Never merge or drop legs; animals and creatures are Clawd in costume
  too (Odette's crab legs and Grull's horse body are drawn over the four).
- Everyone keeps the books' on-page name, exactly as the plan's table gives it. No narrators', actors' or real
  people's names.
- No em dashes anywhere (code, comments, strings). Use commas, colons or parentheses.
- Sprite canvas is 72x52. Outlines are cut at the frame edge: nothing may touch the canvas edge unless it's on
  purpose (shots, thrown things). Check with `build/preview edges <out.txt> <names...>` and fix anything flagged.
- Effects (magic, glows, shots, flames) must read on a DARK desktop: no dark-on-dark effects. See-through flames are
  never half-opaque at the frame edge.
- Lessons so far: a red or dark emblem centred just under Clawd's eyes reads as a mouth or moustache, so keep chest
  emblems at row 33 or below; dotted hair reads as a bun, draw hair as strands; props too small to read, white on
  white outlines fading, and busy clusters of tiny details (Ball of Swine, the Hoarder) are the weak spots of phase 2.
- Each character must be told apart at a glance by silhouette, colour pair and headgear, from each other and from
  look-alikes already drawn (the Sledge and Bomo, Mordecai's bird, Bautista's tiger). Weapon colours: the plan's
  table; no two characters in one group sharing a colour.
- Doc comment per character in the phase 1 and 2 voice: what they wear, colours, weapon, and what the signature does.
- Every character gets a signature move (Pose.signature 0...1 over `signature:` seconds) as the plan describes, and
  the plan's callout where one is listed.
- Agent-only small fry (and Garret) still get full art.

## Build and check (in your worktree)
- `zsh Tools/Preview/build.sh` (4 to 7 minutes when several helpers build at once; run it with a long timeout), then
  `build/preview cast <out.png> <names...>` for every pose, `build/preview edges <out.txt> <names...>`,
  `build/preview place <out.png> <placeKey>` for places. `build/preview` with no args prints usage. Names that clash
  with other universes need `crawl:` in front (`crawl:rory`, `crawl:samantha`); use the enum case names.
- `QUICK=1 Tools/CheckUniverse/check.sh DungeonCrawlerClawd` must stay clean apart from the expected "size" warning.
- Look at every render yourself (Read the PNG) and fix what doesn't read. Zoom in: crop and upscale with python PIL
  to check details. Iterate until each one clearly reads as the character at a glance.
- Save review renders to `~/Desktop/dungeon-crawler-clawd-phase-3/<your-file>/` (never into build/: build.sh wipes
  it): a cast sheet, and a zoomed idle portrait per character (or per place: the window strip and the screen saver
  frame).

## Finish
- Commit in your worktree: Conventional Commits, scope `crawl`, e.g. `feat(crawl): draw the rest of the crawlers
  (Tran, Li Jun ...)`, with a body saying what's in it. NEVER add Co-Authored-By or any Claude or AI attribution line.
- Report back: the commit hash and branch, the file, a one-line description per character or place, anything you
  were unsure of, and anything weak you'd flag for the polish pass. Keep the report short.
