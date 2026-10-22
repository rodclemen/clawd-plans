# What changed in Clawd Clash 3.6.0 (2026-10-17) for anyone building a universe

Released as [v3.6.0](https://github.com/rodclemen/clawd-clash/releases/tag/v3.6.0). Branches started before it
(`buffy`, Henrik's `feature-burton`) should merge `main` and go through the points below before their PR.

- **Read the guide's new "Look and style" section** (`clawdify_guide.md`, copied here). It sets the house style in
  one place: Clawd in costume on four legs, flat pixel art lit from the front-left, no hand-drawn silhouette outline
  (the app adds it), bodies and props fully opaque, see-through only for glows and smoke and never half-opaque along
  an edge, and how places keep the crew readable.
- **The frame rule.** Solid art must stay at least a pixel inside the 72×52 frame in every pose at every moment, or
  its white outline is cut off. 50 characters broke it and were fixed in 3.6.0. Check yours with
  `build/preview edges out.txt "<Universe title>"` (80 moments of every state, 40 of every habit and signature move):
  everything it lists must be on purpose (shots, thrown things, exits, things coming from the sky). The engine now
  gives back hop and hover lift that would push a character onto the edge, so the tallest hop a little lower.
- **Pull requests from forks go through a guard** (`scripts/pr-guard.py`, see `CONTRIBUTING.md`). A universe's own
  folder is fine; registration files are read closely; build scripts, the hook, installers, dotfiles and instructions
  for AI assistants are refused. In universe code: no file, process, network or other-app APIs, only the drawing
  imports, every new top-level name prefixed with the universe's prefix (or `private`), extensions only on `Scenes`,
  `Location`, `Cast` and your own types. Run it on your branch first: `python3 scripts/pr-guard.py main <branch>`.
- **Speech:** a character's `callout` now shows as dark text on a cream rounded backing, so long lines read on any
  place. Keep them short and in character as before.
- **Thanks:** when a contributor's PR is merged, they're added to Settings → About's "Thanks to"
  (`OverlayController.collaborators`), with the universes they made.
- **The promo** shows every universe as a comic-book page and grows with the universe list, so a new universe gets
  its page there once it's released. Its 1080p render is capped under GitHub's 100 MB file limit.

# Picking up on another computer

Updated 2026-10-22: Stranger Clawds, phase 5 (the trips between places) done and pushed (3920bce); phase 6 next.

## clawd-clash
```sh
cd "<your code folder>/clawd-clash"
git fetch origin
git switch stranger-clawds   # phase 5 done (3920bce)
./build.sh                   # builds, installs and launches (wipes build/)
Tools/Preview/build.sh       # the Preview tool for character/place sheets
Tools/Transitions/build.sh   # the transitions renderer
```
The plan is `in-progress/stranger-clawds.md` here. Its note at the top says the folder flow (the universe-modules
refactor) replaces its old wiring section: the trips plug in through `HawkinsUniverse.transitions`.

**Phase 5, done** (all in `Sources/App/Universes/StrangerClawds/`): `HawkinsTrips.swift` (the ten kinds, timings,
owners, turf, the pick), `HawkinsLights.swift` (Joyce's lights at the end of every trip), and a file per trip:
Title, Flip, Gate, Walkie, Void, Storm, Clock, Natural20, Fireworks, InsertCoin (`Hawkins…Trip.swift`). The owner
OK'd the renders on 2026-10-22; the CHANGELOG's Stranger Clawds bullet describes all ten.

**Next: phase 6, the polish pass** (see the plan). Render review material outside `build/` (e.g.
`~/Desktop/hawkins-trips/`), since `./build.sh` wipes it. `check.sh`'s "hand-off scope" fails if the local `main`
is stale; compare with `origin/main`. The engine files it lists are this branch's own earlier phases.

**Rules for this universe:** the secret mechanic (the flip) never appears in public text: CHANGELOG, README, commit
messages. "The Flip" transition is a different thing and fine to name. No em dashes anywhere. No Co-Authored-By lines.

## Claude's memory
Claude Code keeps its memory per machine. To bring it over, copy `claude-memory/*.md` into
`~/.claude/projects/<the clawd-clash folder's path with every non-letter/digit replaced by ->/memory/`
(start Claude once in the clawd-clash folder first so the folder exists, then copy). `MEMORY.md` here merges both
machines' indexes, so it can replace the one there.
