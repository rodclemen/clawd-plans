# Plan: a new universe, Battleclawd Galactica (Battlestar Galactica parody)

## Context

Clawd Clash has seven universes on `main` (d471352, 2026-10-17, after 3.6.0). This plan adds a parody of the 2004 Battlestar Galactica: the miniseries, the four seasons, *Razor*, *The Plan* and the prequel *Caprica*. It's **small and sharp on purpose**: a cult classic, with just enough cast to stay fun. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

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
| **Battleclawd Galactica (proposed)** | **26** | **25** | **51** | **17** | **10** |

(heroCount includes HEM; villainCount includes one agent-only small fry, the Raider pup.)

- **Viability: viable, only just, and small on purpose.** 25 drawn heroes and 24 drawn villains, both over the 20 threshold. The series alone only just reaches 20 villains, because it has only seven humanoid Cylon models and its point is that they look like ordinary people. *Caprica* gives the villains real visual variety (the U-87, the Soldiers of the One, the Ha'la'tha, Daniel Graystone). It's the smallest universe in the app; that was the user's choice: fewer, sharper characters rather than a row of look-alike pilots.
- **Name: Battleclawd Galactica** (chosen on 2026-10-17). The alternatives were Battlestar Clawlactica, Clawlactica and So Say We Clawd.
- **Code naming** avoids the franchise name, as the other universes do:
  - `case fleet` with key `"fleet"`.
  - Folder `Sources/App/Universes/BattleclawdGalactica/`, file prefix `Fleet` (`FleetRoster.swift`, `FleetHeroes1.swift`, `FleetWipes.swift` …). No file in the repo uses `Fleet` as a prefix today. Top-level names start with `fleet` or are `private`, as `scripts/pr-guard.py` asks.
  - Branch `battlestar`. Trailer `REEL=fleet`.
- **Raw value: next free when the build starts.** Check before the skeleton commit: `main` uses 0 to 6 (`middleEarth = 6`); the `buffy` branch claims `slayer = 6`, which clashes and needs renumbering before it merges; Henrik's Clawd Burton lives on his fork (HEM42/clawd-clash) with a value of its own; Superclawdtural (`hunters`) may have taken one by then. Read other branches with `git show <branch>:Sources/Shared/Universe.swift`, never by switching. Ids are rawValue*1000 and permanent.
- **Naming style:** light puns where they read at a glance: Admiral **Adclawma**, **Clawbuck** (Starbuck), President **Clawslin**. Everyone else keeps the on-screen name or callsign (Apollo, Helo, Athena, Cavil, Leoben), because a forced pun is worse than none. Actors' names are never used.
- **Scope:** the 2004 miniseries, seasons 1 to 4, *Razor*, *The Plan* and *Caprica*. *Blood & Chrome* is left out.
- **Size:** 51 characters and 17 places.

### How the cast is split

Heroes are the Colonial fleet and, in *Caprica*, the people who stand against the Soldiers of the One and the mob. Villains are the Cylons who hunt the fleet, the humans who turn on it, and *Caprica*'s fanatics and gangsters. The rule for the grey ones is **what fans remember them for**:
- **Athena → hero.** A Cylon who chooses the fleet; her double **Boomer → villain**.
- **The Final Five split.** Tigh, Tyrol and Anders stay heroes (they fight for the fleet to the end); **Ellen Tigh** and **Tory Foster → villains** (Ellen sells out New Caprica, Tory kills Cally).
- **Gaeta → villain**, as the leader of the mutiny, his arc's peak.
- **Baltar → villain**: President of New Caprica under the Cylons. Head Six is part of his drawing, not a character.
- **Zoe-A → hero.** The first Cylon, but the show is on her side. Her robot body, the **U-87**, is a villain of its own: the menacing chrome prototype as the world sees it.
- **Sam Adama → villain** (a Ha'la'tha hitman), his brother **Joseph → hero**.
- **Daniel Graystone → villain**: the tycoon who builds the Cylons.

### Tone: what's left out, and why

The show is a war story with dark themes. Clawd Clash is a desktop toy, so:
- **Left out entirely:**
  - Gina's story and Lieutenant Thorne (sexual violence), and the Cylon "farms";
  - Starbuck's interrogation of Leoben;
  - Dualla's death;
  - the nuclear attack on the Colonies as a transition or a place (no mushroom clouds);
  - Hera and young Willie Adama (children at the heart of the plot);
  - *Caprica*'s train bombing and Ben Stark, too close to real-world suicide bombing. Sister Clarice and Barnabas are in, but nothing about them touches bombings.
