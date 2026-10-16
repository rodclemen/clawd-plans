# Plan: a new universe, Clawd Trek (Star Trek parody)

## Context

Clawd Clash has six universes. This plan adds a Star Trek parody as a full ensemble, the same way Doctor Clawd covered every Doctor. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

| Universe              | Heroes | Villains | Total | Places | Transitions |
|-----------------------|--------|----------|-------|--------|-------------|
| Star Clawds           |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds      |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds      |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd          |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files       |     36 |       46 |    82 |     20 |          10 |
| Stevie Clawdberg      |     64 |       54 |   118 |     23 |          10 |
| Clawd Trek (proposed) |     53 |       47 |   100 |     21 |          13 |

(heroCount includes HEM; villainCount includes agent-only.)

- **Name: Clawd Trek** (chosen on 2026-10-16).
- **Scope:** the Original Series, The Next Generation, Deep Space Nine, Voyager, and the ten films made with those crews (The Motion Picture to Nemesis). Enterprise, Discovery, Picard, Strange New Worlds, Lower Decks and the 2009–2016 films are left out by default; see Open questions.
- **Code naming** follows the other universes:
  - `case clawdTrek` with key `"clawdTrek"`.
  - Folder `Sources/App/Universes/ClawdTrek/`, file prefix `Trek…`.
  - Branch `star_trek`.
- **Raw value:** the next free one when its build starts (Buffy is planned as 6); ids are rawValue*1000 and permanent.
- **Naming style:** light puns on the on-screen names (Captain James T. Quirk, Mr. Spawk, Captain Jean-Luc Pinchard). A near-spelling beats a forced pun. Actors' names are never used. Species are misspelt lightly, the way Doctor Clawd has Dalicks and Sontarons: the Borgg, the Gawn, the Jem'Hadda.
- **Size:** **100 characters**: 53 heroes including HEM and one agent-only pet, and 47 villains including 3 agent-only. Plus **21 places**. That sits next to Doctor Clawd (98).
- **Viability:** comfortably clears the bar. 51 heroes and 44 villains can lead a session, so nothing repeats too often. Star Trek is one of the deepest casts there is: the hard part was choosing, not finding.
- **Claude's side:** the heroes (Starfleet and friends), as in every universe since Doctor Clawd.
- **Tone:** Star Trek is mostly optimistic, so very little has to go. Left out:
  - **Armus** (the tar creature that kills Tasha Yar): its whole point is cruelty.
  - **Gul Madred** ("There are four lights"): a torturer.
  - **The Vidiians:** they harvest organs.
  - **Lon Suder:** a murderer, played straight.
  - **The Ceti eels:** ear-crawling body horror.
  - **The Intendant** (Mirror Kira): sexualised. Mirror Spawk represents the Mirror Universe on his own.
  - Seven of Nein and Lt. Uhurrah are drawn in their uniforms (silver suit, red duty dress), never sexualised.

## How a universe plugs in (checked against main, ebc02be, on 2026-10-16)

**New code: `Sources/App/Universes/ClawdTrek/`**
- `TrekRoster.swift`:
  - `enum TrekVillain` and `enum TrekHero`, append-only, with `hem` as the last hero.
  - The persona dictionaries, `.reduce([.hem: hemPersona(.clawdTrek)])`, as `ClawdbergRoster.swift` does.
  - `Location.trekHome(of:)`, `trekNemeses`, the ride closure, `let trekTheme = Theme(...)`.
  - The `static let` place keys and `let trekPlaces` merged from the Places files.
