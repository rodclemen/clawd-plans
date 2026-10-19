# Plan: a new universe, Stranger Clawds (Stranger Things parody)
<!-- track: repo=rodclemen/clawd-clash branch=stranger-things folder=StrangerClawds title="Stranger Clawds" cast=45 places=16 -->

## Context

Clawd Clash has seven universes on `main` (d270b63, 2026-10-17, after 3.6.0). This plan adds a parody of Stranger Things: all five seasons, with no spin-offs (not the stage play *The First Shadow*, not the animated *Tales from '85*). It's **a limited experience, and you chose it knowingly**: the heroes are many and strong, the villains are thin (about a dozen real ones, with the Demodogs and their kin as small fry). The ideas carry it: the neon title, Joyce's Christmas lights and the Upside Down, which now and then really is upside down.

| Universe                             | Heroes | Villains | Total | Places | Transitions |
|--------------------------------------|--------|----------|-------|--------|-------------|
| Star Clawds                          |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds                     |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds                     |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd                         |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files                      |     36 |       46 |    82 |     20 |          11 |
| Stevie Clawdberg                     |     64 |       54 |   118 |     23 |          10 |
| Clawd of the Rings                   |     38 |       38 |    76 |     22 |           9 |
| Superclawdtural (planned)            |     35 |       45 |    80 |     20 |          12 |
| Battleclawd Galactica (planned)      |     26 |       25 |    51 |     17 |          10 |
| **Stranger Clawds (proposed)**       | **29** | **16** | **45** | **16** | **10** + the lights |

(heroCount includes HEM; villainCount includes the four agent-only small fry.)

- **Viability: a limited experience.** 28 drawn heroes, well over 20. Only 12 drawn villains, under the 20 threshold: the same villains' faces will come round often, and some fights will be thin. You weighed the three choices on 2026-10-17 (go ahead small, widen with the spin-offs, pick another show) and chose to go ahead small, with all five seasons and no spin-offs.
- **Name: Stranger Clawds** (chosen on 2026-10-17). The alternatives were Stranger Thclawds and The Upside Clawd.
- **Code naming** avoids the franchise name:
  - `case hawkins` with key `"hawkins"`.
  - Folder `Sources/App/Universes/StrangerClawds/`, file prefix `Hawkins` (`HawkinsRoster.swift`, `HawkinsHeroes1.swift`, `HawkinsWipes.swift` …). No file in the repo uses `Hawkins` as a prefix today. Top-level names start with `hawkins` or are `private`, as `scripts/pr-guard.py` asks.
  - Branch `stranger-things`. Trailer `REEL=hawkins`.
- **Raw value: next free when the build starts.** Check before the skeleton commit: `main` uses 0 to 6 (`middleEarth = 6`); the `buffy` branch claims `slayer = 6`, which clashes and needs renumbering before it merges; Henrik's Clawd Burton lives on his fork (HEM42/clawd-clash) with a value of its own; Superclawdtural (`hunters`) and Battleclawd Galactica (`fleet`) may have taken one by then. Read other branches with `git show <branch>:Sources/Shared/Universe.swift`, never by switching. Ids are rawValue*1000 and permanent.
- **Naming style:** light puns only where they read at a glance: Lucas **Sinclawd**, Steve **Harringclawd**, Eddie **Munclawd**, the **Democlawgon**. Everyone else keeps the on-screen name (Eleven, Dustin, Vecna), because a forced pun is worse than none. Actors' names are never used.
- **Size:** 45 characters and 16 places. The smallest universe in the app.

### How the cast is split

Heroes are the Party, the teenagers, the grown-ups of Hawkins and the allies who come over to their side. Villains are the Upside Down's monsters and the people who hunt the kids. The grey ones go by **what fans remember them for**:
- **Dr. Owens → hero** (he protects Eleven from season 3 on).
- **Billy → villain** (the bully, then the Mind Flayer's host), though he dies a hero.
- **Alexei and Yuri → heroes**, the Russians who help.
- **Kali → hero.**
- **Colonel Sullivan → villain** (he hunts Eleven in season 4).
- **Derek Turnbow → hero**: the rich, arrogant boy from season 5 who ends up helping the other captured kids.

### Tone: what's left out, and why

The show is horror with children at its heart. Clawd Clash is a desktop toy, so:
- **Drawn eerie, never gory:** Vecna's victims float and stiffen; no bones breaking, no eyes gone.
- **Only hinted:** Brenner's experiments on children (the lab, the number tattoo).
- **Left out entirely:** the season 4 lab massacre (Eleven, a child, in the middle of it); the bath-tank scenes; the Flayed (Mrs. Driscoll and the others) and the season 3 flesh monster, too gruesome, with the Mind Flayer standing for them.
- **Barb is a hero, not a victim.**
- **Kept apart from Stevie Clawdberg:** its 80s kids on bikes (E.T., The Goonies) are already in the app. This universe stands apart with the Upside Down's blue-grey and red spores, neon and Christmas lights; nobody wears a Goonies-style outfit.
- **No real people, no actors' names.**
- **Music:** synth arpeggios in our own notes, never the theme, and never "Running Up That Hill" or any other real song.

## How a universe plugs in (checked against the code on 2026-10-17, main d270b63)

**New code: `Sources/App/Universes/StrangerClawds/`**
- `HawkinsRoster.swift`:
  - `enum HawkinsHero` and `enum HawkinsVillain`, append-only, with `hem` as the last hero.
  - The persona dictionaries, `.reduce([.hem: hemPersona(.hawkins)])`.
  - `Location.hawkinsHome(of:)` for heroes and villains, `hawkinsNemeses`, the ride closure, `let hawkinsTheme = Theme(...)`.
  - The `static let` place keys and `let hawkinsPlaces` merged from the Places files.
- `Art/HawkinsHeroes1…3.swift` and `Art/HawkinsVillains1…2.swift`, 8 to 10 personas per file, in the pattern of `ClawdbergHeroes1.swift`. Shared helpers (80s clothes, walkie-talkies, the Upside Down's vines and spores, the Demogorgon's petal head) go in one `HawkinsKit.swift` with `hawkins`-prefixed names.
- `Places/HawkinsScenes1…2.swift` as `let hawkinsScenesN: [Location: Place]`.
- `HawkinsIcon.swift`: the menu bar icon, 28×26, colour and mono. A walkie-talkie, or a string of Christmas lights.
- `HawkinsTaken.swift`: the compaction mechanic (see Mechanics).
- `HawkinsFlip.swift`: the timing of the rare flip (see Mechanics). The drawing side of it lives in the app's own files, below.
- `HawkinsWipes.swift`: the transitions and the Christmas-lights finishing touch, last.

**Wiring into the existing code.** Copy what `middleEarth` and `clawdberg` did. Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎.
- **`Sources/Shared/Universe.swift`:**
  - `:9–15` the case; `:17` `key`; `:25` `title`; `:33` `villainCount` (16); `:37` `heroCount` (29);
  - `:50` `agentOnly` (Demodog, Dart, Demobat, flayed rat);
  - `:65` `claudeSide` (default false: Claude plays the heroes);
  - `:68` `rivals` (Vecna and One; today it's `self == .starWars ? [0, 1] : []`, so it becomes a switch, which Superclawdtural or Battleclawd Galactica may already have done);
  - `:90` `abductees`: the ones who've been to the Upside Down (see Mechanics), the way Clawdberg lists its time travellers;
  - `:106` `isReleased`: return `false` for `.hawkins` until phase 6 if it's built on `main`, as Clawd of the Rings was.
- **`Sources/App/Theme.swift:40`:** `Theme.of`. **`:89`** add `bikes` to `enum Ride`, and **`:93`** add it to `Ride.drives`: the BMX bikes come in along the ground.
- **`Sources/App/Locations.swift:70–72`:** `.merging(hawkinsPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift`:** in phase 1, add `.hawkins` next to Star Clawds in `pick` (`case .starWars, .hawkins: return nil`, `:40–62`), as the guide now says. In phase 5, take it out of that line and add a `.hawkins(HawkinsTrip)` case at `:8–13`, in `duration` (`:15–23`), `draw` (`:26–35`) and `pick`, and the doc comment at `:3–6`.
- **`Sources/App/Universes/Hem.swift:15–31, 63–104, 113–118, 130, 203`:** HEM's persona and costume in every switch.
- **`Sources/App/Rides.swift`:** the bikes' drawing (phase 4), in `drawRide` (`:18`) next to the others.
- ⚠︎ **`Sources/Saver/SaverView.swift`:** nothing to add for the universe itself; the Options list and the trip choice build themselves from `Universe.offered`. Only the doc comment at `:80` names universes. **The flip** needs a hook here (the crew is laid out at `:385`), see Mechanics.
- ⚠︎ **`Sources/App/Drills.swift:51`:** the meditation guard (`meditates`). Stranger Clawds doesn't meditate, so add `universe != .hawkins`. **`:72`** and the bespoke-drill table: merge `hawkinsBespokeDrills`.
- ⚠︎ **`Sources/App/Overlay.swift`:**
  - `:875–878` the Playground prompts (five, below), a `case .hawkins:` next to `.clawdberg` and `.middleEarth`;
  - `:1271–1272` is where `OutaTime` is chosen for `clawdberg` (`MissingTime` is the fallback for everyone else in `abductees`); `HawkinsTaken` hooks in the same way, and its caption at `:1353`;
  - the nosebleed, Vecna's clock and babysitter habits hook into the tick;
  - **the flip:** the window's drawing (`windowMode`, `:133`) gets the scene-wide upside-down flag (see Mechanics);
  - the cast-size check is at `:180`.
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`**: decide per universe-specific `if`. Stranger Clawds joins none of the existing ones; it adds its own habits.
- ⚠︎ **Compaction:** `StatusStore.swift:341` already marks any leader in `abductees`; check it picks up `.hawkins` without changes. `HookInstaller.swift` already registers the hook.
- **Clawd Royale** picks the cast and places up through `Universe.allCases`. Check the menu bar icon and arch-enemies still behave when a scene is in a Stranger Clawds place, and that the flip never fires in a Clawd Royale desktop scene.
- **Tools:**
  - `Tools/Preview/main.swift:19–24` (the arguments: add the `--flipped` switch, see Mechanics) and `:64–95`: the batch doc comment, the batch arrays (`hawkinsHeroes1…`, `hawkinsVillains1…`), the universe lookup (`"hawkins": Theme.of(.hawkins).cast`), the enum lookups by case name.
  - `Tools/Transitions/main.swift:13–14` (usage comment) and `:131–133` (the branch that renders this universe's trips, phase 5).
  - Phase 6: `Tools/RenderPromo` (`REEL=hawkins`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts** (`Overlay.swift:875`):
1. "Spell the error out on the Christmas lights."
2. "Find out what's living in the Upside Down of the build folder."
3. "Roll a d20 for the flaky test."
4. "Get the Party on their bikes and ride to the deploy."
5. "Suzie, do you copy? Send the logs over."

## Cast

How the engine's weapons map onto the show. This is a show about kids, so a lot of `.none`:
- **`.lightning` + `Magic`** for the powers: Eleven's telekinesis (pale red `waves`), Kali's illusions (violet `spell`), Will's season 5 power (violet `waves`, to re-check at the audit), Vecna's and One's mind power (red `rings`).
- **`.saber`** for things swung: Steve's nail bat, Joyce's axe, Karen's broken wine bottle, Eddie's spear and spiky shield, the monsters' claws and tendrils, Billy's fists.
- **`.blaster` + `.bullet`** for the guns: Hopper, Nancy, Jonathan, and the bad men.
- **`.blaster` + `.thrown(grey)`** for Lucas's wrist-rocket slingshot; **`.fire`** for Murray's flamethrower.
- **`bulk`** for Vecna and the Mind Flayer; **`canSit: false`** for the Mind Flayer and the Democlawgon.
- Everyone, monsters included, is Clawd in costume on Clawd's four legs.

### Heroes (29)

Enum order is the table order. Eleven, Mike and Dustin come first for the skeleton.

**The Party (7)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Eleven | season 1: pink dress, blue jacket, buzz cut | telekinesis (lightning, pale red `waves`) | eats an Eggo; her nose bleeds | "Friends don't lie." |
| 2 | Mike Wheeler | dark hair, striped shirt, walkie-talkie | none | talks into his walkie-talkie | "Over." |
| 3 | Dustin Henderson | cap, curls, no front teeth | none | into Cerebro's radio | "Suzie, do you copy?" |
| 4 | Lucas Sinclawd | camo bandana, binoculars | wrist-rocket slingshot (thrown, grey) | lifts the binoculars | none |
| 5 | Will Byers | bowl cut, flannel shirt, drawings | his season 5 power (lightning, violet `waves`; re-check at the audit) | holds up one of his drawings | none |
| 6 | Max Mayfield | red hair, skateboard, Walkman | none | puts on her headphones and kicks off on the skateboard | none |
| 7 | Erica Sinclair | pigtails, attitude | none | crosses her arms | "Nerds." |

**The teenagers (8)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 8 | Steve Harringclawd | big hair, season 2 open jacket | nail bat (saber) | sprays his hair | none |
| 9 | Nancy Wheeler | short coat, shotgun | sawn-off shotgun (bullet) | racks the shotgun | none |
| 10 | Jonathan Byers | dark hair, camera round his neck | revolver (bullet) | takes a photo with a big flash | none |
| 11 | Robin Buckley | Scoops Ahoy sailor's uniform | none | salutes in her sailor's hat | "Ahoy!" |
| 12 | Eddie Munclawd | long curly hair, Hellfire t-shirt, denim vest | spear and spiky shield (saber) | plays a guitar solo | none |
| 13 | Argyle | Surfer Boy Pizza uniform, long hair | none | holds out a slice of pizza | "Duuude." |
| 14 | Barb | big glasses, frilly blouse | none | pushes up her glasses | none |
| 15 | Derek Turnbow | rich kid's polo shirt and a sneer (season 5; re-check the look at the audit) | none | none | none |

**The grown-ups (7)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 16 | Chief Hopper | sheriff's hat, tan shirt, moustache | revolver (bullet) | sips coffee | "Mornings are for coffee." |
| 17 | Joyce Byers | messy hair, Christmas lights | axe (saber) | the Christmas lights round her blink | none |
| 18 | Murray Bauman | glasses, bald, a vodka bottle | flamethrower (fire) | takes a swig of vodka | none |
| 19 | Bob Newby | RadioShack shirt, glasses | none | draws a map of the tunnels | none |
| 20 | Mr. Clarke | science teacher's cardigan | none | draws on the board | none |
| 21 | Benny Hammond | diner apron, beard | none | serves a plate of fries | none |
| 22 | Dr. Owens | suit, glasses | none | none | none |

**Allies (4)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 23 | Kali | punk: dark eye make-up, leather | illusions (lightning, violet `spell`) | a ghostly illusion shows up next to her and fades | none |
| 24 | Suzie | big glasses, braces | none | talks into her ham radio | none |
| 25 | Alexei | Russian scientist's coat | none | sips a cherry Slurpee | none |
| 26 | Yuri | smuggler's furs | none | eats peanut butter from a jar | none |

**Season 5's Wheelers (2)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 27 | Holly Wheeler | about ten, blonde, *A Wrinkle in Time* under her arm | none | waves to Mr. Whatsit, who appears next to her for a moment (a friendly man in a cardigan) and is gone | none |
| 28 | Karen Wheeler | blonde perm, dressing gown, a glass of wine | broken wine bottle (saber), as in her season 5 fight with the Demogorgon | sips her wine | none |

**HEM (last hero)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 29 | HEM | Hellfire Club t-shirt, cap, walkie-talkie on his belt | nail bat (saber) | swings the bat onto his shoulder |

### Villains (16)

Vecna comes first for the skeleton.

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Vecna | tall, vine-covered skin, long claws, `bulk` | mind power (lightning, red `rings`) | raises a hand, and the vines writhe | none |
| 2 | One (Henry Creel) | the lab orderly's whites, blond | telekinesis (lightning, red `rings`) | his fingers twitch and a clock chimes; for a moment the whites flicker into Mr. Whatsit's cardigan and kind smile, then back | none |
| 3 | The Mind Flayer | a towering spider of black smoke, `bulk`, `canSit: false` | tendrils (saber) | its legs spread across the sky | none |
| 4 | The Democlawgon | no face; its head opens like a flower, `canSit: false` | claws (saber) | its face opens and shuts | none |
| 5 | Dr. Brenner | white hair, suit | none | holds out his hand | "Hello, Eleven." |
| 6 | Billy Hargrove | mullet, lifeguard's red, sunglasses | fists (saber) | lowers his sunglasses | none |
| 7 | Grigori | Russian hitman, moustache, leather coat | pistol (bullet) | none | none |
| 8 | Jason Carver | letterman's jacket | pistol (bullet) | none | none |
| 9 | Mayor Kline | sleazy suit, big grin | none | waves to the crowd | none |
| 10 | Dr. Kay | military officer (season 5) | pistol (bullet) | none | none |
| 11 | Lieutenant Colonel Sullivan | army uniform | rifle (bullet) | none | none |
| 12 | Connie Frazier | Department of Energy suit | pistol (bullet) | none | none |

**Small fry, as agents only (4):** a Demodog, **Dart** (Dustin's pet), a Demobat, a flayed rat. Ids 13 to 16, all in `agentOnly`.

**Claude's side:** the heroes (the default).

### Telling them apart

- **Vecna and One** are the same person in two forms: Vecna's grey-red vines against One's bright white uniform. They're **rivals** (`Universe.rivals`), so they never lead two sessions back to back.
- **Next to Stevie Clawdberg's Goonies:** the Party have walkie-talkies, Eleven her pink dress, Dustin his cap. Nobody looks like Chunk or Mikey.
- **Robin and Steve** both wear Scoops Ahoy in season 3; Steve is drawn in his season 2 jacket instead.
- **Holly and Max** (both small, light-haired at a glance): Holly is blonde with her book, Max red-haired with her skateboard.

### Nemeses (12)

| Hero | Villain | Why |
|---|---|---|
| Eleven | Brenner | Papa |
| Max | Vecna | "Running Up That Hill", season 4 |
| Holly | One | Mr. Whatsit, season 5 |
| Will | the Mind Flayer | its host in season 2 |
| Karen | the Democlawgon | her kitchen fight, season 5 |
| Steve | Billy | their fight, season 2 |
| Hopper | Grigori | season 3 |
| Lucas | Jason | season 4 |
| Nancy | Mayor Kline | she uncovers his story at the paper, season 3 |
| Joyce | Dr. Kay | season 5's military hunt |
| Owens | Sullivan | season 4 |
| Kali | Connie Frazier | Brenner's people |

### Left out of the cast

- **Troy, Tommy H., Angela:** bullies with no signature.
- **Victor Creel, Enzo:** too little to draw, or no clear look.
- **The Flayed and the season 3 flesh monster:** see Tone.

## Places (16)

All keys start with `hawkins`, so none clash with another universe (checked with `grep -rn 'Location("' Sources/App/Universes`). The first is the default.

| # | Key | Place | Still | Moving | Tall (screen saver) |
|---|---|---|---|---|---|
| 1 | `hawkinsBasement` | **The Wheelers' basement** (default) | the D&D table, the old couch, Eleven's blanket fort, the stairs | the lamp flickers, the dice tray rattles | shelves of boxes, the stairs going up |
| 2 | `hawkinsByers` | **The Byers' living room** | the alphabet painted on the wall, Christmas lights strung over it | the lights blink letter by letter | wood panelling, a ceiling light |
| 3 | `hawkinsLab` | **Hawkins National Laboratory** | a cold corridor, the Gate room, a "RESTRICTED" sign | fluorescent tubes flicker | the Gate's crack in the wall above |
| 4 | `hawkinsUpsideDown` | **The Upside Down** (home of the rare flip, see Mechanics) | Hawkins in blue-grey, vines over everything | spores float, red lightning | the Mind Flayer's storm cloud |
| 5 | `hawkinsStarcourt` | **Starcourt Mall** | neon, the fountain, Scoops Ahoy | neon flickers, the fountain splashes | the atrium's skylights |
| 6 | `hawkinsArcade` | **The Palace Arcade** | rows of cabinets, MADMAX on the high-score screen | the screens flash | neon signs above |
| 7 | `hawkinsCabin` | **Hopper's cabin** | a box of Eggos, the TV, a tripwire across the door | TV static | the trees round it |
| 8 | `hawkinsCastleByers` | **Castle Byers** | the fort in the woods made of blankets and boards, "FRIENDS ONLY" | leaves fall | the forest |
| 9 | `hawkinsCreel` | **The Creel house** | a haunted, empty 1950s house | lightbulbs flicker, a clock ticks | the dark upstairs |
| 10 | `hawkinsMind` | **Vecna's mind** | a red sky, floating debris, the grandfather clock | debris drifts, the clock's pendulum | the red sky |
| 11 | `hawkinsTrailer` | **Eddie's trailer** | the Forest Hills trailer, a guitar on the wall | a string of lights sways | the trees and the night sky |
| 12 | `hawkinsKamchatka` | **Kamchatka** | the Russian prison in snow, the Demogorgon pit | snow falls | guard towers |
| 13 | `hawkinsVoid` | **Eleven's void** | black, with a thin sheet of water on the floor | ripples spread | endless black |
| 14 | `hawkinsPool` | **Hawkins Community Pool**, by day | the pool, the lifeguard's chair, sun loungers | the water glints | the high board, a clear blue sky |
| 15 | `hawkinsSnowBall` | **The Snow Ball** | the school gym with balloons, crepe paper and paper snowflakes | the mirror ball turns | streamers hanging from the ceiling |
| 16 | `hawkinsBennys` | **Benny's Burgers** | the counter, a grill, booths | the grill sizzles | the menu board |

A mix of day (the pool, the mall, Benny's) and night, with the Upside Down's blue-grey, Vecna's red, Kamchatka's snow and the void's black standing apart. Keep the floor band plain and mid-to-dark everywhere so white outlines and labels read; the Christmas lights and neon stay above the crew.

**Left out:** Camazotz and the Abyss (season 5; not enough known about their look, and Vecna's mind covers Camazotz's red memories), Lenora Hills and Surfer Boy Pizza (only Argyle would live there), the police station (Hopper's home is his cabin).

### Homes

| Place | Heroes | Villains |
|---|---|---|
| Wheelers' basement | Mike, Nancy, Holly, Karen, Barb, Suzie (on the radio), HEM | |
| Byers' living room | Joyce, Jonathan, Bob | |
| Hawkins Lab | Dr. Owens, Kali (where she was "Eight") | Brenner, Connie Frazier, Dr. Kay, Sullivan |
| The Upside Down | | the Democlawgon, the Mind Flayer, Demodog, Dart, Demobat, flayed rat |
| Starcourt Mall | Steve, Robin, Erica, Derek, Alexei | Mayor Kline, Grigori |
| Palace Arcade | Max | |
| Hopper's cabin | Hopper, Eleven | |
| Castle Byers | Will | |
| Creel house | | One |
| Vecna's mind | | Vecna |
| Eddie's trailer | Eddie, Argyle | |
| Kamchatka | Murray, Yuri | |
| Eleven's void | | (nobody: she visits it) |
| Community Pool | | Billy, Jason |
| Snow Ball | Lucas, Dustin, Mr. Clarke | |
| Benny's Burgers | Benny | |

## Mechanics that make it its own universe

1. **The ride: BMX bikes** (`Ride.bikes`, in `Ride.drives`). The Party race in along the ground with walkie-talkie aerials and headlamps, skid to a stop, and the crew hops off or on.
2. **Compaction mechanic: taken to the Upside Down** (`HawkinsTaken.swift`). The lights flicker, and the leader is pulled backwards into a wall that stretches like a membrane. A moment later they come back, slimy and with spores in their hair; the caption reads **THE UPSIDE DOWN**. It uses the `abductees` clock with an effect of its own, the way Clawdberg's `OutaTime` does. Limited to the ones who've been there: **Will, Eleven, Max, Holly, Nancy, Steve, Robin, Eddie.**
3. **Habits:**
   - **Nosebleed:** after Eleven wins a fight, she wipes her nose with the back of her hand.
   - **Vecna's clock:** while Vecna is on stage, now and then a hero stops still and a ghostly grandfather clock appears behind them for a moment, then fades. Eerie, not frightening.
   - **The babysitter:** now and then Steve walks over and stands near the Party kids, bat on his shoulder, keeping an eye on them.
4. **Bespoke drills:** Eleven crushes a soda can with her mind (her training with Hopper); the Party roll a big d20; Steve practises his bat swings. **No meditation:** nobody floats cross-legged.
5. **The flip: "Upside Down, literally"** (below).

### The flip: "Upside Down, literally"

Your idea, 2026-10-17: a rare random event where the Upside Down really is upside down.

**What you see:**
- Now and then, when the crew arrives at **`hawkinsUpsideDown`**, the whole scene slowly turns over, as if the picture flipped on its horizontal axis, in about **1.5 seconds**.
- Then the place and everyone in it are **upside down**: the crew walks along the ceiling, the vines hang upwards, the spores "fall" up, the Mind Flayer's storm cloud is at the bottom.
- After **30 to 60 seconds**, or as soon as the crew moves on, it turns back the right way up, with the same half-turn.

**How rare:** a random event, about **1 in 10 arrivals** at the Upside Down. Tune the exact chance once it's seen in the build: rare enough to be a "did you see that?!" moment.

**Where:**
- **Only in window mode and the screen saver**, where the place fills the frame.
- **Never in desktop mode** (the crew stands on the bottom edge of your screen; there's no ceiling to walk on), and never in a Clawd Royale desktop scene.

**What stays readable:**
- Names and speech bubbles are drawn **upright**, under the characters' feet (which is now "above their heads").
- The AI-colour outline follows on its own, since it's drawn round the sprite.
- **Clicks on characters** use the flipped coordinates, so they land on who you clicked.

**The art:** the Upside Down is drawn so it reads both ways up: a floor band and a "sky" band that both hold up, and a tall screen-saver version whose upper part (the storm cloud), now at the bottom, still looks right.

**The engine work (phase 4):**
- `HawkinsFlip.swift` (in the universe's folder) decides when the flip starts and ends, and the half-turn's progress.
- A **scene-wide upside-down flag** in the app's own drawing: the window (`Overlay.swift`, `windowMode` at `:133`) and the screen saver (`SaverView.swift`, crew laid out at `:385`). It's one vertical flip of the place and the crew together, with text drawn upright and click hit-testing flipped.
- Those two files are the maintainer's (`CONTRIBUTING.md`). Built from a fork, the PR describes what the flag needs instead.

#### Kept secret in public

The flip is a surprise for people to find. It is **never mentioned or shown** in:
- the README;
- `llms.txt`;
- the showcase repo;
- the roster and locations sheets (`Tools/RenderDocs`);
- the social preview (`Tools/MakeSocial`);
- the trailer's storyboard;
- the trailer.

The **CHANGELOG** only says "the Upside Down, with a surprise or two". The Upside Down itself is listed as a place like any other, drawn the right way up, so nothing hints that it can turn over.

#### Testing it while building

You asked for this explicitly: the flip is secret in public, but while it's being built it has to be easy to see and check that it works as intended.
- **Preview:** a `--flipped` switch for `place` (`build/preview place out.png "Stranger Clawds" --flipped`) draws the Upside Down both ways up side by side, with a crew standing on it and their labels showing.
- **Edges:** `build/preview edges` covers the flipped state too, so nothing is cut off at the frame's new "floor".
- **The Playground** in the app gets a hidden trigger that starts the flip at once, to watch the half-turn, the 30 to 60 seconds upside down and the turn back. For the build and checking only; never documented in public.
- **In the app, check that:**
  - the flip comes up at about the planned rate (roughly 1 in 10 arrivals);
  - it **never** fires in desktop mode or Clawd Royale's desktop scenes;
  - names and speech bubbles are upright and readable;
  - clicks on characters land where they should while flipped;
  - the screen saver's tall version reads upside down;
  - it turns back when the crew leaves mid-flip.

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one. A `CHANGELOG.md` entry each phase (the flip's entry stays vague, see above).

1. **Skeleton:**
   - settle the raw value first (see Context);
   - the universe case and all the wiring above;
   - Eleven, Mike and Dustin, and Vecna (the enums' first cases);
   - the Wheelers' basement, the menu icon, HEM's costume, Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with plain wipes (`case .starWars, .hawkins: return nil` in `ComicTransition.pick`).
2. **Core ensemble.** About 20 characters:
   - the rest of the Party, Steve, Nancy, Jonathan, Robin, Hopper, Joyce;
   - One, the Mind Flayer, the Democlawgon, Brenner, Billy;
   - 8 places: the basement, the Byers' living room, the Lab, the Upside Down (right way up for now), Starcourt, Hopper's cabin, Vecna's mind, the Creel house; with homes and nemeses for these.

   The enum cases can go in first as stand-ins and be drawn in a second commit, as The Clawd Files did.
3. **The rest:** all 45 characters and all 16 places, every home filled in. Ends with **the character audit**: every weapon, shot, motion, signature and callout checked against the show and this plan, a mismatches table for your OK. Re-check two things flagged at the roster: **Will's season 5 power** (its look and colour) and **Derek Turnbow's look**.
4. **Mechanics:** the bikes, Taken to the Upside Down, the three habits, the bespoke drills, and **the flip**: `HawkinsFlip.swift`, the scene-wide flag in the window and the screen saver, upright labels, flipped clicks, the Upside Down's art reading both ways up, and **all of its tests** (Preview `--flipped`, `edges` flipped, the hidden Playground trigger, the in-app checks above), shown to you before phase 5.
5. **Transitions:** the ten `HawkinsTrip`s and the Christmas-lights finishing touch, through `ComicTransition`.
6. **Polish pass** (always before docs): every weak spot noted in phases 2 to 5, split by file and fixed in parallel, with before-and-after renders for your OK.
7. **Docs and release:**
   - README (universe table column, screen-saver paragraph, a collapsible cast-and-places section, developer notes), `llms.txt` (universe list, folder and prefix, the compaction mechanic), **none of them mentioning the flip**;
   - `Tools/RenderDocs`: a `hawkinsLineup` desktop strip, `roster-stranger-clawds.png`, the locations sheet (the Upside Down the right way up) and a social preview; `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - the trailer, `REEL=hawkins`, without the flip;
   - flip `isReleased` if it was built on `main`;
   - **needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

**Weak spots to expect** (note them as they come up, fix them in the polish pass): the Party's kids all the same height and blurring together; Eleven's nosebleed and Eggo at agent size; Holly's book and Mr. Whatsit's flicker reading at 72×52; Vecna's vines and claws against the frame rule; the Mind Flayer's smoke legs (see-through edges must be solid or faint, never half-opaque); the void and Vecna's mind too dark or too red for outlines; the Christmas-lights lettering too small at window size; the Upside Down's art when flipped.

## Verification

- **Build:** `./build.sh`. The cast-size `precondition` in `Overlay.swift:180` catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` for slow type-checks before calling a phase done.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Eleven"`;
  - `build/preview fight out.png "Steve Harringclawd" "The Democlawgon"`;
  - `build/preview place out.png "Stranger Clawds"`;
  - `build/preview edges out.txt "Stranger Clawds"`: everything it lists must be on purpose (shots, Lucas's slingshot stones, Max's skateboard kick-off);
  - and the batch sheets, one per Art file. Look at the PNGs before showing them.
- **The flip** (phase 4 onwards, every phase after):
  - `build/preview place out.png "Stranger Clawds" --flipped`: the Upside Down both ways up, crew and labels upright and readable;
  - `build/preview edges` with the flipped state;
  - the hidden Playground trigger in the app: the half-turn, the 30 to 60 seconds, the turn back, the turn back when the crew leaves;
  - in the app: about 1 in 10 arrivals, never in desktop mode or Clawd Royale's desktop scenes, clicks landing on the right character, the screen saver's tall version.
- **Pull request guard:** `python3 scripts/pr-guard.py main stranger-things` before any PR.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> hawkinsBasement hawkinsUpsideDown`.
- **In the app:**
  - Settings → Universe → Stranger Clawds: sessions are heroes, subagents include villains and the small fry;
  - the screen saver's Options list it;
  - Random and Clawd Royale reach it.
- **Taken to the Upside Down:** `/compact` in a session led by Eleven or Will.
- **Before release:** grep the README, `llms.txt`, the showcase repo and the rendered docs for any mention or picture of the flip. There must be none.

## Transitions (`HawkinsTrip`, 10)

| # | Name | What happens | Comes up more with |
|---|---|---|---|
| 1 | **The Title** (signature opening, longest and rarest) | In the dark, red neon letters slide in from the edges to a synth pulse and lock together. The camera then pushes through the gap in a letter, into the new place. | Eleven, Mike |
| 2 | **The Flip** | The old place drains to the Upside Down's blue-grey. Vines creep over it and spores rise. Then it splits like a membrane, onto the new place. | Will · turf: Upside Down |
| 3 | **The Gate** | A red, glowing crack splits the screen from top to bottom, pulses, and opens wide, showing the new place through it. | Brenner, Owens · turf: Lab |
| 4 | **Walkie Static** | Static lines and "DO YOU COPY? OVER." The picture tunes in through the noise onto the new place. | Mike, Dustin, Suzie · turf: basement |
| 5 | **The Void** | Everything goes black, with a thin sheet of water on the floor. The new place shows as a reflection in the water and rises out of it. | Eleven, Kali · turf: the void |
| 6 | **The Storm** | A red storm cloud rolls in, and the Mind Flayer's spider shape looms in it. Lightning, and the clouds part onto the new place. | the Mind Flayer, Will · turf: Upside Down |
| 7 | **Vecna's Clock** | The grandfather clock fills the screen and chimes four times. The glass cracks more with each chime, and on the fourth it shatters onto the new place. | Vecna, One · turf: Vecna's mind, the Creel house |
| 8 | **Natural 20** | A giant d20 tumbles across the screen, stops on **20**, flashes, and the new place appears in the flash. | Eddie, Mike, Dustin, Lucas · turf: trailer, basement |
| 9 | **Fireworks** | Fireworks burst across the dark (the battle of Starcourt), and the new place lights up in their glow. | Steve, Robin, Erica, Dustin · turf: Starcourt |
| 10 | **Insert Coin** | An arcade screen fills the picture: GAME OVER, "INSERT COIN", and the new place loads like the next level. | Max, Dustin · turf: the arcade |

"The Flip" (#2) is a transition into a place; it has nothing to do with the secret flip mechanic, and it's fine to show in public.

**Finishing touch: Joyce's Christmas lights.** After every transition, the new place's name is spelled out letter by letter in blinking bulbs over the painted alphabet, the way Will talks to Joyce from the Upside Down. Check the lettering reads at window size.

**Style:** pixel art in Upside Down blue-grey and red, 80s neon, the warm yellow of the Christmas lights, with a little grain on the Title and Walkie Static. Nothing painted or glossy; no fine detail that won't read at pixel scale.

**Left out:**
- "Running Up That Hill": a copyrighted song. Vecna's Clock gives the same feeling.
- Camazotz and the Abyss: not enough known about their look.
- A D&D map: Stevie Clawdberg's map route and Clawd of the Rings' map already use one, so this universe has the dice.
- The Russian code: too fine to read.

## Promo: the trailer (`REEL=hawkins`)

Built on `doctorShots`, about 45 to 50 seconds, rendered with the app's own sprites, places and transitions. Storyboard first, for your OK. **The flip never appears, in the storyboard or the video.**

- **Intro (~9 s): The Title.** Darkness, a synth pulse. Red neon letters slide in from the edges and lock together into **STRANGER CLAWDS** in our own lettering; the glow swells, and the camera pushes through the gap in a letter into the Wheelers' basement. Sound: synth arpeggios and a low pulse, in our own notes.
- **Set piece (~9.5 s): the battle of Starcourt.** Night at the mall, neon flickering. The Mind Flayer looms at the skylights; the Party fire fireworks at it (the Fireworks transition's look), Steve and Robin in their Scoops Ahoy hats, Dustin cheering. Eleven steps forward, her nose bleeds, she raises her hand, and the monster recoils into its smoke. Caption: "Friends don't lie."
- **Hook (4 s):** shared.
- **Desktop (~4.6 s):** `brawl(ctx, .hawkins, …)`: "Something is living in your build folder."
- **Status (~4.2 s):** four characters, one per state; the aside: "Mornings are for coffee."
- **Agents (4 s):** "Every subagent gets to join the Party."
- **Window (~4.8 s):** `windowShot(ctx, .hawkins, …, at: .hawkinsBasement)`, the Christmas lights spelling the place's name: "The lights will tell you where."
- **AIs (~4.4 s):** the BRING YOUR OWN AI* line-up, one character per AI.
- **End card (~4.2 s):** the Wheelers' basement, the crew lined up, the title lands in neon, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS", the app icon and the GitHub URL.

No logo or melody is copied: the title is our own lettering, and the music only evokes the synth sound.

## Sources

- [Stranger Things 5 episode 8 ending explained (Netflix Tudum)](https://www.netflix.com/tudum/articles/stranger-things-5-episode-8-ending-explained)
- [Stranger Things finale ending explained (AOL)](https://www.aol.com/articles/stranger-things-finale-ending-explained-120000962.html)
- [Linda Hamilton's Dr. Kay (Inverse)](https://www.inverse.com/entertainment/stranger-things-season-5-linda-hamilton-dr-kay-villain)
- [Stranger Things season 5 new characters, ranked (Soap Central)](https://ww4.soapcentral.com/shows/stranger-things-season-5-new-characters-ranked-from-scene-stealer-forgettable)
- [Stranger Things finale: Holly's ending (The Hollywood Reporter)](https://www.hollywoodreporter.com/tv/tv-features/stranger-things-finale-holly-ending-nell-fisher-interview-1236462724/)
- [Chapter Two: The Vanishing of Holly Wheeler (Wikipedia)](https://en.wikipedia.org/wiki/Chapter_Two:_The_Vanishing_of_Holly_Wheeler)
- [Did Max and Holly escape from Camazotz? (Soap Central)](https://bravo-www.soapcentral.com/shows/stranger-things-season-5-part-2-did-max-holly-escape-camazotz-details-revealed)
- [Mrs. Wheeler vs. the Demogorgon (Popverse)](https://www.thepopverse.com/tv-stranger-things-5-mrs-wheeler-vs-demogorgon-cara-buono/)
- [Stranger Things 5: Cara Buono interview (Netflix Tudum)](https://www.netflix.com/tudum/articles/stranger-things-5-cara-buono-interview)

## Decisions (2026-10-17)

All the gates are passed:
- **Name: Stranger Clawds.** Puns: Sinclawd, Harringclawd, Munclawd, the Democlawgon; everyone else by name.
- **Scope:** all five seasons, no spin-offs.
- **Size:** a limited experience, accepted: 45 with HEM and the four small fry.
- **Raw value:** settled at build time, after checking `main`, the open branches, the forks, Superclawdtural and Battleclawd Galactica.
- **Roster:** approved, with Holly Wheeler (a major part of season 5) and Karen Wheeler (her wine-bottle fight) added at your request.
- **Places and homes:** the 16 approved; the void is nobody's home.
- **Mechanics:** the BMX bikes, Taken to the Upside Down, the nosebleed, Vecna's clock and babysitter habits, the drills, no meditation.
- **The flip:** your idea. Rare and random, window and screen saver only, **secret in all public material**, and **fully testable while building** (Preview `--flipped`, `edges`, a hidden Playground trigger, the in-app checks).
- **Transitions:** the ten above, opening with The Title, finished with Joyce's Christmas lights.

The plan is ready for phase 1 when you say start.