- **No real people:** the show has none.
- **The palette:** gunmetal greys, military olive, CIC amber, Cylon red, Caprica's bright blue-white. It stays apart from Star Clawds' space.

## How a universe plugs in (checked against the code on 2026-10-17, main d471352)

**New code: `Sources/App/Universes/BattleclawdGalactica/`**
- `FleetRoster.swift`:
  - `enum FleetHero` and `enum FleetVillain`, append-only, with `hem` as the last hero.
  - The persona dictionaries, `.reduce([.hem: hemPersona(.fleet)])`.
  - `Location.fleetHome(of:)` for heroes and villains, `fleetNemeses`, the ride closure, `let fleetTheme = Theme(...)`.
  - The `static let` place keys and `let fleetPlaces` merged from the Places files.
- `Art/FleetHeroes1…3.swift` and `Art/FleetVillains1…3.swift`, 8 to 10 personas per file, in the pattern of `ClawdbergHeroes1.swift`. Shared helpers (flight suits, duty blues, deck overalls, Centurion chrome, the red scanner eye) go in one `FleetKit.swift` with `fleet`-prefixed names.
- `Places/FleetScenes1…2.swift` as `let fleetScenesN: [Location: Place]`.
- `FleetIcon.swift`: the menu bar icon, 28×26, colour and mono. Galactica's silhouette head-on, or a Viper.
- `FleetResurrection.swift`: the compaction mechanic (see Mechanics).
- `FleetWipes.swift`: the transitions, last.