- `Art/TrekHeroes1…6.swift` and `Art/TrekVillains1…5.swift`, about 8–10 personas per file. Shared helpers (the uniform tunic, the combadge, the Vulcan ear, Klingon ridges, the bat'leth) go in one `TrekKit.swift` with `trek`-prefixed names, as `ClawdbergKit.swift` does. Uniforms come up in almost every sprite, so a shared kit pays here more than anywhere.
- `Places/TrekScenes1…N.swift` as `let trekPlacesN: [Location: Place]`.
- `TrekIcon.swift`: the menu bar icon, 28×26, colour and mono. A starship silhouette seen from above (a saucer and two nacelles), drawn our own way rather than as the real ship's outline.
- `TrekRides.swift`: the transporter, the Bird-of-Prey and the Borgg beam (see Mechanics).
- `TrekAssimilation.swift`: the compaction mechanic (see Mechanics).
- `TrekDrills.swift`: the bespoke drills.
- `TrekWipes.swift`: the transitions, last.

**Wiring into the existing code.** Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎. Copy what `clawdberg` did in each spot.
- **`Sources/Shared/Universe.swift:8–33`:** the case, `key`, `title` ("Clawd Trek"), `villainCount` (47), `heroCount` (53).
- **`Universe.swift:44–52`:** `agentOnly`: Spot, the tribbel, the vole and the targh (global ids).
- **`Universe.swift:58`:** `claudeSide` stays the default (heroes).
- **`Universe.swift:61`:** `rivals`: Pinchard and Locutus (the same man, so never back to back).
- **`Universe.swift:66–79`:** the TNG senior staff go in `abductees` for assimilation (see Mechanics), with a doc comment like the other two.
- **`Sources/App/Theme.swift:47`:** `Theme.of`.
- **`Sources/App/Locations.swift:74`:** `.merging(trekPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift:12, 16, 26, 36–38`:** `nil` in phase 1; a `.trek(TrekTrip)` case in `duration`, `draw` and `pick` in phase 5, and the doc comment.
- **`Sources/App/Universes/Hem.swift:27, 87, 101, 121, 143, 180`:** HEM's costume in every switch: a gold command tunic with a combadge, a communicator on his belt and a phaser.
- **`Sources/App/Rides.swift`:** new `Ride` cases `.transporter`, `.birdOfPrey`, `.borgBeam` in `drawRide` (phase 4).
- ⚠︎ **`Sources/Saver/SaverView.swift:79, 89, 214`:** the Options doc comment, the choices list and the trip switch (`case "clawdTrek": …`).
- ⚠︎ **`Sources/App/Drills.swift:54`:** add `clawdTrek` to the meditation guard. Vulcans meditate, but sitting on the floor, never floating; that goes in a bespoke drill instead.
- ⚠︎ **`Drills.swift:488`:** `.merging(trekBespokeDrills)`.
- ⚠︎ **`Sources/App/Overlay.swift:865`:** the Playground prompts. Five in-universe ones:
  - "Make it so: refactor the warp core module"
  - "Run a level-3 diagnostic on the test suite"
  - "Scan the logs for life signs"
  - "Reroute auxiliary power to the build"
  - "Boldly delete the code no one has touched before"
- ⚠︎ **`Overlay.swift:1113, 1226`:** how clawdberg hooked in its set piece and its OutaTime effect. Assimilation draws in the same place (line 1226); the Borgg link habit (if approved) hooks into the tick next to line 1113.
- ⚠︎ **`Sources/Shared/StatusStore.swift`, `Sources/App/HookInstaller.swift`:** nothing new, as assimilation reuses the missing-time clock. Check it anyway.
- ⚠︎ **`Sources/App/Pose.swift`, `Habits.swift`:** decide whether Clawd Trek joins each universe-specific `if`.
- **Clawd Royale** picks the new cast and places up through `Universe.allCases`. Check that the menu bar icon and arch-enemies still hold when the scene is a Clawd Trek place.
- **Tools:**
  - `Tools/Preview/main.swift:60–93`: the batch names (`trekHeroes1…`), the universe lookup and the enum lookups.
  - `Tools/Transitions/main.swift:12, 122`: the `clawdTrek` branch (phase 5).
  - `Tools/RenderPromo` (`REEL=trek`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase` in phase 6.

## Cast

How the engine's weapons map onto Star Trek:
- **The phaser** is `.blaster` + `.beam(core:glow:)`, a continuous ray, the main weapon on the hero side. The colour follows the era, which also helps tell the crews apart:
  - **Original crew and Pique:** pale blue-white. The Original Series was inconsistent (mostly blue, sometimes red); blue is what most fans picture for it.
  - **Next Generation onwards:** orange-red, which the later shows used almost without exception.
- **Disruptors** are `.blaster` + `.energy`: bolts, not a ray, so villains' fire reads differently from a phaser:
  - **Klingon:** red-pink bolts.
  - **Romulan:** green bolts.
  - **Cardassian:** an amber-yellow beam (`.beam`, it's a phaser of theirs).
  - **Jem'Hadda:** blue plasma bolts.
  - **Brean, Kazon, Hirogen:** check each colour on screen in phase 3; the sources disagree.
- **The bat'leth** and other blades and fists are `.saber`: Wharf, Martoc, Gowrun, Jadzia Dacks, Korr.
- **Godlike powers** are `.lightning` + `Magic`, each with its own look (the list after the villains).
- **`armoured: true`** for the Borgg (shots ricochet off their shields once they've adapted), the Gawn, Species 8472 and Nomadd.
- **Uniform colours** do the heavy lifting against Star Clawds, the other sci-fi universe: nobody there wears a coloured tunic with a badge. Within the universe they also sort the crews: Original Series gold (command), blue (science), red (operations); TNG red (command), gold (operations), teal-blue (science); DS9 and Voyager have the same colours with grey-black shoulders.

### Heroes (53)

**The original crew, with the films (11)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Captain James T. Quirk | gold command tunic, brown hair | phaser (blue) | the two-fisted hammer blow, then dusts off his tunic |
| 2 | Mr. Spawk | blue tunic, black bowl cut, pointed ears, upswept brows | phaser (blue) | raises one eyebrow; the Vulcan salute |
| 3 | Dr. McCloy | blue tunic, scowl | none | waves his medical scanner and shakes his head |
| 4 | Mr. Scuttly | red tunic, moustache | phaser (blue) | thumps a console back into life |
| 5 | Lt. Uhurrah | red duty dress, silver earpiece | phaser (blue) | a hand to her earpiece, "Hailing frequencies open" |
| 6 | Lt. Suloo | gold tunic | fencing foil (melee) | a fencing flourish ("The Naked Time") |
| 7 | Ensign Checkoff | gold tunic, mop-top hair | phaser (blue) | raises a finger: it was invented in Russia |
| 8 | Nurse Chapple | blue medical dress, blonde updo | none | a hypospray hiss |
| 9 | Captain Pique | the older tan-and-gold tunic, square jaw | laser pistol (red beam) | stares at the viewscreen; a Talosian illusion flickers round him |
| 10 | Ambassador Sareck | Vulcan robes, grey hair | none | the Vulcan salute, slowly |
| 11 | Lt. Saavyk | maroon films jacket, Vulcan ears | phaser (blue) | sits at the Kobayashi Maru chair, unbothered |

**The Next Generation (14)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 12 | Captain Jean-Luc Pinchard | red command tunic, bald | phaser (orange) | tugs his tunic straight; a facepalm now and then |
| 13 | Commander Will Rikker | red tunic, beard | phaser (orange) | swings a leg over a chair to sit (the famous move) |
| 14 | Lt. Cmdr. Datum | gold tunic, pale gold skin, yellow eyes | phaser (orange) | tilts his head, then plays a few bars on a violin |
| 15 | Lt. Cmdr. Geordi La Forje | gold tunic, silver VISOR across the eyes | phaser (orange) | the VISOR sweeps a scan line |
| 16 | Lt. Wharf | gold tunic, Klingon ridges, sash, long hair | bat'leth (melee) | a bat'leth kata, then a growl |
| 17 | Counsellor Deanna Troix | plum jumpsuit, big dark curls | none | a hand to her temple: "I sense…" |
| 18 | Dr. Beverly Clawsher | blue tunic, red hair, blue lab coat | none | opens a medical tricorder, it chirps |
| 19 | Wesley Clawsher | the rainbow jumper | none | tinkers with a tricorder; it sparks |
| 20 | Lt. Tasha Yarr | gold tunic, short blonde hair | phaser (orange) | a martial-arts stance |
| 21 | Guinanne | huge round hat, flowing robes | none | the hands-up claw stance she aims at Q |
| 22 | Lt. Reg Barclawy | gold tunic, hunched | none | stammers and fidgets; a puff on an inhaler |
| 23 | Ensign Ro Larren | red tunic, Bajoran nose ridges, ear chain | phaser (orange) | folds her arms, unimpressed |
| 24 | Lwaxana Troix | towering hairdo, bright gown | none | holds out a gift box to whoever's nearest |
| 25 | Hugh | a freed Borgg drone, one implant, gentle face | none | puts a hand to his chest, "I am Hugh" |

**Deep Space Nine (14)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 26 | Captain Benjamin Sizko | red DS9 uniform with grey shoulders, bald, goatee | phaser (orange) | tosses his baseball up and catches it |
| 27 | Major Kyra Nerys | rust Bajoran uniform, short red hair, nose ridges, ear chain | phaser (orange) | hands on hips; the Bajoran ear chain glints |
| 28 | Constable Oddo | tan uniform, smooth unfinished face, slicked hair | morphing arm (melee) | melts into a puddle of orange gel and reforms |
| 29 | Lt. Jadzia Dacks | teal-shouldered uniform, spots down the temples, long ponytail | bat'leth (melee) | twirls a bat'leth and grins |
| 30 | Dr. Julian Basher | teal-shouldered uniform, dark hair | none | throws a dart |
| 31 | Chief Miles O'Bryan | gold-shouldered uniform, toolkit | phaser (orange) | bangs a panel with a spanner |
| 32 | Quarck | Ferengi ears, loud waistcoat | none | counts bars of gold-pressed latinum |
| 33 | Romm | Ferengi ears, engineer's overalls | none | fumbles a tool, then fixes the thing |
| 34 | Nogg | Ferengi ears, Starfleet cadet uniform | phaser (orange) | snaps a salute |
| 35 | Jake Sizko | civilian jacket, a padd | none | scribbles on his padd |
| 36 | Elim Garrak | Cardassian neck ridges, tailor's tunic | Cardassian phaser (amber) | holds up a measuring tape, smiling too much |
| 37 | General Martoc | Klingon armour, one eye patch | bat'leth (melee) | raises a mug of bloodwine |
| 38 | Morn | big grey lumpy alien at the bar | none | drains his drink; never says a word |
| 39 | Vic Fountaine | tuxedo, a slight holographic shimmer | none | snaps his fingers and croons (music notes) |

**Voyager (10)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 40 | Captain Kathryn Janeweigh | red-shouldered uniform, auburn bun | phaser (orange) | sips from a coffee mug |
| 41 | Commander Chakotai | red-shouldered uniform, forehead tattoo | phaser (orange) | opens a medicine bundle |
| 42 | Lt. Tuvoc | gold-shouldered uniform, Vulcan ears, dark skin | phaser (orange) | steeples his fingers |
| 43 | B'Elanna Torrez | gold-shouldered uniform, Klingon ridges | phaser (orange) | kicks a console that won't behave |
| 44 | Lt. Tom Parish | red-shouldered uniform | phaser (orange) | puts on Captain Proton's rocket helmet (black and white for a moment) |
| 45 | Ensign Harry Kimm | gold-shouldered uniform, young | phaser (orange) | plays a clarinet |
| 46 | The Holo-Doc | blue-shouldered uniform, receding hairline, holographic shimmer | none | sings an aria (music notes) |
| 47 | Neelicks | Talaxian, mottled orange-and-yellow scalp, loud patterned clothes | none | stirs a bubbling pot |
| 48 | Kess | small, blonde crop, Ocampa ears | telepathy (rings, gold) | a cup lifts and floats in front of her |
| 49 | Seven of Nein | silver-blue suit, Borgg eyepiece, hair up | phaser rifle (orange) | arches a brow: "Irrelevant." |

**Friends of the Federation (2)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 50 | The Horta | round orange-brown rocky blob, `canSit: false` | acid (melee) | burrows into the floor and pops up; burns NO KILL I into the floor |
| 51 | Zefram Clawchrane | scruffy 2060s jacket, wild hair | none | dances to the jukebox |

**Agent-only (1)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 52 | Spot | Datum's orange tabby cat | none | curls up on a console |

**HEM (1)**, as in every universe, last: a gold command tunic with a combadge, a communicator on his belt and a blue-beam phaser.

**Callouts** (`Persona.callout`) for the leads:
- Quirk: "Beam me up!"
- Spawk: "Fascinating."
- McCloy: "I'm a doctor, not a crab!"
- Scuttly: "She cannae take it!"
- Uhurrah: "Hailing frequencies open."
- Checkoff: "Nuclear wessels!"
- Pinchard: "Make it so." and "Engage!"
- Rikker: "Shields up!"
- Datum: "Intriguing."
- Wharf: "A good day to die!"
- Troix: "I sense deception."
- Sizko: "I can live with it."
- Kyra: "Not on my station."
- Oddo: "Quarck!"
- Quarck: "Profit!"
- Garrak: "Plain, simple Garrak."
- Martoc: "Qapla'!"
- Vic Fountaine: "Pallie!"
- Janeweigh: "Coffee. Black."
- Tuvoc: "Indeed."
- Holo-Doc: "State the emergency."
- Seven of Nein: "Irrelevant."
- Hugh: "I am Hugh."
- Clawchrane: "Let's rock 'n' roll!"
- Morn has no callout: that's the joke.

### Villains (47)

**The Borgg (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Borgg Drone | pale grey skin, black armour, tubes, a green eye laser | assimilation tubules (melee), `armoured` | turns its head; the green eye laser sweeps |
| 2 | The Borgg Queen | pale head and shoulders over a black body, cables at the neck | assimilation (touch, green) | her head lowers onto her body, the way she arrives in First Contact |
| 3 | Locutus | Pinchard in Borgg armour, red eye laser, one implant | tubules (melee), `armoured` | turns slowly to the viewer: "Resistance is futile." |

**Original Series villains (12)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 4 | Kahn Noonien Singe | big grey mane, open-chested Ceti Alpha leathers | phaser, melee | clenches a fist and glares; quotes at you |
| 5 | The Gawn | green lizard, gold faceted eyes, silver tunic, `bulk`, `armoured` | thrown rocks (`.thrown`, grey) | lifts a boulder over its head |
| 6 | Harry Mudde | curly hair, moustache, frilly shirt | none | rubs his hands; holds up a gadget for sale |
| 7 | Trelayne, Squire of Gothos | Regency coat, ruffled cravat | powers (sparkles, pink) | flourishes a duelling pistol, then sulks |
| 8 | Commander Korr | Klingon, gold sash, swept brows (no ridges, as in the Original Series) | disruptor (red-pink) | laughs, hands on hips |
| 9 | The Romulan Commander | grey Romulan uniform, cropped hair, shoulder pads | disruptor (green) | a cool smile over folded arms |
| 10 | Balock | small, bald, friendly face, holding a scary puppet head | none | swaps his face for the puppet's glare, then offers a drink |
| 11 | Nomadd | floating grey probe with a glowing slit, `.hover`, `canSit: false`, `armoured` | steady ray (cold cyan) | scans: "You are the creator." |
| 12 | The Salt Vampire | shaggy grey, sucker-fingered creature | sucker fingers (melee) | reaches for the salt cellar; eerie, never grisly |
| 13 | Mirror Spawk | Spawk with a goatee, sash, dagger | phaser (blue), knife | strokes his beard |
| 14 | Gary Mitchel | silver eyes, gold tunic | lightning (forked, silver) | his eyes flash silver |
| 15 | The Talosian Keeper | bald head with throbbing veins, shimmery robe | illusion (rings, peach-pink) | the veins on his head pulse |

**Film villains (4)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 16 | Commander Krudge | Klingon armour, long hair, with his pet targ | disruptor (red-pink) | pats his targ |
| 17 | General Chaang | Klingon, bald, an eye patch bolted on | disruptor (red-pink) | taps his eye patch; quotes Shakespeare |
| 18 | Dr. Tolian Sorran | grey hair, long coat | disruptor (red-pink) | checks his pocket watch, eyes on the sky (the Nexus) |
| 19 | Shinzonn | bald, black Reman armour, pale | disruptor (green) | glares from a throne-like chair |

**Next Generation villains (10)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 20 | Q | red Starfleet captain's tunic or judge's robes, smug | the snap (touch, white-blue flash) | snaps his fingers and vanishes, then reappears behind someone |
| 21 | Lorr | Datum's face, gold tunic, a sneer | phaser (orange) | grins wickedly, a twitch of the head |
| 22 | Commander Tomalack | Romulan, grey uniform, swept hair | disruptor (green) | hands behind his back, smug |
| 23 | Commander Selah | Romulan, blonde, Tasha's face | disruptor (green) | a cold stare |
| 24 | Lursah | Klingon, big hair, leather armour | disruptor (red-pink) | raises a goblet |
| 25 | B'Ettor | Klingon, big hair, leather armour (a different colour from her sister) | disruptor (red-pink) | finishes her sister's sentence |
| 26 | Professor Moriartee | Victorian frock coat, top hat | none | sketches the holodeck arch on paper |
| 27 | The Crystalline Entity | huge glittering snowflake, `.hover`, `canSit: false` | steady ray (prismatic white) | spins and chimes |
| 28 | DaiMon Bokk | Ferengi, red-brown armour | Ferengi energy whip (melee) | holds up a coin and hisses |
| 29 | A Pakkled | bulky padded suit, round face | none | "We look for things." |

**Deep Space Nine villains (10)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 30 | Gul Dukatt | Cardassian armour, neck ridges, slicked hair | Cardassian phaser (amber) | spreads his arms like a friend; his eyes flash red (the Pah-wraith) |
| 31 | Weyoon | Vorta, pale, ridged ears, purple tunic | none | a too-pleased smile, hands clasped |
| 32 | The Founder Leader | the Female Changeling, smooth orange-gold face | morphing arm (melee) | melts into gel and reforms |
| 33 | Jem'Hadda Soldier | grey bumpy skin, horn ridges, a white tube at the neck | rifle (blue bolts) | shrouds: fades to nearly invisible, then back |
| 34 | Kai Wynne | Bajoran vedek robes and tall hat | none | a pious smile, hands together |
| 35 | Legate Damarr | Cardassian armour | Cardassian phaser (amber) | drinks kanar from the bottle |
| 36 | Liquidator Bront | Ferengi in an FCA suit | none | waves a writ: "Profit forbidden!" |
| 37 | Grand Nagus Zekk | old Ferengi, tall headdress, cane with a gold head | none | leans on his cane and cackles |
| 38 | A Brean Soldier | refrigeration suit, snout-like helmet | rifle (colour to check) | a crackle of static where its voice should be |
| 39 | Chancellor Gowrun | Klingon, robes, wide staring eyes | bat'leth (melee) | his eyes widen and bulge |

**Voyager villains (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 40 | Species 8472 | tall cream-coloured alien, long head, `armoured`, `bulk` | claws (melee) | a telepathic shimmer round its head |
| 41 | Maj Culluh | Kazon, tangled hair crest, ragged armour | rifle (colour to check) | thumps his chest |
| 42 | Seskah | Cardassian disguised as Bajoran, then herself | Cardassian phaser (amber) | peels off her Bajoran nose ridges |
| 43 | The Hirogen Alpha | huge, armoured, mask, `bulk` | rifle (colour to check) | hangs a trophy on his belt (a helmet) |
| 44 | Doctor Chaoticka | all black and white, cape, high collar | death ray (grey beam) | raises his arms: "Spaceship of DOOM!" |

**Agent-only small fry (3).** Like the MSE-6, these only ever appear as agents:
- 45, **a tribbel** (a ball of fur that purrs and multiplies);
- 46, **a vole** (the Cardassian vole Quarck hates);
- 47, **a targh** (the Klingon hog-dog).

### Powers, each with its own look

No two characters here draw their power alike, and none copies a power from another universe (the Pusher's and Gibson's purple rings, E.T.'s red fingertip):
- **Q:** `touch`, white-blue: the snap is a white flash at his fingers, and a glow round whoever he points at.
- **The Borgg Queen:** `touch`, green: the glow creeps up the target like circuit lines.
- **Trelayne:** `spell`, pink: a ribbon of sparkles.
- **Gary Mitchel:** forked lightning, silver-white with a cold grey glow.
- **The Talosian Keeper:** `rings`, peach-pink, slow and pulsing like his veins.
- **Kess:** `rings`, gold, quick.
- **Nomadd:** steady ray, cold cyan, from its glowing slit.
- **The Crystalline Entity:** steady ray, prismatic (white core, shifting pink-blue glow).
- Oddo and the Founder Leader both morph an arm into a whip, but Oddo's gel is tan-gold and the Founder's is brighter orange with a liquid sheen.

### Nemeses (25)

Each pair faces off on the same stage:
- Quirk ↔ Kahn
- Spawk ↔ Mirror Spawk
- McCloy ↔ the Salt Vampire (it took the face of his old flame)
- Uhurrah ↔ Nomadd (it wiped her memory)
- Suloo ↔ General Chaang
- Pique ↔ the Talosian Keeper
- Pinchard ↔ Q
- Rikker ↔ Commander Tomalack
- Datum ↔ Lorr
- La Forje ↔ Dr. Sorran
- Wharf ↔ Lursah and B'Ettor
- Yarr ↔ Commander Selah (her daughter, from another timeline)
- Barclawy ↔ Professor Moriartee
- Janeweigh ↔ the Borgg Queen
- Seven of Nein ↔ the Borgg Drone
- Sizko ↔ Gul Dukatt
- Kyra ↔ Kai Wynne
- Oddo ↔ the Founder Leader
- Quarck ↔ Liquidator Bront
- Garrak ↔ Legate Damarr
- Martoc ↔ Chancellor Gowrun
- Chakotai ↔ Seskah
- Parish ↔ Doctor Chaoticka
- Kess ↔ Species 8472
- the Holo-Doc ↔ the Hirogen Alpha

**Rivals:** Pinchard and Locutus never lead back to back: they're the same face.

### Telling sprites apart

Inside the universe:
- **Same-uniform crews.** Many officers share a tunic colour, so each needs one strong extra: Spawk's ears and bangs, Datum's gold skin, La Forje's VISOR, Wharf's ridges and sash, Rikker's beard, Pinchard's bald head, Suloo's foil, Checkoff's mop-top.
- **Datum and Lorr** share a face: Lorr gets a sneer and a slightly different hair part. **Pinchard and Locutus**: Locutus is mostly armour, with a red eye laser. **Yarr and Selah**: Selah is in grey Romulan uniform with Romulan brows.
- **Vulcans vs Romulans:** Romulans get a V-shaped forehead ridge and grey shoulder pads.
- **Lursah and B'Ettor:** different armour colours, mirrored poses.
- **The Klingon men** (Korr, Krudge, Chaang, Gowrun, Martoc): Korr has no ridges (Original Series style), Chaang has the bolted eye patch, Martoc the cloth one, Gowrun the robes and eyes, Krudge the targ.

Against the other universes (they meet in Clawd Royale):
- **The Borgg vs Doctor Clawd's Cyberpersons:** Cyberpersons are all silver; the Borgg are pale skin, black armour, tubes and green light.
- **The Gawn vs Silurean, Sea Devvil and the Lizzard:** the Gawn gets the gold faceted eyes, silver tunic and bulk.
- **The Talosian Keeper vs the Clawd Files' Grey:** the Talosian is pale pink with veins and a shimmery robe; the Grey is grey with black eyes.
- **Datum vs Clawdberg's Data** (the Goonie): the name is why he's Datum.
- **Quirk vs Clawdberg's Captain Clawk:** different names, and nothing alike to look at.
- **The transporter vs the Clawd Files' abduction beam:** the transporter is a column of sparkles where the person stands, with no ship and no cone of light.

## Places (21)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. Keys are all prefixed `trek` so they can't clash with any universe, now or planned.

| # | Key | Place | Still | Moving | Tall-canvas extras |
|---|---|---|---|---|---|
| 1 | `trekBridge` | **The Enterprise bridge (Original Series):** the default | red rail, the captain's chair, bright primary-coloured consoles | buttons blink, stars drift on the viewscreen | the domed ceiling and its ring of lights |
| 2 | `trekBridgeD` | **The Enterprise-D bridge** | wood-trim rail, beige carpet, the wide viewscreen | orange-and-lilac LCARS panels flicker, warp streaks on screen | the curved ceiling and the tactical arch |
| 3 | `trekTransporter` | **The transporter room** | the pads in a ring, the console | a pad shimmers now and then | the ceiling emitters glowing |
| 4 | `trekWarpCore` | **Main engineering** | the warp core, the master display table | the core pulses blue up and down | the core rises out of sight above |
| 5 | `trekTenForward` | **Ten Forward** | the bar, the slanted windows | stars stream past outside | more windows, a passing ship |
| 6 | `trekHolodeck` | **The holodeck** | yellow grid on black, the arch | the grid flickers into a scene (foggy London, a lounge) and back | the grid running up the walls |
| 7 | `trekPromenade` | **The Promenade, Deep Space Nine** | Quark's bar front, the upper walkway | the dabo wheel spins, lights chase | the upper level and its curved windows |
| 8 | `trekOps` | **Ops, Deep Space Nine** | Cardassian ribs, the round ops table, the office up the stairs | console lights, the turbolift rising | the dark Cardassian ceiling ribs |
| 9 | `trekWormhole` | **The wormhole, outside the station** | the station's rings against space | the wormhole blooms open, swirls blue-white, closes | the station's docking pylons tower |
| 10 | `trekVoyager` | **Voyager's bridge** | the compact grey-blue bridge, the captain's chair | screens flicker, stars on the viewscreen | the ceiling and its skylight |
| 11 | `trekSickbay` | **Voyager's sickbay** | biobeds, the office window | readouts beep, a hologram flickers | overhead scanners |
| 12 | `trekBorgCube` | **Inside a Borgg cube** | walls of alcoves, pipes, green light | green lights pulse, a drone shifts in its alcove | the shaft going up forever |
| 13 | `trekGreatHall` | **The Great Hall, Qo'noS** | the throne, banners, a stone floor | braziers flicker | the vaulted roof in firelight |
| 14 | `trekRomulus` | **Romulus** | green skyline, tall spires | green clouds drift, ships cross the sky | the twin planet in the sky |
| 15 | `trekArena` | **The arena rocks** (the Gawn duel) | the leaning sandstone slabs, a blue sky | dust blows, the Metron glow on the horizon | the tall slanted rocks |
| 16 | `trekGothos` | **Trelayne's castle, Gothos** | a dark stone hall, a harpsichord, a mirror | the fire crackles, candles flicker | the gloomy vaulted ceiling |
| 17 | `trekCetiAlpha` | **Ceti Alpha V** | Kahn's wrecked cargo pods in the sand | a sandstorm blows | the bleached, howling sky |
| 18 | `trekRuraPenthe` | **Rura Penthe** | the Klingon ice-prison yard, a mine shaft | snow blows, prisoners' lamps sway | the ice cliffs |
| 19 | `trekVeridian` | **Veridian III** | Sorran's rocket platform on a rocky ridge | the Nexus ribbon ripples across the sky | the crashed saucer section on the horizon |
| 20 | `trekBozeman` | **Bozeman, 2063** | the missile silo, the Phoenix rocket inside, Clawchrane's bar | the jukebox lights, a searchlight sweeps | the rocket's nose rising out of the silo |
| 21 | `trekGuardian` | **The Guardian of Forever** | the stone ring among ruins on a dead planet | flashes of history roll through the ring | a purple sky and toppled columns |

**Homes:**
- **Original crew:** the Original Series bridge (Quirk, Spawk, McCloy, Scuttly, Uhurrah, Suloo, Checkoff, Chapple, Pique, Sareck, Saavyk).
- **TNG:** the Enterprise-D bridge (Pinchard, Rikker, Troix, Wharf, Yarr, Ro, Clawsher, Wesley); main engineering (Datum, La Forje); Ten Forward (Guinanne, Lwaxana, Spot); the holodeck (Barclawy); the Borgg cube (Hugh).
- **DS9:** Ops (Sizko, Kyra, Oddo, Dacks, O'Bryan); the Promenade (Quarck, Romm, Nogg, Jake, Basher, Garrak, Morn); the holodeck (Vic Fountaine); the Great Hall (Martoc).
- **Voyager:** the bridge (Janeweigh, Chakotai, Tuvoc, Torrez, Parish, Kimm, Neelicks, Seven of Nein); sickbay (the Holo-Doc, Kess).
- **Friends:** the arena rocks (the Horta); Bozeman (Clawchrane).
- **Borgg:** the cube (Drone, Queen, Locutus, and Lorr, who led rogue Borgg; Species 8472).
- **Klingons:** the Great Hall (Korr, Krudge, Gowrun, the targh); Rura Penthe (Chaang); Veridian III (Lursah, B'Ettor, Sorran).
- **Romulans:** Romulus (the Romulan Commander, Tomalack, Selah, Shinzonn).
- **Original Series oddities:** Kahn on Ceti Alpha V; the Gawn at the arena; Trelayne on Gothos; Mudde and Mirror Spawk in the transporter room; Balock and Nomadd on the Original Series bridge; the Salt Vampire, Gary Mitchel and the Talosian Keeper at the Guardian's ruins; the tribbel on the Original Series bridge.
- **TNG oddities:** Q on the Enterprise-D bridge; Moriartee on the holodeck; the Crystalline Entity at the wormhole; Bokk on the Promenade; the Pakkled in main engineering.
- **Dominion and Cardassia:** Dukatt, Damarr and the vole in Ops; Weyoon, the Founder Leader, the Jem'Hadda and the Brean at the wormhole; Kai Wynne, Bront and Zekk on the Promenade.
- **Voyager's foes:** Culluh and Seskah on Voyager's bridge; the Hirogen and Chaoticka on the holodeck.

## Mechanics that make it its own universe

1. **Rides.** Three new `Ride` cases in `Rides.swift`:
   - **Heroes beam in and out by transporter** (`.transporter`). There's no ship: a column of sparkles rises where they stand. The colour follows the era: gold sparkles for the Original Series crew, a blue-white swirl for TNG, DS9 and Voyager. The ride closure picks the variant.
   - **Klingons arrive by Bird-of-Prey** (`.birdOfPrey`): it decloaks with a shimmer, its wings swing down, a ramp drops.
   - **The Borgg beam in green** (`.borgBeam`): the same idea as the transporter, but a green, angular, blocky effect, so it can't be confused with Starfleet's.
   - Everyone else walks on, as in the other universes.
2. **Assimilation, which is Clawd Trek's regeneration.** When a Claude Code or pi session led by one of the **TNG senior staff** (Pinchard, Rikker, Datum, La Forje, Wharf, Troix, Dr. Clawsher) compacts its context, the Borgg take them for a moment:
   - green circuit lines creep over them, black armour plates and an eyepiece snap on, an eye laser sweeps, and RESISTANCE IS FUTILE types itself out above them;
   - for Pinchard, the peak frame is Locutus himself;
   - a beat later the implants clank off, and they shake their head. Same session, same face.

   Losing your context and becoming part of a collective fits compaction, and the Borgg are TNG's great enemy, so the group is a clear one. It reuses the missing-time clock (`SessionRecord.abducted`, `missingTimeLength`), as Clawdberg's OutaTime does; the list goes in `Universe.abductees` and the effect is drawn in `TrekAssimilation.swift`, hooked in where the overlay draws OutaTime (`Overlay.swift:1226`).
3. **Habits:**
   - Oddo sits by melting into his bucket when his session idles.
   - The Jem'Hadda shroud: now and then they fade almost to nothing and come back.
   - Q pops out in a white flash and reappears somewhere else on the stage.
   - Borgg drones walk straight past anyone who isn't a threat (they don't start fights with idle characters).
   - Morn never says anything, even when leading a session (no callout).
   - **Tribbels** (decided 2026-10-16): now and then a hatch over the stage pops open and tribbels pour out onto whoever stands below (Quirk, if he's there), purring, then roll off. A habit, not a trailer beat.
   - **The Collective (decided: yes, in phase 4, if it stays cheap; needs new engine code):** when a Borgg leads a session, its subagents show a thin green link line back to their leader, the Collective. Nothing like this exists yet (`Theme` has no leader-specific agent hooks), so it would be new code in the overlay's tick. If it turns out costly, it is dropped rather than bending the engine for it.
4. **Bespoke practice drills:**
   - Wharf runs his bat'leth calisthenics programme;
   - Datum plays the violin; Pinchard plays his Ressikan flute; Rikker plays the trombone;
   - Spawk and Tuvoc meditate, sitting on the floor with a candle (no floating);
   - Suloo fences;
   - Quarck counts latinum;
   - Seven of Nein regenerates in an alcove (green glow);
   - Neelicks cooks;
   - the Horta tunnels.

   Nobody floats cross-legged in meditation (`Drills.swift:54`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one.

1. **Skeleton:**
   - the universe case, theme and Universe wiring;
   - Captain Quirk, Mr. Spawk and the Borgg Drone (the first enum cases);
   - the Original Series bridge, the menu icon, HEM's costume, the saver option and Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with plain wipes for now.
2. **Core ensemble.** About 38 characters:
   - the rest of the original crew and the TNG crew;
   - the Borgg Queen and Locutus, Kahn, the Gawn, Q, Korr, the Romulan Commander, Lorr, Tomalack, Lursah and B'Ettor;
   - Sizko, Kyra, Oddo, Quarck, Dukatt and the Founder Leader;
   - 8 places (the two bridges, the transporter room, engineering, Ten Forward, the Borgg cube, the Great Hall, Ceti Alpha V), with the nemeses for these.
3. **Rest of the cast and places.** Up to 100 characters and 21 places, with every home filled in. Ends with **the character audit**: every persona's weapon, shot colour, magic, motion, signature and callout checked against the source and this roster, and a table of only the mismatches.
4. **Mechanics:** the three rides, assimilation, the habits and the bespoke drills.
5. **Transitions:** the thirteen `TrekTrip`s and the LCARS caption (see below).
6. **Docs and release:**
   - the README, roster and location sheets, a desktop line-up and a social preview;
   - `llms.txt`, and a `CHANGELOG.md` entry each phase;
   - a trailer, `REEL=trek`, opening on the signature opening;
   - **Needs your OK first, since it's public:** a showcase repo and a cask in `release.sh`.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber. Enum order follows the tables above, except that the skeleton's three come first (they already do).

## Polish pass (after phase 5, before phase 6)

The weak-spot list is kept at the end of every phase and fixed here, all together, split by file across helpers in their own worktrees, with before-and-after renders for your approval. Likely spots to watch, noted now:
- the Original Series gold vs TNG gold at 72×52: the two golds should be clearly different (TOS is a warmer, greener gold);
- combadges and Ferengi ear details are a few pixels;
- Datum's skin vs plain Clawd orange: gold-white, not orange;
- the Horta's NO KILL I may be too small to read: a short burn mark may have to do;
- the Crystalline Entity's fine crystal arms;
- the holodeck's grid against its scene;
- the warp core's blue against the Borgg cube's green, so the two read as different places on the screen saver.

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` for long type-checks before calling a phase done.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Captain James T. Quirk"`;
  - `build/preview fight out.png "Captain James T. Quirk" "Kahn Noonien Singe"`;
  - `build/preview place out.png "Clawd Trek"`;
  - the batch sheets, one per Art file.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> trekBridge trekBorgCube`.
- **In the app:**
  - Settings → Universe → Clawd Trek: new sessions are Starfleet and friends, subagents can be villains or small fry.
  - The screen saver's Options include it.
  - Random and Clawd Royale reach it.
- **Assimilation:** `/compact` in a Claude session led by a TNG officer; and one led by someone else (nothing happens).

## Transitions (`TrekTrip`, 13)

Each is weighted by who is on screen and where, like `DoctorTrip`.

**Style.** Every transition is drawn in the app's pixel art. The palette is deep space black with the franchise's two looks: the Original Series' bright primaries (red, gold, blue) and the later shows' LCARS colours (orange, lilac, pale blue, peach). Stars are single pixels; glows are stepped, never glossy. No lens flares.

**Ending.** Every transition ends with an **LCARS caption**: a rounded orange-and-lilac bar slides in at the corner with the place's name and a stardate ("STARDATE 41153.7 · TEN FORWARD"), the way a captain's log opens a scene. In Original Series places it's a plainer caption in TOS colours. It replaces the usual place-name label in this universe.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **Space, the Final Frontier** (the signature opening) | Stars drift. A caption types SPACE… and fades. A starship swoops out of the distance, swells past the camera with a whoosh, and its wake pulls the new place in behind it. The longest and rarest. | any time, rarely |
| 2 | **Warp Speed** | The stars stretch into streaks, the picture squeezes towards a point, a flash, and the new place snaps into view as the streaks shrink back to stars. | anyone; trips between far-apart places |
| 3 | **Energise** | The old place breaks into a column of sparkles that rises and fades; the new place sparkles in from the bottom up. Gold for the Original Series, blue-white later. | the transporter room; any Starfleet crew |
| 4 | **On Screen** | The camera pulls back: the old place is on a bridge viewscreen. The screen cuts to the new place and the camera pushes through it. | the bridge crews; the three bridges |
| 5 | **Decloak** | The old place shimmers and turns glassy, fades out; a ship's outline ripples into view and the new place decloaks behind it. | Klingons and Romulans; Romulus, the Great Hall |
| 6 | **Assimilation** | Green circuit lines grow across the picture, it breaks into a grid of cubes, the cubes turn and reassemble as the new place. Only with a Borgg on screen (`needsOwner`). | the Borgg; the cube |
| 7 | **The Snap** | A white flash from the corner, and the new place is simply there, with a puff of sparkle. Only with Q on screen (`needsOwner`). | Q |
| 8 | **Computer, End Program** | The yellow holodeck grid sweeps over the old place, the scene flickers away to bare grid, then a new scene builds up square by square. | the holodeck; Barclawy, Moriartee, Chaoticka, Vic, the Hirogen |
| 9 | **The Wormhole** | A blue-white flower blooms in the middle, swirls open, swallows the picture, and spits it out on the new place before closing. | DS9; the wormhole, Ops, the Promenade |
| 10 | **Red Alert** | Red light pulses, the alert bars flash at the edges, the picture shakes and tilts like a hit to the ship, and it settles on the new place. | Wharf, Klingons, the Jem'Hadda; any fight |
| 11 | **Changeling** | The old place melts into orange-gold gel that runs down, pools, then rises and firms up into the new place. | Oddo, the Founder Leader |
| 12 | **The Guardian** | A stone ring appears; history flickers through it, the camera steps through the ring into the new place. | the Original Series crew; the Guardian's ruins |
| 13 | **The Genesis Effect** | A wireframe planet on a computer screen; a wave of fire races across it and leaves green life in its wake, which becomes the new place. | Kahn, Saavyk; Ceti Alpha V |

**Not used:** the Nexus ribbon (it overlaps warp speed's glow and lives in Veridian III's sky instead); the tractor beam (overlaps the transporter); photon torpedoes (a weapon, not a change of scene); lens flares (from the later films, out of scope and not pixel art); the Mirror Universe (out of scope beyond Mirror Spawk); a tribble avalanche (better as a habit or set piece, see Open questions); and the TNG title's solar system pass (it's folded into the opening).

**Promo.** The opening (#1) is the trailer's title sequence: `REEL=trek` opens on it, the way Doctor Clawd's trailer opens on its time vortex.

**Check them** with `Tools/Transitions`, which renders all thirteen between two Clawd Trek places.

## Promo: the trailer (`REEL=trek`)

Rendered in `Tools/RenderPromo/main.swift`, modelled on the Doctor Clawd trailer, about 45–50 seconds.

- **Intro (~9 s): the signature opening.** Black, then stars. A narrator-style caption types SPACE… and fades. A planet slides by in the corner. The starship (our own pixel design: a saucer and two nacelles) swoops from a dot to filling the frame and past the camera with a whoosh. The stars streak into warp, a flash, and **CLAWD TREK** stretches out of the streaks and settles. The music evokes the opening's sound (a soaring solo voice and a brass fanfare, timpani) but in our own notes.
- **Set piece (~9.5 s): the Borgg board the Enterprise-D.** The bridge, calm. Red Alert. Green beams: three Borgg drones materialise. Wharf fires; the shots ricochet (they've adapted). Pinchard tugs his tunic straight: "Make it so." La Forje changes the frequency, the next shot drops a drone, Datum steps forward, and the ship warps away in a burst of streaks.
- **Desktop:** "Make it so." (brawl, Clawd Trek cast)
- **Status:** four characters, one per state, with "He's dead, Jim." as the error state's aside.
- **Agents:** "Every subagent gets to be a redshirt."
- **Window:** at the Original Series bridge, "Engage."
- **End card:** the Original Series bridge, the crew lined up, the title lands, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS".

No logos or the real ship's outline are copied, and the theme tune isn't reproduced.

## Decisions (2026-10-16)

All the open questions are settled:
- **Name: Clawd Trek.**
- **Scope:** the Original Series, TNG, DS9, Voyager and the classic films, as written. Enterprise, Discovery, Picard, Strange New Worlds, Lower Decks and the 2009–2016 films can come later as an add-on (ids only append).
- **Compaction:** Borgg assimilation of the TNG senior staff, with Locutus as Pinchard's peak frame.
- **The Collective habit:** yes, in phase 4, if it stays cheap.
- **Q** is just Q. **Species 8472** keeps its real number.
- **Tribbles:** yes, as a habit.
- **Swaps:** none; the cast stands as written.

The plan is ready for phase 1 when you say start.