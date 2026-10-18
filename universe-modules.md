# Plan: universes as modules (one folder each)

> **Status, 18 October 2026.** Started on branch `universe-modules` in clawd-clash, off `main` after 3.7.0. Clawd Slayer was built the old way and released as universe 7, so it's the eighth universe to port in phase 2 (everywhere below, "the eight" are numbers 0–7). The open questions are settled with the recommended answers: numbers are handed out in `NUMBERS` before work starts; the manifest is a plain `universe.conf`; Clawd Royale sessions from a removed universe keep their characters until they end; the owner's curated pictures keep naming universes by hand; only the three original universes have casks (`cask` stays empty for new ones). Phase 8 is now "the next new universe is the first built from the template". **Done so far:** phase 0 (`Tools/Baseline`, `build/preview ids`), phase 1, phase 2 (every per-universe case in the core is a `UniverseModule` member or facts value; ride drawings, drills, HEM's costumes, quirks, shoot-outs, compaction looks in their folders), and the `Universe` struct (moved after phase 2, once the switches were gone). Baselines live in `.baseline/` (git-ignored), since `build.sh` deletes `build/`.

## Context

### The problem

Universes are going to be added by other people, not just the owner. Today, adding one means editing many shared files that the owner also keeps changing. Every hand-off turns into a merge fight.

You can see it happening right now. Clawd Slayer's skeleton (branch `buffy`, committed there as `23e3206`) already touches **9 shared files with 52 changed lines**: `Universe.swift`, `Theme.swift`, `Locations.swift`, `Drills.swift`, `Overlay.swift`, `Hem.swift`, `ComicTransition.swift`, `SaverView.swift` and `Tools/Preview/main.swift`. That's before a single transition, ride, trailer or docs picture. Stevie Clawdberg, finished, names itself in 14 shared files outside its own folder (about 120 lines), plus its trailer inside `RenderPromo`.

### The goal

Make adding a universe a matter of **adding one folder**:
- A contributor starts from a **template**: a working mini-universe with every rule written next to the code it applies to. It says how things work and what the engine lets you use.
- When they're finished, they hand off **only the folder**. Nothing else in the repo needs to change.
- Users can **turn universes on and off** in Settings.
- **The template is never shown in the app.** Not by accident, not in a release, not in Clawd Royale, not anywhere.

### Constraints

- **Ids are forever.** A character's id is `universe number × 1000 + local id`. It's saved in `~/.claude/clawd-clash/state.json`, in the screen-saver feed, and in each AI's running session. The eight existing numbers (0–7) and every saved id must stay exactly the same. That isn't up for discussion.
- **One signed app.** Universes stay compiled into the one notarised app. They are source-level modules, **not runtime plugins**. Plugins were looked at and turned down:
  - Swift has no stable ABI for this kind of thing between separately built pieces.
  - Every plugin would need its own signing and notarisation.
  - The screen saver runs sandboxed inside macOS's screen-saver host, which won't load our own extra code.
  - There's nothing to save. Memory isn't a problem (see below).
- **No memory cost worth worrying about.** Measured today (16 October, six universes): the app binary is 20.4 MB, the screen saver carries its own copy at 18.4 MB, and the hook is 1.1 MB. The running app sits at about 25–33 MB of memory. Each universe adds about 2–3 MB of binary per copy, and only the pictures on screen get drawn. Loading universes lazily would save almost nothing.
- **Each step leaves the app identical for users** until the Universes checkboxes arrive in Settings. "Identical" is checked by comparing pictures pixel for pixel, and the id tables entry for entry (see Verification).

### What the code looks like today

- Each universe already has a folder, `Sources/App/Universes/<Name>/` (Swift lines: Star Clawds 5.9k, Marvelous 25.3k, Detective 31.5k, Doctor 10.6k, Clawd Files 10.2k, Clawdberg 14.9k, Clawd of the Rings 23.9k). Each one also has a roster file that builds a `Theme`.
- But the core asks about universes in **`switch` statements and `if universe == .x` checks** spread across the code: `Universe.swift`, `Theme.of`, the places merge, HEM's costume, `ComicTransition`, rides, drills, poses, habits, the overlay's special cases, the screen saver, the hook's compaction handling, and every tool.
- The build scripts compile `Sources/App/Universes/**/*.swift`. That pattern would also compile a template folder, so it has to go before any template exists (see "Never shown in the app").
- **The hook compiles only `Sources/Shared/`.** It needs to know each universe's cast sizes, agent-only characters, rivals, Claude's side and compaction lists, but it can't see `Sources/App`. This shapes the design: each universe needs a small part the hook can compile too.

---

## The design

### One universe = one folder

```
Sources/App/Universes/<Name>/
  universe.conf              the manifest: number, key, title, file prefix, reel, cask (read by the build scripts)
  <Prefix>Facts.swift        plain data, no drawing: the hero and villain enums, agent-only, rivals, Claude's side,
                             compaction. Compiled into the hook as well as the app and the saver.
  <Prefix>Universe.swift     the entry: `struct <Prefix>Universe: UniverseModule`. Everything the core asks.
  <Prefix>Roster.swift       personas, homes, nemeses, who rides what, the Theme, the place keys
  <Prefix>Hem.swift          HEM's costume here
  <Prefix>Icon.swift         the menu bar icon
  <Prefix>Wipes.swift        the transitions
  <Prefix>Rides.swift, <Prefix>Drills.swift, mechanics…   as needed
  Art/<Prefix>Heroes1…N.swift, Art/<Prefix>Villains1…N.swift
  Places/<Prefix>Scenes1…N.swift
  Promo/<Prefix>Reel.swift   the trailer, compiled only into RenderPromo
  Promo/<Prefix>Showcase.swift   the showcase pictures, compiled only into RenderShowcase (optional)
```

The manifest is plain `key = value` lines, so the shell scripts can read it without parsing Swift:

```
number = 5
key    = clawdberg
title  = Stevie Clawdberg
prefix = Clawdberg
entry  = ClawdbergUniverse
reel   = clawdberg
cask   =                    # empty: no Homebrew cask of its own (the owner decides, see release.sh)
```

`HEM.swift`, `ComicTransition.swift` and `ShootsFirst.swift` move out of `Universes/` into `Sources/App/`. They're engine code, and `Universes/` should hold nothing but universe folders.

### Two protocols: facts (for the hook) and the module (for the app)

The facts are plain numbers that everything needs: the app, the saver and the hook. The module is everything about drawing. Splitting them means the hook stays small and never compiles a sprite.

```swift
// Sources/Shared/UniverseFacts.swift: compiled into the app, the hook and the saver.

/// What every part of Clawd Clash needs to know about a universe: plain numbers, no drawing.
/// Local ids: villains 0..<100, heroes 100… (the universe's number × 1000 is added for you).
struct UniverseFacts {
    let villainCount: Int          // VillainEnum.allCases.count, never typed by hand
    let heroCount: Int             // HEM included, always last
    var agentOnly: Set<Int> = []   // small fry that only turn up as agents
    var claudeSide: Bool? = false  // false: Claude plays the heroes; nil: whoever came first (Star Clawds)
    var rivals: Set<Int> = []      // never lead two sessions back to back (Vader and Kylo)
    var compaction: Compaction? = nil
}

/// What happens to a session's leader when its context is compacted (`StatusStore`'s PreCompact).
enum Compaction {
    case regenerate(order: [Int])  // Doctor Clawd: the next face in the list, same session
    case away(who: Set<Int>)       // The Clawd Files, Stevie Clawdberg: gone for a moment, back the same
}

protocol UniverseFactsProvider { static var facts: UniverseFacts { get } }
```

```swift
// Sources/App/UniverseModule.swift

/// One universe, as the app sees it. Each folder has exactly one type conforming to this, named in its
/// universe.conf. Members without a default must be written; the rest have sensible defaults.
protocol UniverseModule {
    // Must be written
    var theme: Theme { get }                       // cast, places in order, homes, nemeses, rides, menu icon, legend
    var places: [Location: Place] { get }          // every place's drawing
    var hem: HemCostume { get }                    // HEM's hat, coat, legs and prop here
    var preview: PreviewInfo { get }               // Preview's batch names and case names
    var docs: DocsInfo { get }                     // desktop line-up, social preview title and groups

    // Have defaults
    var transitions: TransitionSet? { get }        // nil: plain edge and clock wipes (Star Clawds)
    var placeCaption: PlaceCaption? { get }        // The Clawd Files' typed place names
    var drills: [Cast: BespokeDrill] { get }       // characters' own practice sets
    var meditation: Meditation { get }             // who floats cross-legged (.never, .casters, .castersAndSabers)
    var poseStyle: PoseStyle { get }               // .modern; .classic is Clawd Wars' guns (Star Clawds only)
    var moonwalkers: Set<Cast> { get }             // the moonwalk habit
    var quirks: [StageQuirk] { get }               // the Weeping Angle, Captain Clawk's flinch… (see Engine toolkit)
    var shootOuts: [ShootOut] { get }              // Han and Greedo, Indy and the Cairo Swordsman
    var compactionEffect: CompactionEffect? { get } // what a compaction looks like (needs facts.compaction)
    var swingLine: Px? { get }                     // the web line's colour (Detective Clawds' grey)
    var playgroundPrompts: [String] { get }        // five sample prompts for the Playground's cards
    var isTemplate: Bool { get }                   // only the template says true (see "Never shown in the app")
}
```

The core then asks one question everywhere: `Universe.module(u)` (or `u.module`). Every `switch` on `Universe` goes away.

**Transitions** get a protocol instead of an enum with a case per universe:

```swift
/// One trip between two places: Marvel's comic panels, the TARDIS's vortex, The Clawd Files' black oil…
protocol Trip {
    var duration: Double { get }
    var kindName: String { get }                   // for sheets, and so the next trip is a different kind
    func draw(_ ctx: CGContext, old: CGImage, new: CGImage, k: Double, in r: CGRect)
}

struct TransitionSet {
    /// The trip to `to`. `last` is the previous trip if it was in this universe, so it can pick a different kind.
    let pick: (_ last: Trip?, _ cast: [Cast], _ from: Location?, _ to: Location) -> Trip
    /// One of every kind, from `from` to `to`, for Tools/Transitions' sheets.
    let every: (_ from: Location, _ to: Location) -> [Trip]
}

/// Shared by the window and the screen saver. Replaces the six-case enum.
struct ComicTransition { let universe: Universe; let trip: Trip }
```

`ComicTransition.pick` becomes three lines: find the place's universe, pass `last?.trip` only if `last?.universe` matches, and return nil when `transitions` is nil.

**Rides** become a struct instead of a closed enum (`Ride` is never saved, so this is safe):

```swift
struct Ride: Hashable {
    enum Arrival { case flies, drives, materialises }
    let key: String                                // Hashable by key
    var arrival: Arrival = .flies                  // the TARDIS materialises; the sedan, DeLorean and jeep drive
    var canvasHeight = Ride.height                 // taller for something that stands (the TARDIS: 36)
    var boardingOffset: CGFloat = 14               // how far left of centre people walk to board
    let draw: (PixelCanvas, _ ramp: Double, _ lit: Bool, _ gear: Bool) -> Void
}
```

Each universe's rides move into its folder: the Falcon to Star Clawds; the Quinjet and Milano to Marvelous; the Javelin and Batwing to Detective; the TARDIS to Doctor; the Great Eagle to Clawd of the Rings. The shared hull helpers (`profile`, `hull`, `drawRamp`, `drawGear`) stay in `Rides.swift` as the ride kit.

**HEM's costume** is the one thing every universe has to provide, and today it's five `switch`es and a dozen `u == .x` checks in `Hem.swift`:

```swift
/// HEM in this universe. His face, buns, body and fist-shaking signature are the engine's (Hem.swift);
/// the costume is yours.
struct HemCostume {
    let persona: (_ draw: @escaping (PixelCanvas, Pose) -> Void) -> Persona  // weapon, shot or magic, muzzle, pivot, headTop
    let legs: (PixelCanvas, Pose) -> Void          // before the breath: trousers, shoes, a robe's hem
    let top: (main: Px, shade: Px, arm: Px, armRight: Px)
    let chest: (PixelCanvas, Pose) -> Void         // what shows over the body: a shirt, a lanyard, a bow tie
    var headwear: ((PixelCanvas, Pose) -> Void)? = nil  // the fez, the helmet, the fedora, Harlee's heart
    var hair: HemHair = .plain                     // .dyed(pink, blue) for Detective Clawds
    let prop: (PixelCanvas, Pose, _ out: Bool, _ lift: Int) -> Void  // the blaster, the shield, the sonic, the whip
}
```

This also breaks two hidden links between universes: HEM's legs currently borrow `drawDressShoes` from The Clawd Files' art and `cbBoots`/`cbFedora` from Stevie Clawdberg's kit. Each costume calls its own universe's helpers, from inside its own folder.

### `Universe` stays almost the same to use

`Universe` changes from an `enum` to a small struct that behaves the same way, so most call sites don't change:

```swift
struct Universe: Hashable, Comparable, CaseIterable, Codable, RawRepresentable {
    let rawValue: Int                               // the permanent number
    init?(rawValue: Int)                            // nil for a number that isn't registered, as before
    init?(key: String)
    var key: String, title: String, base: Int       // base = rawValue * 1000, exactly as today
    var facts: UniverseFacts                        // villainCount, heroCount… read through from here
    static var allCases: [Universe]                 // every registered universe, in number order
    static var fallback: Universe                   // the lowest registered number: Star Clawds (0), as `?? .starWars` was
}
```

- `.starWars`, `.marvel`, `.dc`, `.doctor`, `.clawdFiles`, `.clawdberg` and `.middleEarth` still exist as `static let`s, generated from the manifests. Code inside a universe's folder keeps writing `Cast(universe: .clawdberg, …)`. Code in the core never names one (a check enforces this, see check-universe).
- `villainCount`, `heroCount`, `agentOnly`, `rivals`, `claudeSide`, `hem`, `isHem`, `darkCast`, `lightCast`, `adopt` and `of(_:)` keep their names and give exactly the same results. They read from `facts` and add `base`, where today they `switch`.
- `abductees` and `regenerations` become one `compaction` read by `StatusStore`. The global ids are the same.
- **It encodes as a single `Int`**, the same as the enum did, so anything that ever encodes a `Universe` stays byte for byte the same.
- **Number order is kept everywhere it matters:** the Settings menu, `Location.everywhere`, Clawd Royale and, most importantly, `magicVariants`. That one numbers every magic user's look *in order through every universe*. A new universe, with a higher number, only ever adds to the end, so nobody else's lightning changes.
- **Counts come from the enums.** Today `villainCount`/`heroCount` are typed by hand in `Universe.swift`, with an `assert` in `Overlay.swift` to catch a mismatch. Once the enums live in `<Prefix>Facts.swift`, the counts are `allCases.count`, and the mismatch can't happen. The enum cases are cut and pasted as they are, in the same order, so every id stays the same.

### The registry, generated from the folders

A new universe should need **no shared edits**, so the list of universes is generated at build time and never committed:

- **`Tools/universes.sh`**, sourced by `build.sh`, every `Tools/*/build.sh`, and the build commands written in the RenderPromo, RenderDocs, RenderShowcase, MakeSocial and MakeIcon headers. It:
  1. reads every `Sources/App/Universes/*/universe.conf`, **skipping folders whose names start with `_`** (unless `TEMPLATE=1`);
  2. checks each one against `NUMBERS` (below), and stops with a clear message if anything's off;
  3. writes `build/gen/UniverseList.swift` (for Shared: the `Universe` constants, keys, titles and `allCases`, and the facts list for the hook);
  4. writes `build/gen/UniverseModules.swift` (for the App: `let registeredModules: [Universe: UniverseModule] = [.starWars: StarClawdsUniverse(), …]`);
  5. sets source lists for the scripts to use instead of the `**` globs: `UNIVERSE_FACTS` (just the `*Facts.swift` files, for the hook), `UNIVERSE_APP` (everything in the registered folders except `Promo/`) and `UNIVERSE_PROMO`;
  6. writes `build/gen/universes.tsv` (number, key, title, folder, prefix, reel, cask) for `release.sh`.
- `build/` is already git-ignored, so the generated files never show up in a diff.
- **Fallback, if generation turns out to be a nuisance:** one hand-edited `Sources/App/Universes/Registry.swift` with a line per universe. That's one shared line per hand-off. It's still far better than today, but it can conflict, so generation is the recommendation.
- An editor's Swift tooling won't see `build/gen/` unless you build once first. That's a small price.

### The permanent number: the only shared thing

The number is the one thing two contributors could clash over, because it decides every id. So it's handed out, not picked:

```
# Sources/App/Universes/NUMBERS: the owner's list. One line per universe, ever. Never reuse a number.
# number  key         folder            status
0         starWars    StarClawds        shipped
1         marvel      MarvelousClawds   shipped
2         dc          DetectiveClawds   shipped
3         doctor      DoctorClawd       shipped
4         clawdFiles  ClawdFiles        shipped
5         clawdberg   StevieClawdberg   shipped
6         middleEarth ClawdOfTheRings   shipped
7         slayer      ClawdSlayer       active
999       template    _Template         template
```

- **Only the owner edits `NUMBERS`.** They add a `reserved` line when someone starts a universe, and change it to `shipped` at the release that first carries it. It's a one-line commit on `main` before the work starts, so it never conflicts with anyone's hand-off.
- `universes.sh` refuses to build if:
  - a folder's number, key or folder name doesn't match its line;
  - two folders claim the same number or key;
  - a `shipped` line has no folder (a universe can't quietly disappear and leave saved ids pointing at nothing);
  - a number is 900 or above outside a `TEMPLATE=1` build (that range is kept for the template).
- **How 0–7 stay the same:** the existing eight get exactly their current numbers and keys in `NUMBERS` and in their manifests. `base` is still `number × 1000`. The enums are moved but not reordered. Verification dumps every id, name, place key and magic variant before and after, and the two lists must be identical.

---

## The inventory: every place that names a universe outside its own folder

Counted on `main` at `e6f639c`; the line numbers below were checked against `main` at `d270b63` on 2026-10-17 (they drift, so treat them as a guide), and the counts in this paragraph are still `e6f639c`'s. A broad search finds **658 lines in 24 shared files** that mention a specific universe, its types, rides, reels or places. About 20 of those files make real decisions; the rest are comments. On top of those lines, whole blocks of one universe's code live in shared files: about 3,500 lines of trailers in `RenderPromo`, 450 lines of showcases, 270 lines of drills, 280 lines of rides, 150 lines of HEM costumes, and 100 lines of overlay special cases.

### Sources

| File:lines | What it decides | Where it goes |
|---|---|---|
| `Shared/Universe.swift:8–15` | the cases and their numbers | the manifests + `NUMBERS`; generated constants |
| `Shared/Universe.swift:17–30` | `key`, `title` | the manifest |
| `Shared/Universe.swift:33–40` | `villainCount`, `heroCount` | `facts`, from `allCases.count` |
| `Shared/Universe.swift:50–61` | `agentOnly` | `facts.agentOnly` |
| `Shared/Universe.swift:65–68` | `claudeSide`, `rivals` (Star Wars only) | `facts.claudeSide`, `facts.rivals` |
| `Shared/Universe.swift:90–102` | `abductees` (Files, Clawdberg), `regenerations` (Doctor) | `facts.compaction` |
| `Shared/Universe.swift:70–83` | `guises` and `homebound` (Clawd of the Rings only, new since `e6f639c`) | not in the design yet |
| `Shared/Universe.swift:104–110` | `isReleased` (true for every universe today) and `Universe.offered`, which Settings, Random, Clawd Royale and the saver already read | not in the design yet; the removed list would sit beside it |
| `Shared/StatusStore.swift:336–350` | PreCompact: abduct or regenerate | stays, reads `facts.compaction` (same logic, same results) |
| `Shared/StatusStore.swift:70`, `SaverFeed.swift:11` | `?? .starWars`, the saver's choice keys in comments | `Universe.fallback`; comments say "a universe key" |
| `App/Theme.swift:40–50` | `Theme.of` switch | `u.module.theme` |
| `App/Theme.swift:89–90` | the `Ride` enum, 14 cases from 6 universes | `Ride` struct; each ride in its universe's folder |
| `App/Locations.swift:22, 29` | which universe a place is in; every place | a dictionary built once from the registry (faster too) |
| `App/Locations.swift:70–72` | merging eight places dictionaries | merged from `module.places`; **a duplicate key becomes an error** (today `merging { a, _ in a }` silently drops one) |
| `App/Universes/Hem.swift:13–34` | HEM's persona per universe | `module.hem.persona` |
| `Hem.swift:62–107, 111–120, 123–149` | legs, colours, chest | `hem.legs`, `hem.top`, `hem.chest` |
| `Hem.swift:55–58, 151–153, 157–184, 195–196` | the sonic's lift, helmet, fez, fedora, heart, shield on the back, and Éowyn's Rohan helmet coming off in her signature (which also starts the fist-shake later) | `hem.headwear`, `hem.prop` |
| `Hem.swift:200–230, 233–324, 326–427` | each universe's prop and its drawing; the last range is the Rohan kit, which Clawd of the Rings' own art also uses | `hem.prop`, the helpers into each folder |
| `Hem.swift:37`, `Overlay.swift:1185, 1351, 1816–1825` | HEM's bun lines for Princess Laya | a Star Clawds `StageQuirk.remark` |
| `App/Universes/ComicTransition.swift:1–64` | six cases, three switches; `pick` lists every universe explicitly, only Star Clawds returning nil | `ComicTransition` struct + `module.transitions` |
| `App/Rides.swift:18–35` | `drawRide` switch | `ride.draw` |
| `Rides.swift:84–367, 375–478` | the Quinjet, Milano, Falcon, Javelin, Batwing, TARDIS and Great Eagle drawings | each into its folder's `<Prefix>Rides.swift` |
| `Rides.swift:368–373`, `Theme.swift:91–98` | `materialises`, `canvasHeight`, `drives`, `boardingOffset` (all in the core now; Files' code no longer asks about Clawdberg's rides) | fields on each `Ride` |
| `App/Drills.swift:50–56` | who meditates (not Doctor, Files, Clawdberg; sabers only in Star Wars) | `module.meditation` |
| `Drills.swift:144` | Star Wars' meditation motes are lifted stones | `Meditation` carries the motes style |
| `Drills.swift:251–489` | Star Wars', Marvel's and Doctor's bespoke drills, merged with Files' and Clawdberg's | each into `<Prefix>Drills.swift`; the core merges `module.drills` |
| `Drills.swift:491–525` | `drawElevate`, `drawMarch` (Doctor), `drawLiftedStones` (Star Wars) | into those folders |
| `App/Pose.swift:77` (used at 108–218) | Star Wars draws guns the Clawd Wars way | `module.poseStyle` |
| `App/Habits.swift:121–122` | Marvel's moonwalkers | `module.moonwalkers` |
| `App/Overlay.swift:175–183` | the cast-size check (a `precondition` now) | gone: counts come from the enums |
| `Overlay.swift:868–883` | Playground prompts for Doctor, Files, Clawdberg, Clawd of the Rings | `module.playgroundPrompts` |
| `Overlay.swift:891–892` | `--missing-time` comment names Files and Clawdberg | comment only: "universes with `.away` compaction" |
| `Overlay.swift:951–966` | the Weeping Angle moves only while unseen | `StageQuirk.onlyMovesUnseen` (Doctor) |
| `Overlay.swift:1124–1163, 1234–1240, 1340–1349, 1437–1441, 1567–1570` | Han shoots first, and Indy's version (`isHan`/`isGreedo`, `.clawdberg` checks) | engine feature "shoot-out"; pairs come from `module.shootOuts` |
| `Overlay.swift:1224` | Doctor's golden regeneration flare | `module.compactionEffect` (Doctor) |
| `Overlay.swift:1268–1298` | 88 mph for Clawdberg, otherwise the abduction beam | `module.compactionEffect` (Clawdberg, Files) |
| `Overlay.swift:1310–1313, 1352, 1782–1792` | Captain Clawk flinches at the Croc Clock's tick | `StageQuirk.jitter` (Clawdberg) |
| `Overlay.swift:1315–1319, 1794–1814` | T. Wrecks's glass of water | `StageQuirk.prop` (Clawdberg) |
| `Overlay.swift:1594` | Detective Clawds' grey web line | `module.swingLine` |
| `Overlay.swift:2487–2512` | Settings → Universe lists every universe people can pick (`Universe.offered`) | added universes only (see Add and remove) |
| `Overlay.swift:2846–2856` | first launch takes after the old apps (Star Wars, Marvel, DC) | stays, but looks them up by key (`Universe(key: "dc")`). The one allowed exception: keys never change |
| `Overlay.swift:2894` | Random picks from every universe people can pick (`Universe.offered`) | from enabled universes |
| `App/WindowMode.swift:567–574, 605–624` | The Clawd Files' typed place name in the window | `module.placeCaption` |
| `Saver/SaverView.swift:23` | starts in Star Wars' first place | `Universe.fallback` |
| `SaverView.swift:79–90` | the Options list, built from `Universe.offered` (no longer a line per universe) | built from enabled universes |
| `SaverView.swift:206–214, 237–239` | the choice → universe lookup (`Universe.offered(key:)`, `?? .starWars`); Random | `Universe(key:)`; Random from enabled universes |
| `SaverView.swift:908–935, 1054` | The Clawd Files' typed caption and its box | `module.placeCaption` |

### Couplings between universes (one folder naming another)

| Where | What | How it breaks |
|---|---|---|
| `StarClawds/StarClawdsRoster.swift:86–88` | `isHan`/`isGreedo` include Clawdberg's Indy and the Cairo Swordsman | each universe lists its own `ShootOut` pairs |
| `StarClawds/ShootsFirst.swift:19–23` | Indy's lines, chosen by `universe == .clawdberg` | the lines go in the `ShootOut` value; `ShootsFirst` moves to the engine |
| `Theme.swift:91–98` (was `ClawdFiles/FilesRides.swift`) | no longer a coupling: `drives` and `boardingOffset` moved into the core, which lists the TARDIS's, Files' and Clawdberg's rides | fields on each `Ride` |
| `Hem.swift:102, 106, 172` | HEM wears Files' dress shoes and Clawdberg's boots and fedora | each costume uses its own helpers |
| `ClawdOfTheRings/Art/RingsHeroes3.swift:4–58` | Éowin and Théodone draw with the Rohan kit in the core's `Hem.swift:326–427` | the kit moves into the Rings folder with HEM's Rings costume |
| `Overlay.swift:1816–1825` | HEM talks to Laya (Star Clawds); only Star Clawds' own HEM now (`a.cast.universe == .starWars`), so not a coupling any more | a Star Clawds quirk: "HEM near Laya says one of these" |

### Tools

| File:lines | What it decides | Where it goes |
|---|---|---|
| `Tools/Preview/main.swift:63–120` | batch names and enum-case lookups for all eight | `module.preview` (batches, `caseNames`); the tool loops over the registry |
| `Preview/main.swift:409–424` | the rides sheet lists 13 rides (not yet the Eagle) | every module's rides |
| `Tools/Transitions/main.swift:4–15, 48–95, 129–133` | one function and branch per universe | `module.transitions.every(from:to:)` |
| `Transitions/main.swift:96–110, 190, 201` | Files' caption at the end of each clip | `module.placeCaption` |
| `Transitions/main.swift:209–312, 353–357` | Stevie Clawdberg's showcase video and title | `StevieClawdberg/Promo/ClawdbergShowcase.swift` |
| `Tools/RenderDocs/main.swift:89–162, 215–221` | eight desktop line-ups (Clawd of the Rings' borrows Files' `filesPair`) | `module.docs.lineup` (`Extra` moves to the core as `LineupSlot`) |
| `RenderDocs/main.swift:313–340` | eight social previews' titles, subtitles and groups | `module.docs.social` |
| `Tools/RenderShowcase/main.swift:115–193, 249–407, 408–579, 580–751` | Doctor's, Files', Clawd of the Rings' and Clawdberg's showcase pictures, and the switch that picks one | each folder's `Promo/<Prefix>Showcase.swift`, behind a small `Showcase` protocol |
| `Tools/RenderPromo/main.swift:2168–4333, 4637–5493` | eight trailers: shots, beats, sound, title, set pieces | each folder's `Promo/<Prefix>Reel.swift`, behind a `PromoReel` protocol |
| `RenderPromo/main.swift:250–257, 5500–5512, 5557–5561, 6158–6169, 6309–6310, 6324–6326, 6336–6345` | the reel switches: the `gemini ▸` line, shots, poster, soundtrack, file names, storyboard |
| `RenderPromo/main.swift:751–766, 5576–5596, 5972–5996` | the shot transitions: Star Wars', Marvel's, DC's and Clawd of the Rings' own cases, the rest through `.trip(ComicTransition)` | not in the design yet | from the registered reels |
| `RenderPromo/main.swift:785–1911, 1912–2167, 4334–4636` | the main promo, the bloopers and the Clawd Royale teaser (they mix universes) | stay in the tool: the owner's reels |
| `Tools/MakeSocial/main.swift:35–50, 88–90, 165–169` | the comic-cover panels, one per universe | stays: the owner's artwork. A new universe doesn't need a panel |
| `Tools/MakeIcon/main.swift:128` | Captain Americlawd on the icon | stays: the owner's artwork |
| `build.sh:71, 78`; `Preview/build.sh`; `Transitions/build.sh`; the tool headers | `Universes/**/*.swift` globs | the source lists from `universes.sh` |
| `release.sh:111, 144–200` | four casks, the `others` list, the presets | from `build/gen/universes.tsv` |

---

## Engine toolkit and engine requests

### The rule

A universe may use anything in the **toolkit** below, freely, from inside its folder. Anything beyond it is an **engine request**. The owner builds it into the core first, as a general hook, and then any universe can use it. That's how Clawdberg's version of Han shoots first should have worked, instead of `if han.cast.universe == .clawdberg` in `Overlay.swift`.

Why: the core is the part everybody shares. If each universe slips its own `if` into it, we're back to merge fights, and the core fills up with special cases nobody can follow.

### The toolkit (what a universe may use)

| Area | What | Where it lives |
|---|---|---|
| Characters | `Persona` (weapon, shot, magic, motion, `armoured`, `canSit`, `bulk`, `callout`, `signature`, `headTop`, `muzzle`, `pivot`) | `Persona.swift` |
| Drawing | `PixelCanvas` (72×52, facing right), `Pose` (`breathe`, `step`, `armRaise`, `signature` 0…1, `gunY`), `drawLegs`, `Look`, `C(0xRRGGBB)`, `lerp`, `noise`, `gradient`, `pattern`, outlines | `Pixel.swift`, `Pose.swift`, `Characters.swift`, `Locations.swift` |
| Weapons | `.saber`, `.blaster` + `ShotStyle` (`.energy`, `.beam`, `.bullet`, `.arrow`, `.fire`, `.ice`, `.card`, `.thrown`, `.web`), `.lightning` + `Magic` (families and variants), `.none` | `Persona.swift`, `Fights.swift` |
| Motion | `.walk`, `.fly`, `.hover`, `.swing` (with `swingLine`) | `Persona.swift` |
| Places | `Place(name:panel:still:moving:)`, `Scenes.isTall` for the screen saver | `Locations.swift` |
| Rides | `Ride` (flies, drives, materialises), the ride kit (`hull`, `drawRamp`, `drawGear`) | `Rides.swift` |
| Practice | `BespokeDrill`, `standing`, `setRamp`, `drawSkyShot`, `drawSkyCast`, `drawPortal`, `Meditation` | `Drills.swift` |
| Habits | `moonwalkers`; the habit kinds in `Habits.swift` | `Habits.swift` |
| Transitions | `Trip`, `TransitionSet`, `Wipe` helpers, `PlaceCaption` | `ComicTransition.swift` |
| Compaction | `Compaction.regenerate` / `.away`, the two clocks (`regenerationFlare` 3 s, `missingTimeLength` 6 s, both moved into the engine), `CompactionEffect` | `StatusStore.swift`, `Overlay.swift` |
| Stage | `StageQuirk` (below), `ShootOut` | `Overlay.swift` |
| HEM | `HemCostume` | `Hem.swift` |
| Promo | the promo kit: `Shot`, `Mix`, `brawl`, `windowShot`, `statusOf`, `agentsOf`, `everyAI`, the hook shot, the end card | `Tools/RenderPromo/Kit/` |

### General hooks that today are one universe's special case

Each of these becomes a general hook in phase 2, with its current user as the first one. After that, any universe can use it.

| Today | Becomes | First user(s) |
|---|---|---|
| Weeping Angle check in the overlay's walk | `StageQuirk.onlyMovesUnseen(Cast)`: moves only while nobody faces it | Doctor Clawd |
| `clawkFlinch` | `StageQuirk.jitter(Cast, every:, near: Cast or Location, line:)`: a jump and a shiver on a beat, near something | Stevie Clawdberg |
| `waterGlassItem` for T. Wrecks | `StageQuirk.prop(Cast, draw:)`: a small sprite on the ground in front, drawn every frame | Stevie Clawdberg |
| `hemBunTalk` | `StageQuirk.remark(who: Cast, near: Cast, lines:, every:)`: turn and say something | Star Clawds (HEM and Laya) |
| Han shoots first (+ Indy) | `ShootOut(shooter:, target:, shooterLine:, comebacks:, switchesToGun:)`; the animation is `ShootsFirst` in the engine | Star Clawds, Stevie Clawdberg |
| `drawRegeneration`, `MissingTime` beam, `OutaTime` | `CompactionEffect`: given `k` 0…1 and `t`, returns the sprites to draw and how far to lift the leader | Doctor, Files, Clawdberg |
| `FilesCaption` in the window and saver | `PlaceCaption`: typed lines, font, a dark box, extra time at the end of a trip | The Clawd Files |
| `universe == .dc` web colour | `swingLine` | Detective Clawds |
| the `classic` pose | `PoseStyle.classic`: kept for Star Clawds only; new universes use `.modern` | Star Clawds |
| the meditation guard | `Meditation` | all eight |

### Asking for a new hook

A contributor who needs something the toolkit can't do (a new compaction effect, a new habit kind, a new motion) opens an issue that says what should happen on screen and who uses it. The owner builds it as a general hook on `main`. The contributor then rebases and uses it from their folder. Engine changes and universe folders never travel in the same pull request.

---

## The template

### What it is, and what it isn't

`Sources/App/Universes/_Template/` is a tiny universe that **compiles and runs the moment it's copied and renamed**. It's day one only.

To be clear about how a contributor works:
- They clone **the whole app**, and build and run **the real app**, with all the universes plus theirs.
- They copy the template once, to get a skeleton that already works.
- From there, they grow it into a full universe: 80–110 characters, about 20 places, 8–15 transitions, a ride, and mechanics if the franchise has any. They test it the whole way in the real app, the window, the screen saver, Clawd Royale and the Preview sheets, following the clawdify guide.

### What's in it

```
_Template/
  universe.conf              number 999, key template, prefix Template, template = yes
  TemplateFacts.swift        enum TemplateHero { sampleHero, hem }, enum TemplateVillain { sampleVillain };
                             commented examples of agent-only, rivals, claudeSide and each compaction kind
  TemplateUniverse.swift     the entry, with every protocol member written out and its rules beside it.
                             The file to read first: its header is the "start here".
  TemplateRoster.swift       personas, a home for each, one nemesis pair, ride closure, the Theme, the place key
  TemplateHem.swift          HEM's costume: a hat, a coat, a prop
  TemplateIcon.swift         menu icon, colour and mono
  TemplateWipes.swift        one transition kind, with pick/draw and owner/turf weighting
  Art/TemplateHeroes1.swift  one hero (blaster), drawn step by step
  Art/TemplateVillains1.swift one villain (magic), drawn step by step
  Places/TemplateScenes1.swift one place: still picture, moving layer, tall-canvas extras
  Promo/TemplateReel.swift   a reel with the shared shots only (hook, desktop, status, end card), ready to fill
```

The characters are deliberately plain: "Sample Hero" and "Sample Villain" in "Sample Meadow". They're there to show how things are done, not to be kept.

### The comments, at every spot

Each rule is written where it applies, in the guide's voice. At least:
- **The canvas:** 72×52, facing right, feet on row 44. Every character is Clawd, the orange body in costume, always on Clawd's **four legs**. Legs and shoes first, then `c.oy += p.breathe`, then the body. Anything that hangs over the legs (coat tails, skirts, robes) goes after the breath and still leaves four legs showing.
- **Poses:** `armRaise`, melee angles, `gunY`, sitting (`seatedPose`), what `Pose.swift`'s header explains.
- **The signature:** 2–4 seconds (`signature:`); the drawing reads `p.signature` (0…1) and starts and ends in the normal pose. It has to read at desktop size.
- **Weapons:** the table of `.saber`, `.blaster` + `ShotStyle`, `.lightning` + `Magic`, `.none`; `armoured`, `bulk`, `canSit`, motion.
- **Magic variants:** don't set `magic.variant` yourself. The engine numbers every magic user in order through all universes, so no two look alike.
- **Ids:** the enums are append-only. HEM is always the last hero. Never reorder or remove a case once it's on `main`.
- **Places:** the first is the default. Keys are unique across all universes. The moving layer is drawn every frame, so keep it light. Scale landmarks up when `Scenes.isTall`.
- **Names:** every file starts with your prefix. Every top-level name is unique across the app (Preview compiles all universes together), so prefix shared helpers and keep the rest `private`.
- **Transitions:** 8–15, the signature opening among them, drawn in pixel art.
- **What you may use**, and how to ask for more (the engine toolkit, above).

### How to start from it

`Tools/new-universe.sh <Folder> <Prefix> <key> "<Title>" <number>` copies `_Template` to `<Folder>`. It renames files, types, place keys and the prefix; fills in the manifest; and takes out the `#if CLAWD_TEMPLATE` lines. Copying by hand works too, and the checks catch anything missed.

---

## Never shown in the app

The template must never reach a user. One guard could fail, so there are several, each one enough on its own:

1. **Not compiled at all.** `universes.sh` skips every folder whose name starts with `_`. The source lists come only from registered folders, so the template's files aren't even handed to the compiler. There's nothing to leak: no places in the merge, no place keys, no magic variants, no rides.
2. **The `**` globs are gone first.** Today's `Sources/App/Universes/**/*.swift` would compile `_Template` too. So every glob (two in `build.sh`, the Preview and Transitions build scripts, the five tool header commands) is replaced in phase 3, **before** the template is added in phase 4. `universes.sh` and check-universe both fail if a `Universes/**` glob turns up again in any build script.
3. **Compiled to nothing even if a glob slips back.** Every template file is wrapped in `#if CLAWD_TEMPLATE … #endif`. Only `TEMPLATE=1` passes `-D CLAWD_TEMPLATE`.
4. **A number nobody else can have.** The template is `999` in `NUMBERS`, marked `template`. `universes.sh` refuses number 999, key `template`, any number from 900 up, and any manifest with `template = yes`, unless `TEMPLATE=1` is set.
5. **Never in a release.** `build.sh --release` refuses `TEMPLATE=1` outright. It then checks the generated list for the template before signing. `release.sh` also runs the built app with a new `--list-universes` flag and stops if the list contains `template`, any number from 900 up, or doesn't match the `shipped` and `reserved` lines it expects.
6. **The app refuses it too.** The template's module says `isTemplate = true`. The registry stops with a `fatalError` if it meets a template module in a build without `CLAWD_TEMPLATE`. A release build passes `-D CLAWD_RELEASE`, where it refuses even with the flag.
7. **A template build stays out of your real setup.** `TEMPLATE=1 ./build.sh` means `--no-install` (it runs from `build/`, the hooks are left alone) and launches with `--template-preview`. That counts as a test run, so it never writes the universe to the hook's state file. Real sessions are shown adopted into the template's cast for a look, and nothing with a 999 id is ever saved.
8. **Copying without renaming fails loudly.** `universes.sh` stops with a plain message if a folder that doesn't start with `_` still has key `template`, number 999, prefix `Template`, entry `TemplateUniverse`, a `Template…` file name, a `sample…` place key, or a leftover `CLAWD_TEMPLATE` line. For example: "ClawdSlayer/ still says `key = template`: give it its own key and number from NUMBERS". This matters because two folders with the same key would otherwise fail later with a confusing compile error.
9. **Every place it could show up is fed by one list.** Clawd Royale, Random, Settings → Universe, the saver's Options, the saver's Random, `Location.everywhere`, the Location menu, `magicVariants`, the hook's casting, RenderDocs' roster/locations/line-up loops, the reels, and Preview's `all` and per-universe batches all come from `Universe.allCases`. That's the registered list, which never holds the template outside a `TEMPLATE=1` build. The promo, docs and Preview tools are built through `universes.sh` like the app, so they can't see it either.
10. **The template doesn't rot.** Because it's never compiled normally, an engine change could break it without anyone noticing. So `release.sh` (and check-universe `--template`) builds `TEMPLATE=1 Tools/Preview/build.sh` into a scratch folder and renders its sheets. That's only a tool build, never the app. A template that no longer compiles fails the release.

---

## Add and remove universes in Settings

Every universe ships inside the app, so nothing is downloaded or installed. A checkbox only chooses which ones the app uses; unchecking one removes it from the app, checking it adds it back. (Real install/uninstall as runtime plugins was turned down, see Constraints.)

### What the user sees

A new **Universes** section in Settings lists every universe in number order, each with a **checkbox**. Every universe is checked by default.
- **At least one stays checked.** The last checked box can't be unchecked, with the note "At least one universe stays in."
- Saved as a list of **removed (unchecked) keys** (`universesRemoved` in the app's defaults). It saves what's removed, not what's added, so a universe that comes with an update shows up checked. Keys are used rather than numbers because they're readable, and they're just as permanent.
- Checking a universe again is instant, and everything about it is exactly as before.

### What removing one does

- It **drops out of** Settings → Universe, Random, Clawd Royale's cast and places, the Location menu in Clawd Royale, and the saver's Options, Random and Clawd Royale.
- **Arch-enemies** and **HEM** follow by themselves: nemeses only pair inside one universe, and `Roster.hems` only holds the universes in the roster.
- **The hook needs to know**, because it casts new characters in Clawd Royale. The app writes the list into `state.json` as `removed: [Int]?`, and into the saver feed. Old files without it decode fine (it's read leniently, like the other fields), and the hook's `Roster` leaves those universes out.
- **The universe on show is removed:** the app switches to the lowest-numbered universe still added, with the usual whole-window transition. Everyone is recast into it, exactly as picking a universe from the menu does today (`switchScene`).
- **The saver's own choice is removed:** it acts as "The same as Clawd Clash".
- **The saved `universe` is removed at launch:** the app starts in the first universe still added.

### Sessions already cast from a universe that gets removed

**Decision: they keep their character until the session ends. Only new casting stops, and it stops straight away.** This only matters in Clawd Royale. In a single universe everyone is already shown as one of that universe (`adopt`).
- **Why:** the character's id is saved in `state.json` and belongs to a running session. Rewriting it would break the one rule we never break, and adding the universe back should bring everything back exactly as it was.
- A face changing in the middle of a session would also be confusing: "who's that, and where did Doctor Ten go?"
- Agents are the same: they keep their character until they finish, which is usually minutes.
- If the owner would rather they vanish at once, they can be *shown* adopted into a universe that's still added, without touching the saved id (see Open questions).

---

## check-universe

`Tools/CheckUniverse/check.sh <Folder>` (or `--all`, or `--template`). It's partly shell, for the files, and partly a small Swift tool built through `universes.sh` with the whole registry, for what can only be checked by running. It prints a list:

```
Clawd Slayer (slayer, 7)
  ✓ manifest: number 7 matches NUMBERS (reserved), key and folder match
  ✓ not the template: no template key, number, prefix or CLAWD_TEMPLATE left
  ✓ only this folder changed since main (14 files under ClawdSlayer/)
  ✓ file names: all start with Slayer, none clash with another universe's
  ✗ top-level names: `drawStake` in Art/SlayerHeroes2.swift isn't prefixed or private
  ✓ counts: 41 villains, 47 heroes (from the enums); HEM is the last hero
  ✓ homes: every character's home is one of this universe's 20 places; the default place is first
  ✓ place keys: 20, unique across all 8 universes
  ✓ magic: 9 magic users, each with its own variant; no earlier universe's variants changed
  ✗ signatures: Spike has signature: 3.0 but his drawing never reads p.signature
  ✓ ids: every existing id (0–7) has the same character as on main
  ✓ nemeses: 14 pairs, each a hero and a villain from this universe
  ✓ transitions: 11 kinds, each renders start to end; durations 1.6–6.0 s
  ✓ the core doesn't name this universe; this universe doesn't name any other
  ✓ builds: app (native and --release type-check), hook, saver, Preview, Transitions
  ✓ sheets written to build/check/slayer/ (cast batches, places, rides, transitions)
  ! size: 88 characters, 20 places (in range); 21 heroes (the guide's minimum is 20)
```

What it checks, and how:
- **Manifest and numbers:** against `NUMBERS`; the key, prefix and entry are unique; not 900 or above.
- **Not the template:** the same tests as guard 8.
- **Hand-off scope:** `git diff --name-only main...HEAD` lists only files under the folder.
- **Names:** every `.swift` file starts with the prefix. File names are unique repo-wide (Swift needs that). Top-level `func`/`let`/`var`/`struct`/`enum` names that aren't `private` must start with the prefix, in any letter case. Duplicates would fail the build anyway, but only once a second universe happens to pick the same name.
- **Counts:** `facts` counts against the `Theme`'s persona lists; HEM is last and drawn with the engine's HEM.
- **Homes:** every cast member's `home` is in `theme.places`, and every place in `theme.places` has a drawing.
- **Place keys:** the number of merged places equals the sum of every universe's places, so nothing was dropped.
- **Magic variants:** every `(family, variant)` pair is unique across all universes, and the variants of universes 0–7 match main's.
- **Signatures:** every persona with a `signature` is drawn at `signature` 0.5 and at none; identical pixels mean the drawing never uses it. Leads without one are listed as a note.
- **Ids:** dumps `id → name` for every universe and compares it with the same dump built from `main`. Any change to an existing id fails.
- **Core-blind lint:** no file outside the folder mentions its types, keys or place names (except the known owner-curated tools and the old-app migration lines), and the folder mentions no other universe's.
- **Builds:** everything `universes.sh` feeds, including a release-style type check (`-warn-long-expression-type-checking=300`) for the dense drawing code that trips up universal builds.
- **Sheets:** Preview batches, places, rides and every transition, written to `build/check/<key>/` to look at.

---

## Hand-off and contributor flow

From the first clone to the merged pull request:

1. **Pick a franchise** and check it with the clawdify guide (steps 1–2: research and viability). No code yet.
2. **Ask the owner for a number.** The owner adds a `reserved` line to `NUMBERS` on `main`. That's the only shared change, and it's the owner's.
3. **Clone the repo** (or fork it) and branch off `main`.
4. **Start from the template:** `Tools/new-universe.sh ClawdSlayer Slayer slayer "Clawd Slayer" 7`.
5. **Build and run the real app:** `./build.sh` (or `--no-install`). Settings → Universe → Clawd Slayer. Two characters, one place and one transition are already working, next to all the other universes.
6. **Follow the guide's approval gates** (roster, places, mechanics and transitions, the plan), then its build phases. Grow the folder: the full cast, about 20 places, transitions, ride, mechanics. Check each phase in the app, the window, the screen saver, Clawd Royale and the Preview sheets.
7. **Need something new from the engine?** Open an issue (see "Asking for a new hook"). The owner adds the hook on `main`. Rebase and use it.
8. **The trailer:** fill in `Promo/<Prefix>Reel.swift` using the promo kit. Show the storyboard first.
9. **Run `Tools/CheckUniverse/check.sh <Folder>`** until it's all ticks.
10. **Open a pull request that adds only the folder.** Put the changelog text and the README blurb in the PR description, not in the shared files.
11. **The owner reviews and merges.** After merging, the owner does the public and shared parts: `CHANGELOG.md`, the README universe table, `llms.txt`, the docs pictures (RenderDocs reads them from the module), a cask if wanted (the manifest's `cask` line), the release, and `NUMBERS` → `shipped`.
12. **From then on the enums are append-only.** Fixes and polish are later pull requests that again touch only the folder.

### The clawdify guide, rewritten around the template

The guide keeps its voice, its research steps and its approval gates. What changes:
- **Step 0 (Understand the request):** "check `Universe.swift` for raw values" becomes "ask the owner for a number from `NUMBERS`, then run `new-universe.sh`".
- **Step 2 (Overview), item 4 (Code naming):** the number comes from `NUMBERS`; the folder, prefix and key go in `universe.conf`.
- **Step 6 (Write the plan), "How a universe plugs in":** becomes "Your folder". There's no list of shared files to wire any more.
- **Step 7 (Build it):** phase 1 (Skeleton) is now "copy the template and rename it". "New files" is rewritten around `<Prefix>Facts.swift` and `<Prefix>Universe.swift`. **The wiring checklist is deleted.** In its place: a table of `UniverseModule`'s members, what each one does, and which ones have defaults. Verification adds check-universe.
- **New section: the engine toolkit and engine requests** (from this plan).
- **Step 8 (Docs and release):** split into what the contributor does (nothing outside the folder) and what the owner does after merging.
- **Promo:** the reel lives in `Promo/<Prefix>Reel.swift`. The 10-item "Wiring a new reel" checklist is replaced by the `PromoReel` protocol's members.
- **House style:** adds "never edit outside your folder".
- The copy at `clawd-plans/clawdify_guide.md` is updated to match.

---

## Phases

Every phase builds, passes the verification below, and **leaves the app identical for users**, apart from phase 6, which adds the Universes checkboxes. Commit at the end of each step, with a `CHANGELOG.md` entry where users would notice anything (most phases are internal, so the entry is short or empty).

### 0. A baseline

- On `main`, render the reference set into `build/baseline/` (not committed): every Preview batch, every universe's places, the rides sheet, a fight and a drills sheet per universe, every transition's key frames, RenderDocs' pictures (already committed in `docs/`, a free baseline), RenderShowcase's, and each reel's storyboard and a few fixed frames.
- Add a hidden `--dump-ids` flag (to Preview, so the app doesn't change) that prints every `id, universe key, name`, every place key with its universe, every magic variant, and the hook's global sets (agent-only, rivals, compaction lists). Save it as the baseline.
- A tiny `Tools/Baseline/compare.sh` renders the same set again and compares it with `cmp` (same pixels give the same PNG bytes from the same encoder), listing anything that differs.

### 1. The protocols and a hand-written registry, the eight adapted in place

- Add `UniverseFacts`, `UniverseModule` (every member with a default for now), `Trip` and `TransitionSet`.
- Turn `Universe` into the struct, with a **hand-written** list of the eight in `Sources/Shared` for now.
- Give each universe a `<Prefix>Facts.swift` (enums moved from the roster file, unchanged and in order) and a `<Prefix>Universe.swift` that returns what already lives in its folder: theme, places, trips, Files' and Clawdberg's drills.
- Swap the core's simple switches for registry lookups: `Theme.of`, the places merge, `Universe`'s properties, `ComicTransition`, Preview's universe list.
- Check: pixel-identical baseline, identical `--dump-ids`.

### 2. Move each universe's scattered lines into its folder

- **2a, the general hooks**, each with today's behaviour exactly: `Ride` as a struct, `HemCostume`, `Meditation`, `PoseStyle`, `StageQuirk`, `ShootOut` (with `ShootsFirst` moved to the engine), `CompactionEffect`, `PlaceCaption`, `swingLine`, `playgroundPrompts`, `moonwalkers`. Move `Hem.swift`, `ComicTransition.swift` and `ShootsFirst.swift` out of `Universes/`.
- **2b–2g, one universe per commit.** Each commit moves that universe's HEM costume, rides, drills, quirks, prompts, compaction effect and caption into its folder, and deletes its lines from the core. Order:
  1. **Stevie Clawdberg** first, because it's the most tangled (Han shoots first, the rides `drives`, HEM's boots, 88 mph, Clawk, T. Wrecks), so it proves the hooks;
  2. The Clawd Files;
  3. Doctor Clawd;
  4. Detective Clawds;
  5. Marvelous Clawds;
  6. Clawd of the Rings;
  7. Star Clawds last, which ends with HEM and Laya and `classic` poses.
- At the end of phase 2, the core-blind search finds no universe names in `Sources/`, apart from the old-app migration lines.
- Check after every commit: pixel-identical baseline, identical `--dump-ids`, and a scripted PreCompact run of the hook (a Doctor regenerates to the next, an FBI agent and Marty get `abducted`, everyone else is untouched).

### 3. Generated registry and the tools

- `NUMBERS`, the manifests and `Tools/universes.sh`. `build.sh`, the Preview and Transitions build scripts, and the five tool header commands switch to its source lists. **No `Universes/**` glob is left.** The hook compiles only the facts files.
- Preview, Transitions, RenderDocs and RenderShowcase find universes through the registry (`module.preview`, `transitions.every`, `module.docs`, `Showcase`).
- **RenderPromo split**: first the shared parts move into `Tools/RenderPromo/Kit/` (shots, mix, text, backgrounds, window mode, storyboard), with `main.swift` keeping the main promo, the bloopers and the Royale teaser. Then each trailer moves into its folder's `Promo/<Prefix>Reel.swift` behind `PromoReel` (name, file base, storyboard title, shots, beats, sound, poster time, and the bits the shared shots ask for: window cast and prompts, brawl cast, the "pick your universe" caption, the `gemini ▸` line). One reel per commit.
- **Why the reel goes in the universe's folder** and not in `Tools/RenderPromo/Reels/`: the folder is what gets handed off, and the trailer is the universe's own work. `universes.sh` keeps `Promo/` out of the app, so it costs the app nothing.
- `release.sh` writes casks from `build/gen/universes.tsv`. Only universes whose manifest has a `cask` line get one, and the `others` list and presets come from the same file. The generated `.rb` files must be byte-identical to today's four.
- Check: the baseline, plus each reel's storyboard and fixed frames, plus `REEL=… check` for each reel.

### 4. The template and the never-shown guards

- Add `_Template/`, `new-universe.sh`, guards 3–8 and 10, and `--list-universes`.
- Check: a normal build, a release build and every tool build show no sign of it (list, Preview `all`, docs loops). `TEMPLATE=1 ./build.sh` runs it from `build/` without writing state. A copy left unrenamed fails with the plain message. `new-universe.sh` produces a universe that builds and runs.

### 5. check-universe

- `Tools/CheckUniverse/`. Run `--all` on the eight: everything passes, or the misses are fixed (expected: a few unprefixed top-level helpers, and maybe a signature or two never drawn).

### 6. Add and remove universes

- Settings' Universes section with a checkbox per universe, `universesRemoved`, `removed` in `state.json` and the saver feed, and the behaviour above. This is the one phase users will notice, so it gets a real changelog entry.

### 7. The guide

- Rewrite `clawdify_guide.md` (sections above) and refresh the copy in `clawd-plans`.

### 8. The next universe, the first built from the template

- Clawd Slayer was built the old way and released in 3.7.0, so it's ported in phase 2 with the others. The next planned universe (the top-level plans in clawd-plans) starts with `new-universe.sh`, as a pull request that adds only its folder, which proves the whole flow.

---

## Verification

- **Pixels.** After every commit in phases 1–5: the full baseline set (Preview batches, places, rides, fights, drills, transition key frames, RenderDocs and RenderShowcase pictures, reel storyboards and fixed frames) compared byte for byte. The only allowed differences are deliberate ones, named in the commit.
- **Saved ids.** `--dump-ids` identical: every id's character, every place key's universe, every magic variant, the hook's agent-only, rival and compaction sets. That proves a session saved by today's app and hook opens as the same character after the refactor.
- **The hook.** A fixture `state.json` fed through the built hook binary with PreCompact, SessionStart and SubagentStart events: the same output before and after. Then, with `off` set, Clawd Royale never casts from a universe that's off.
- **Release build.** `./build.sh --release <version>` builds universal binaries (watch the type-checker on the moved drawing code). `--list-universes` lists the eight, with no template. The casks match today's.
- **The screen saver.** Installed from the app: the Options list is the same ten entries in the same order (until phase 6, then without the ones that are off). Each universe, Clawd Royale and Random work, and The Clawd Files' typed caption still types.
- **In the app.** Each universe in Settings, Random, Clawd Royale, the menu bar icons, the Playground's prompts, `--missing-time` (FBI agents' beam, Marty's 88 mph), `/compact` with a Doctor, Han and Greedo, Indy and the swordsman, the Weeping Angle, Clawk and the Croc Clock, T. Wrecks's glass, HEM and Laya.
- **Size and memory.** The binary sizes and the running app's memory before and after. They're expected to be the same within a few hundred KB; the hook grows a little from the enums.

---

## Risks

- **Subtle changes while moving code.** Five thousand lines of promo and several hundred of drawing move. That's why there's a pixel baseline, one universe per commit, and the reels split one at a time.
- **Losing the compiler's "you missed a spot".** Today an exhaustive `switch` turns a forgotten universe into a compile error. With a struct, required protocol members (no default) and check-universe take over that job. That's better for contributors, because the compiler then points at their own folder, not at the core.
- **Order-dependent results.** `magicVariants`, the places merge and the menu order depend on the registry being in number order. The registry sorts by number, and `--dump-ids` would catch any slip.
- **Random picks.** Moving `ComicTransition.pick` could change how random numbers are used, so the same run picks a different trip. Nobody sees that, and pixel checks use the deterministic tools, but it's worth knowing.
- **Generated code.** A contributor who never runs a build script won't have `build/gen/`. Every script runs `universes.sh` first, so this only affects editor completion.
- **Phase 2 is the long one.** Eight universes, each with its own surprises. It can be spread over several sessions, because each commit stands on its own.

## Open questions for the owner

1. **Clawd Slayer is already under way** on `buffy`, with a skeleton touching 9 shared files, committed there (`23e3206`) as number 6, which Clawd of the Rings now has on `main`. Pause it after its planning steps while phases 0–4 land, then start its code from the template? Or finish its skeleton the old way and port it in phase 2, as an eighth universe? Pausing is less work in total.
2. **Numbers:** handed out in `NUMBERS` before work starts (recommended)? Or a development range (900–989) that contributors use until the owner assigns the real number at merge? The range spares contributors a wait, but means one line changes at merge, and any test sessions they saved become orphans.
3. **The manifest:** a plain `universe.conf` (recommended, because the shell scripts and `release.sh` can read it)? Or everything in Swift, plus a hand-edited one-line registry?
4. **Removed universes in Clawd Royale:** keep their characters until the session ends (recommended), or show them at once as someone from a universe that's still added (the saved id stays the same either way)?
5. **The owner's curated pictures:** MakeSocial's comic cover, MakeIcon and the main promo, bloopers and Royale teaser keep naming universes by hand. Fine as the owner's own art? Or should modules offer an optional social panel too?
6. **Casks:** only the three old universes have one today. Should new universes get casks at all? The manifest's `cask` line makes it possible but optional.
7. **Contributors and credit:** where are contributors credited (README, CHANGELOG, the universe's showcase)? About already has a "Thanks to" list with the universes each person made (`Overlay.swift:2693–2697`). Do their pull requests need anything about the MIT licence?
8. **Who signs off the approval gates** when someone else drives the guide: the contributor alone, or the owner at the roster and transitions gates? The second avoids rejecting a finished universe late.