**Wiring into the existing code.** Copy what `middleEarth` and `clawdberg` did. Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎.
- **`Sources/Shared/Universe.swift`:**
  - `:9–15` the case; `:17` `key`; `:25` `title`; `:33` `villainCount` (25); `:37` `heroCount` (26);
  - `:50` `agentOnly` (the Raider pup);
  - `:65` `claudeSide` (default false: Claude plays the heroes);
  - `:68` `rivals` (the two Centurions; today it's `self == .starWars ? [0, 1] : []`, so it becomes a switch, which Superclawdtural may already have done);
  - `:90` `abductees`: the seven humanoid Cylon models, the way Clawdberg lists its time travellers;
  - `:106` `isReleased`: return `false` for `.fleet` until phase 6 if it's built on `main`, as Clawd of the Rings was.
- **`Sources/App/Theme.swift:40`:** `Theme.of`. **`:89`** add `raptor` to `enum Ride`. It flies in, so it stays out of `Ride.drives` (`:93`).
- **`Sources/App/Locations.swift:70–72`:** `.merging(fleetPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift`:** in phase 1, add `.fleet` next to Star Clawds in `pick` (`case .starWars, .fleet: return nil`, `:40–62`), as the guide now says. In phase 5, take it out of that line and add a `.fleet(FleetTrip)` case at `:8–13`, in `duration` (`:15–23`), `draw` (`:26–35`) and `pick`, and the doc comment at `:3–6`.
- **`Sources/App/Universes/Hem.swift:15–31, 63–104, 113–118, 130, 203`:** HEM's persona and costume in every switch.
- **`Sources/App/Rides.swift`:** the Raptor's drawing (phase 4), in `drawRide` (`:18`) next to `drawFalcon` (`:182`) and the others.
- ⚠︎ **`Sources/Saver/SaverView.swift`:** nothing to add; the Options list and the trip choice build themselves from `Universe.offered`. Only the doc comment at `:80` names universes.
- ⚠︎ **`Sources/App/Drills.swift:51`:** the meditation guard (`meditates`). Battleclawd Galactica doesn't meditate (see Mechanics), so add `universe != .fleet`. **`:73`** and the bespoke-drill table: merge `fleetBespokeDrills`.
- ⚠︎ **`Sources/App/Overlay.swift:875–878`:** the Playground prompts (five, below), a `case .fleet:` next to `.clawdberg` and `.middleEarth`. **`:1271–1272`** is where `OutaTime` is chosen for `clawdberg` (`MissingTime` is the fallback for everyone else in `abductees`); `FleetResurrection` hooks in the same way, and its caption at **`:1353`**. The Head Six and "So say we all" habits hook into the tick here too.
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`**: decide per universe-specific `if`. Battleclawd Galactica joins none of the existing ones; it adds its own habits.
- ⚠︎ **Compaction:** `StatusStore.swift:341` already marks any leader in `abductees`; check it picks up `.fleet` without changes. `HookInstaller.swift` already registers the hook.
- **Clawd Royale** picks the cast and places up through `Universe.allCases`. Check the menu bar icon and arch-enemies still behave when a scene is in a Battleclawd Galactica place.
- **Tools:**
  - `Tools/Preview/main.swift:64–95`: the batch doc comment, the batch arrays (`fleetHeroes1…`, `fleetVillains1…`), the universe lookup (`"fleet": Theme.of(.fleet).cast`), the enum lookups by case name.
  - `Tools/Transitions/main.swift:13–14` (usage comment) and `:131–133` (the branch that renders this universe's trips, phase 5).
  - Phase 6: `Tools/RenderPromo` (`REEL=fleet`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts** (`Overlay.swift:875`):
1. "Jump the build to the next set of coordinates."
2. "Find out which of the tests is a Cylon."
3. "Plot the deploy on DRADIS and launch the Vipers."
4. "Update the survivors count on the whiteboard."
5. "Run the FOD walk over the warnings."

## Cast

Each entry gives the parody name, look, weapon or motion, signature move and callout. How the engine's weapons map onto the show:
- **`.blaster` + `.bullet`** is the main weapon: Colonial sidearms and rifles. This is a military show.
- **Cylon Centurions** have guns built into their arms: `.blaster` + `.bullet`, `armoured: true`.
- **Raiders** fly (`motion: .fly`, `canSit: false`) and shoot `.bullet`.
- **`.saber`** for the deck crew's wrenches, knives, and fists (Caprica Six, the U-87).
- **`.blaster` + `.thrown(colour)`** for Anders' pyramid ball (red-brown).
- **`.none`** for the talkers, doctors and politicians.
- **No magic at all.** The only "rays" are the Cylons' red scanner eyes, and those are signatures, never weapons.
- **`armoured: true`** for the Centurions, the U-87 and Serge; **`bulk`** for the Heavy Raider.
- Everyone is Clawd in costume on Clawd's four legs, as in every universe; the Raiders and the Heavy Raider are Clawd in a half-living ship, legs folded under as landing gear.

### Heroes (26)

Enum order is the order below. The skeleton's heroes come first.

**The skeleton (3)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Admiral Adclawma | duty blues, glasses, moustache | sidearm (bullet) | works on his model sailing ship | "So say we all!" |
| 2 | Clawbuck (Starbuck) | olive flight suit, blonde, cigar | sidearm (bullet) | lights a cigar and grins | "Nothin' but the rain." |
| 3 | Apollo | flight suit, dark hair, helmet under his arm | sidearm (bullet) | tucks his helmet under his arm, at attention | none |

**Galactica (6)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 4 | Colonel Tigh | eyepatch, bald, duty blues | sidearm (bullet) | swigs from a flask | "Frak!" |
| 5 | Dualla | comms headset, duty blues | sidearm (bullet) | puts a hand to her headset | "Action stations!" |
| 6 | Doc Cottle | white coat, cigarette | none | snaps on a rubber glove | none |
| 7 | Chief Tyrol | orange deck overalls, cap | wrench (saber) | wipes the grease off his hands | none |
| 8 | Cally | orange deck overalls, ponytail | wrench (saber) | none | none |

**The pilots (5)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 9 | Helo | flight suit, big smile | rifle (bullet) | none | none |
| 10 | Athena | flight suit, ATHENA on her helmet | sidearm (bullet) | a flicker of red light in her eyes, for a moment | none |
| 11 | Kat | flight suit, short hair | sidearm (bullet) | none | none |
| 12 | Racetrack | flight suit, dark hair, Raptor pilot | sidearm (bullet) | none | none |
| 13 | Anders | civvies, a pyramid ball | pyramid ball (thrown, red-brown) | bounces the pyramid ball | none |

**The government (4)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 14 | President Clawslin | suit, glasses | none | updates the survivors count on the whiteboard | none |
| 15 | Billy Keikeya | aide's suit, a folder | none | hands over a folder | none |
| 16 | Romo Lampkin | lawyer, round sunglasses, cane | none | strokes his cat | none |
| 17 | Kendra Shaw | Pegasus duty uniform, short hair (*Razor*) | sidearm (bullet) | none | none |

**Caprica (6)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 18 | Joseph Adama | Tauron lawyer's suit | none | none | none |
| 19 | Amanda Graystone | doctor's coat | none | none | none |
| 20 | Agent Duram | grey Global Defence Department suit | pistol (bullet) | holds up his badge | none |
| 21 | Tamara | V-world gunslinger in a duster coat | two pistols (bullet) | spins both pistols | none |
| 22 | Serge | the Graystones' slim, glossy robot butler, `armoured` | none | carries a tray of drinks | none |
| 23 | Zoe-A | V-world avatar, a schoolgirl, dark hair | none | glitches into pixels and back (she's an avatar) | none |

**From *Razor* and *The Plan* (2)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 24 | Young Adama | First Cylon War flight suit, vintage helmet and goggles, clearly younger than the Admiral (*Razor*) | sidearm (bullet) | pushes his goggles up and grins | none |
| 25 | Jean Barolay | Caprica resistance, civvies (*The Plan*) | rifle (bullet) | none | none |

**HEM (the last hero)**
| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 26 | **HEM** | olive flight suit, helmet under his arm, dog tags | sidearm (bullet) | tosses his helmet up and catches it |

### Villains (25)

**The skeleton (1)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Caprica Six | red dress, blonde | fists (saber) | tilts her head | "Are you alive?" |

**The humanoid Cylons (6)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 2 | Brother Cavil | priest's collar, sour face | pistol (bullet) | shrugs with a sneer | none |
| 3 | Leoben | stubble, dark coat | knife (saber) | draws a circle in the air | "All this has happened before." |
| 4 | D'Anna Biers | reporter, camera on her shoulder | pistol (bullet) | films with her camera | none |
| 5 | Simon | doctor's coat | none | none | none |
| 6 | Doral | suit and tie, PR man | none | none | none |
| 7 | Boomer | black tank top, Cylon red glow down her spine | pistol (bullet) | the red glow pulses along her back | none |

**Cylon machines (6)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 8 | Centurion | chrome, the new style, `armoured` | arm guns (bullet) | its red eye sweeps from side to side | none |
| 9 | Old Centurion | silver, First Cylon War, `armoured` | rifle (bullet) | its red eye sweeps | "By your command." |
| 10 | Raider | half-living ship, `fly`, `canSit: false` | guns (bullet) | its red eye sweeps | none |
| 11 | Heavy Raider | wide troop carrier, `fly`, `bulk`, `canSit: false` | guns (bullet) | its hatch opens | none |
| 12 | The Hybrid | in a tank of goo, `canSit: false` | none | babbles, lights blinking | "End of line." |
| 13 | U-87 | Caprica's bulky chrome prototype, `armoured` | fists (saber) | its red eye wobbles uncertainly (Zoe inside) | none |

**Humans (7)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 14 | Admiral Cain | Pegasus greys, short hair | sidearm (bullet) | none | none |
| 15 | Tom Zarek | beard, leather jacket | pistol (bullet) | none | none |
| 16 | Gaeta (the mutiny) | CIC uniform | rifle (bullet) | none | none |
| 17 | Baltar | suit, curly hair, glasses | none | Head Six (a habit, see Mechanics) | "I'm not a Cylon!" |
| 18 | Ellen Tigh | cocktail dress, a glass | none | sips her drink | none |
| 19 | Tory Foster | aide's suit | none | none | none |
| 24 | Colonel Fisk | Pegasus XO's uniform (*Razor*) | sidearm (bullet) | opens his coat, which is full of contraband (cigars, bottles) | none |

**From *Caprica* (4)**
| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 20 | Sister Clarice | headmistress, the Soldiers of the One's ∞ pendant | none | holds up the infinity sign | none |
| 21 | Barnabas | Soldiers of the One rebel | pistol (bullet) | none | none |
| 22 | Sam Adama | Ha'la'tha hitman, Tauron tattoos | knife (saber) | flips the knife | none |
| 23 | Daniel Graystone | tycoon, smart suit | none | holds up the glowing MCP chip | none |

(Colonel Fisk is enum case 24, after Daniel Graystone: he was added last.)

**Small fry, as an agent only (1)**
| # | Name | Look |
|---|---|---|
| 25 | Raider pup | a little Raider, red eye and all, `fly` |

### Telling them apart

- **Athena and Boomer** have the same face. Athena is always in her flight suit with her helmet; Boomer is in the tank top with the red glow down her spine.
- **Young Adama and the Admiral**: the vintage helmet and goggles and a younger face against the glasses, moustache and duty blues.
- **The two Centurions**: the new one is sleek chrome with blade-like hands; the old one is boxy silver with a rifle. They're rivals, so they never lead back to back.
- **The Centurions and Marvelous Clawds' Ultron Sentry** are both chrome robots. The Centurions are known by the red eye sweeping across a black visor.
- **Head Six isn't a separate character:** she's part of Baltar's habit, so she can't be cast alongside him.
- **The pilots** in olive flight suits are told apart by hair and props: Clawbuck's cigar and blonde hair, Apollo's helmet, Helo's smile, Kat's short hair, Racetrack's Raptor patch.

### Nemeses (14)

They face off first when both are on stage:
- Adclawma ↔ Cain (the Pegasus showdown)
- Clawslin ↔ Baltar
- Clawbuck ↔ Leoben
- Apollo ↔ Zarek
- Athena ↔ Boomer (the same model, different choices)
- Tigh ↔ Cavil
- Tyrol ↔ Tory
- Dualla ↔ Gaeta (the mutiny in CIC)
- Kendra ↔ the Hybrid (*Razor*)
- Joseph Adama ↔ Daniel Graystone
- Amanda ↔ Clarice
- Duram ↔ Barnabas
- Young Adama ↔ Old Centurion (the First Cylon War)
- Barolay ↔ Simon

**Rivals:** the two Centurions. **Claude's side:** the heroes (the fleet).

### Left out of the cast

- **More Sixes** (Shelly Godfrey, Natalie, Gina) and a second Doral: the same face again and again; Gina also for tone.
- **Hotdog, Seelix, Hoshi, Crashdown, Narcho:** no signature, and too alike in flight suits.
- **The second Cavil and Simon's family** from *The Plan*: a duplicate, and no clear look.
- **The ancient Hybrid** from *Razor*: too like the Hybrid already in, and her story is about experiments on people.
- **Hera, Willie Adama, Ben Stark:** see Tone.

## Places (17)

Each is a pixel-art backdrop with a still picture, a moving layer and tall extras for the screen saver. Keys start with `fleet` and are unique across all universes (checked with `grep -rn 'Location("' Sources/App/Universes` and the `buffy` branch's `slayer…` keys). The first is the default.

| # | Key | Place | Still | Moving | Tall (screen saver) |
|---|---|---|---|---|---|
| 1 | `fleetCIC` | **Galactica's CIC** (default) | the plotting table, amber DRADIS screens, the hanging ring of monitors | the DRADIS sweep turns, contacts blink | the monitor ring and the catwalk above |
| 2 | `fleetHangar` | **The hangar deck** | Vipers in a row, deck carts, stencilled markings | welding sparks, a Viper's landing lights | launch tubes, cranes |
| 3 | `fleetReadyRoom` | **The pilots' ready room** | rows of chairs, the briefing board, helmets on hooks | the briefing projector flickers | the board with a map of the fleet |
| 4 | `fleetJoes` | **Joe's Bar** | bottles, a bar built from scrap, a card table | a lamp sways, cigar smoke | pipes, a JOE'S sign |
| 5 | `fleetQuarters` | **Adama's quarters** | books, the model ship, the couch, a lamp | the lamp glows, a page turns | bookshelves, wood panelling |
| 6 | `fleetColonialOne` | **Colonial One** | the President's office, the whiteboard tally, a round window | stars drift past the window | the ship's ceiling and the Colonial seal |
| 7 | `fleetRagnar` | **Ragnar Anchorage** | the old armoury in the gas giant's storm, crates of old weapons | purple lightning in the storm outside | the storm clouds |
| 8 | `fleetKobol` | **Kobol** | a rocky forest, ancient ruins, the opera house far off | rain, a hawk circling | tall pines, clouds |
| 9 | `fleetNewCaprica` | **New Caprica** | a tent city in mud, grey sky | rain, puddles rippling | low, heavy cloud |
| 10 | `fleetBasestar` | **A Cylon basestar** | glowing red corridors, a watery data floor, the Hybrid's tank | red light pulses, data ripples through the water | the ship's curved ribs |
| 11 | `fleetResurrection` | **The Resurrection Ship** | rows of tanks of milky goo | bubbles rise in the tanks | more tanks, going up |
| 12 | `fleetPegasus` | **Pegasus** | a harsher CIC in red emergency light | warning lights flash | piping and the battlestar's bulk |
| 13 | `fleetEarth` | **Earth**, from the finale | an African savannah in the sun, flat-topped trees | grass waving, a bird or two | a huge sky |
| 14 | `fleetCapricaCity` | **Caprica City** (the prequel, before the fall) | gleaming towers, a maglev, bright sun | the maglev glides past | more towers and sky |
| 15 | `fleetGraystone` | **Graystone Industries' lab** | the U-87 on its workbench, holobands, screens | sparks, code scrolling on the screens | the lab's glass ceiling |
| 16 | `fleetVWorld` | **V-world, New Cap City** | a noir city of neon and rain, the game's gangsters | neon flickers, rain falls | neon skyscrapers |
| 17 | `fleetLittleTauron` | **Little Tauron** | a Tauron neighbourhood: a bar, market stalls, washing lines | lanterns sway, steam rises | stacked flats |

A mix of the grey ship, the red Cylons, Caprica's gleaming city and noir neon, and New Caprica's mud. Floors stay plain and mid-to-dark so the crew reads; the CIC's monitors, the hangar's Vipers and the city skylines go high and to the sides.

**Not used:** the memorial wall (beautiful, but too sad as somewhere people stand about), the Temple of Five (too fine at pixel scale), Cloud Nine and the pyramid court (nobody would live there), the ruined Earth of season 4 (grey and empty; the finale's savannah stands for Earth).

### Homes

| Place | Heroes | Villains |
|---|---|---|
| CIC | Tigh, Dualla, HEM | Gaeta |
| Hangar | Tyrol, Cally, Racetrack, Young Adama | |
| Ready room | Clawbuck, Apollo, Helo, Athena, Kat | |
| Joe's Bar | Doc Cottle | Ellen Tigh |
| Adama's quarters | Admiral Adclawma | |
| Colonial One | Clawslin, Billy, Lampkin | Zarek, Tory |
| Ragnar | | Leoben, Old Centurion |
| Kobol | | D'Anna (the opera house of her visions) |
| New Caprica | Anders, Barolay | Baltar (its President), Doral |
| Basestar | | Boomer, Centurion, Raider, Heavy Raider, the Hybrid, Raider pup |
| Resurrection Ship | | Cavil, Simon |
| Pegasus | Kendra Shaw | Admiral Cain, Fisk |
| Earth | | (nobody: it's the end of the journey) |
| Caprica City | Amanda Graystone, Duram | Caprica Six, Clarice, Barnabas |
| Graystone lab | Serge | Daniel Graystone, U-87 |
| V-world | Zoe-A, Tamara | |
| Little Tauron | Joseph Adama | Sam Adama |

Earth is nobody's home on purpose; the crew still reaches it on trips and in the screen saver.

## Mechanics that make it its own universe

1. **The ride: a Raptor** (`Rides.swift`, a new `Ride.raptor`). It jumps in with a white FTL flash and a deep boom, hovers, sets down on its skids, and drops off or picks up the crew. Then it lifts and jumps out with the same flash. It flies in, so it's not in `Ride.drives`. Everyone rides it.
2. **Resurrection: the compaction mechanic.** When a Claude Code or pi session led by one of the **seven humanoid Cylon models** (Caprica Six, Cavil, Leoben, D'Anna, Simon, Doral, Boomer) compacts its context, its leader "dies" in a short white flash and wakes in a resurrection tank: bursting up out of the milky goo, gasping and dripping. The caption reads **DOWNLOAD COMPLETE**, and they're back as themselves. A session losing its memory and coming back is exactly how the show's Cylons work. It reuses the clock Clawdberg's 88 mph uses: the seven go in `Universe.abductees`, and `FleetResurrection.swift` draws the effect where the overlay draws `OutaTime` (`Overlay.swift:1271`). Everyone else ignores compaction.
3. **Habits** (`Habits.swift`, the Overlay tick):
   - **Head Six.** Now and then a Six in a red dress appears beside Baltar, leans in and whispers. **Only he sees her:** if another character comes near, she's gone at once. She's drawn as part of Baltar, never a character of her own, so she can't be cast.
   - **"So say we all!"** When the Admiral or the President says it, the heroes nearby raise their fists and echo it. Check in phase 4 whether the engine can do an echo; if not, only the one who started it says the line.
4. **Bespoke practice drills** (`Drills.swift`):
   - the deck crew (Tyrol, Cally, Racetrack): the FOD walk, stooping in a line across the floor to pick up debris, as season 1's episodes open;
   - the pilots: sparring in boxing gloves, from "Unfinished Business";
   - the Centurions: marching on the spot in step.

   Nobody floats cross-legged in meditation (`Drills.swift:51`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one. A `CHANGELOG.md` entry each phase.

1. **Skeleton:**
   - settle the raw value first (see Context);
   - the universe case and all the wiring above;
   - Admiral Adclawma, Clawbuck and Apollo, and Caprica Six (the enums' first cases);
   - Galactica's CIC, the menu icon, HEM's costume, Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with plain wipes (`ComicTransition.pick` returns nil for it).
2. **Core ensemble.** About 25 characters:
   - Galactica's command, the pilots, Clawslin, Billy;
   - the seven humanoid Cylons, the Centurions, the Raider, the Hybrid, Cain, Zarek, Baltar;
   - 8 places: the CIC, the hangar, the ready room, Joe's Bar, Adama's quarters, Colonial One, the basestar, New Caprica; with homes and nemeses for these.

   The enum cases can go in first as stand-ins and be drawn in a second commit, as The Clawd Files did.
3. **The rest:** all 51 characters (the Final Five's villains, *Razor*, *The Plan*, all of *Caprica*) and all 17 places, every home filled in. Ends with **the character audit**: every weapon, shot, motion, signature and callout checked against the show and this plan; a mismatches table for your OK.
4. **Mechanics:** the Raptor, Resurrection, Head Six and "So say we all", the bespoke drills.
5. **Transitions:** the ten `FleetTrip`s, through `ComicTransition`.
6. **Polish pass** (always before docs): every weak spot noted in phases 2 to 5, split by file and fixed in parallel, with before-and-after renders for your OK.
7. **Docs and release:**
   - README (universe table column, screen-saver paragraph, a collapsible cast-and-places section, developer notes), `llms.txt` (universe list, folder and prefix, the compaction mechanic);
   - `Tools/RenderDocs`: a `fleetLineup` desktop strip, `roster-battleclawd-galactica.png`, the locations sheet and a social preview; `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - the trailer, `REEL=fleet`;
   - flip `isReleased` if it was built on `main`;
   - **needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

**Weak spots to expect** (note them as they come up, fix them in the polish pass): the many olive flight suits blurring together; Athena and Boomer; the Cylons' red eye being a single pixel at rest; Adama's model ship and Lampkin's cat at agent size; the Raiders' wings at the frame's edge in flight; the Hybrid's tank against the frame rule; the basestar and Resurrection Ship being too dark or too milky for outlines; Ragnar's lightning flashing across the crew.

## Verification

- **Build:** `./build.sh`. The cast-size `precondition` in `Overlay.swift:180` catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` for slow type-checks before calling a phase done.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Admiral Adclawma"`;
  - `build/preview fight out.png "Clawbuck" "Leoben"`;
  - `build/preview place out.png "Battleclawd Galactica"`;
  - `build/preview edges out.txt "Battleclawd Galactica"`: everything it lists must be on purpose (shots, the Raiders flying in, Anders' ball);
  - and the batch sheets, one per Art file. Look at the PNGs before showing them.
- **Pull request guard:** `python3 scripts/pr-guard.py main battlestar` before any PR.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> fleetCIC fleetBasestar`.
- **In the app:**
  - Settings → Universe → Battleclawd Galactica: sessions are heroes, subagents include villains and the Raider pup;
  - the screen saver's Options list it;
  - Random and Clawd Royale reach it.
- **Resurrection:** `/compact` in a session led by Caprica Six (a villain leads when another AI's session is cast from the dark side, or with Claude's side switched in a test build).

## Transitions (`FleetTrip`, 10)

Each is weighted by who is on screen and where, like `DoctorTrip`.

**Style.** Everything in the app's pixel art. The palette is gunmetal grey, military olive, CIC amber, Cylon red and Caprica's bright blue-white, with grain and a slight handheld shake on Snap Zoom and Galactica Falls. Nothing glossy.

**Finishing touch: none.** The show doesn't caption places.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Cylons Were Created by Man** (signature opening) | The picture goes black. White lines of text appear one by one: "The Cylons were created by man. / They rebelled. / They evolved. / There are many copies. / And they have a plan." Then the whiteboard tally **SURVIVORS: 47,973** ticks down by one, and the new place opens up behind the board. The longest and rarest. | Clawslin, Adclawma |
| 2 | **FTL Jump** | The old place squeezes towards the centre and stretches; a white flash with a boom; the new place pops in. The everyday one. | everyone · turf: CIC, Colonial One |
| 3 | **DRADIS** | The picture turns to DRADIS, amber on black. The sweep line circles, contacts blink, and each turn of the sweep paints in more of the new place. | Dualla, Gaeta, Tigh · turf: CIC |
| 4 | **Cylon Eye** | A Centurion's black visor fills the screen. The red eye sweeps from one side to the other and back; on the last pass it leaves the new place in its wake. | the Centurions, the Raiders · turf: basestar |
| 5 | **Viper Launch** | Inside the launch tube: lights race past, faster and faster; a slam of acceleration; black space; the new place. | Clawbuck, Apollo, the pilots · turf: hangar |
| 6 | **Snap Zoom** | The show's handheld, documentary camera: the frame shakes, snaps in on a corner of the old place, blurs, then snaps back out on the new place. | anyone (no owner) |
| 7 | **Projection** | The Cylons' trick of seeing a place as they choose: the old place breaks into glowing tiles that turn over one by one, showing the new place underneath. | the humanoid Cylons · turf: basestar, Resurrection Ship |
| 8 | **Galactica Falls** | High in the sky over the old place, Galactica jumps in, falls burning through the clouds, launches her Vipers in mid-air, and jumps away in a flash, leaving the new place below. | Adclawma, Apollo · turf: New Caprica |
| 9 | **Holoband** | Caprica's virtual world: red scan lines draw across the screen, the old place fades out, and the new one rezzes in from the lines. | Zoe-A, Tamara, Daniel Graystone · turf: V-world, Graystone lab |
| 10 | **Fleet Pass** | Galactica's huge flank slides across the screen in front of the camera, filling it with plating; when the stern passes, the new place is behind. | Adclawma, Tigh · turf: Pegasus |

**Not used:**
- **The nuclear attack on the Colonies:** tone.
- **A resurrection transition:** it's the compaction effect already.
- **The opera house of the visions:** too fine at pixel scale.
- **"All Along the Watchtower":** a copyrighted song.
- **Starbuck's Viper vanishing over the gas giant:** too like the FTL jump.

**Promo.** The Cylons Were Created by Man (#1) opens the trailer.

## Promo: the trailer (`REEL=fleet`)

Built on `doctorShots`, about 45 to 50 seconds, rendered with the app's own sprites, places and transitions. Storyboard first, for your OK.

- **Intro (~9 s): The Cylons Were Created by Man.** Black. The white lines appear one by one, each with a low drum hit. The last line, "And they have a plan.", holds. The whiteboard: **SURVIVORS: 47,973**, a marker ticks it down by one. The board slides away and **BATTLECLAWD GALACTICA** rises out of a white FTL flash in our own lettering; the camera plunges into the flash. Sound: taiko drums building, a reedy wind lead and a low chant, all in our own notes, never the show's themes.
- **Set piece (~9.5 s): the New Caprica rescue.** Rain over the tent city; Centurions patrol, red eyes sweeping; Anders and Barolay crouch behind crates. Thunder. Above the clouds, a flash: Galactica jumps in, falls burning through the sky, Vipers pouring out of her launch tubes in mid-air (the Galactica Falls transition's look). The Vipers strafe; the Centurions scatter. A Raptor lands (the ride) and the crew runs for it. Galactica jumps away in a flash just above the ground. Caption: "So say we all."
- **Hook (4 s):** shared.
- **Desktop (~4.6 s):** `brawl(ctx, .fleet, …)`: "Some of your agents are Cylons. You'll never guess which."
- **Status (~4.2 s):** four characters, one per state; the aside: "End of line."
- **Agents (4 s):** "Every subagent gets to be a Viper pilot."
- **Window (~4.8 s):** `windowShot(ctx, .fleet, …, at: .fleetCIC)`: "Jump the build. Keep the fleet together."
- **AIs (~4.4 s):** the BRING YOUR OWN AI* line-up, one character per AI.
- **End card (~4.2 s):** Galactica's CIC, the crew lined up, the title lands, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS", the app icon and the GitHub URL. A last FTL boom.

No logo or melody is copied: the title is our own lettering, and the music only evokes the drums, reeds and chant.

## Decisions (2026-10-17)

All the gates are passed:
- **Name: Battleclawd Galactica.** Puns: Adclawma, Clawbuck, Clawslin; everyone else by name or callsign.
- **Scope:** the miniseries, seasons 1 to 4, *Razor*, *The Plan* and *Caprica*; no *Blood & Chrome*.
- **Size:** small and sharp, on purpose. No extra pilots (Hotdog, Seelix, Crashdown…) to pad the count.
- **Raw value:** settled at build time, after checking `main`, the open branches, the forks and Superclawdtural.
- **Roster:** approved, 51 with HEM and the Raider pup, including Young Adama and Jean Barolay (heroes) and Colonel Fisk (villain) from *Razor* and *The Plan*.
- **Places and homes:** the 17 approved; Earth is nobody's home.
- **Mechanics:** the Raptor, Resurrection for the seven humanoid models, Head Six and "So say we all", the FOD walk, boxing and Centurion drills, no meditation.
- **Transitions:** the ten above, opening with The Cylons Were Created by Man.

The plan is ready for phase 1 when you say start.
