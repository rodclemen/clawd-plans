# Picking up on another computer

Written 2026-10-23, after the 4.0.0 release. Nothing is left open: the showcase repos' "clawd" names are done too, and
everything is pushed.

## Where things stand
- **Clawd Clash 4.0.0 is out** (notarized, GitHub release, Homebrew cask): Stranger Clawds, plus Full Screen, the
  bubbles on tall characters, the park gates, Roald Doll Plass, the renames below. `stranger-clawds` is merged into
  `main`, and NUMBERS has 9 as `shipped`.
- **On `main` since, for the next release (4.0.1):** the screen saver's ticker says when it was an agent
  ("Dustin, Eleven's agent, finished and left: ..."), and the guide's line on counting version numbers.
- **New version rule:** a universe raises the first number (5.0.0), a feature the middle one (4.1.0), anything else
  the last one (4.0.1, and on past 4.0.9 to 4.0.10). Don't pick it: `scripts/next-version.sh` reads it from the
  commits, and `./release.sh` with no version uses it. So `feat:` only for real features.
- **For trying trips:** Shift-double-click the window's scene (off the crew) goes to the next place now; in Full
  Screen, a Shift-click does the same for the screen saver's view. The transitions tool's `ART=1` renders trips the
  way the window draws them (art-size pictures).

## clawd-clash
```sh
cd "<your code folder>/clawd-clash"
git fetch origin
git switch main
git pull
./build.sh                   # builds, installs and launches (wipes build/)
```

## Done: the "clawd" names in the showcase repos

clawd-slayer, the-clawd-files, stevie-clawdberg and doctor-clawd now use the names 4.0.0 gave the "claw" puns (Buffy
Clawdmers, Clawdula, Deep Clawd, Captain Clawd, Susan Foreclawd and the rest), pushed 2026-10-23:
- README, CHANGELOG (a "Clawd Clash 4.0.0" entry in each) and llms.txt, alt texts included.
- Pictures rendered again: the rosters, desktops, social previews and locations sheets that had changed, the Slayer
  locations sheet with the pixel Sunnydale sign, the Stevie transitions sheet with the JURASSIC CLAWD gates, and the
  Tabula Rasa and DeLorean strips.
- **Left as they are, on purpose:** three app screenshots still show old names (clawd-slayer's
  `window-sunnydale-high-library.png` and `screensaver-clawd-slayer.png`, stevie-clawdberg's `window-jolly-roger.png`),
  and the trailers in `promo/`. Don't redo them.

## Claude's memory
Claude Code keeps its memory per machine. To bring it over, copy `claude-memory/*.md` into
`~/.claude/projects/<the clawd-clash folder's path with every non-letter/digit replaced by ->/memory/`
(start Claude once in the clawd-clash folder first so the folder exists, then copy). `MEMORY.md` here merges both
machines' indexes, so it can replace the one there. Updated today: `version-rule`, `stranger-clawds`,
`github-video-uploads`.
