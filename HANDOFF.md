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
