# Plan: a new universe, Transclawmers (Transformers parody)

## Context

Clawd Clash has six universes on `main` (ebc02be, 2026-10-16): Star Clawds, Marvelous Clawds, Detective Clawds, Doctor Clawd, The Clawd Files and Stevie Clawdberg. This plan adds a Transformers parody as a full ensemble, built the same way as The Clawd Files. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

- **Name: Transclawmers** (recommended; see Open questions). The alternatives are Clawdbots and Robots in Disguise: Clawd.
- **Scope:** the G1 cartoon (1984–87, seasons 1–4, including the three-part *The Rebirth*) and *The Transformers: The Movie* (1986). Beast Wars is an optional widening, and the live-action films are only an option (see Open questions).
- **Code naming** avoids the franchise name, as the other universes do:
  - `case transclawmers` with key `"transclawmers"`, title `"Transclawmers"`.
  - Folder `Sources/App/Universes/Transclawmers/`, file prefix `Bots…` (`BotsRoster.swift`, `BotsHero`, `BotsVillain`, `botsTheme`, `BotsWipe`/`BotsTrip`).
  - Branch `transformers`. Promo reel `REEL=bots`.
- **Raw value:** the next free one when its build starts (Buffy is planned as 6). Ids are rawValue*1000 and permanent.
- **Naming style:** light puns on the on-screen names (Optimus Prim, Megaclaw, Starscreech, Sunpreener). A near-spelling where no pun works (Ironhyde, Kupp). Actors' names are never used. Nothing here is a real person.
- **Size:** **92 characters**: 51 heroes including HEM, and 41 villains including 5 agent-only. Plus **20 places** and **12 transitions**.
- **Claude's side:** the heroes, the Autobots (`claudeSide` false, as in every universe except Star Clawds).
- **Tone:** the cartoon is already a toy show, so very little has to go. Characters don't die on screen: the movie's deaths (Optimus on his bed, Ironhide's execution, the shuttle massacre, Unicron digesting the Lithones) are left out, and Unicron's belly is gears and conveyor belts, not acid. Mild movie swearing is left out of callouts. Fights are laser-tag silly, like the cartoon: robots get knocked over and get up.

| Universe                   | Heroes | Villains | Total | Places | Transitions |
|----------------------------|--------|----------|-------|--------|-------------|
| Star Clawds                |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds           |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds           |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd               |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files            |     36 |       46 |    82 |     20 |          10 |
| Stevie Clawdberg           |     64 |       54 |   118 |     23 |          10 |
| **Transclawmers (proposed)** | **51** | **41** | **92** | **20** |      **12** |

(heroCount includes HEM; villainCount includes agent-only.)

**Viability: clears the bar easily.** There are well over 20 good heroes and 20 good villains in G1 and the movie alone, all with distinct colours, a clear weapon and, for most of them, a built-in signature move (they transform). The hard part isn't finding characters but choosing: around 300 G1 toys appeared on screen. The rule for picking was the guide's: recognisable as a 72×52 sprite, distinct in colour and silhouette, something to do. That ruled out most of the same-mould repaints (see "Left out").

## Clawd in costume: how a robot stays Clawd

Every character is Clawd, the orange body on four legs. Transclawmers are Clawd wearing robot armour:
- **A helmet with a faceplate:** Optimus's mouthplate and ear antennae, Megatron's bucket, Bumblebee's horns, Shockwave's single eye. The helmet does most of the work of saying who it is.
- **Armour plates in the character's colours** on the chest and back, with **vehicle parts** on top. That's the G1 look: a car's windscreen panes on the chest, wheels at the shoulders, wings on the back for jets, a smokestack for Optimus.
- **The orange body still shows:** along the sides, the belly and the four legs. Plates cover at most the top two-thirds, so Clawd's orange reads in every sprite. Nobody is drawn in Clawd orange armour, so the orange always means "this is Clawd underneath".
- **Four legs, always.** For cars, the four legs are the four wheels, which is what makes the transform work (below).

### The transform (the signature move for most of the cast)

The G1 transform is big, quick and noisy, so it reads well at 72×52. Most characters' signature (`Persona.signature`, 2.5–3.5 s) is a round trip, robot → vehicle → robot. The drawing gets `p.signature` 0…1:
- **0.00–0.25, fold:** the head sinks into the shoulders and the faceplate slides down. The arms swing back flat along the sides. The body drops 4–6 px and stretches 6–8 px longer. A wheel (dark tyre, grey hub) grows over each foot, so the four legs become the four wheels. The chest's windscreen tips up to become the roof. Two white spark pixels flash at the joints on the frames where panels move.
- **0.25–0.75, vehicle:** the car, truck or van silhouette in the character's colours, with orange showing as the chassis and wheel arches. Headlights blink once, it rolls 3–4 px forward and back, and a puff of exhaust comes out the back.
- **0.75–1.00, unfold:** the same moves in reverse, ending on the normal pose with a 1-px hop, the cartoon's "transformed" pose.

Variations:
- **Jets** (Starscreech, Skyfyre, the Seekers): wings slide out from the sides, a nose cone covers the face, it lifts 2–3 px and the legs tuck up into short landing gear.
- **Dinobots and beasts** (Slagg, Snarle, Sludje, Ravidge, Scorpionok, Weirdwulf, Pridaking's lion): a dino or beast head pushes forward and a tail grows out the back. Four-legged animals are a gift: Clawd's four legs simply stay legs.
- **Giants and combiners** don't transform in their signature. They "lock": their limbs flash in their members' colours one by one.

All this is one shared helper in `BotsKit.swift` (`botsFold(c, p, …)` with the vehicle's outline, colours and wheel positions as parameters), so 50 characters don't each re-invent the fold.

**Parked when idle.** A session that's been idle long enough sits. In this universe, characters with a vehicle mode **park in vehicle mode** instead: the drawing checks `p.seated` and draws the frame from the middle of the transform. This needs no engine change, and it's the most "robots in disguise" thing the universe can do: a row of idle sessions becomes a car park.

### Armour without boring fights

Almost everyone here is a robot, but `armoured: true` means "shots ricochet off this one". In the engine it changes 2 of every 11 shot outcomes from a duck to a ricochet (`boltOutcome` in `Fights.swift`); hits still land. If everyone had it, it would stop meaning anything. So:
- **Only 17 characters are armoured:** the giants and the famously tough (Ironhyde, Brawny, Grimlawk, Ultra Magnum, Omega Supremo, Metroplex, Fortress Maximum, Superiorn, Defensa, Megaclaw, Galvaclaw, Devastaclaw, Menacer, Brutalicus, Triptycon, Unicrawn, Scorpionok). A ricochet becomes a "this one's tough" tell.
- **Everyone else ducks, shields and gets knocked over** like any other universe's cast. The cartoon's robots are knocked flat constantly, so that fits.
- **Variety comes from weapons:** about half the cast are rifle shooters (in different shot colours), a third melee (fists, swords, pile drivers, dino bites), and a handful use special powers (magnetism, sound, mind control, time). Giants have `bulk`, so duels stand further apart.

## How a universe plugs in (checked against the code on 2026-10-16, main ebc02be)

**New code: `Sources/App/Universes/Transclawmers/`**
- `BotsRoster.swift`:
  - `enum BotsHero` and `enum BotsVillain`, append-only, with `hem` as the last hero.
  - The persona dictionaries, merged from the Art files with `.reduce([.hem: hemPersona(.transclawmers)])`.
  - `Location.botsHome(of:)` for heroes and villains, `botsNemeses`, the `ride:` closure, `let botsTheme = Theme(...)`.
  - The `static let` place keys (all `bots…`) and `let botsPlaces` merged from the Places files.
- `Art/BotsHeroes1…6.swift` and `Art/BotsVillains1…5.swift`, about 8–10 personas per file, in the pattern of `ClawdbergHeroes1.swift`.
- `BotsKit.swift`: shared drawing helpers with prefixed names: the fold (`botsFold`), wheels, windscreen panes, faceplates, the faction badges.
- `Places/BotsScenes1…3.swift` as `let botsScenesN: [Location: Place]`.
- `BotsIcon.swift`: the menu bar icon, 28×26, colour and mono. A robot head with a faceplate and Clawd's eyes, in our own red insignia style (not the Autobot face).
- `BotsRides.swift`: the Autobot shuttle, Astrotrayne and the space bridge.
- `BotsMatrix.swift`: the Matrix of Leadership effect (the compaction mechanic).
- `BotsDrills.swift`: bespoke drills.
- `BotsWipes.swift`: the transitions (phase 5).

**Wiring into the existing code.** Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎. Copy what `clawdberg` did in each spot.
- **`Sources/Shared/Universe.swift:8–33`:** the case, `key`, `title`, `villainCount` (41), `heroCount` (51).
- **`Universe.swift:44–52`:** `agentOnly`, the five small fry (villain indices 36–40, so `base + 36…40`).
- **`Universe.swift:58`:** `claudeSide` stays false (heroes).
- **`Universe.swift:61`:** `rivals`: Megaclaw and Galvaclaw (see Cast).
- **`Universe.swift:66–79`:** `regenerations` gains the Matrix chain (see Mechanics). `abductees` is unchanged.
- **`Sources/App/Theme.swift:47`:** `Theme.of`.
- **`Sources/App/Locations.swift:74`:** `.merging(botsPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift:12, 16, 26, 36–38`:** `nil` in phase 1; a `.transclawmers(BotsTrip)` case in `duration`, `draw` and `pick` in phase 5, and the doc comment.
- **`Sources/App/Universes/Hem.swift:27, 87, 101, 121, 143, 180`:** HEM's costume in every switch.
- **`Sources/App/Rides.swift`:** three new ride cases and their drawing (phase 4).
- ⚠︎ **`Sources/Saver/SaverView.swift:79, 89, 214`:** the Options doc comment, the choices list and `case "transclawmers": tripUniverse = …`.
- ⚠︎ **`Sources/App/Drills.swift:54`:** the meditation guard. Transclawmers don't float cross-legged: nobody in G1 meditates. **`:488`:** merge the bespoke drills.
- ⚠︎ **`Sources/App/Overlay.swift:865`:** five Playground prompts. Lines 1113/1226 show how `clawdberg` hooked in its set piece and its OutaTime effect; the Matrix effect hooks in the same way (as Doctor Clawd's regeneration flare does, but with its own drawing).
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`:** decide per universe-specific `if`. The parked-in-vehicle-mode idea lives in the drawing functions, not here.
- ⚠︎ **`Sources/Shared/StatusStore.swift:330–343`:** PreCompact already walks `regenerations`; nothing to change for the Matrix unless the optional Megaclaw → Galvaclaw chain is approved (see Open questions).
- **Clawd Royale** picks up the cast and places through `Universe.allCases`. Check the menu bar icon and arch-enemies when a scene is in a `bots…` place.
- **Tools:**
  - `Tools/Preview/main.swift:60–93`: batch names (`botsHeroes1…`, `botsVillains1…`), the universe lookup, the enum lookups.
  - `Tools/Transitions/main.swift:12, 122`.
  - Phase 6: `Tools/RenderPromo` (`REEL=bots`), `Tools/RenderDocs` (`botsLineup`), `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts** (five, in-universe): "Roll out the new release", "Find the Decepticon in the test suite", "Transform this function into a class", "Scan the logs, Teletraan", "Refuel with energon and refactor".

## Cast

How the engine's weapons map onto the cartoon:
- **`.blaster`** is the standard G1 rifle or arm gun. The cartoon's lasers came in every colour, so each shooter gets its own shot colour (listed in the tables) so a fight is readable. Megaclaw's fusion cannon is a `.beam` (a continuous ray); most rifles are `.energy` bolts.
- **`.saber`** (melee) is for fists, swords and bites: Grimlawk's sword, Rumble's pile drivers (as Grumble), Ravidge's claws, Springr's sword, Wreck-Garr's axe, the combiners' fists.
- **`.lightning` + `Magic`** for the few special powers, each with its own family and colour (see "Powers" below).
- **`.none`** for the pacifists and humans who don't fight: Beachbummer, Spike, Sparkplug, Carly, Alpha Tryon.
- **`motion: .fly`** for the jets and flyers (Starscreech and the Seekers, Skyfyre, Swoopp, Laserbeek, Cyclonis, Scurge, Superiorn, Sky Lynks). **`.hover`** for the Quintessential Judge on his tentacles (`canSit: false`).
- **`bulk`** for giants: the combiners, Omega Supremo, Metroplex, Fortress Maximum, Triptycon, Scorpionok, Unicrawn.

### Heroes (51)

**The Ark crew, seasons 1–2 (22)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Optimus Prim | red chest with windscreen panes, blue arms, blue helmet with mouthplate and antennae, twin smokestacks | ion blaster rifle (`.energy`, white/red) | transforms into the red cab of a semi truck; callout "Autobots, roll out!" |
| 2 | Bumblebeep | small, yellow, round helmet with two little horns | small blaster (`.energy`, yellow) | transforms into a yellow Beetle and beeps the horn; callout "Hi, Spike!" |
| 3 | Jazzy | white and black, blue visor, a stripe on the chest | photon rifle (`.energy`, blue/white) | shoulder speakers pop up, a light show of coloured flashes; callout "Do it with style!" |
| 4 | Ironhyde | red, square, no faceplate (a grey face), van-shaped body | arm sprayer, liquid nitrogen (`.ice`), `armoured` | transforms into a red van; callout "Let's lock and load!" |
| 5 | Ratchett | white with a red cross on the chest and red stripes | wrench (`.saber`) | the medic: welds a wound with sparks flying |
| 6 | Wheeljank | white, green and red, lights on the sides of his head that flash when he talks | gyro-gun (`.energy`, green) | an invention blows up in his hands, he's left blackened and coughing smoke; callout "It works! …oops." |
| 7 | Prowler | black and white police car, red light bar on the head | acid-pellet rifle (`.energy`, white/black-blue) | light bar flashes red-blue as he transforms into a patrol car; callout "Freeze!" |
| 8 | Mirrage | white and blue, slim, racing livery | rifle (`.energy`, pale blue) | fades invisible and back (his electro-disruptor): a shimmering outline only |
| 9 | Houndog | green, jeep-shaped, spare wheel on the back | rifle (`.energy`, green-yellow) | projects a hologram tree beside himself, then switches it off |
| 10 | Sideswype | red twin, rocket pack on his back | fists (`.saber`) | rocket-pack leap: jumps 8 px with a flame trail and lands |
| 11 | Sunpreener | yellow twin of Sideswype, a vain look | shoulder launcher (`.energy`, yellow-orange) | holds up a mirror and polishes his chest |
| 12 | Cliffhanger | small, red, flat-topped helmet (no horns, unlike Bumblebeep) | glass-gas gun (`.energy`, red/white) | charges forward head-down, hot-headed; callout "Let me at 'em!" |
| 13 | Brawny | small, brown and green Land Rover body, bulky arms | fists (`.saber`), `armoured` | lifts a boulder above his head |
| 14 | Windcharjer | red, slim, little magnets on the arms | magnetism (see Powers) | pulls a steel girder through the air towards himself, drops it |
| 15 | Trailblazer | black, truck camper on the back | rifle (`.energy`, white) | throws up his force field: a pale blue dome flickers round him |
| 16 | Blabstreak | silver-grey, blue and red, shoulder cannons | shoulder cannons (`.energy`, white/silver) | never stops talking: speech lines pour out of him; callout "…and another thing!" |
| 17 | Smokeskreen | red, white and blue racing car, "38" on the chest | rifle (`.energy`, blue) | puffs out a smoke screen, then rolls dice in the clearing |
| 18 | Dread Alert | white and red fire chief, light bar | rifle (`.energy`, red) | lights spin, he looks left and right, alarmed; callout "Intruder alert!" |
| 19 | Infurno | red fire truck, ladder on his back | water cannon (`.beam`, white/blue) | ladder swings up and sprays a fan of water |
| 20 | Perceptacle | red and black, a microscope barrel on the shoulder | concussion blaster (`.beam`, cyan) | transforms into a microscope and peers; callout "Fascinating." |
| 21 | Boomblaster | red, boombox chest with a tape door, handle on the back | electro-scrambler (`.energy`, red/yellow) | music notes pour from his chest, a cassette pops out; callout "Rock and roll!" |
| 22 | Beachbummer | blue dune buggy, roll bar | none (a pacifist) | holds up a glittering mineral and admires it; callout "Peace, man." |

**The Dinobots (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 23 | Grimlawk | grey and gold, red visor, crown-like crest | sword (`.saber`), `armoured` | turns into a T. rex and roars, a puff of fire; callout "Me Grimlawk king!" |
| 24 | Slagg | grey and red, triceratops frill on the back | fire breath (`.fire`) | turns into a triceratops and paws the ground |
| 25 | Sludje | grey and gold, long brontosaurus neck folded behind | stomp (`.saber`) | turns into a brontosaurus; the ground shakes under his foot |
| 26 | Snarle | grey and red, stegosaurus plates on the back | tail swipe (`.saber`) | turns into a stegosaurus and fans his back plates |
| 27 | Swoopp | red, blue and grey, pteranodon wings | missiles (`.energy`, orange-red), `.fly` | turns into a pteranodon and circles |

**Humans (5).** Clawd in human costume, like the other universes' humans.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 28 | Spike Wickwitty | dark hair, red and white top, jeans | none | waves to Bumblebeep; callout "Bumblebee!" |
| 29 | Sparkplug Wickwitty | white hair, cap, mechanic's overalls, a spanner | none | taps an engine with his spanner, listens |
| 30 | Carly | blonde, green top, a clipboard | none | sketches a diagram on her clipboard |
| 31 | Danny Wickwitty | small, blond, in a little exo-suit | exo-suit blaster (`.energy`, yellow) | the exo-suit's visor snaps shut |
| 32 | Marissa Fairclawn | dark hair, EDC uniform, beret | laser pistol (`.bullet`) | salutes |

**Giants and specialists (7)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 33 | Skyfyre | huge, white and red, jet nose on the chest, wings | rifle (`.energy`, white/red), `.fly`, `bulk` | transforms into a big white jet and banks |
| 34 | Omega Supremo | huge, grey and red, claw on one arm, gun barrel on the other | arm cannon (`.beam`, red), `armoured`, `bulk` | turns into a rocket on its pad, lifts an inch, settles; callout "Constructicons!" |
| 35 | Superiorn | Aerialbots combined: white and grey, red visor, yellow wings | rifle (`.energy`, white), `.fly`, `armoured`, `bulk` | five little jets dock into him one by one, the limbs flash |
| 36 | Defensa | Protectobots combined: white, red and blue, shield on the arm | fists (`.saber`), `armoured`, `bulk` | his force-field shield glows as each limb locks on |
| 37 | Sky Lynks | blue, white and red space shuttle with a lynx's head | claws (`.saber`), `.fly` | turns from shuttle into lynx on four legs, preens; callout "Magnificent!" |
| 38 | Metroplex | a walking city: grey, blue, towers on the shoulders | shoulder cannons (`.energy`, blue), `armoured`, `bulk` | city towers rise out of his back, then sink; callout "Metroplex heeds!" |
| 39 | Fortress Maximum | huge, green and white, red visor | rifle (`.energy`, green), `armoured`, `bulk` | his head lifts off and turns out to be a smaller robot (Cerebros), who drops back in |

**Cybertron's past (2)** (season 2's flashback episodes)

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 40 | Alpha Tryon | ancient, red and blue, long moustache-like faceplate, hooded helmet | none | holds up a glowing data tablet and nods slowly |
| 41 | Elita Won | rose red and cream, crested helmet, gold trim | time-freeze (see Powers) | freezes time: everything round her tints lilac for a beat |

**The Movie and after (9)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 42 | Hot Rodd | maroon with yellow flames, spoiler on the back | twin pistols (`.energy`, orange-yellow) | transforms into a flamed sports car and revs; callout "Not now, Kupp!" |
| 43 | Rodimus Prim | Hot Rodd grown up: bigger, maroon and gold flames, the Matrix glowing in his chest | rifle (`.energy`, gold/white) | the chest opens and the Matrix shines; callout "Till all are one!" |
| 44 | Ultra Magnum | white armour over blue, red trim, shoulder missiles | rifle (`.energy`, white/blue), `armoured` | tries to open the Matrix, it won't light, he sighs; callout "I'm just a soldier." |
| 45 | Kupp | green-grey, old, battered | musket laser (`.energy`, teal) | leans on his musket and lifts a finger, a speech bubble with dots; callout "Reminds me of the time…" |
| 46 | Springr | green triple changer, rotor blades on the back | sword (`.saber`) | the rotors spin up and he lifts off a couple of pixels |
| 47 | Arcy | hot pink and white, round helmet, slim | pistol (`.energy`, pink) | her red visor slides down to scan |
| 48 | Blurrr | blue, long and thin, a fin on the helmet | electro-laser rifle (`.energy`, blue) | zooms off-sprite in a streak and back before you saw him go; callout "Gottagogottago!" |
| 49 | Wheelee | tiny, orange-red and white | slingshot (`.thrown`, grey) | fires a pebble from his slingshot (he speaks in rhyme, but there's no short canon line) |
| 50 | Wreck-Garr | junk-pile body, wheel on the back, TV-aerial ears | axe (`.saber`) | pulls a little TV out of himself and laughs at it; callout "Wreck and rule!" |

**HEM (1)**, as in every universe, last.

| 51 | HEM | a red Autobot-style chest with windscreen panes, a blue faceplate and helmet, wheels on the shoulders | ion blaster (Prime's) | the usual HEM routine |

### Villains (41)

**The original Decepticons (12)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Megaclaw | silver-grey, bucket helmet, black fusion cannon on the right arm | fusion cannon (`.beam`, dark violet core/magenta glow), `armoured` | the cannon charges with a glow, he shakes his fist; callout "Decepticons, attack!" |
| 2 | Starscreech | grey, red and blue jet, wings on the back, a pointed helmet | null rays (`.energy`, purple), `.fly` | rubs his hands, then cackles with a fist up; callout "I should be leader!" |
| 3 | Soundwav | blue, a tape-deck chest, shoulder cannon, red visor | sonic waves (see Powers) | the chest door opens and a tiny cassette pops out and back; callout "Soundwav superior." |
| 4 | Shockclaw | purple, one big yellow eye, no face, a gun for a left hand | arm gun (`.energy`, yellow) | the eye flares; callout "Logic!" |
| 5 | Thundercracka | Seeker jet in blue | rifle (`.energy`, blue/white), `.fly` | transforms into a jet; a sonic-boom ring bursts round him |
| 6 | Skywarpe | Seeker jet in black and purple | rifle (`.energy`, purple), `.fly` | teleports a few pixels with a purple pop |
| 7 | Ramjett | conehead Seeker: white, red and black, a nose cone on his head | headbutt (`.saber`), `.fly` | ducks his cone and rams forward |
| 8 | Laserbeek | red and gold condor, small | eye lasers (`.energy`, red), `.fly` | perches and turns his camera head, a red light blinking |
| 9 | Ravidge | black jaguar on four legs, red eyes, a missile pod | claws (`.saber`) | crouches low and pounces |
| 10 | Grumble | small, blue, round visor | pile-driver arms (`.saber`) | his arms turn into pile drivers and the ground shakes |
| 11 | Astrotrayne | purple and white, shuttle wings, train wheels | rifle (`.energy`, white) | turns into a steam engine and blows smoke, then back |
| 12 | Blitzwyng | purple and tan, tank turret and jet wings | turret cannon (`.thrown`, dark grey shell) | flips between tank turret and jet wings |

**The Insecticons (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 13 | Shrapnell | stag beetle: purple and gold, pincers | lightning from his antennae (see Powers) | echoes himself: "-nel, -nel" speech bubble; pincers snap |
| 14 | Bombshel | rhinoceros beetle: purple and black | cerebro-shells, mind control (see Powers) | fires a tiny shell that sticks on a head and blinks |
| 15 | Kickbak | grasshopper: black and gold, long legs | kicks (`.saber`) | a big springy hop |

**Combiners and their teams (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 16 | Devastaclaw | Constructicons combined: green and purple, a crane arm, a scoop for a hand | fists (`.saber`), `armoured`, `bulk` | six parts flash one after another as he locks together |
| 17 | Motormonster | black and grey semi truck, a purple face, a sword | sword (`.saber`) | transforms into a black semi; callout "I am the king of the road!" |
| 18 | Menacer | Stunticons combined: black, grey and purple, sword | sword (`.saber`), `armoured`, `bulk` | the limbs clunk into place, a red visor flares |
| 19 | Swindler | tan jeep, shifty | rifle (`.energy`, orange) | holds up a "FOR SALE" tag; callout "Have I got a deal for you!" |
| 20 | Brutalicus | Combaticons combined: purple and green, tank cannon on the shoulder | shoulder cannon (`.thrown`, grey shell), `armoured`, `bulk` | the parts lock and his visor glows |

**Earthbound schemers (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 21 | Dr. Arkevil | human, bald, white lab coat, goggles | none | rubs his hands and cackles |
| 22 | Nightbyrd | slim, black ninja robot, red visor | nunchaku (`.saber`) | a ninja backflip |
| 23 | Reflecta | grey and black camera with a big lens | rifle (`.energy`, white) | his lens flashes as he takes a photo |

**The Movie and season 3 (10)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 24 | Galvaclaw | purple and white, a crowned helmet, a huge cannon arm | cannon (`.energy`, white core/red glow), `armoured` | rants, the cannon flares, fist up; callout "Such a pity…" |
| 25 | Cyclonis | purple and grey, horned helmet, red eyes | rifle (`.energy`, red), `.fly` | transforms into a space jet |
| 26 | Scurge | blue-grey, a hooded "sweep" cowl and cape, red eyes | rifle (`.energy`, green), `.fly` | his eyes sweep left and right as he tracks |
| 27 | Unicrawn | a planet-sized robot: dark grey and rust, horned head, a ring round his body | eye ray (see Powers), `armoured`, `bulk` | turns into his planet (a sphere with a ring) and back; menace |
| 28 | Snarkticon | purple and grey shark-robot, huge teeth | bite (`.saber`) | chomp chomp, teeth flashing |
| 29 | The Quintessential Judge | a five-faced egg on tentacles, robe-like body | none, `.hover`, `canSit: false` | his head turns through faces, a gavel drops; callout "Guilty!" |
| 30 | Triptycon | dinosaur city: purple, black and green | chest cannon (`.energy`, green), `armoured`, `bulk` | stomps and roars, a crane swings on his back |
| 31 | Octaine | purple and grey, a fuel tank on the back | rifle (`.energy`, amber) | wings slide out (jet mode), then the tanker wheels |
| 32 | Pridaking | Predacons combined: red, gold and black, a lion's head on his chest | claws and sword (`.saber`), `bulk` | the lion head roars; his wings flare |
| 33 | Sixshooter | purple and grey, a six-changer | rifle (`.energy`, purple-white) | flickers through his modes: wolf, tank, jet, gun, car, robot |

**The Headmasters, season 4 (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 34 | Mindswipe | purple and black, bat wings | hypnosis (see Powers) | his wings spread and his eyes spiral |
| 35 | Weirdwulf | gold and black, wolf head | claws (`.saber`) | turns into a wolf and howls; callout "Hunt we will!" (he talks backwards) |
| 36 | Scorpionok | huge, purple and black, scorpion claws and a tail | claws and tail (`.saber`), `armoured`, `bulk` | turns into a scorpion (four legs), tail stings |

**Agent-only small fry (5).** Bit parts that only ever appear as agents:

| # | Name | Look | Weapon |
|---|---|---|---|
| 37 | Frenzie | Grumble's twin in red | sonic screech (`.energy`, red) |
| 38 | Buzzsore | gold condor cassette | eye lasers (`.energy`, gold), `.fly` |
| 39 | Ratbatt | purple bat cassette | bite (`.saber`), `.fly` |
| 40 | A Sweep | Scurge's lookalike troops, blue-grey | rifle (`.energy`, green), `.fly` |
| 41 | An Insecticon clone | a dull purple beetle | bite (`.saber`) |

**Totals:** heroes 22 + 5 + 5 + 7 + 2 + 9 + HEM = **51**. Villains 12 + 3 + 5 + 3 + 10 + 3 = 36, plus 5 agent-only = **41**. **92** in all.

### Powers (each one looks different)

| Who | Family | Colours | What you see |
|---|---|---|---|
| Windcharjer | `waves` | red core, white glow | magnetic arcs pulsing out, horseshoe-shaped |
| Soundwav | `waves` | yellow core, blue glow | sound rings from the shoulder speaker |
| Shrapnell | jagged lightning | pale yellow core, violet glow | forked bolts from both antennae |
| Bombshel | `rings` | lime core, dark green glow | rings along a faint ray to the target's head |
| Mindswipe | `spell` | magenta core, purple glow | a twinkling spiral ribbon |
| Elita Won | `touch` | rose core, lilac glow | a glowing fingertip; the target tints lilac and stops |
| Unicrawn | steady ray (`jagged: false`) | deep violet core, rust glow | a thick wavering ray from both eyes |

`magicVariants` gives each a different variant within its family on top of the colours. Windcharjer and Soundwav share the waves family but differ in colour and variant. None of these colours copies a power elsewhere in the app (Doctor Clawd's golden regeneration, the Clawd Files' greens): check in Clawd Royale.

### Lookalikes, inside and across universes

- **The Seekers** (Starscreech, Thundercracka, Skywarpe, Ramjett) share one body in the cartoon. They're kept apart by colour (red-blue, blue, black-purple, white with a cone head) and by signature. Only four, not the cartoon's six: Dirge and Thrust were cut as repaints.
- **Bumblebeep and Cliffhanger** are one mould: yellow with horns vs red with a flat crest.
- **Sideswype and Sunpreener** are twins: red with a rocket pack vs yellow with a mirror.
- **Ironhyde, Ratchett and Infurno:** red van, white ambulance with a red cross, red fire truck with a ladder.
- **Optimus Prim and Motormonster** are both semi trucks: red-blue with a mouthplate vs black-grey with a purple face and a sword.
- **Arcy and Elita Won:** hot pink and white with a round helmet vs rose red and cream with a crest and gold.
- **Megaclaw and Galvaclaw:** silver bucket helmet vs purple crown. They're also the `rivals` pair: the same mech in two bodies shouldn't lead two sessions back to back.
- **Hot Rodd, Rodimus Prim and Unicrawn** have orange in the source. They're drawn maroon (with yellow flames) and rust, never Clawd orange.
- **Against other universes:** Iron Clawd and War Machina (Marvelous Clawds) are red-gold and grey armour with a human-shaped faceplate; our robots carry vehicle parts (windscreens, wheels, wings) which they never do. The Cyberpersons (Doctor Clawd) are silver like Megaclaw, but he has the bucket helmet and cannon. The Sentinal (Marvelous) is purple like Shockclaw, but Shockclaw has a single eye and no face. The Star Clawds droids are small and gold-white, unlike anyone here.

### Nemeses (22)

Each pair faces off first when both are on stage:
- Optimus Prim ↔ Megaclaw
- Hot Rodd ↔ Galvaclaw
- Rodimus Prim ↔ Unicrawn
- Ultra Magnum ↔ Scurge
- Boomblaster ↔ Soundwav (the cartoon's own rivalry)
- Skyfyre ↔ Starscreech (old friends turned enemies)
- Omega Supremo ↔ Devastaclaw
- Superiorn ↔ Menacer
- Defensa ↔ Brutalicus
- Metroplex ↔ Triptycon
- Fortress Maximum ↔ Scorpionok
- Grimlawk ↔ Pridaking
- Bumblebeep ↔ Grumble
- Ironhyde ↔ Astrotrayne
- Mirrage ↔ Skywarpe (the vanisher vs the teleporter)
- Houndog ↔ Ravidge (dog vs cat)
- Wheeljank ↔ Dr. Arkevil (the two inventors)
- Perceptacle ↔ Shockclaw (the two scientists)
- Dread Alert ↔ Reflecta (security vs surveillance)
- Kupp ↔ The Quintessential Judge
- Wreck-Garr ↔ Snarkticon
- Arcy ↔ Cyclonis

**Rivals:** Megaclaw and Galvaclaw.

### Callouts for the leads (short list)

Optimus Prim "Autobots, roll out!" · Megaclaw "Decepticons, attack!" · Starscreech "I should be leader!" · Soundwav "Soundwav superior." · Rodimus Prim "Till all are one!" · Hot Rodd "Not now, Kupp!" · Ultra Magnum "I'm just a soldier." · Galvaclaw "Such a pity…" · Grimlawk "Me Grimlawk king!" · Kupp "Reminds me of the time…" · Wreck-Garr "Wreck and rule!" · Motormonster "I am the king of the road!" · The Quintessential Judge "Guilty!" · Blurrr "Gottagogottago!" · Boomblaster "Rock and roll!"

### Left out, and why

- **Same-mould repaints** with nothing of their own: Dirge and Thrust (Seekers), most Constructicon, Stunticon, Aerialbot, Protectobot, Combaticon and Predacon members (the combined giant reads far better at 72×52 than five similar small robots), Frenzy as a lead (he's agent-only).
- **Huffer:** orange; he'd read as plain Clawd. **Gears** overlaps Brawny (grumpy little brawler). **Hoist, Grapple, Tracks, Seaspray, Powerglide, Warpath, Cosmos:** fine characters with less to do on screen; they're the first swaps if you want any.
- **Chip Chase:** his wheelchair can't be drawn honestly on Clawd's four legs.
- **Crossover cameos** (G.I. Joe's Flint, Cobra Commander): other franchises.
- **On-screen deaths** and the movie's swearing (see Tone). Optimus Prim's death is never drawn: the Matrix passing (Mechanics) is the cheerful version.
- **Megaclaw's pistol mode:** Clawd on four legs as a handgun doesn't read and isn't great on a desktop. His signature is the cannon instead.

## Places (20)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. Keys all start with `bots`, so they can't clash with the six universes or the sibling plans. The palette swings between 80s Earth (bright blue sky, desert orange-pink, green grass) and Cybertron's metal blues and purples.

| # | Key | Place | Still | Moving | Tall extras |
|---|---|---|---|---|---|
| 1 | `botsArk` | **The Ark, the Autobot base** (default) | the crashed ship's inside: hexagon wall panels, the Teletraan-1 computer's big screen and console | Teletraan's screen scrolls a schematic, console lights blink | the volcanic rock ceiling, the Ark's girders, energon lines |
| 2 | `botsMountHilary` | **Mount St. Hilary** | the volcano with the Ark's nose sticking out of the side, pine forest | smoke from the crater, a bird crossing | a tall blue sky, the summit |
| 3 | `botsNemesis` | **The Decepticon base under the sea** | purple corridors, a big porthole window, Megaclaw's chair | bubbles and passing fish through the porthole | the dark sea above, a shaft of light |
| 4 | `botsIacon` | **Iacon, Cybertron** | the Autobots' golden-age city of metal towers | energon pulses along conduits in the floor | Cybertron's two moons, towers reaching up |
| 5 | `botsSpaceBridge` | **The space bridge** | Shockclaw's tower on Cybertron, a launch pad ringed by pylons | a green-yellow shimmer column on the pad, then gone | the bridge's beam rising into a black sky |
| 6 | `botsEnergonDam` | **The dam** (the pilot's power raid) | a sunny hydroelectric dam, stacks of pink energon cubes | water pouring over the spillway, cubes glowing | the full dam wall and the reservoir (sunny, unlike the Clawd Files' night-time Ruskin Dam) |
| 7 | `botsDinobotIsland` | **Dinobot Island** | palm trees, ferns, a smoking volcano, primeval swamp | lava bubbling, ferns swaying, a pterosaur gliding | the volcano's peak, a giant dragonfly |
| 8 | `botsHighway` | **The desert highway** | an American desert road, red mesas, a road sign | heat shimmer, a tumbleweed rolling past | big mesas and a wide sky |
| 9 | `botsCityStreet` | **The city at night** | a downtown street, parked cars, billboards | traffic lights cycling, neon flickering | skyscrapers with lit windows |
| 10 | `botsGoldenLagoon` | **The Golden Lagoon** | a jungle pool of shining gold liquid | the gold surface ripples and glints | jungle canopy, hanging vines |
| 11 | `botsSkyfireIce` | **The Arctic ice cave** | blue ice walls with Skyfyre's giant silhouette frozen inside | sparkles of ice, dripping water | an ice ceiling with shafts of light |
| 12 | `botsVectorSigma` | **Vector Sigma's chamber** | a deep vault under Cybertron with a huge golden sphere | the sphere pulses, glyphs flow over it | the vault's dark height, rings of light |
| 13 | `botsAutobotCity` | **Autobot City, Earth 2005** | domes and towers, Metroplex's city mode, a shuttle on the pad | windows lighting, a shuttle's engines glowing | more towers, the shuttle's launch tower |
| 14 | `botsMoonbase` | **Autobot Moonbase** | grey lunar dome, Earth in the black sky | blinking beacons, stars | Unicrawn's ringed shape far off in the sky (eerie, not moving) |
| 15 | `botsUnicronSpace` | **Unicrawn's orbit** | the planet-sized robot in deep space, rust and grey | debris drifting past, a slow turn | his horned head looming over everything |
| 16 | `botsUnicronBelly` | **Inside Unicrawn** | giant gears and conveyor belts, red-lit | gears turning, conveyor moving | towering machinery, steam vents (no acid, no digestion) |
| 17 | `botsJunkion` | **Junkion** | the junk planet: heaps of scrap, TVs, aerials | TVs flicker with static and test patterns | towers of junk |
| 18 | `botsQuintessa` | **Quintessa's courtroom** | the Quintessons' high bench, a plank over a pool | fins circling in the pool | the court's gloomy height, five-faced statues |
| 19 | `botsChaar` | **Chaar** | the Decepticons' grey ash planet, broken towers | ash falling, a flicker of energon | a dim sky, a dead sun |
| 20 | `botsNebulos` | **Nebulos** | the Headmasters' planet: pink and purple sky, organic towers | spores drifting, a flowering plant opening | twin suns, floating islands |

**Homes:**
- **Ark crew** and **humans:** the Ark. Except Beachbummer (the Golden Lagoon), Skyfyre (the Arctic ice cave), Houndog (Mount St. Hilary, he loves Earth's outdoors).
- **Dinobots:** Dinobot Island.
- **Giants:** Omega Supremo, Metroplex, Superiorn and Defensa at Autobot City; Sky Lynks at the Moonbase; Fortress Maximum on Nebulos.
- **Cybertron's past:** Alpha Tryon at Vector Sigma's chamber; Elita Won at Iacon.
- **Movie Autobots:** Autobot City. Wheelee on Quintessa (where he was found), Wreck-Garr on Junkion.
- **Original Decepticons:** the base under the sea. Shockclaw at the space bridge; the Seekers at the dam; Astrotrayne and Blitzwyng at the space bridge.
- **Insecticons:** the city at night (raiding the power). **Devastaclaw:** the dam. **Stunticons** (Motormonster, Menacer, Swindler): the desert highway. **Brutalicus:** Chaar.
- **Earthbound schemers:** the city at night.
- **Movie Decepticons:** Galvaclaw, Cyclonis, Scurge, Octaine, Sixshooter and Pridaking on Chaar; Unicrawn in his orbit; Snarkticon and the Judge in Quintessa's court; Triptycon at Autobot City (he's there to attack it).
- **Headmasters:** Nebulos.

## Mechanics that make it its own universe

1. **Rides** (`Rides.swift`, three new ones):
   - **The Autobot shuttle** (white and red, from the movie) picks up and drops off the movie crew and the giants who'd fit: Hot Rodd, Rodimus, Ultra Magnum, Kupp, Springr, Arcy, Blurrr, Wheelee, Danny, Spike.
   - **Astrotrayne** carries Decepticons: he's a triple changer whose job in the cartoon is literally being the Decepticon shuttle. The ride is his purple-and-white shuttle mode. Whenever Astrotrayne is on stage himself, the others still ride a shuttle that looks like him; that's the cartoon's logic too.
   - **The space bridge** (a ring of pylons and a green-yellow shimmer column) for anyone from Cybertron: Shockclaw, Alpha Tryon, Elita Won.
   - Everyone else leaves on foot, or (optional, see Open questions) **rolls out**: plays the fold, then drives off-stage in vehicle mode.
2. **The Matrix of Leadership, which is Transclawmers' regeneration.** When a Claude Code or pi session led by a **Matrix bearer** compacts its context, the Matrix passes to the next bearer: **Optimus Prim → Ultra Magnum → Rodimus Prim → Optimus Prim** (the last step is season 3's *The Return of Optimus Prime*). Compaction is a session handing on what it knows, and that's what the Matrix does: it holds the wisdom of past Primes. It uses the existing `regenerations` list and `StatusStore` PreCompact path as it stands (it wraps round, and skips anyone already leading another session).
   - The effect, drawn in `BotsMatrix.swift`: the leader's chest opens, the Matrix's handle-shaped crystal glows, blue-white light pours up in a column with drifting sparkles, and the new bearer is standing in it as the light fades. Caption: "LIGHT OUR DARKEST HOUR". This deliberately looks nothing like Doctor Clawd's golden flare: blue-white, a column, not a burst.
   - Local hero indices: Optimus Prim 0, Ultra Magnum 43, Rodimus Prim 42, so `regenerations` = `[0, 43, 42].map { base + StatusStore.heroBase + $0 }`.
   - Optional, needs an engine change: **Megaclaw → Galvaclaw**, Unicrawn's reformatting, one way. `regenerations` is one list per universe today, so this would need a list of chains (see Open questions).
3. **Habits:**
   - **Parked in vehicle mode** when a session sits (all characters with a vehicle mode; in the drawings, not the engine).
   - **Soundwav ejects a cassette:** now and then a tiny Laserbeek flies a lap round him and docks.
   - **Mirrage goes invisible** when idle for a while: just a shimmering outline, until someone needs him.
   - **Skywarpe teleports** a short hop along the stage with a purple pop.
   - **Kupp's stories:** a long speech bubble of dots, and whoever stands next to him nods off (a "z").
   - **Starscreech schemes:** when Megaclaw is on stage, he edges behind him and mimes wearing his helmet, then snaps back when Megaclaw turns.
4. **Practice drills, which are bespoke:**
   - Autobots at the target range in the Ark (Teletraan pops up red targets);
   - Decepticons stack pink energon cubes into a pyramid (the pilot's plan);
   - Wheeljank tests an invention, which blows up;
   - the Dinobots stomp and roar at a boulder until it cracks;
   - Boomblaster and Soundwav play music (notes from the chest);
   - Perceptacle peers into his microscope.
   
   Nobody floats cross-legged in meditation (`Drills.swift:54`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one.

1. **Skeleton:**
   - the universe case and all the wiring above;
   - **Optimus Prim, Bumblebeep and Megaclaw** (the enum's first cases: heroes 0–1, villain 0), each with the transform signature, so `BotsKit.swift`'s fold helper is written now and proven on a truck and a Beetle;
   - the Ark (`botsArk`), the menu icon, HEM's costume, the saver option and Preview support; plain wipes for now.
   
   It runs end to end in the app, the window, the screen saver and Clawd Royale.
2. **Core ensemble.** About 38 characters:
   - all 51 hero and 41 villain enum cases committed first as stand-ins, then the art;
   - drawn: the Ark crew, the Dinobots, Spike and Sparkplug; the original Decepticons, the Insecticons, Devastaclaw;
   - 8 places: the Ark, Mount St. Hilary, the base under the sea, Iacon, the space bridge, the dam, Dinobot Island, the desert highway; with homes and nemeses for these;
   - parked-in-vehicle-mode for everyone drawn so far.
3. **Rest of the cast and places.** All 92 characters and 20 places, every home filled. Ends with **the character audit** (every weapon, shot colour, power, motion, signature and callout checked against the source; a table of only the mismatches).
4. **Mechanics:** the three rides, the Matrix of Leadership, the habits and the bespoke drills.
5. **Transitions:** the twelve `BotsTrip`s and the chrome place-name finishing touch (see below).
6. **Polish pass** (always before docs): every weak spot from phases 2–5, split by file and fixed in parallel, with before-and-after renders.
7. **Docs and release:**
   - the README's universe table and a cast-and-places section, roster and locations sheets, a `botsLineup` desktop strip and a social preview (`docs/roster-transclawmers.png` …);
   - `llms.txt` (universe list, folder and `Bots…` prefix, the Matrix mechanic), and a `CHANGELOG.md` entry each phase;
   - a trailer, `REEL=bots`, opening on the transformation logo morph.
   - **Needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order in the tables above, and phases never renumber.

## Polish pass (after phase 5, before docs)

The weak-spot list starts empty and is filled in at the end of each phase. Things to watch for from the start:
- the fold helper at window size: the transform must still read at agent size (small), not just leader size;
- vehicle colours that drown out Clawd's orange;
- the giants' `bulk` in duels with small robots (Wheelee vs Scorpionok);
- the four Seekers and the twin pairs side by side in one sheet.

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`. Before calling a phase done, `./build.sh --release <version>` with `-Xfrontend -warn-long-expression-type-checking=300` to catch slow fold maths.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Optimus Prim"` (check every frame of the transform);
  - `build/preview fight out.png "Optimus Prim" "Megaclaw"`;
  - `build/preview place out.png "Transclawmers"`;
  - the batch sheets, one per Art file. Look at the PNGs before showing them.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> botsArk botsIacon`.
- **In the app:**
  - Settings → Universe → Transclawmers: new sessions are Autobots; subagents can be Decepticons or small fry.
  - Idle sessions park in vehicle mode.
  - The screen saver's Options include it; Random and Clawd Royale reach it.
- **The Matrix:** `/compact` in a Claude session led by Optimus Prim: the light, and Ultra Magnum steps out.

## Transitions (`BotsTrip`, 12)

**Style.** Pixel art in the look of a mid-80s cel cartoon: bold dark outlines, flat colours with one highlight, no gradients except the chrome lettering's banded shine. The palette is Autobot red, Decepticon purple, chrome greys with a white highlight band, energon pink, Matrix blue-white, and starfield black. Halftone only for the explosions and the Matrix light. Nothing glossy or painted. The insignias are our own: a red, rounded robot face with Clawd's eyes for the heroes, a purple, angular one for the villains. Neither copies the real Autobot or Decepticon faces.

**Sound** (trailer only; the app is silent): the transforming whir-and-clunk evoked with our own synth notes, never the real sound effect or theme.

**Finishing touch.** Every transition ends with the place's name sliding in from the side in **chrome lettering** with a shine sweeping across it, the cartoon's title-card style, before it fades. It replaces the usual place-name label in this universe.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Transformation Logo Morph** (signature opening) | The old place breaks into square metal tiles that flip and slide like a robot's panels folding, with a white spark at each joint. A car shape in the middle folds up into a robot head; TRANSCLAWMERS slams in in chrome, the shine sweeps across, then the panels unfold onto the new place. The longest and rarest. | any time, rarely |
| 2 | **The Insignia Spin** | The cartoon's scene-break bumper: the hero insignia zooms out of the old place and spins; mid-spin it flips into the villain insignia (or back), then zooms into the new place. | anyone; the side of whoever's arriving picks which face it ends on |
| 3 | **Roll Out** | A convoy (a red semi, a yellow Beetle, a white racer) drives across the panel left to right; the new place is behind them, the old one ahead, with a dust trail at the join. | Optimus Prim, the car Autobots; the desert highway, the city at night |
| 4 | **The Space Bridge** | A shimmering green-yellow column comes down on the old place, the picture is drawn up into it in streaks, and it comes back down on the new place. | Shockclaw, Astrotrayne, Alpha Tryon; Iacon, the space bridge |
| 5 | **Teletraan Alert** | The old place shrinks onto Teletraan-1's big screen, "ALERT" flashes red with scanlines, the screen changes to the new place, and the camera pushes through it. | the Ark crew, Dread Alert; the Ark |
| 6 | **Energon Cubes** | Glowing pink cubes stack up from the floor until the panel is a wall of them, then they lift away one row at a time onto the new place. | the Decepticons, Devastaclaw; the dam, the base under the sea |
| 7 | **Light Our Darkest Hour** | The Matrix opens in the middle of the panel, blue-white light floods out in a widening column until the old place is gone, and it fades on the new place. | Optimus Prim, Rodimus Prim, Ultra Magnum, Hot Rodd; Autobot City |
| 8 | **Unicrawn Devours** | Unicrawn's ringed planet shape drifts across the old place, his jaws open, close over the picture, and open again on the new place. Only comes up with him present (`needsOwner`). | Unicrawn, Galvaclaw; his orbit, his belly, the Moonbase |
| 9 | **Combiners Lock** | The panel splits into five vertical strips that slide and clunk together like limbs locking on (a flash at each join), a giant's silhouette forms, then breaks apart on the new place. | the combiners and Omega Supremo |
| 10 | **Seeker Fly-by** | Three jets in a V scream across, their contrails wiping the old place to the new one. | Starscreech, Thundercracka, Skywarpe, Ramjett; open skies (the dam, Mount St. Hilary) |
| 11 | **Eject!** | Soundwav's tape door fills the panel and opens; a cassette with the old place on its label pops out, a new one with the new place slides in, the door shuts, and we zoom into the label. | Soundwav, Boomblaster, Laserbeek, Ravidge, Grumble |
| 12 | **Dinobot Stomp** | A huge dino foot stamps down, cracks spread across the old place, and it falls away in chunks onto the new place. | the Dinobots; Dinobot Island |

**Not used:**
- **Junkion channel-surf** (overlaps Teletraan Alert).
- **Sharkticon chomp** (overlaps Unicrawn Devours).
- **Quintesson faces turning** (five small faces won't read at panel scale).
- **Headmaster head pop** and **Vector Sigma's glow** (too small, and the Matrix light covers the glow).
- **Galvatron's rebuild** belongs to the optional reformatting mechanic, not a transition.

**Promo.** The Transformation Logo Morph (#1) is the trailer's title sequence.

## Promo: `REEL=bots`

About 45–50 seconds, on the `doctorShots` pattern:
- **`intro` (~9 s), the logo morph:** black; a spark; metal panels slide across the screen in time with a synth whir-and-clunk. A sports car folds up into a robot head with Clawd's eyes, the two insignias flip past each other, and **TRANSCLAWMERS** slams in in chrome with a shine sweeping across. The tagline under it, our own pun: **"More than meets the AI."** Panels fold away into white.
- **Set piece (~9.5 s), the battle of Autobot City:** Astrotrayne lands on the pad and Decepticons pour out; Devastaclaw stomps over a tower. Optimus Prim's truck roars in from the left (the movie's charge), transforms in mid-air and lands, rifle up; a short exchange of fire with Megaclaw, who's knocked flat. Then Unicrawn's shadow falls over the city, Rodimus Prim opens the Matrix, and the blue-white light washes the screen.
- **`hook`, `status`, `agents`, `ais`, `endcard`** as in the other trailers. Copy ideas:
  - `desktop`: "Robots in disguise. Agents in disguise."
  - `status`: four characters, one per state, "Idle? It's parked."
  - `agents`: "Every subagent gets to be a robot in disguise."
  - `window`: at `botsArk`, "There's more to this window than meets the eye."
- **Music:** 80s synth rock: driving synth bass, a gated drum, a power-chord synth stab on the title. Our own notes; never the theme's melody or the real transform sound.

## Open questions for you

1. **Name:** Transclawmers (recommended: it reads at once and keeps the "Clawd" pun), Clawdbots, or Robots in Disguise: Clawd.
2. **Scope:** G1 and the 1986 movie as planned. **Beast Wars** would add about 20 good ones (Optimus Primal, Rhinox, Cheetor, Rattrap, Dinobot, Silverbolt, Megatron the T. rex, Tarantulas, Waspinator, Inferno, Terrorsaur, Rampage), and four-legged animals suit Clawd's body very well; that would take it to about 112. The **live-action films** I'd leave out: busy designs that don't read at 72×52.
3. **Megaclaw → Galvaclaw on compaction:** a second, one-way chain next to the Matrix. Fun and true to the movie, but `regenerations` is one list per universe, so it needs a small engine change (a list of chains in `Universe` and `StatusStore`). Yes or skip?
4. **Roll out on leaving:** characters with a vehicle mode play the fold and drive off-stage instead of walking. It reuses each drawing's vehicle frame, but needs a small hook where walk-offs are drawn. Yes or skip?
5. **Names to check:** Optimus Prim (or Optimus Clawd?), Unicrawn, the Quintessential Judge, Grumble (for Rumble), Sunpreener (for Sunstreaker).
6. **Swaps:** any character you'd rather have in or out. Hoist, Tracks, Seaspray, Powerglide, Dirge and the Constructicon members are the first in line. A swap keeps the count.
