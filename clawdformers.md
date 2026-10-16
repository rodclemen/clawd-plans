# Plan: a new universe, Clawdformers (Transformers parody)

## Context

Clawd Clash has six universes on `main` (ebc02be, 2026-10-16): Star Clawds, Marvelous Clawds, Detective Clawds, Doctor Clawd, The Clawd Files and Stevie Clawdberg. This plan adds a Transformers parody as a full ensemble, built the same way as The Clawd Files. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

- **Name: Clawdformers** (decided 2026-10-16).
- **Scope:** the G1 cartoon (1984–87, seasons 1–4, including the three-part *The Rebirth*), *The Transformers: The Movie* (1986) and **Beast Wars** (1996–99, the Maximals and Predacons). The live-action films are left out.
- **Code naming** avoids the franchise name, as the other universes do:
  - `case clawdformers` with key `"clawdformers"`, title `"Clawdformers"`.
  - Folder `Sources/App/Universes/Clawdformers/`, file prefix `Bots…` (`BotsRoster.swift`, `BotsHero`, `BotsVillain`, `botsTheme`, `BotsWipe`/`BotsTrip`). Place keys all start with `bots`.
  - Branch `transformers`. Promo reel `REEL=bots`. Docs files `docs/roster-clawdformers.png` and so on.
