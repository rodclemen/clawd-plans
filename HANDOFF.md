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

## clawd-clash
```sh
cd "<your code folder>/clawd-clash"
git fetch origin
git switch buffy          # Clawd Slayer phase 1 (23e3206) + promo pick page (2307bd0)
./build.sh                # builds, installs and launches
Tools/Preview/build.sh    # the Preview tool for character/place sheets
```
`CLAWD-SLAYER-PLAN.md` at the repo root is the working plan (same as `in-progress/buffy.md` here). Delete it before merging.

**Next:** phase 2, the core ensemble: the rest of the Scooby Gang, Faith, Kendra, Jenny, Angstel, Wesley, the
vampires and the Big Bads (~35 characters), plus 7 places (Bronze, cemetery, Revello, Magic Box, crypt, sunken
church, Hellmouth). New files go in `Sources/App/Universes/Slayer/Art/SlayerHeroes2…` and `Places/SlayerScenes2…`,
added to the arrays in `SlayerRoster.swift` and to the Preview batches.

**Promo:** the Pick-your-universe page is now the pop-art layout (a panel per universe, no Settings pop-up),
committed on `buffy` (2307bd0) and on `main` (90eecab, without the Slayer lines). The full re-render still waits for the LOTR universe. The Clawd Royale teaser still assumes
three universes (`royaleCollide`'s `from`/`meet`/`rest` arrays) and will crash until that's fixed. Build the promo
tool as `-o build/renderpromo` (the binary must be named `renderpromo`).

**Open question:** keep building Slayer the current way and port it later, or do the `universe-modules.md` refactor
first.

## Claude's memory
Claude Code keeps its memory per machine. To bring it over, copy `claude-memory/*.md` into
`~/.claude/projects/<the clawd-clash folder's path with every non-letter/digit replaced by ->/memory/`
(start Claude once in the clawd-clash folder first so the folder exists, then copy).
