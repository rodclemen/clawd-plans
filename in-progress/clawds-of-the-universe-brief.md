# Brief: Clawds of the Universe, phase 3 art (shared by all helpers)

You are drawing part of phase 3 of a new universe in Clawd Clash, a macOS app that shows AI coding sessions as
pixel-art characters ("Clawds": a blocky orange critter on four legs, in costume) fighting on a desktop strip and a
full-screen screen saver. The universe is a He-Man / She-Ra parody, "Clawds of the Universe", Swift, folder
`Sources/App/Universes/Eternia/`, prefix `Eternia`. You work in your own git worktree on a branch made from
`clawds-of-the-universe` (HEAD: 0a43403, the phase 3 stand-ins). The enum cases, homes and wiring already exist; you only fill in ONE file.

## Read first
- `clawdify_guide.md` sections "Look and style" (Characters, Places), "House style", "Verification, every phase".
- The plan: `clawds-of-the-universe.md` (next to this brief, in clawd-plans): "Telling the barbarians apart", "Magic, one look per
  caster", your rows of the Heroes/Villains tables or the Places table, and the callouts list.
- Phases 1 and 2, the bar to match (same style, same comment voice). Phase 2 is the whole core ensemble: Art/EterniaHeroes2-4.swift, Art/EterniaVillains2-3.swift, Places/EterniaScenes2-3.swift. Read the files nearest your group (rebels for rebels, the Horde for the Horde, the Evil Warriors for the Evil Warriors) and match them.
- The plan's "Weak spots so far (phase 2)" list: those are the mistakes not to repeat (white on white outlines fading, props too small to read, emblems that read as faces, stair-stepped rears, plain-stick props).
- Phase 1:
  `Art/EterniaHeroes1.swift` (He-Clawd, Orkko), `Art/EterniaVillains1.swift` (Skeleclawd), `EterniaKit.swift`
  (shared helpers: `eterniaHand`, `eterniaReach`, `eterniaBar`, `eterniaSword`, `eterniaFur`), `EterniaHem.swift`,
  `Places/EterniaScenes1.swift` (Castle Greyskull, just redrawn: the owner said the first version "wasn't good enough",
  so this redraw is the minimum bar for places).
- `Sources/App/Persona.swift` (Persona fields; argument order matters: name, weapon, motion, shot, magic, armoured,
  canSit, muzzle, pivot, handGun, bulk, headTop, signature, callout, fidgets, ..., draw), `Sources/App/Pose.swift`,
  and the shared body helpers (`drawBody`, `drawLegs`, `drawBoots`, `drawHood`, `Look` ...; grep for them). Look at a
  couple of other universes' art files for how fly/hover/bulk/blaster/thrown/ice characters are done.

## Hard rules (the owner is strict about these)
- Write ONLY your assigned file. Do not touch any other file (Facts, Roster, Kit, other art). If you truly need a
  shared helper, make it `private` in your file.
- Every top-level name is `private` or starts with `eternia`.
- Places: members you add to `extension Scenes` start with `eternia` too (`Scenes.eterniaAvion`, `Scenes.eterniaAvionLife`), the `Place` uses the `Location` constant you are given (already declared in EterniaRoster.swift), and each place has a still, a moving layer and the plan's tall-canvas extras for the screen saver. Castle Greyskull's redraw (blown-up landmark, `q` scale) and phase 2's scenes are the bar.
- Clawd always has FOUR legs (x 19, 23, 31, 35). Never merge or drop legs; animals are Clawd in costume too.
- Pun names say "clawd", never a bare "claw" (names are given below; use them exactly).
- No em dashes anywhere (code, comments, strings). Use commas, colons or parentheses.
- Sprite canvas is 72x52. Outlines are cut at the frame edge: nothing may touch the canvas edge. Check with
  `build/preview edges <out.png> <names...>` and fix anything flagged.
- Effects (magic, glows, shots, clouds) must read on a DARK desktop: no dark-on-dark effects.
- Lessons from phase 1: a red/dark emblem centred just under Clawd's eyes reads as a mouth or moustache, so keep
  chest emblems on a plate at row 33 or below; dotted hair reads as a bun, draw hair as strands; small grey squares
  on the shoulders read as cheeks.
- Each character must be told apart at a glance by colour pair and headgear (see "Telling the barbarians apart"),
  and from the other universes' look-alikes listed there. Magic colours: use the plan's table.
- Doc comment per character in the phase 1 voice: what they wear, colours, weapon, and what the signature does.
- Every character gets a signature move (Pose.signature 0...1 over `signature:` seconds) as the plan describes, and
  the plan's callout where one is listed.
- Agent-only small fry still get full art.

## Build and check (in your worktree)
- `zsh Tools/Preview/build.sh` (about 2 minutes; run it in the background or with a long timeout), then
  `build/preview cast <out.png> <names...>` for every pose, `build/preview edges ...`, `build/preview place <out.png> <placeKey>`
  for places. `build/preview` with no args prints usage; `build/preview list` style help exists, read
  `Tools/Preview/main.swift` header.
- `QUICK=1 Tools/CheckUniverse/check.sh Eternia` must stay clean apart from the expected "size" warning.
- Look at every render yourself (Read the PNG) and fix what doesn't read. Zoom in: crop and upscale with python PIL
  to check details. Iterate until each one clearly reads as the character at a glance.
- Save review renders to `~/Desktop/clawds-of-the-universe/phase3/<your-group>/` (never into build/: build.sh wipes it):
  a cast sheet, and a zoomed idle portrait per character (or per place: the window strip and the screen saver frame).

## Finish
- Commit in your worktree: conventional commit, scope `eternia`, e.g. `feat(eternia): draw the Evil Warriors (Evil-Lynn ...)`,
  with a body saying what's in it. NEVER add Co-Authored-By or any Claude/AI attribution line.
- Report back: the commit hash and branch, the file, a one-line description per character/place, anything you
  were unsure of, and anything weak you'd flag for the polish pass. Keep the report short.
