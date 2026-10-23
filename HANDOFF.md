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

Updated 2026-10-23 (end of day, second machine): four fixes and a new menu item on top of Stranger Clawds, see
"Done 2026-10-23" below. Branch `stranger-clawds` at 025b485. What's left is under "Next" (the 2026-10-22 list still
stands; nothing from it was done yet).

## clawd-clash
```sh
cd "<your code folder>/clawd-clash"
git fetch origin
git switch stranger-clawds   # everything so far (025b485)
git pull
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

**Phase 6, done:** the kids stand shorter (`hawkinsKidDrop` in `HawkinsKit.swift`: the Party 2 rows, Erica, Derek
and Holly 3; never while sitting), with Eleven's and Will's powers, Lucas's slingshot and Mike's walkie moved down
with them; Yuri's greyer beard and bigger open jar; Barb's glasses push-up and glint; Robin's salute edged against her
cap; Benny's cream tin ceiling. The owner OK'd the before/after renders on 2026-10-22 (in `~/Desktop/hawkins-polish/`
on the first machine). The height change is subtle; raise `hawkinsKidDrop` if it should show more.

**Phase 7, done today (2026-10-22), all pushed:**
- The trailer, `Promo/HawkinsReel.swift` (storyboard OK'd): 49 s, the opening titles slowed right down, then the shared
  shots. Renders on the first machine: `~/Desktop/hawkins-promo/` (1080p and `720p/Stranger-Clawds.mp4`, 9.6 MB).
  Re-render anywhere: build RenderPromo (header of `Tools/RenderPromo/main.swift`), `REEL=hawkins <bin> video <dir>`
  and `REEL=hawkins <bin> 720p <dir>`, into a folder outside `build/`.
- README section, desktop strip, roster, places, `llms.txt`, the comic cover's panel (Eleven against Vecna), the
  module's `docs` line-up.
- **The showcase repo, https://github.com/rodclemen/stranger-clawds (public)**: README, CHANGELOG, llms.txt, LICENSE,
  the 1080p trailer and storyboard in `promo/`, and `docs/` (icon, bikes and Upside Down strips from
  `Promo/HawkinsShowcase.swift` via `build/rendershowcase docs hawkins`; the transitions sheet from
  `build/transitions <dir> hawkinsBasement hawkinsStarcourt`; the window shot cropped from the trailer's frame at
  39.2 s; the screen saver shot from `scripts/saveshot.swift` here, which runs the real saver view offscreen with sample
  sessions, because screen capture isn't permitted from Claude's shell: build it with the saver's swiftc line from
  `build.sh` plus that file). It says "comes with Clawd Clash 3.8.0 and later", so release before linking it widely.

**Also done today, on the same branch (engine changes, the owner asked for each):**
- **Trips cover the crew**, in every universe, window and screen saver: the trip (or Star Clawds' wipe) is drawn over
  the characters, who fade back in over the trip's last 12% (`ComicTransition.cover`). In the saver the cards, clock
  and place name stay on top (`Item.underTrip`, layer zPositions 0/1/2). The owner hasn't watched it in the app yet.
- **Screen saver privacy**: Settings → Screen Saver gets "Show the banner" and "Show the session cards"; the saver's
  Options sheet has the same two. The app's choice travels in the feed (`SaverFeed.Privacy`, with a timestamp); the
  Options write theirs to the saver's own options.json with a timestamp; the later one wins. Cards off: name tags show
  the character's name, not the project. The app's window always shows everything.
- **Location in Settings → General**, under Universe: the Location menu's choices (`locationChoices()`), one setting
  (`pickedLocation`), hidden in Clawd Royale.
- **Every pun says "clawd"** (owner's rule, in memory `clawd-not-claw`): the Democlawgon is the **Democlawdgon**, and
  26 names in the released universes got their "d" (list in CHANGELOG's Unreleased "Changed"; Draclawla is Clawdula,
  Deep Clawt is Deep Clawd, Captain Clawk is Captain Clawd, Ian Malclawm is Ian Malclawd). Only displayed names
  changed; code identifiers (`buffyClawmers`) kept, so no ids move. Rosters and desktop strips of those four universes
  re-rendered into `docs/`.
- The Democlawdgon's look: the owner tried a two-legged and an in-between version and chose the original, square,
  four-legged one. No change.

**Done 2026-10-23, on the same branch, all pushed (the owner asked for each; none of it tried in the app by
the owner yet):**
- **Full Screen in the menu bar menu** (`Sources/App/FullScreen.swift`, `openFullScreen` in `Overlay.swift`): the
  saver view itself in native macOS full screen on the display under the mouse, its own Space there. A click on it or
  Escape closes it; the other display keeps working. Path to it: an always-on-top window first did nothing (behind
  other windows), then worked once (fixed: `isShown` guard, `onClose` deferred), then missed the second monitor
  (NSWindow's `screen:` init parameter makes the rect screen-relative; dropped), then the owner didn't want it on every
  Space, hence native full screen. A pinned window and the desktop panel are on every Space and floated over it;
  removing `.fullScreenAuxiliary` didn't help, so they're ordered out on that display while it's open and come back on
  close. **Check:** open, swipe Spaces, work on the other display, close; the pinned window must not show over it and
  must come back after.
- **Status bubbles on tall characters** (`Cast.bubbleLift`): measured per character at rest; 135 of 986 had art
  within 3 rows of the bubble (the dinosaurs, Abominator, Galacticus, Smaug, the Tall Visitor...) and get it raised to
  the usual 7-row gap. **Check** a Jurassic Park dinosaur's bubble in the app.
- **Jurassic Park's gate trip** (`ClawdbergWipes.swift`): the place behind is drawn at full resolution (the window's
  list text was pixelated in a universe change), a dusk jungle (`jungle()`) frames the gates so the swap no longer
  shows around them, and the sign reads JURASSIC CLAWD. Render: `build/transitions <dir> <a Clawdberg place> ...`.
  The other nine Clawdberg trips still pixelate text in a universe change; the same fix would work if the owner wants.
- **Roald Doll Plass face lift** (`DoctorScenes2.swift`, `plassBuildings()`): same layout, bigger sun and reflection,
  fuller Millennium Centre and Pierhead, lamps on the rail. Before/after were in `~/Desktop/roald-doll-plass/` on the
  second machine.

**Next:**
0. **Try the 2026-10-23 changes above** in the app (the "Check" lines), fix what's off.
1. **Upload the trailer**: drag `720p/Stranger-Clawds.mp4` (not on the second machine; re-render it if the first
   machine's Desktop doesn't have it)
   into a GitHub issue comment on clawd-clash, copy the URL. Put it in clawd-clash's README video table (a ninth
   entry, starting a new row) and at the top of the showcase README (as clawd-slayer's has it), then push both.
2. **Try today's engine changes in the app**: a place change in the window and the saver (crew hidden, fading back),
   the two privacy toggles both in Settings and in System Settings' Options (reinstall the saver first), and
   Settings → General → Location.
3. **Release 3.8.0**: merge `stranger-clawds` into `main`, `NUMBERS` 9 from `reserved` to `shipped`, a 3.8.0 heading
   in the CHANGELOG over Unreleased (it now also lists Full Screen, the bubbles, the gates and the plass),
   `./release.sh 3.8.0`, push. A cask is optional (none decided; the manifest's
   `cask` line is empty, so none is written).
4. **The other showcase repos** (clawd-slayer, the-clawd-files, stevie-clawdberg, doctor-clawd) still use the old
   "claw" names in their READMEs, CHANGELOGs, llms.txt and pictures; update them after the release. Their trailers
   show some old names too (re-render if wanted).
5. Optional: `HawkinsFlipTrip.swift:45` takes ~5 s to type-check (check.sh warns); worth a look before the release
   build.

**Rules for this universe:** the secret mechanic (the flip) never appears in public text: CHANGELOG, README, commit
messages. "The Flip" transition is a different thing and fine to name. No em dashes anywhere. No Co-Authored-By lines.

## Claude's memory
Claude Code keeps its memory per machine. To bring it over, copy `claude-memory/*.md` into
`~/.claude/projects/<the clawd-clash folder's path with every non-letter/digit replaced by ->/memory/`
(start Claude once in the clawd-clash folder first so the folder exists, then copy). `MEMORY.md` here merges both
machines' indexes, so it can replace the one there.
