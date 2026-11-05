# Picking up on another computer

## Latest: 2026-11-05, Dungeon Crawler Clawd's polish pass

Everything is pushed. To pick up:
```sh
cd "<your code folder>/clawd-plans" && git pull
cd "<your code folder>/clawd-clash" && git fetch && git switch dungeon-crawler-clawd && git pull
Tools/Preview/build.sh
```
- **Dungeon Crawler Clawd:** phases 1 to 6 done on `dungeon-crawler-clawd`, full check clean. Next is your review: `review/dungeon-crawler-clawd/Polish/Needs your call/` here, 21 images each with a question. The plan's last Status section has everything else that's open.
- **Branch `fix-idle-session-records`** (from `main`, pushed, not merged): a session idle over 3 hours kept showing as disconnected, and could raise a false "isn't reporting" banner. Installed on the work machine only, built from `main`, so that app doesn't have the universe. To merge once it has proved itself: leave a session idle for over 3 hours, restart the app, and it should stay idle and asleep with no banner. Ships as a patch release.
- **Open question:** the app drops a subagent from the stage while it waits on its own background work, because that looks like it finished. Check what `SubagentStop` carries, or add it to clawd-clash issue #7. That issue could also link openai/codex#51272.
- **Memory:** copy `claude-memory/dungeon-crawler-clawd.md` over as described below.

## Earlier: 2026-10-25

Written 2026-10-25, after the 4.1.0 release. Everything is pushed except one branch, `background-jobs`.

## Where things stand
- **Clawd Clash 4.1.0 is out** (notarized, GitHub release, Homebrew cask): Superclawdtural, number 10, plus the
  grip magic, habits that carry the name tag, rides at their own height, the ticker's agent lines and the promo fixes
  (every universe on the comic page, Clawd Royale's smacks, the CLAWD CLASH thumbnail). `superclawdtural` is merged
  into `main`, and NUMBERS has 10 as `shipped`. The showcase repo rodclemen/superclawdtural is public; its social
  preview still has to be uploaded by hand (Settings → General → Social preview).
- **Not pushed: branch `background-jobs`** (01f06c8, on top of 4.1.0, builds): a new "waiting on a job" state, a
  teal hourglass, for an AI that ended its turn on a job it left running in the background (Claude Code, Qwen Code,
  Copilot CLI, Gemini CLI with its wake-up settings on). Next release, 4.1.1. Codex and pi are open in clawd-clash
  issue #7.
- **Version rule:** a universe raises the middle number, anything else the last. `scripts/next-version.sh` reads it
  from the commits, and `./release.sh` with no version uses it.

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
