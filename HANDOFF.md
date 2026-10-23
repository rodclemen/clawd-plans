# Picking up on another computer

Written 2026-10-23, after the 4.0.0 release. One job is left: the four older showcase repos still use the old "claw"
names. Everything else is done and pushed.

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

## The job: the "clawd" names in the showcase repos

Every pun says "clawd" (memory `clawd-not-claw`), and 4.0.0 renamed 27 characters in the app. Their showcase repos
still show the old names in text and pictures:
[clawd-slayer](https://github.com/rodclemen/clawd-slayer),
[the-clawd-files](https://github.com/rodclemen/the-clawd-files),
[stevie-clawdberg](https://github.com/rodclemen/stevie-clawdberg) and
[doctor-clawd](https://github.com/rodclemen/doctor-clawd).
(stranger-clawds is already right.)

**The names, old → new:**
- Clawd Slayer: Buffy Clawmers → Buffy Clawdmers, Dawn Clawmers → Dawn Clawdmers, Joyce Clawmers → Joyce Clawdmers,
  Willow Rosenclaw → Willow Rosenclawd, Tara Maclaw → Tara Maclawd, Jenny Clawlendar → Jenny Clawdlendar,
  Kate Lockclaw → Kate Lockclawd, Miss Kitty Fanclawstico → Miss Kitty Fanclawdstico, Draclawla → Clawdula,
  Mayor Wilclaws → Mayor Wilclawds, Glorificlaws → Glorificlawds
- The Clawd Files: Deep Clawt → Deep Clawd, Clyde Bruckclaw → Clyde Bruckclawd, Leyla Harriclaw → Leyla Harriclawd,
  Frank Blackclaw → Frank Blackclawd, Tad O'Clawley → Tad O'Clawdley, Dr. Blockclaw → Dr. Blockclawd,
  Alex Clawcek → Alex Clawdcek, Diana Fowlclaw → Diana Fowlclawd, Eugene Clawms → Eugene Clawdms
- Stevie Clawdberg: Captain Clawk → Captain Clawd, Ian Malclawm → Ian Malclawd, Clara Clawton → Clara Clawdton,
  Dr. Clawtheter → Dr. Clawdtheter, Murray Futterclaw → Murray Futterclawd, Mutt Willclaws → Mutt Willclawds
- Doctor Clawd: Susan Foreclaw → Susan Foreclawd

(From clawd-clash commit 0493913. Only displayed names changed; code identifiers like `buffyClawmers` stay.)

**In each repo:**
1. **Text:** `README.md`, `CHANGELOG.md` and `llms.txt`, including picture alt texts. A plain find and replace of
   the list works, but read each hit: possessives ("Buffy Clawmers'") and names inside longer phrases.
2. **Pictures in `docs/`:** the roster, desktop, locations and social preview have the same file names in
   clawd-clash's `docs/`, already re-rendered with the new names in 4.0.0; copy those four over. Two need a fresh
   render first, because 4.0.0 also redrew a sign in them:
   - `locations-clawd-slayer.png`: the Welcome to Sunnydale sign is pixel art now. Re-render with `Tools/RenderDocs`
     in clawd-clash, then copy.
   - `transitions-stevie-clawdberg.png` (optional): the park gates' sign is in a pixel font now. Re-render with
     `build/transitions <dir> hillValley1955 moonHill` (the sheet is `transitions.png`).
   Other pictures (window shots, the vehicle and move strips) show no names, or names too small to matter; look
   at them, but leave them unless a name reads.
3. **A CHANGELOG line** in each showcase's own CHANGELOG under a "Clawd Clash 4.0.0" heading: the names that
   got their "d".
4. **The trailers** (`promo/`) show some old names. Re-rendering is optional; if you do, the 720p copy needs a new
   upload (memory `github-video-uploads`: a comment on closed issue #4), and the README links change.

Commit with `docs:` (they're the showcase repos, no release follows). No em dashes, no Co-Authored-By lines.

## Claude's memory
Claude Code keeps its memory per machine. To bring it over, copy `claude-memory/*.md` into
`~/.claude/projects/<the clawd-clash folder's path with every non-letter/digit replaced by ->/memory/`
(start Claude once in the clawd-clash folder first so the folder exists, then copy). `MEMORY.md` here merges both
machines' indexes, so it can replace the one there. Updated today: `version-rule`, `stranger-clawds`,
`github-video-uploads`.