- **Raw value:** the next free one when its build starts (Buffy is planned as 6). Ids are rawValue*1000 and permanent.
- **Naming style: coding-language names.** The leads, and anyone where a coding pun lands cleanly, get one: Optimus Runtime, Megabyte, Stackscream, Sound.wav, Rat.catch(). The rule is that it must still read at a glance as the real name. Characters with no natural coding pun keep a light pun or a near-spelling (Ironhyde, Blabstreak, Grumble, Snarkticon); a forced pun is worse than none. Actors' names are never used. Nothing here is a real person.
- **Size:** **112 characters**: 61 heroes including HEM, and 51 villains including 5 agent-only. Plus **23 places** and **12 transitions**.
- **Claude's side:** the heroes, the Autobots and Maximals (`claudeSide` false, as in every universe except Star Clawds).
- **Tone:** the cartoon is already a toy show, so very little has to go. Characters don't die on screen: the movie's deaths (Optimus on his bed, Ironhide's execution, the shuttle massacre, Unicron digesting the Lithones) and Beast Wars' (Dinobot's last stand, Tigatron and Airazor taken by the Vok) are left out, and Unicron's belly is gears and conveyor belts, not acid. RAM-page is a cackling crab and nothing more: his backstory isn't told. Mild swearing is left out of callouts. Fights are laser-tag silly, like the cartoon: robots get knocked over and get up.

| Universe                   | Heroes | Villains | Total | Places | Transitions |
|----------------------------|--------|----------|-------|--------|-------------|
| Star Clawds                |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds           |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds           |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd               |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files            |     36 |       46 |    82 |     20 |          10 |
| Stevie Clawdberg           |     64 |       54 |   118 |     23 |          10 |
| **Clawdformers**           | **61** | **51** | **112** | **23** |      **12** |

(heroCount includes HEM; villainCount includes agent-only.)

**Viability: clears the bar easily.** There are well over 20 good heroes and 20 good villains in G1 and the movie alone, all with distinct colours, a clear weapon and, for most of them, a built-in signature move (they transform). Beast Wars adds 20 more, and its animals suit Clawd's four legs better than anything. The hard part isn't finding characters but choosing: around 300 G1 toys appeared on screen. The rule for picking was the guide's: recognisable as a 72×52 sprite, distinct in colour and silhouette, something to do. That ruled out most of the same-mould repaints (see "Left out").

## Clawd in costume: how a robot stays Clawd

Every character is Clawd, the orange body on four legs. Clawdformers are Clawd wearing robot armour:
- **A helmet with a faceplate:** Optimus's mouthplate and ear antennae, Megatron's bucket, Bumblebee's horns, Shockwave's single eye. The helmet does most of the work of saying who it is.
- **Armour plates in the character's colours** on the chest and back, with **vehicle parts** on top. That's the G1 look: a car's windscreen panes on the chest, wheels at the shoulders, wings on the back for jets, a smokestack for Optimus. The Beast Wars cast wear **beast parts** instead: a gorilla's chest, a rat's tail, a raptor's head on the shoulder.
- **The orange body still shows:** along the sides, the belly and the four legs. Plates cover at most the top two-thirds, so Clawd's orange reads in every sprite. Nobody is drawn in Clawd orange armour, so the orange always means "this is Clawd underneath".
- **Four legs, always.** For cars, the four legs are the four wheels, which is what makes the transform work (below). For beasts, the four legs are simply the animal's legs.

### The transform (the signature move for most of the cast)

The G1 transform is big, quick and noisy, so it reads well at 72×52. Most characters' signature (`Persona.signature`, 2.5–3.5 s) is a round trip, robot → vehicle → robot. The drawing gets `p.signature` 0…1:
- **0.00–0.25, fold:** the head sinks into the shoulders and the faceplate slides down. The arms swing back flat along the sides. The body drops 4–6 px and stretches 6–8 px longer. A wheel (dark tyre, grey hub) grows over each foot, so the four legs become the four wheels. The chest's windscreen tips up to become the roof. Two white spark pixels flash at the joints on the frames where panels move.
- **0.25–0.75, vehicle:** the car, truck or van silhouette in the character's colours, with orange showing as the chassis and wheel arches. Headlights blink once, it rolls 3–4 px forward and back, and a puff of exhaust comes out the back.
- **0.75–1.00, unfold:** the same moves in reverse, ending on the normal pose with a 1-px hop, the cartoon's "transformed" pose.

Variations:
- **Jets** (Stackscream, Skyfirewall, the Seekers): wings slide out from the sides, a nose cone covers the face, it lifts 2–3 px and the legs tuck up into short landing gear.
- **Dinobots and G1 beasts** (Slagg, Snarle, Kludge, Garbage Collector, Scorpio-404, Weirdwulf, Pridaking's lion): a dino or beast head pushes forward and a tail grows out the back. Four-legged animals are a gift: Clawd's four legs simply stay legs.
- **Beast mode (the Beast Wars cast):** the same fold, but robot → animal → robot, with the show's call ("Maximize!" for the Maximals, "Errorize!" for the Predacons) in the speech bubble on the way back. Fur or shell panels slide over the armour, the robot head sinks and the animal head comes up. Gorillas knuckle-walk, cats and the rat stay on four legs, the flyers spread wings, the spiders and insects grow two thin extra pairs of legs and mandibles, and the manta ray flattens and lifts.
- **Giants and combiners** don't transform in their signature. They "lock": their limbs flash in their members' colours one by one.

All this is one shared helper in `BotsKit.swift` (`botsFold(c, p, …)` with the vehicle's or animal's outline, colours and wheel or leg positions as parameters), so 60 characters don't each re-invent the fold.

**Parked when idle.** A session that's been idle long enough sits. In this universe, characters with a vehicle mode **park in vehicle mode** instead, and the Beast Wars cast **curl up in beast mode**: the drawing checks `p.seated` and draws the frame from the middle of the transform. This needs no engine change, and it's the most "robots in disguise" thing the universe can do: a row of idle sessions becomes a car park.

**Roll out on leaving (decided).** Characters with a vehicle mode play the fold and drive off-stage instead of walking or fading; beast-mode characters change into their animal and run, or fly, off. It reuses each drawing's vehicle or beast frame (see Mechanics for the hook).

### Armour without boring fights

Almost everyone here is a robot, but `armoured: true` means "shots ricochet off this one". In the engine it changes 2 of every 11 shot outcomes from a duck to a ricochet (`boltOutcome` in `Fights.swift`); hits still land. If everyone had it, it would stop meaning anything. So:
- **Only 20 characters are armoured:** the giants and the famously tough (Ironhyde, Brawny, Grimdeadlock, Ultra Macros, Sudo Supreme, Metroplex, Fortress MaxInt, Superiorn, Defensa, Rhinux, Megabyte, Gigabyte, DevOpsastator, Menacer, Brutalicus, Triptycon, Unicron Job, Scorpio-404, Megabyte Rex, RAM-page). A ricochet becomes a "this one's tough" tell.
- **Everyone else ducks, shields and gets knocked over** like any other universe's cast. The cartoon's robots are knocked flat constantly, so that fits.
- **Variety comes from weapons:** about half the cast are rifle shooters (in different shot colours), a third melee (fists, swords, pile drivers, dino bites, claws), and a handful use special powers (magnetism, sound, mind control, time, weather). Giants have `bulk`, so duels stand further apart.

## How a universe plugs in (checked against the code on 2026-10-16, main ebc02be)

**New code: `Sources/App/Universes/Clawdformers/`**
- `BotsRoster.swift`:
  - `enum BotsHero` and `enum BotsVillain`, append-only, with `hem` as the last hero.
  - The persona dictionaries, merged from the Art files with `.reduce([.hem: hemPersona(.clawdformers)])`.
  - `Location.botsHome(of:)` for heroes and villains, `botsNemeses`, the `ride:` closure, `let botsTheme = Theme(...)`.
  - The `static let` place keys (all `bots…`) and `let botsPlaces` merged from the Places files.
- `Art/BotsHeroes1…7.swift` and `Art/BotsVillains1…6.swift`, about 8–10 personas per file, in the pattern of `ClawdbergHeroes1.swift`.
- `BotsKit.swift`: shared drawing helpers with prefixed names: the fold (`botsFold`, vehicles and beasts), wheels, windscreen panes, faceplates, the faction badges (our own red and purple insignias, with Maximal and Predacon variants).
- `Places/BotsScenes1…3.swift` as `let botsScenesN: [Location: Place]`.
- `BotsIcon.swift`: the menu bar icon, 28×26, colour and mono. A robot head with a faceplate and Clawd's eyes, in our own red insignia style (not the Autobot face).
- `BotsRides.swift`: the Autobot shuttle, Astro Retrain and the space bridge.
- `BotsMatrix.swift`: both compaction effects, the Matrix of Leadership and Gigabyte's reformatting.
- `BotsDrills.swift`: bespoke drills.
- `BotsWipes.swift`: the transitions (phase 5).

**Wiring into the existing code.** Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎. Copy what `clawdberg` did in each spot.
- **`Sources/Shared/Universe.swift:8–33`:** the case, `key`, `title`, `villainCount` (51), `heroCount` (61).
- **`Universe.swift:44–52`:** `agentOnly`, the five small fry (villain indices 46–50, so `base + 46…50`).
- **`Universe.swift:58`:** `claudeSide` stays false (heroes).
- **`Universe.swift:61`:** `rivals`: Megabyte and Gigabyte (see Cast).
- **`Universe.swift:66–79`:** `regenerations` becomes a list of chains (see Mechanics): the Matrix chain, which wraps, and Megabyte → Gigabyte, one way. `abductees` is unchanged.
- **`Sources/App/Theme.swift:47`:** `Theme.of`.
- **`Sources/App/Locations.swift:74`:** `.merging(botsPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift:12, 16, 26, 36–38`:** `nil` in phase 1; a `.clawdformers(BotsTrip)` case in `duration`, `draw` and `pick` in phase 5, and the doc comment.
- **`Sources/App/Universes/Hem.swift:27, 87, 101, 121, 143, 180`:** HEM's costume in every switch.
- **`Sources/App/Rides.swift`:** three new ride cases and their drawing (phase 4).
- ⚠︎ **`Sources/Saver/SaverView.swift:79, 89, 214`:** the Options doc comment, the choices list and `case "clawdformers": tripUniverse = …`.
- ⚠︎ **`Sources/App/Drills.swift:54`:** the meditation guard. Clawdformers don't float cross-legged: nobody in G1 or Beast Wars meditates. **`:488`:** merge the bespoke drills.
- ⚠︎ **`Sources/App/Overlay.swift:865`:** five Playground prompts. Lines 1113/1226 show how `clawdberg` hooked in its set piece and its OutaTime effect; the Matrix and Gigabyte effects hook in the same way (as Doctor Clawd's regeneration flare does, but with their own drawing).
- ⚠︎ **`Sources/App/Overlay.swift:1255`:** the roll-out hook, where an actor leaving without a ride fades and sinks (see Mechanics).
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`:** decide per universe-specific `if`. The parked-in-vehicle-mode idea lives in the drawing functions, not here.
- ⚠︎ **`Sources/Shared/StatusStore.swift:330–343`:** PreCompact walks `regenerations` (line 336); it changes to find the chain holding the leader and step along it (see Mechanics).
- **Clawd Royale** picks up the cast and places through `Universe.allCases`. Check the menu bar icon and arch-enemies when a scene is in a `bots…` place.
- **Tools:**
  - `Tools/Preview/main.swift:60–93`: batch names (`botsHeroes1…`, `botsVillains1…`), the universe lookup, the enum lookups.
  - `Tools/Transitions/main.swift:12, 122`.
  - Phase 7: `Tools/RenderPromo` (`REEL=bots`), `Tools/RenderDocs` (`botsLineup`), `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts** (five, in-universe): "Roll out the new release", "Find the Decepticon in the test suite", "Transform this function into a class", "Scan the logs, Teletraan", "Refuel with energon and refactor".

## Cast

How the cartoon maps onto the engine's weapons:
- **`.blaster`** is the standard G1 rifle or arm gun. The cartoon's lasers came in every colour, so each shooter gets its own shot colour (listed in the tables) so a fight is readable. Megabyte's fusion cannon is a `.beam` (a continuous ray); most rifles are `.energy` bolts. The two spiders shoot `.web`.
- **`.saber`** (melee) is for fists, swords, claws and bites: Grimdeadlock's sword, Rumble's pile drivers (as Grumble), Garbage Collector's claws, Springr's sword, Wreck-Git's axe, Dinobyte's blade, the combiners' fists.
- **`.lightning` + `Magic`** for the few special powers, each with its own family and colour (see "Powers" below).
- **`.none`** for the pacifists and humans who don't fight: Beachbummer, Spike, Sparkplug, Carly, Alpha Build.
- **`motion: .fly`** for the jets and flyers (Stackscream and the Seekers, Skyfirewall, Swoopp, Laserbreak, Cyclonis, Scurge, Superiorn, Sky Lynks, Silverboot, Airazure, Tygerhawk, Waspiterator, Errorsaur, Infernode). **`.hover`** for the Quintessential Judge on his tentacles (`canSit: false`) and Depth Charj, the manta ray.
- **`bulk`** for giants: the combiners, Sudo Supreme, Metroplex, Fortress MaxInt, Triptycon, Scorpio-404, Unicron Job.

### Heroes (61)

**The Ark crew, seasons 1–2 (22)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Optimus Runtime | red chest with windscreen panes, blue arms, blue helmet with mouthplate and antennae, twin smokestacks | ion blaster rifle (`.energy`, white/red) | transforms into the red cab of a semi truck; callout "Autobots, roll out!" |
| 2 | Bumblebug | small, yellow, round helmet with two little horns | small blaster (`.energy`, yellow) | transforms into a yellow Beetle and beeps the horn; callout "Hi, Spike!" |
| 3 | Jazz.js | white and black, blue visor, a stripe on the chest | photon rifle (`.energy`, blue/white) | shoulder speakers pop up, a light show of coloured flashes; callout "Do it with style!" |
| 4 | Ironhyde | red, square, no faceplate (a grey face), van-shaped body | arm sprayer, liquid nitrogen (`.ice`), `armoured` | transforms into a red van; callout "Let's lock and load!" |
| 5 | Patchet | white with a red cross on the chest and red stripes | wrench (`.saber`) | the medic: welds a wound with sparks flying |
| 6 | Wheelhack | white, green and red, lights on the sides of his head that flash when he talks | gyro-gun (`.energy`, green) | an invention blows up in his hands, he's left blackened and coughing smoke; callout "It works! …oops." |
| 7 | Crawl | black and white police car, red light bar on the head | acid-pellet rifle (`.energy`, white/black-blue) | light bar flashes red-blue as he transforms into a patrol car; callout "Freeze!" |
| 8 | Mirr.age | white and blue, slim, racing livery | rifle (`.energy`, pale blue) | fades invisible and back (his electro-disruptor): a shimmering outline only |
| 9 | Houndog | green, jeep-shaped, spare wheel on the back | rifle (`.energy`, green-yellow) | projects a hologram tree beside himself, then switches it off |
| 10 | Sideload | red twin, rocket pack on his back | fists (`.saber`) | rocket-pack leap: jumps 8 px with a flame trail and lands |
| 11 | Sunstreamer | yellow twin of Sideload, a vain look | shoulder launcher (`.energy`, yellow-orange) | holds up a mirror and polishes his chest |
| 12 | Cliffhanger | small, red, flat-topped helmet (no horns, unlike Bumblebug) | glass-gas gun (`.energy`, red/white) | charges forward head-down, hot-headed; callout "Let me at 'em!" |
| 13 | Brawny | small, brown and green Land Rover body, bulky arms | fists (`.saber`), `armoured` | lifts a boulder above his head |
| 14 | Windcharjar | red, slim, little magnets on the arms | magnetism (see Powers) | pulls a steel girder through the air towards himself, drops it |
| 15 | Trailbreakpoint | black, truck camper on the back | rifle (`.energy`, white) | throws up his force field: a pale blue dome flickers round him |
| 16 | Blabstreak | silver-grey, blue and red, shoulder cannons | shoulder cannons (`.energy`, white/silver) | never stops talking: speech lines pour out of him; callout "…and another thing!" |
| 17 | Smokeskreen | red, white and blue racing car, "38" on the chest | rifle (`.energy`, blue) | puffs out a smoke screen, then rolls dice in the clearing |
| 18 | Dread Alert | white and red fire chief, light bar | rifle (`.energy`, red) | lights spin, he looks left and right, alarmed; callout "Intruder alert!" |
| 19 | Infurno | red fire truck, ladder on his back | water cannon (`.beam`, white/blue) | ladder swings up and sprays a fan of water |
| 20 | Perceptron | red and black, a microscope barrel on the shoulder | concussion blaster (`.beam`, cyan) | transforms into a microscope and peers; callout "Fascinating." |
| 21 | Bitblaster | red, boombox chest with a tape door, handle on the back | electro-scrambler (`.energy`, red/yellow) | music notes pour from his chest, a cassette pops out; callout "Rock and roll!" |
| 22 | Beachbummer | blue dune buggy, roll bar | none (a pacifist) | holds up a glittering mineral and admires it; callout "Peace, man." |

**The Dinobots (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 23 | Grimdeadlock | grey and gold, red visor, crown-like crest | sword (`.saber`), `armoured` | turns into a T. rex and roars, a puff of fire; callout "Me Grimdeadlock king!" |
| 24 | Slagg | grey and red, triceratops frill on the back | fire breath (`.fire`) | turns into a triceratops and paws the ground |
| 25 | Kludge | grey and gold, long brontosaurus neck folded behind | stomp (`.saber`) | turns into a brontosaurus; the ground shakes under his foot |
| 26 | Snarle | grey and red, stegosaurus plates on the back | tail swipe (`.saber`) | turns into a stegosaurus and fans his back plates |
| 27 | Swoopp | red, blue and grey, pteranodon wings | missiles (`.energy`, orange-red), `.fly` | turns into a pteranodon and circles |

**Humans (5).** Clawd in human costume, like the other universes' humans.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 28 | Spike Wickwitty | dark hair, red and white top, jeans | none | waves to Bumblebug; callout "Bumblebee!" |
| 29 | Sparkplug Wickwitty | white hair, cap, mechanic's overalls, a spanner | none | taps an engine with his spanner, listens |
| 30 | Carly | blonde, green top, a clipboard | none | sketches a diagram on her clipboard |
| 31 | Danny Wickwitty | small, blond, in a little exo-suit | exo-suit blaster (`.energy`, yellow) | the exo-suit's visor snaps shut |
| 32 | Marissa Fairclawn | dark hair, EDC uniform, beret | laser pistol (`.bullet`) | salutes |

**Giants and specialists (7)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 33 | Skyfirewall | huge, white and red, jet nose on the chest, wings | rifle (`.energy`, white/red), `.fly`, `bulk` | transforms into a big white jet and banks |
| 34 | Sudo Supreme | huge, grey and red, claw on one arm, gun barrel on the other | arm cannon (`.beam`, red), `armoured`, `bulk` | turns into a rocket on its pad, lifts an inch, settles; callout "Constructicons!" |
| 35 | Superiorn | Aerialbots combined: white and grey, red visor, yellow wings | rifle (`.energy`, white), `.fly`, `armoured`, `bulk` | five little jets dock into him one by one, the limbs flash |
| 36 | Defensa | Protectobots combined: white, red and blue, shield on the arm | fists (`.saber`), `armoured`, `bulk` | his force-field shield glows as each limb locks on |
| 37 | Sky Lynks | blue, white and red space shuttle with a lynx's head | claws (`.saber`), `.fly` | turns from shuttle into lynx on four legs, preens; callout "Magnificent!" |
| 38 | Metroplex | a walking city: grey, blue, towers on the shoulders | shoulder cannons (`.energy`, blue), `armoured`, `bulk` | city towers rise out of his back, then sink; callout "Metroplex heeds!" |
| 39 | Fortress MaxInt | huge, green and white, red visor | rifle (`.energy`, green), `armoured`, `bulk` | his head lifts off and turns out to be a smaller robot (Cerebros), who drops back in |

**Cybertron's past (2)** (season 2's flashback episodes)

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 40 | Alpha Build | ancient, red and blue, long moustache-like faceplate, hooded helmet | none | holds up a glowing data tablet and nods slowly |
| 41 | Elita 1.0 | rose red and cream, crested helmet, gold trim | time-freeze (see Powers) | freezes time: everything round her tints lilac for a beat |

**The Movie and after (9)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 42 | Hot Reload | maroon with yellow flames, spoiler on the back | twin pistols (`.energy`, orange-yellow) | transforms into a flamed sports car and revs; callout "Not now, Backup!" |
| 43 | Rootimus Prime | Hot Reload grown up: bigger, maroon and gold flames, the Matrix glowing in his chest | rifle (`.energy`, gold/white) | the chest opens and the Matrix shines; callout "Till all are one!" |
| 44 | Ultra Macros | white armour over blue, red trim, shoulder missiles | rifle (`.energy`, white/blue), `armoured` | tries to open the Matrix, it won't light, he sighs; callout "I'm just a soldier." |
| 45 | Backup | green-grey, old, battered | musket laser (`.energy`, teal) | leans on his musket and lifts a finger, a speech bubble with dots; callout "Reminds me of the time…" |
| 46 | Springr | green triple changer, rotor blades on the back | sword (`.saber`) | the rotors spin up and he lifts off a couple of pixels |
| 47 | Arcee-RC1 | hot pink and white, round helmet, slim | pistol (`.energy`, pink) | her red visor slides down to scan |
| 48 | Blurrr | blue, long and thin, a fin on the helmet | electro-laser rifle (`.energy`, blue) | zooms off-sprite in a streak and back before you saw him go; callout "Gottagogottago!" |
| 49 | Wheelee | tiny, orange-red and white | slingshot (`.thrown`, grey) | fires a pebble from his slingshot (he speaks in rhyme, but there's no short canon line) |
| 50 | Wreck-Git | junk-pile body, wheel on the back, TV-aerial ears | axe (`.saber`) | pulls a little TV out of himself and laughs at it; callout "Wreck and rule!" |

**The Maximals, Beast Wars (10).** Their signature is the beast-mode round trip (see "The transform"); the call on the way back is "Maximize!".

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 51 | Optimus Primitive | gorilla: black fur over a grey and blue robot chest, a silver-grey face with a mouthplate | fist blasters (`.energy`, white/blue) | turns into a gorilla, beats his chest and knuckle-walks a step; callout "Maximize!" |
| 52 | Rhinux | rhino: brown-grey hide, a big horn on the helmet, green eyes | twin chain guns (`.bullet`), `armoured` | turns into a rhino, snorts and paws the ground |
| 53 | Rat.catch() | rat: grey-brown fur, a long pink tail, red and black robot plates, antenna ears | pistol (`.energy`, red) and little bombs | plants a little bomb, scurries back, it pops; callout "Aw, slag!" (check in the audit) |
| 54 | Cheetorr | cheetah: yellow with black spots, a green-yellow robot face | tail-gun blaster (`.energy`, yellow-green) | turns into a cheetah and streaks off-sprite and back |
| 55 | Dinobyte | velociraptor: brown and tan, pale belly, a raptor head on his shoulder | rotating blade (`.saber`) | turns into a raptor and snaps; callout "Dinobyte, maximize!" |
| 56 | Tygatron | white tiger with black stripes, a calm green face | tail blaster (`.energy`, white) | sits in beast mode and watches a butterfly settle on his nose |
| 57 | Airazure | falcon: dark brown and white feathers, a beak-shaped visor | talon missiles (`.energy`, white/blue), `.fly` | turns into a falcon, circles and swoops down |
| 58 | Silverboot | wolf and eagle together: silver-grey wolf body, brown-and-white eagle wings, an eagle's head on his chest | feather darts (`.thrown`, silver), `.fly` | the gallant: wings fan out and he bows low |
| 59 | Depth Charj | manta ray: silver and purple, wide flat wings | rifle (`.energy`, blue), `.hover` | flattens into a manta and glides a lap a few pixels up |
| 60 | Tygerhawk | Tygatron and Airazure fused: white tiger body with black stripes, golden hawk wings and a hawk's head | storm powers (see Powers), `.fly` | wings spread and a little whirlwind spins up round him |

**HEM (1)**, as in every universe, last.

| 61 | HEM | a red Autobot-style chest with windscreen panes, a blue faceplate and helmet, wheels on the shoulders | ion blaster (Prime's) | the usual HEM routine |

**Which side:** Dinobyte is a **hero**. He leaves the Predacons in the very first episode, fights as a Maximal for the rest of his life and is remembered as one, so fans see him as a Maximal.

### Villains (51)

**The original Decepticons (12)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Megabyte | silver-grey, bucket helmet, black fusion cannon on the right arm | fusion cannon (`.beam`, dark violet core/magenta glow), `armoured` | the cannon charges with a glow, he shakes his fist; callout "Decepticons, attack!" |
| 2 | Stackscream | grey, red and blue jet, wings on the back, a pointed helmet | null rays (`.energy`, purple), `.fly` | rubs his hands, then cackles with a fist up; callout "I should be leader!" |
| 3 | Sound.wav | blue, a tape-deck chest, shoulder cannon, red visor | sonic waves (see Powers) | the chest door opens and a tiny cassette pops out and back; callout "Sound.wav superior." |
| 4 | Shock.exe | purple, one big yellow eye, no face, a gun for a left hand | arm gun (`.energy`, yellow) | the eye flares; callout "Logic!" |
| 5 | Thunder-hacker | Seeker jet in blue | rifle (`.energy`, blue/white), `.fly` | transforms into a jet; a sonic-boom ring bursts round him |
| 6 | Skywarpe | Seeker jet in black and purple | rifle (`.energy`, purple), `.fly` | teleports a few pixels with a purple pop |
| 7 | RAMjet | conehead Seeker: white, red and black, a nose cone on his head | headbutt (`.saber`), `.fly` | ducks his cone and rams forward |
| 8 | Laserbreak | red and gold condor, small | eye lasers (`.energy`, red), `.fly` | perches and turns his camera head, a red light blinking |
| 9 | Garbage Collector | black jaguar on four legs, red eyes, a missile pod | claws (`.saber`) | crouches low and pounces |
| 10 | Grumble | small, blue, round visor | pile-driver arms (`.saber`) | his arms turn into pile drivers and the ground shakes |
| 11 | Astro Retrain | purple and white, shuttle wings, train wheels | rifle (`.energy`, white) | turns into a steam engine and blows smoke, then back |
| 12 | Bitswing | purple and tan, tank turret and jet wings | turret cannon (`.thrown`, dark grey shell) | flips between tank turret and jet wings |

**The Insecticons (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 13 | Shrapnell | stag beetle: purple and gold, pincers | lightning from his antennae (see Powers) | echoes himself: "-nel, -nel" speech bubble; pincers snap |
| 14 | Bombshel | rhinoceros beetle: purple and black | cerebro-shells, mind control (see Powers) | fires a tiny shell that sticks on a head and blinks |
| 15 | Kick.bak | grasshopper: black and gold, long legs | kicks (`.saber`) | a big springy hop |

**Combiners and their teams (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 16 | DevOpsastator | Constructicons combined: green and purple, a crane arm, a scoop for a hand | fists (`.saber`), `armoured`, `bulk` | six parts flash one after another as he locks together |
| 17 | Motormonster | black and grey semi truck, a purple face, a sword | sword (`.saber`) | transforms into a black semi; callout "I am the king of the road!" |
| 18 | Menacer | Stunticons combined: black, grey and purple, sword | sword (`.saber`), `armoured`, `bulk` | the limbs clunk into place, a red visor flares |
| 19 | Swindler | tan jeep, shifty | rifle (`.energy`, orange) | holds up a "FOR SALE" tag; callout "Have I got a deal for you!" |
| 20 | Brutalicus | Combaticons combined: purple and green, tank cannon on the shoulder | shoulder cannon (`.thrown`, grey shell), `armoured`, `bulk` | the parts lock and his visor glows |

**Earthbound schemers (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 21 | Dr. Arkevil | human, bald, white lab coat, goggles | none | rubs his hands and cackles |
| 22 | Nightbyte | slim, black ninja robot, red visor | nunchaku (`.saber`) | a ninja backflip |
| 23 | Reflection | grey and black camera with a big lens | rifle (`.energy`, white) | his lens flashes as he takes a photo |

**The Movie and season 3 (10)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 24 | Gigabyte | purple and white, a crowned helmet, a huge cannon arm | cannon (`.energy`, white core/red glow), `armoured` | rants, the cannon flares, fist up; callout "Such a pity…" |
| 25 | Cyclonis | purple and grey, horned helmet, red eyes | rifle (`.energy`, red), `.fly` | transforms into a space jet |
| 26 | Scurge | blue-grey, a hooded "sweep" cowl and cape, red eyes | rifle (`.energy`, green), `.fly` | his eyes sweep left and right as he tracks |
| 27 | Unicron Job | a planet-sized robot: dark grey and rust, horned head, a ring round his body | eye ray (see Powers), `armoured`, `bulk` | turns into his planet (a sphere with a ring) and back; menace |
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
| 36 | Scorpio-404 | huge, purple and black, scorpion claws and a tail | claws and tail (`.saber`), `armoured`, `bulk` | turns into a scorpion (four legs), tail stings |

**The Predacons, Beast Wars (10).** Their beast-mode call is "Errorize!" (the show's "Terrorize!").

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 37 | Megabyte Rex | T. rex: purple and green, a T. rex head for a right hand, the tail on his left arm | dino-head flame (`.fire`, red-orange), `armoured` | settles back and holds up a yellow rubber duck, steepling his claws; callout "Yesss." |
| 38 | Tarantulus | tarantula: purple and black, red eyes, spider legs on his back | web launcher (`.web`, lime) | the mad scientist: rubs his claws and cackles, legs twitching |
| 39 | Waspiterator | wasp: green and yellow stripes, big bug eyes, buzzing wings | stinger gun (`.energy`, green), `.fly` | gets blown into pieces, which buzz back together; callout "Waspiterator has plan!" |
| 40 | Errorsaur | pteranodon: red and dark yellow, a long crested head | twin blasters (`.energy`, red), `.fly` | turns into a pterosaur and screeches; callout "Errorize!" |
| 41 | Scorp-200-OK | scorpion: purple and tan, red claws, a stinger tail | claw missiles (`.thrown`, red) | bobs and salutes eagerly, claws snapping |
| 42 | Blackarachnet | black widow: black with a red hourglass on the chest, yellow trim, spider legs on her back | web (`.web`, silver-white) | drops a silk line, swings once and folds her legs |
| 43 | Infernode | fire ant: dark red, antennae, small wings | flamethrower (`.fire`, orange-yellow), `.fly` | bows low, then a burst of flame; callout "For the Royalty!" |
| 44 | Quicksort | scorpion and cobra together: gold and black, a cobra head on the tail | cobra-tail blaster (`.energy`, green) | the cobra tail rears and hisses; callout "Yee-haw!" |
| 45 | RAM-page | crab: chrome silver and purple, big claws | claws (`.saber`), `armoured` | scuttles sideways and snaps both claws, cackling |
| 46 | Dinobyte 2.0 | Dinobyte's clone: dark chrome and red, glowing red eyes | eye lasers (`.energy`, red) | the red eyes flicker on, like booting up, then he snaps |

**Which side:** Blackarachnet is a **villain**. She spends nearly the whole show as a Predacon and only crosses over near the end, and the Silverboot pairing (Nemeses) works best with her on the other side.

**Agent-only small fry (5).** Bit parts that only ever appear as agents, kept last in the villain enum as the other universes do:

| # | Name | Look | Weapon |
|---|---|---|---|
| 47 | Frenzy.exe | Grumble's twin in red | sonic screech (`.energy`, red) |
| 48 | Buzzsore | gold condor cassette | eye lasers (`.energy`, gold), `.fly` |
| 49 | Rat.bat | purple bat cassette | bite (`.saber`), `.fly` |
| 50 | A Sweep | Scurge's lookalike troops, blue-grey | rifle (`.energy`, green), `.fly` |
| 51 | An Insecticon clone | a dull purple beetle | bite (`.saber`) |

**Totals:** heroes 22 + 5 + 5 + 7 + 2 + 9 + 10 + HEM = **61**. Villains 12 + 3 + 5 + 3 + 10 + 3 + 10 = 46, plus 5 agent-only = **51**. **112** in all.

**Ids.** Nothing is committed yet, so the order is free now and permanent once phase 2 commits the enum cases. The Beast Wars cast are added after the G1 and movie cast on each side. HEM stays the last hero (hero index 60). The agent-only five stay at the end of the villains (indices 46–50), as `clawdberg`'s do.

### Powers (each one looks different)

| Who | Family | Colours | What you see |
|---|---|---|---|
| Windcharjar | `waves` | red core, white glow | magnetic arcs pulsing out, horseshoe-shaped |
| Sound.wav | `waves` | yellow core, blue glow | sound rings from the shoulder speaker |
| Shrapnell | jagged lightning | pale yellow core, violet glow | forked bolts from both antennae |
| Tygerhawk | jagged lightning | white core, sky-blue glow | a bolt dropped from a little storm cloud over the target |
| Bombshel | `rings` | lime core, dark green glow | rings along a faint ray to the target's head |
| Mindswipe | `spell` | magenta core, purple glow | a twinkling spiral ribbon |
| Elita 1.0 | `touch` | rose core, lilac glow | a glowing fingertip; the target tints lilac and stops |
| Unicron Job | steady ray (`jagged: false`) | deep violet core, rust glow | a thick wavering ray from both eyes |

`magicVariants` gives each a different variant within its family on top of the colours. Windcharjar and Sound.wav share the waves family, and Shrapnell and Tygerhawk share jagged lightning, but each pair differs in colour and variant. None of these colours copies a power elsewhere in the app (Doctor Clawd's golden regeneration, the Clawd Files' greens): check in Clawd Royale.

### Lookalikes, inside and across universes

- **The Seekers** (Stackscream, Thunder-hacker, Skywarpe, RAMjet) share one body in the cartoon. They're kept apart by colour (red-blue, blue, black-purple, white with a cone head) and by signature. Only four, not the cartoon's six: Dirge and Thrust were cut as repaints.
- **Bumblebug and Cliffhanger** are one mould: yellow with horns vs red with a flat crest.
- **Sideload and Sunstreamer** are twins: red with a rocket pack vs yellow with a mirror.
- **Ironhyde, Patchet and Infurno:** red van, white ambulance with a red cross, red fire truck with a ladder.
- **Optimus Runtime and Motormonster** are both semi trucks: red-blue with a mouthplate vs black-grey with a purple face and a sword.
- **Arcee-RC1 and Elita 1.0:** hot pink and white with a round helmet vs rose red and cream with a crest and gold.
- **Megabyte and Gigabyte:** silver bucket helmet vs purple crown. They're also the `rivals` pair: the same mech in two bodies shouldn't lead two sessions back to back.
- **The three T. rexes:** Grimdeadlock (grey and gold, crown crest, sword), Megabyte Rex (purple and green, a T. rex head for a hand, the rubber duck) and Dinobyte, a raptor not a rex (brown and tan, small). **Megabyte Rex vs Gigabyte**, both purple: green trim and a dino hand vs white trim, a crown and a cannon.
- **Dinobyte and Dinobyte 2.0:** brown and tan vs dark chrome with red eyes.
- **The scorpions:** Scorpio-404 (huge, purple and black, `bulk`), Scorp-200-OK (small, purple and tan, red claws) and Quicksort (gold and black with a cobra tail).
- **The spiders:** Blackarachnet (black, red hourglass, silver web) vs Tarantulus (purple and black, red eyes, lime web).
- **The big cats:** Garbage Collector (black jaguar), Cheetorr (yellow, spotted), Tygatron (white, striped), Sky Lynks (a blue-white shuttle lynx).
- **The pterosaurs:** Swoopp (red, blue and grey) vs Errorsaur (red and dark yellow, crested).
- **Infurno and Infernode:** a red fire truck vs a dark red ant with a flamethrower.
- **Hot Reload, Rootimus Prime, Unicron Job and Errorsaur** have orange in the source. They're drawn maroon (with yellow flames), rust and red, never Clawd orange.
- **Against other universes:** Iron Clawd and War Machina (Marvelous Clawds) are red-gold and grey armour with a human-shaped faceplate; our robots carry vehicle parts (windscreens, wheels, wings) or beast parts, which they never do. The Cyberpersons (Doctor Clawd) are silver like Megabyte, but he has the bucket helmet and cannon. The Sentinal (Marvelous) is purple like Shock.exe, but Shock.exe has a single eye and no face. The Star Clawds droids are small and gold-white, unlike anyone here. Stevie Clawdberg's T. Wrecks is a plain dinosaur; Megabyte Rex is a robot with a dino head for a hand.

### Nemeses (30)

Each pair faces off first when both are on stage:
- Optimus Runtime ↔ Megabyte
- Hot Reload ↔ Gigabyte
- Rootimus Prime ↔ Unicron Job
- Ultra Macros ↔ Scurge
- Bitblaster ↔ Sound.wav (the cartoon's own rivalry)
- Skyfirewall ↔ Stackscream (old friends turned enemies)
- Sudo Supreme ↔ DevOpsastator
- Superiorn ↔ Menacer
- Defensa ↔ Brutalicus
- Metroplex ↔ Triptycon
- Fortress MaxInt ↔ Scorpio-404
- Grimdeadlock ↔ Pridaking
- Bumblebug ↔ Grumble
- Ironhyde ↔ Astro Retrain
- Mirr.age ↔ Skywarpe (the vanisher vs the teleporter)
- Houndog ↔ Garbage Collector (dog vs cat)
- Wheelhack ↔ Dr. Arkevil (the two inventors)
- Perceptron ↔ Shock.exe (the two scientists)
- Dread Alert ↔ Reflection (security vs surveillance)
- Backup ↔ The Quintessential Judge
- Wreck-Git ↔ Snarkticon
- Arcee-RC1 ↔ Cyclonis
- Optimus Primitive ↔ Megabyte Rex (the Beast Wars leaders)
- Rat.catch() ↔ Waspiterator (the show's running bout)
- Rhinux ↔ Tarantulus (the two engineers)
- Silverboot ↔ Blackarachnet (the knight and the spider, the show's cross-lines pairing)
- Depth Charj ↔ RAM-page (Depth Charge's long hunt for Rampage)
- Dinobyte ↔ Dinobyte 2.0 (the warrior and his clone)
- Cheetorr ↔ Quicksort (the two hot-headed rookies)
- Airazure ↔ Errorsaur (the two flyers)

That's more than the guide's usual 10–25, but this is a cast of 112, and every pair is one the shows set up.

**Rivals:** Megabyte and Gigabyte.

### Callouts for the leads (short list)

Optimus Runtime "Autobots, roll out!" · Megabyte "Decepticons, attack!" · Stackscream "I should be leader!" · Sound.wav "Sound.wav superior." · Rootimus Prime "Till all are one!" · Hot Reload "Not now, Backup!" · Ultra Macros "I'm just a soldier." · Gigabyte "Such a pity…" · Grimdeadlock "Me Grimdeadlock king!" · Backup "Reminds me of the time…" · Wreck-Git "Wreck and rule!" · Motormonster "I am the king of the road!" · The Quintessential Judge "Guilty!" · Blurrr "Gottagogottago!" · Bitblaster "Rock and roll!" · Optimus Primitive "Maximize!" · Megabyte Rex "Yesss." · Waspiterator "Waspiterator has plan!" · Errorsaur "Errorize!" · Infernode "For the Royalty!" · Dinobyte "Dinobyte, maximize!" · Quicksort "Yee-haw!" · Rat.catch() "Aw, slag!"

### Left out, and why

- **Same-mould repaints** with nothing of their own: Dirge and Thrust (Seekers), most Constructicon, Stunticon, Aerialbot, Protectobot, Combaticon and Predacon members (the combined giant reads far better at 72×52 than five similar small robots), Frenzy as a lead (he's agent-only as Frenzy.exe).
- **Huffer:** orange; he'd read as plain Clawd. **Gears** overlaps Brawny (grumpy little brawler). **Hoist, Grapple, Tracks, Seaspray, Powerglide, Warpath, Cosmos:** fine characters with less to do on screen.
- **Chip Chase:** his wheelchair can't be drawn honestly on Clawd's four legs.
- **Beast Wars:** Optimal Optimus (Optimus Primitive's upgrade, the same character), Transmutate (a sad story with little to do), the Tripredacus Council (barely on screen), the Vok (formless aliens), the Transmetal repaints of the main cast (same characters).
- **The live-action films:** busy designs that don't read at 72×52.
- **Crossover cameos** (G.I. Joe's Flint, Cobra Commander): other franchises.
- **On-screen deaths** and the movie's swearing (see Tone). Optimus's death is never drawn: the Matrix passing (Mechanics) is the cheerful version.
- **Megabyte's pistol mode:** Clawd on four legs as a handgun doesn't read and isn't great on a desktop. His signature is the cannon instead.

## Places (23)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. Keys all start with `bots`, so they can't clash with the six universes or the sibling plans (checked: no `bots…` key exists in `Sources/App/Universes` today). The palette swings between 80s Earth (bright blue sky, desert orange-pink, green grass), Cybertron's metal blues and purples, and Beast Wars' prehistoric greens, lava reds and crystal pinks.

| # | Key | Place | Still | Moving | Tall extras |
|---|---|---|---|---|---|
| 1 | `botsArk` | **The Ark, the Autobot base** (default) | the crashed ship's inside: hexagon wall panels, the Teletraan-1 computer's big screen and console | Teletraan's screen scrolls a schematic, console lights blink | the volcanic rock ceiling, the Ark's girders, energon lines |
| 2 | `botsMountHilary` | **Mount St. Hilary** | the volcano with the Ark's nose sticking out of the side, pine forest | smoke from the crater, a bird crossing | a tall blue sky, the summit |
| 3 | `botsNemesis` | **The Decepticon base under the sea** | purple corridors, a big porthole window, Megabyte's chair | bubbles and passing fish through the porthole | the dark sea above, a shaft of light |
| 4 | `botsIacon` | **Iacon, Cybertron** | the Autobots' golden-age city of metal towers | energon pulses along conduits in the floor | Cybertron's two moons, towers reaching up |
| 5 | `botsSpaceBridge` | **The space bridge** | Shock.exe's tower on Cybertron, a launch pad ringed by pylons | a green-yellow shimmer column on the pad, then gone | the bridge's beam rising into a black sky |
| 6 | `botsEnergonDam` | **The dam** (the pilot's power raid) | a sunny hydroelectric dam, stacks of pink energon cubes | water pouring over the spillway, cubes glowing | the full dam wall and the reservoir (sunny, unlike the Clawd Files' night-time Ruskin Dam) |
| 7 | `botsDinobotIsland` | **Dinobot Island** | palm trees, ferns, a smoking volcano, primeval swamp | lava bubbling, ferns swaying, a pterosaur gliding | the volcano's peak, a giant dragonfly |
| 8 | `botsHighway` | **The desert highway** | an American desert road, red mesas, a road sign | heat shimmer, a tumbleweed rolling past | big mesas and a wide sky |
| 9 | `botsCityStreet` | **The city at night** | a downtown street, parked cars, billboards | traffic lights cycling, neon flickering | skyscrapers with lit windows |
| 10 | `botsGoldenLagoon` | **The Golden Lagoon** | a jungle pool of shining gold liquid | the gold surface ripples and glints | jungle canopy, hanging vines |
| 11 | `botsSkyfireIce` | **The Arctic ice cave** | blue ice walls with Skyfirewall's giant silhouette frozen inside | sparkles of ice, dripping water | an ice ceiling with shafts of light |
| 12 | `botsVectorSigma` | **Vector Sigma's chamber** | a deep vault under Cybertron with a huge golden sphere | the sphere pulses, glyphs flow over it | the vault's dark height, rings of light |
| 13 | `botsAutobotCity` | **Autobot City, Earth 2005** | domes and towers, Metroplex's city mode, a shuttle on the pad | windows lighting, a shuttle's engines glowing | more towers, the shuttle's launch tower |
| 14 | `botsMoonbase` | **Autobot Moonbase** | grey lunar dome, Earth in the black sky | blinking beacons, stars | Unicron Job's ringed shape far off in the sky (eerie, not moving) |
| 15 | `botsUnicronSpace` | **Unicron Job's orbit** | the planet-sized robot in deep space, rust and grey | debris drifting past, a slow turn | his horned head looming over everything |
| 16 | `botsUnicronBelly` | **Inside Unicron Job** | giant gears and conveyor belts, red-lit | gears turning, conveyor moving | towering machinery, steam vents (no acid, no digestion) |
| 17 | `botsJunkion` | **Junkion** | the junk planet: heaps of scrap, TVs, aerials | TVs flicker with static and test patterns | towers of junk |
| 18 | `botsQuintessa` | **Quintessa's courtroom** | the Quintessons' high bench, a plank over a pool | fins circling in the pool | the court's gloomy height, five-faced statues |
| 19 | `botsChaar` | **Chaar** | the Decepticons' grey ash planet, broken towers | ash falling, a flicker of energon | a dim sky, a dead sun |
| 20 | `botsNebulos` | **Nebulos** | the Headmasters' planet: pink and purple sky, organic towers | spores drifting, a flowering plant opening | twin suns, floating islands |
| 21 | `botsAxalon` | **The Axalon, the Maximal base** | the crashed grey ship wedged into a cliff face above a river, the lift platform at its foot, jungle all round | a waterfall pouring beside the hull, the hull's auto-guns swivelling | the cliff top, the ship's antenna, a pterosaur circling |
| 22 | `botsDarksyde` | **The Darksyde, the Predacon base** | the Predacon ship sunk in a volcanic cave, a river of lava, Megabyte Rex's throne and his bath tank | lava bubbling, a red glow pulsing on the rock | the cave's vault, steam vents, a crack of sky far above |
| 23 | `botsEnergonFields` | **The energon fields** | a prehistoric canyon at dusk: raw energon crystals jutting from the rock in glowing pink clusters, giant ferns | the crystals pulse and throw off little sparks | the sky with **two moons** (the show's big clue to where they really are), a volcano far off |

The energon fields differ from Dinobot Island by being a dusky rocky canyon with crystals, not a palm-tree swamp, and the Darksyde's lava cave is red rock and fire, not Unicron's gears.

**Homes:**
- **Ark crew** and **humans:** the Ark. Except Beachbummer (the Golden Lagoon), Skyfirewall (the Arctic ice cave), Houndog (Mount St. Hilary, he loves Earth's outdoors).
- **Dinobots:** Dinobot Island.
- **Giants:** Sudo Supreme, Metroplex, Superiorn and Defensa at Autobot City; Sky Lynks at the Moonbase; Fortress MaxInt on Nebulos.
- **Cybertron's past:** Alpha Build at Vector Sigma's chamber; Elita 1.0 at Iacon.
- **Movie Autobots:** Autobot City. Wheelee on Quintessa (where he was found), Wreck-Git on Junkion.
- **Maximals:** the Axalon. Except Tygatron and Tygerhawk (the energon fields: Tigatron lived out in the wild) and Depth Charj (the energon fields, the loner on his hunt).
- **Original Decepticons:** the base under the sea. Shock.exe at the space bridge; the Seekers at the dam; Astro Retrain and Bitswing at the space bridge.
- **Insecticons:** the city at night (raiding the power). **DevOpsastator:** the dam. **Stunticons** (Motormonster, Menacer, Swindler): the desert highway. **Brutalicus:** Chaar.
- **Earthbound schemers:** the city at night.
- **Movie Decepticons:** Gigabyte, Cyclonis, Scurge, Octaine, Sixshooter and Pridaking on Chaar; Unicron Job in his orbit; Snarkticon and the Judge in Quintessa's court; Triptycon at Autobot City (he's there to attack it).
- **Headmasters:** Nebulos.
- **Predacons:** the Darksyde. Except Dinobyte 2.0 (the energon fields, where he was made to hunt).

## Mechanics that make it its own universe

1. **Rides** (`Rides.swift`, three new ones):
   - **The Autobot shuttle** (white and red, from the movie) picks up and drops off the movie crew and the giants who'd fit: Hot Reload, Rootimus Prime, Ultra Macros, Backup, Springr, Arcee-RC1, Blurrr, Wheelee, Danny, Spike.
   - **Astro Retrain** carries Decepticons: he's a triple changer whose job in the cartoon is literally being the Decepticon shuttle. The ride is his purple-and-white shuttle mode. Whenever Astro Retrain is on stage himself, the others still ride a shuttle that looks like him; that's the cartoon's logic too.
   - **The space bridge** (a ring of pylons and a green-yellow shimmer column) for anyone from Cybertron: Shock.exe, Alpha Build, Elita 1.0.
   - **Everyone else rolls out (decided).** Characters with a vehicle mode play the fold and drive off-stage in vehicle mode; the Beast Wars cast and the G1 beasts change into their animal and run or fly off; the rest (humans, giants, the Judge) leave as in any universe. The hook is in `Overlay.swift` where an actor leaving without a ride is drawn (~line 1255: today it fades, and sinks or rises): for this universe it slides the actor off-stage over the fade time, and the drawing gets the leaving fraction so it can show the fold, then the vehicle or beast frame (the same frames as parking and the signature).
2. **The Matrix of Leadership, which is Clawdformers' regeneration.** When a Claude Code or pi session led by a **Matrix bearer** compacts its context, the Matrix passes to the next bearer: **Optimus Runtime → Ultra Macros → Rootimus Prime → Optimus Runtime** (the last step is season 3's *The Return of Optimus Prime*). Compaction is a session handing on what it knows, and that's what the Matrix does: it holds the wisdom of past Primes. It wraps round, and skips anyone already leading another session.
   - The effect, drawn in `BotsMatrix.swift`: the leader's chest opens, the Matrix's handle-shaped crystal glows, blue-white light pours up in a column with drifting sparkles, and the new bearer is standing in it as the light fades. Caption: "LIGHT OUR DARKEST HOUR". This deliberately looks nothing like Doctor Clawd's golden flare: blue-white, a column, not a burst.
   - Local hero indices: Optimus Runtime 0, Ultra Macros 43, Rootimus Prime 42, so the chain is `[0, 43, 42].map { base + StatusStore.heroBase + $0 }`.
   - Optimus Primitive isn't a Matrix bearer: Beast Wars never gives him the Matrix, so he's not in the chain.
3. **Megabyte → Gigabyte, the second chain (decided).** When a session led by Megabyte compacts, Unicron Job reformats him into Gigabyte, as in the movie. One way: compacting Gigabyte does nothing, and if Gigabyte is already leading another session, Megabyte stays as he is.
   - The effect, also in `BotsMatrix.swift`: Unicron Job's deep-violet eye ray (his power colours) washes over Megabyte, the silver plates fly off in a ring, and Gigabyte's purple body and crown lock into place with a white flash. Caption: "REFORMATTED".
   - Villain ids: Megabyte `base + 0` → Gigabyte `base + 23`.
   - **The engine change:** `Universe.regenerations` becomes a list of chains, each with whether it wraps (`[(ids: [Int], wraps: Bool)]`). Doctor Clawd's Doctors become one wrapping chain, the Matrix another, and Megabyte → Gigabyte a one-way chain. `StatusStore`'s PreCompact (line 336) finds the chain holding the leader and steps along it, skipping anyone on stage, and stops at the end of a one-way chain. The overlay picks the Matrix or reformatting effect by which chain fired.
4. **Habits:**
   - **Parked in vehicle mode** when a session sits (all characters with a vehicle mode), and **curled up in beast mode** for the Beast Wars cast (in the drawings, not the engine).
   - **Sound.wav ejects a cassette:** now and then a tiny Laserbreak flies a lap round him and docks.
   - **Mirr.age goes invisible** when idle for a while: just a shimmering outline, until someone needs him.
   - **Skywarpe teleports** a short hop along the stage with a purple pop.
   - **Backup's stories:** a long speech bubble of dots, and whoever stands next to him nods off (a "z").
   - **Stackscream schemes:** when Megabyte is on stage, he edges behind him and mimes wearing his helmet, then snaps back when Megabyte turns.
   - **Energon overload:** at the energon fields, the Beast Wars cast stay in beast mode, as the show's raw energon forced them to (the drawing checks the place).
5. **Practice drills, which are bespoke:**
   - Autobots at the target range in the Ark (Teletraan pops up red targets);
   - Decepticons stack pink energon cubes into a pyramid (the pilot's plan);
   - Wheelhack tests an invention, which blows up;
   - the Dinobots stomp and roar at a boulder until it cracks;
   - Bitblaster and Sound.wav play music (notes from the chest);
   - Perceptron peers into his microscope;
   - Dinobyte runs through his sword forms;
   - Rat.catch() sets a booby trap, then steps in it.

   Nobody floats cross-legged in meditation (`Drills.swift:54`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one.

1. **Skeleton:**
   - the universe case and all the wiring above;
   - **Optimus Runtime, Bumblebug and Megabyte** (the enum's first cases: heroes 0–1, villain 0), each with the transform signature, so `BotsKit.swift`'s fold helper is written now and proven on a truck and a Beetle;
   - the Ark (`botsArk`), the menu icon, HEM's costume, the saver option and Preview support; plain wipes for now.

   It runs end to end in the app, the window, the screen saver and Clawd Royale.
2. **Core ensemble.** About 40 characters:
   - all 61 hero and 51 villain enum cases committed first as stand-ins, then the art;
   - drawn: the Ark crew, the Dinobots, Spike and Sparkplug; the original Decepticons, the Insecticons, DevOpsastator; plus Optimus Primitive and Megabyte Rex, to prove the beast-mode fold early;
   - 8 places: the Ark, Mount St. Hilary, the base under the sea, Iacon, the space bridge, the dam, Dinobot Island, the desert highway; with homes and nemeses for these;
   - parked-in-vehicle-mode for everyone drawn so far.
3. **Rest of the cast and places.** All 112 characters and 23 places, every home filled. Ends with **the character audit** (every weapon, shot colour, power, motion, signature and callout checked against the source; a table of only the mismatches).
4. **Mechanics:** the three rides, rolling out, the Matrix of Leadership, Megabyte → Gigabyte with the chains engine change, the habits and the bespoke drills.
5. **Transitions:** the twelve `BotsTrip`s and the chrome place-name finishing touch (see below).
6. **Polish pass** (always before docs): every weak spot from phases 2–5, split by file and fixed in parallel, with before-and-after renders.
7. **Docs and release:**
   - the README's universe table and a cast-and-places section, roster and locations sheets, a `botsLineup` desktop strip and a social preview (`docs/roster-clawdformers.png` …);
   - `llms.txt` (universe list, folder and `Bots…` prefix, the Matrix and reformatting mechanics), and a `CHANGELOG.md` entry each phase;
   - a trailer, `REEL=bots`, opening on the transformation logo morph.
   - **Needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order in the tables above, and phases never renumber.

## Polish pass (after phase 5, before docs)

The weak-spot list starts empty and is filled in at the end of each phase. Things to watch for from the start:
- the fold helper at window size: the transform must still read at agent size (small), not just leader size, for vehicles and beasts alike;
- vehicle colours that drown out Clawd's orange;
- the giants' `bulk` in duels with small robots (Wheelee vs Scorpio-404);
- the four Seekers, the twin pairs, the scorpions, the spiders and the T. rexes side by side in one sheet;
- roll-outs at the stage edge: a vehicle shouldn't pop out of existence mid-drive.

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`. Before calling a phase done, `./build.sh --release <version>` with `-Xfrontend -warn-long-expression-type-checking=300` to catch slow fold maths.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Optimus Runtime"` (check every frame of the transform) and `build/preview cast out.png "Optimus Primitive"` (the beast mode);
  - `build/preview fight out.png "Optimus Runtime" "Megabyte"`;
  - `build/preview place out.png "Clawdformers"`;
  - the batch sheets, one per Art file. Look at the PNGs before showing them.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> botsArk botsIacon`.
- **In the app:**
  - Settings → Universe → Clawdformers: new sessions are Autobots or Maximals; subagents can be Decepticons, Predacons or small fry.
  - Idle sessions park in vehicle mode (or curl up in beast mode).
  - A session ending: cars drive off, beasts run off.
  - The screen saver's Options include it; Random and Clawd Royale reach it.
- **The Matrix:** `/compact` in a Claude session led by Optimus Runtime: the light, and Ultra Macros steps out.
- **Reformatting:** `/compact` in a session led by Megabyte: Unicron Job's ray, and Gigabyte. `/compact` again: he stays Gigabyte. Doctor Clawd's regenerations still work after the chains change.

## Transitions (`BotsTrip`, 12)

**Style.** Pixel art in the look of a mid-80s cel cartoon: bold dark outlines, flat colours with one highlight, no gradients except the chrome lettering's banded shine. The palette is Autobot red, Decepticon purple, chrome greys with a white highlight band, energon pink, Matrix blue-white, and starfield black. Halftone only for the explosions and the Matrix light. Nothing glossy or painted. The insignias are our own: a red, rounded robot face with Clawd's eyes for the heroes, a purple, angular one for the villains. Neither copies the real Autobot, Decepticon, Maximal or Predacon faces.

**Sound** (trailer only; the app is silent): the transforming whir-and-clunk evoked with our own synth notes, never the real sound effect or theme.

**Finishing touch.** Every transition ends with the place's name sliding in from the side in **chrome lettering** with a shine sweeping across it, the cartoon's title-card style, before it fades. It replaces the usual place-name label in this universe.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Transformation Logo Morph** (signature opening) | The old place breaks into square metal tiles that flip and slide like a robot's panels folding, with a white spark at each joint. A car shape in the middle folds up into a robot head; CLAWDFORMERS slams in in chrome, the shine sweeps across, then the panels unfold onto the new place. The longest and rarest. | any time, rarely |
| 2 | **The Insignia Spin** | The cartoon's scene-break bumper: the hero insignia zooms out of the old place and spins; mid-spin it flips into the villain insignia (or back), then zooms into the new place. | anyone; the side of whoever's arriving picks which face it ends on |
| 3 | **Roll Out** | A convoy (a red semi, a yellow Beetle, a white racer) drives across the panel left to right; the new place is behind them, the old one ahead, with a dust trail at the join. | Optimus Runtime, the car Autobots; the desert highway, the city at night |
| 4 | **The Space Bridge** | A shimmering green-yellow column comes down on the old place, the picture is drawn up into it in streaks, and it comes back down on the new place. | Shock.exe, Astro Retrain, Alpha Build; Iacon, the space bridge |
| 5 | **Teletraan Alert** | The old place shrinks onto Teletraan-1's big screen, "ALERT" flashes red with scanlines, the screen changes to the new place, and the camera pushes through it. | the Ark crew, Dread Alert, Rhinux; the Ark, the Axalon |
| 6 | **Energon Cubes** | Glowing pink cubes stack up from the floor until the panel is a wall of them, then they lift away one row at a time onto the new place. | the Decepticons, DevOpsastator; the dam, the base under the sea |
| 7 | **Light Our Darkest Hour** | The Matrix opens in the middle of the panel, blue-white light floods out in a widening column until the old place is gone, and it fades on the new place. | Optimus Runtime, Rootimus Prime, Ultra Macros, Hot Reload; Autobot City |
| 8 | **The Unicron Job** | Unicron Job's ringed planet shape drifts across the old place, his jaws open, close over the picture, and open again on the new place. Only comes up with him present (`needsOwner`). | Unicron Job, Gigabyte, Megabyte; his orbit, his belly, the Moonbase |
| 9 | **Combiners Lock** | The panel splits into five vertical strips that slide and clunk together like limbs locking on (a flash at each join), a giant's silhouette forms, then breaks apart on the new place. | the combiners and Sudo Supreme |
| 10 | **Seeker Fly-by** | Three jets in a V scream across, their contrails wiping the old place to the new one. | Stackscream, Thunder-hacker, Skywarpe, RAMjet; open skies (the dam, Mount St. Hilary) |
| 11 | **Eject!** | Sound.wav's tape door fills the panel and opens; a cassette with the old place on its label pops out, a new one with the new place slides in, the door shuts, and we zoom into the label. | Sound.wav, Bitblaster, Laserbreak, Garbage Collector, Grumble |
| 12 | **Dinobot Stomp** | A huge dino foot stamps down, cracks spread across the old place, and it falls away in chunks onto the new place. | the Dinobots, Megabyte Rex, Dinobyte, Dinobyte 2.0; Dinobot Island, the energon fields |

**Not used:**
- **Junkion channel-surf** (overlaps Teletraan Alert).
- **Sharkticon chomp** (overlaps The Unicron Job).
- **Quintesson faces turning** (five small faces won't read at panel scale).
- **Headmaster head pop** and **Vector Sigma's glow** (too small, and the Matrix light covers the glow).
- **Galvatron's rebuild** belongs to the Megabyte → Gigabyte reformatting (Mechanics), not a transition.
- **A Beast Wars "Maximize!" morph** (it's the same panel fold as the logo morph; the beast mode lives in the signatures instead).

**Promo.** The Transformation Logo Morph (#1) is the trailer's title sequence.

## Promo: `REEL=bots`

About 45–50 seconds, on the `doctorShots` pattern:
- **`intro` (~9 s), the logo morph:** black; a spark; metal panels slide across the screen in time with a synth whir-and-clunk. A sports car folds up into a robot head with Clawd's eyes, the two insignias flip past each other, and **CLAWDFORMERS** slams in in chrome with a shine sweeping across. The tagline under it, our own pun: **"More than meets the AI."** Panels fold away into white.
- **Set piece (~9.5 s), the battle of Autobot City:** Astro Retrain lands on the pad and Decepticons pour out; DevOpsastator stomps over a tower. Optimus Runtime's truck roars in from the left (the movie's charge), transforms in mid-air and lands, rifle up; a short exchange of fire with Megabyte, who's knocked flat. Then Unicron Job's shadow falls over the city, Rootimus Prime opens the Matrix, and the blue-white light washes the screen.
- **`hook`, `status`, `agents`, `ais`, `endcard`** as in the other trailers. Copy ideas:
  - `desktop`: "Robots in disguise. Agents in disguise."
  - `status`: four characters, one per state, "Idle? It's parked."
  - `agents`: "Every subagent gets to be a robot in disguise."
  - `window`: at `botsArk`, "There's more to this window than meets the eye."
- **Music:** 80s synth rock: driving synth bass, a gated drum, a power-chord synth stab on the title. Our own notes; never the theme's melody or the real transform sound.

## Decisions (2026-10-16)

1. **Name: Clawdformers.** Code: `case clawdformers`, key `"clawdformers"`, folder `Sources/App/Universes/Clawdformers/`. The `Bots…` file prefix, `bots…` place keys, the `transformers` branch and `REEL=bots` stay.
2. **Scope:** G1, the 1986 movie and **Beast Wars**. Beast Wars adds 20 characters: 10 Maximal heroes (Optimus Primitive, Rhinux, Rat.catch(), Cheetorr, Dinobyte, Tygatron, Airazure, Silverboot, Depth Charj, Tygerhawk) and 10 Predacon villains (Megabyte Rex, Tarantulus, Waspiterator, Errorsaur, Scorp-200-OK, Blackarachnet, Infernode, Quicksort, RAM-page, Dinobyte 2.0). Dinobyte is a hero and Blackarachnet a villain (reasons under the tables). Three places are added (the Axalon, the Darksyde, the energon fields), with 8 new nemesis pairs. The live-action films are out. New totals: **61 heroes, 51 villains (5 agent-only, indices 46–50), 112 characters, 23 places, 12 transitions.**
3. **Compaction, two chains:** the Matrix passing on (Optimus Runtime → Ultra Macros → Rootimus Prime, wrapping), and **Megabyte → Gigabyte**, one way, caption "REFORMATTED". `regenerations` becomes a list of chains, each with a wraps flag.
4. **Roll out on leaving:** yes. Vehicle-mode characters fold and drive off, beasts run or fly off, via a small hook where walk-offs are drawn (`Overlay.swift` ~1255).
5. **Naming rule:** coding-language names for the leads and anyone where a coding pun lands cleanly; everyone else keeps a light pun. Your list is applied everywhere. G1 Scorponok becomes **Scorpio-404**, since the Beast Wars one is Scorp-200-OK.
   **Renames I chose myself (veto any):**
   - Trailblazer → **Trailbreakpoint**
   - Sunpreener → **Sunstreamer**
   - Windcharjer → **Windcharjar**
   - Sludje → **Kludge**
   - Fortress Maximum → **Fortress MaxInt**
   - Elita Won → **Elita 1.0**
   - Ramjett → **RAMjet**
   - Kickbak → **Kick.bak**
   - Nightbyrd → **Nightbyte**
   - Reflecta → **Reflection**
   - Ratbatt → **Rat.bat**
   - Beast Wars names you didn't give: Cheetor → **Cheetorr**, Silverbolt → **Silverboot**, Airazor → **Airazure**, Tigatron → **Tygatron**, Tigerhawk → **Tygerhawk**, Depth Charge → **Depth Charj**, Blackarachnia → **Blackarachnet**, Tarantulas → **Tarantulus**, Quickstrike → **Quicksort**, Dinobot II → **Dinobyte 2.0**.
   - The "Unicrawn Devours" transition is now **The Unicron Job**.
   - Kept as light puns, since no coding pun read cleanly: Ironhyde, Houndog, Cliffhanger, Brawny, Blabstreak, Smokeskreen, Dread Alert, Infurno, Beachbummer, Slagg, Snarle, Swoopp, Superiorn, Defensa, Sky Lynks, Metroplex, Springr, Blurrr, Wheelee, Skywarpe, Grumble, Shrapnell, Bombshel, Motormonster, Menacer, Swindler, Brutalicus, Cyclonis, Scurge, Snarkticon, Triptycon, Octaine, Pridaking, Sixshooter, Mindswipe, Weirdwulf, Buzzsore, the humans and the Judge.
6. **Swaps:** none.

The plan is ready for phase 1 when you say start.

**Still open (small, can wait until phase 4):**
- A **stasis-pod ride** for the Beast Wars cast (a pod streaks down from orbit and opens), as a fourth ride. Without it they simply roll out like everyone else.
