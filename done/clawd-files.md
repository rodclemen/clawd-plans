# Plan: a new universe, The Clawd Files (X-Files parody)
<!-- track: repo=rodclemen/clawd-clash branch=x-files folder=ClawdFiles title="The Clawd Files" source="The X-Files" cast=82 places=20 -->

## Context

Clawd Clash has four universes: Star Clawds, Marvelous Clawds, Detective Clawds and Doctor Clawd. This plan adds an X-Files parody as a full ensemble, the same way Doctor Clawd was built. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

- **Name: The Clawd Files** (chosen on 2026-10-15).
- **Code naming** avoids the franchise name, as the other universes do:
  - `case clawdFiles` with key `"clawdFiles"`.
  - Folder `Sources/App/Universes/ClawdFiles/`, file prefix `Files…`.
  - Branch `x-files`.
- **Raw value: `case clawdFiles = 4`.** It comes before Stevie Clawdberg (decided 2026-10-15), so that plan moves to 5. Ids are `rawValue * 1000` and are saved, so this can't change once it ships.
- **Naming style:** light puns on the on-screen names (Fox Clawder, Dana Scrawly). Actors' names are never used.
- **Size:** about **82 characters**, which is Star Clawds' size: 36 heroes including HEM, and 46 villains including 3 agent-only. Plus **20 places**.
- **Tone:** the show swings from comedy to real horror. Characters are picked so they stay fun at desktop-toy scale. That rules out Donnie Pfaster, the Peacock family ("Home") and Gerry Schnauz.

## How a universe plugs in (checked against the code on 2026-10-15)

**New code: `Sources/App/Universes/ClawdFiles/`**
- `FilesRoster.swift`:
  - `enum FilesVillain` and `enum FilesHero`, append-only, with `hem` as the last hero.
  - The persona dictionaries, `.merging([.hem: hemPersona(.clawdFiles)])`.
  - `Location.filesHome(of:)`, `filesNemeses`, the ride closure, `let filesTheme = Theme(...)`.
- `Art/FilesHeroes1…N.swift` and `Art/FilesVillains1…N.swift`, about 8–10 personas per file, in the pattern of `DoctorHeroes1.swift`.
- `Places/FilesScenes1…N.swift` as `let filesPlacesN: [Location: Place]` plus `static let` keys. Keys must be unique across universes.
- `FilesIcon.swift`: the menu bar icon, 28×26, colour and mono. A flying saucer over a sliver of beam, or a manila folder stamped X.
- `FilesWipes.swift`: the transitions, last (see the end of this plan).

**Wiring into the existing code.** Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎.
- **`Sources/Shared/Universe.swift`:** the case, `title`, `villainCount`, `heroCount`, `agentOnly`, `claudeSide` (default: Claude is the heroes), `rivals` if one pair should never lead back to back.
- **`Sources/App/Theme.swift:42`:** `Theme.of`.
- **`Sources/App/Locations.swift:73`:** `.merging(filesPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift`:** a `.files(FilesTrip)` case in `duration`, `draw` and `pick`.
- **`Sources/App/Universes/Hem.swift`:** HEM's costume in every switch: a trench coat, an FBI lanyard and a flashlight.
- **`Sources/App/Rides.swift`:** the ride (see Mechanics).
- ⚠︎ **`Sources/Saver/SaverView.swift:77, 86, 209`:** the Options choice and the trip switch. The build won't complain if this is missed.
- ⚠︎ **`Sources/App/Drills.swift:53`:** whether this universe floats cross-legged in meditation. It shouldn't: nobody in the show meditates in the air.
- ⚠︎ **`Sources/App/Overlay.swift:855`:** the Playground's sample prompts per universe.
- **Clawd Royale** picks the new cast and places up through `Universe.allCases`. Check that the menu bar icon and arch-enemies still hold when the scene is a Clawd Files place.
- **Tools:**
  - `Tools/Preview/main.swift:60–83`: batches and lookups.
  - `Tools/Transitions/main.swift:81`.
  - `Tools/MakeIcon`, `Tools/RenderShowcase`, `Tools/RenderPromo` (`REEL=files`), `Tools/RenderDocs`.

## Cast

Each entry gives: parody name, weapon or motion, and signature move. How the engine's weapons map onto the show:
- **`.blaster`** with a small `ShotStyle` is the FBI sidearm, the main weapon on the hero side. Agents shoot; that's the show.
- **The flashlight** is a steady beam (`.lightning`, `Magic(jagged: false)`, pale yellow, short reach) on top of the pistol as a signature. Mulder and Scully are never without one.
- **`.saber`** (melee) is for brawlers: Doggett, Skinner, Krycek.
- **Paranormal powers** use `.lightning` / magic: the Pusher's will, Gibson's mind-reading, Cecil L'ively's fire.
- **`armoured: true`** fits the super soldiers (bullets don't stop them) and the Alien Bounty Hunter.

### Heroes (36)

**The X-Files unit and the FBI (7)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Fox Clawder | grey suit, wide tie, trench coat | pistol + flashlight | spits sunflower seeds; points at the sky, "I want to believe" |
| 2 | Dana Scrawly | red bob, long coat, gold cross | pistol + flashlight | holds up her badge; one raised eyebrow |
| 3 | A.D. Walter Skinnard | bald, glasses, shirt sleeves | pistol, melee | takes off his glasses and rubs his eyes |
| 4 | John Doggedd | crew cut, dark suit | pistol, melee | squares up, fists first |
| 5 | Monica Reyez | long dark hair, leather jacket | pistol | blows a gum bubble; "did you feel that?" shimmer |
| 6 | Agent Einstine | blonde, sceptic's frown | pistol | arms folded, unimpressed |
| 7 | Agent Millar | young, eager, suit | pistol | flips open a laptop |

**The Lone Gunclawds (5)**

| 8 | Bytes (Byers) | beard, suit and tie | none | adjusts his tie, reads a pamphlet |
| 9 | Frohack (Frohike) | short, leather jacket, camera | camera flash (steady ray) | snaps a photo with the flash |
| 10 | Lanky (Langly) | long blond hair, band T-shirt | none | types furiously; headphones |
| 11 | Jimmy Bondd | big, sweet, cap | none | gives a thumbs-up |
| 12 | Yves Harlowe | sleek, black coat | pistol | vanishes in a step (short blink) |

**Informants and allies (15)**

| 13 | Deep Clawt (Deep Throat) | trench coat, grey hair | none | passes an envelope in the shadows |
| 14 | Mister X | tall, black overcoat | pistol | sticks a tape X on the window |
| 15 | Marita Covarrubyass | blonde, UN suit | pistol | a cool glance over the shoulder |
| 16 | Gibson Prays | boy, glasses | mind-reading (soft ray) | moves a chess piece without touching it |
| 17 | Samantha Clawder | girl, 1970s pyjamas | none | glows in a beam of light |
| 18 | Melissa Scrawly | hippie, crystals | none | holds up a crystal that sparkles |
| 19 | Margaret Scrawly | cardigan, pearls | none | a mother's hug |
| 20 | Jeffrey Spendr | young agent, sharp suit | pistol | shreds a file (he's on our side now) |
| 21 | Shannon McMahawk | the good super soldier | `armoured`, melee | lifts a car door off its hinges |
| 22 | Max Fenig | NICAP cap, glasses | none | a UFO-chaser's camera |
| 23 | Agent Pendrill | lab coat | none | blushes when Scrawly walks past |
| 24 | Arthur Dales | retired agent, cardigan | pistol | swings a baseball bat |
| 25 | Clyde Bruckclaw | sad hat, rumpled suit | none | sees a death, shudders; holds a kewpie doll |
| 26 | Jose Chung | writer, glasses | none | taps a typewriter, pages fly |
| 27 | Leyla Harriclaw | eager agent, notebook | pistol | knows every case by heart (file folders flutter) |

**Friendly oddities (5).** The Humbug circus and the show's comic side; they look like nobody else.

| 28 | Dr. Blockclaw | bald, tattooed | none | hammers a nail into his nose (the circus trick) |
| 29 | The Conundrum | tattooed, silent | none | eats anything, a goldfish included |
| 30 | Sheriff Hartwell ("Bad Blood") | buck teeth, cowboy hat | pistol | tips his hat |
| 31 | Tad O'Clawley | conspiracy webcaster | none | shouts into a microphone |
| 32 | Frank Blackclaw | the Millennium crossover, grey hair | pistol | sees visions in flashes |

**Pets and small friends (3)**

| 33 | Queequeg | Pomeranian | none (bites, melee) | yaps |
| 34 | Daggoo | Mulder's goldfish, in a bowl | none, `.hover`, `canSit: false` | blows a bubble (agent-friendly) |
| 35 | Teena Clawder | Clawder's mother, twinset, pearls | none | a guarded look; keeps the family secrets |

**HEM (1)**, as in every universe, last.

### Villains (46)

**The Syndicate and the conspiracy (10)**

| Name | Weapon | Signature |
|---|---|---|
| The Cigarette-Smoking Clawd | pistol (rarely fires) | lights up; smoke rings drift across the stage |
| Alex Clawcek | pistol, melee; one arm in later seasons | black-oil eyes now and then |
| The Well-Manicured Clawd | none | sips brandy |
| The First Elder | none | taps a cane |
| Strughold | pistol | stern stare |
| Diana Fowlclaw | pistol | stands just behind Clawder |
| Deputy Director Kersh | none | slams a file on the desk |
| A.D. Follmer | pistol | sneers |
| The Toothpick Man | `armoured`, melee | chews a toothpick |
| Bill Clawder (the father) | pistol | a Syndicate man with a guilty conscience; looks away |

**Aliens and their soldiers (10)**

| Name | Weapon | Signature |
|---|---|---|
| The Alien Bounty Hunter | stiletto (melee), `armoured` | shape-shifts into whoever is beside him, then back |
| The Black Oil | `.hover`, `canSit: false` | slides across the floor; seeps into someone's eyes |
| The Grey | steady ray (light from the hands) | tilts its head |
| A Faceless Rebel | fire (lightning, orange) | burnt-shut face, torch |
| The Colonist | none, `.hover` | pupil-less eyes, leans |
| Knowle Rohrer | `armoured`, melee | metal spine shows when he's hit |
| Billy Miles | `armoured`, melee | pulls himself back together |
| Duffy Haskell | `armoured`, melee | reassembles after a fall |
| Lord Kinbote (Jose Chung's alien) | steady ray | a towering red alien |
| The Crew-Cut Man | pistol | the Syndicate's assassin, flat-top haircut |

**Monsters of the week (23)**

| Name | Weapon | Signature |
|---|---|---|
| Eugene Clawms (Tooms) | melee (claws) | stretches thin and slides into a vent |
| The Flukeman | melee | rises out of a sewer pipe |
| The Pusher (Robert Modell) | will (steady ray) | "you will…": the target freezes and sways |
| Leonard Betts | melee | sheds his head (keep it cartoonish) |
| The Great Mutato | none | a cheese sandwich and a Cher song; sympathetic |
| The Jersey Devil | melee | leaps across the stage |
| The Wendigo | melee | runs on all fours |
| Mr. Chuckleteeth | none | grins in a clown mask |
| Eve 6 | poison (steady green ray) | twin clones finish each other's sentences |
| Virgil Incanto | melee | a fat-sucker; keep it tame |
| The Chupacabra | melee | hunched, quills |
| Big Blue | `.hover` (in water), `canSit: false` | rises out of the lake, head only |
| Tithonus (Alfred Fellig) | camera flash (steady ray) | photographs the next death |
| Cecil L'ively | fire (lightning, orange) | sets himself alight unharmed |
| Luther Lee Boggs | none | channels the dead |
| Eddie Van Blundht | none | shape-shifts into Clawder (comic) |
| Ronnie Strickland ("Bad Blood") | melee (fangs) | the hapless pizza-boy vampire |
| Guy Mann ("Were-Monster") | melee | a lizard in a sports jacket |
| The Trashman ("Home Again") | melee | made of garbage; Band-Aid nose |
| The Tulpa ("Arcadia") | melee | a garbage creature summoned by a wish |
| The Mothmen ("Detour") | melee | camouflaged in the trees, only their red eyes show |
| The Rain King | weather (lightning, blue) | brings a storm and frogs |
| The Teliko | melee | pale as chalk, blowpipe |

**Agent-only small fry (3).** Like the MSE-6, these only ever appear as agents:
- a killer bee (fly),
- a robot cockroach ("War of the Coprophages"),
- a flukeworm.

### Nemeses

Each pair faces off on the same stage:
- Clawder ↔ the Cigarette-Smoking Clawd
- Scrawly ↔ Eugene Clawms
- Skinnard ↔ Alex Clawcek
- Doggedd ↔ Knowle Rohrer
- Reyez ↔ the Toothpick Man
- Einstine and Millar ↔ the Trashman
- Bytes, Frohack, Lanky ↔ Strughold
- Deep Clawt ↔ the Well-Manicured Clawd
- Mister X ↔ the Alien Bounty Hunter
- Marita ↔ the Black Oil
- Gibson Prays ↔ the Faceless Rebel
- Spendr ↔ the First Elder
- Arthur Dales ↔ the Colonist
- Sheriff Hartwell ↔ Ronnie Strickland
- Jose Chung ↔ Lord Kinbote
- Dr. Blockclaw ↔ the Jersey Devil

## Places (20)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. Many are at night, so flashlight beams and headlights do the lighting.

1. **The X-Files office (FBI basement):** the default. The I WANT TO BELIEVE poster, pencils stuck in the ceiling tiles, a slide projector flickering.
2. **Skinnard's office, FBI HQ:** blinds, the flag, rain on the window.
3. **The Lone Gunclawds' den:** banks of monitors, a reel-to-reel spinning.
4. **Clawder's apartment, #42:** the fish tank bubbling, the couch, a tape X glowing on the window.
5. **Bellefleur woods at night:** flashlight beams through the trees, lights in the sky.
6. **Area 51:** desert, a black helicopter, a hangar door.
7. **The Antarctic ice field:** the alien ship rising out of the ice.
8. **The Syndicate's club, 46th Street:** cigar smoke curling, leather chairs.
9. **The quarantine railcar ("731"):** strip lights flicker, a ticking bomb counter.
10. **Tooms's apartment block, Baltimore:** a liver-lit vent and a nest of newspaper.
11. **The sewers of Newark:** dripping pipes, something moving in the water.
12. **Gibsonton, Florida ("Humbug"):** the circus folks' trailers and a sideshow banner.
13. **The cornfield and the bee domes:** glowing domes, bees swarming.
14. **Lake Okobogee:** the dock, the water rippling.
15. **The Mutato's farm:** black and white, like the episode.
16. **Ruskin Dam:** the faceless rebels' fire on the bridge.
17. **The autopsy bay:** steel tables, a hanging microphone, Scrawly's scales.
18. **Chaney, Texas ("Bad Blood"):** a motel at night, a pizza sign flickering.
19. **The Reflecting Pool at night:** the informants' meeting place, the Washington Monument lit up.
20. **The mothership:** a vast saucer interior, light from below.

**Homes:**
- Agents work from the basement office.
- The Gunclawds have their den.
- Aliens live in the Antarctic ice field or the mothership.
- The Syndicate sits in its club.
- Each monster has the place from its episode.

## Mechanics that make it its own universe

1. **Rides.** These replace ships flying in:
   - **Heroes:** the unmarked FBI sedan pulls up with its headlights on.
   - **Villains:** the black helicopter.
   - **Aliens:** leave by **abduction**, rising in a beam of light from a saucer.
2. **Missing time, which is Clawd Files' regeneration.** When a Claude Code or pi session led by an **FBI agent** compacts its context, the agent is abducted. The FBI agents are the seven of the unit: Clawder, Scrawly, Skinnard, Doggedd, Reyez, Einstine and Millar. Everyone else ignores compaction, as non-Doctors do in Doctor Clawd.
   - a beam of light comes down, and the agent rises out of view;
   - a beat later they're set back down, dazed, with a "MISSING TIME" caption.
   
   Compacting is a session losing time, so this fits the show. It reuses the `PreCompact` path Doctor Clawd already added (`StatusStore`, `DoctorRegeneration.swift`), with the same face rather than a new one. The list of who can be abducted goes in `Universe` next to `regenerations`.
3. **Habits:**
   - The Cigarette-Smoking Clawd's smoke drifts across the stage.
   - The Alien Bounty Hunter takes on the look of a character next to him for a few seconds.
   - Tooms slides off through a vent when idle.
   - The Pusher's targets freeze.
   - Krycek's eyes go black now and then.
4. **Practice drills, which are bespoke:**
   - agents at the FBI firing range (paper targets);
   - Scrawly reads a case file;
   - the Gunclawds hack (green text over their heads);
   - Skinnard does jumping jacks (push-ups were tried: Clawd's body is wider than tall, so lying down it reads as a box on its end);
   - Queequeg chases his tail.
   
   Nobody floats cross-legged in meditation (`Drills.swift:53`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one.

1. **Skeleton:**
   - the universe case, theme and Universe wiring;
   - Clawder, Scrawly and the Cigarette-Smoking Clawd;
   - the basement office, the menu icon, HEM's costume, the saver option and Preview support.
   
   It runs end to end in the app, the window, the screen saver and Clawd Royale.
2. **Core ensemble.** About 35 characters:
   - the FBI unit, the Gunclawds, Deep Clawt, X, Marita, Gibson and Samantha;
   - the Syndicate and the aliens;
   - Tooms, the Flukeman, the Pusher and the Jersey Devil;
   - 8 places, with the nemeses for these.
3. **Rest of the cast and places.** Up to 82 characters and 20 places, with the homes complete.
4. **Mechanics:** the rides, missing time, the habits and the bespoke drills.
5. **Transitions:** the ten `FilesTrip`s and the typewriter caption (see below).
6. **Docs and release:**
   - the README, roster and location sheets, a desktop line-up and a social preview;
   - the app icon gains a fifth universe;
   - `llms.txt`, and a `CHANGELOG.md` entry each phase;
   - a trailer, `REEL=files`, opening on the montage transition as its title sequence.
   - **Needs your OK first, since it's public:** a showcase repo and a cask in `release.sh` (`write_cask`, the `others` list and its `preflight_steps` universe preset).

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

## Polish pass (after everything else is done)

Weak spots found in phase 2, to come back to once phases 3–6 are done (the user asked for this on 2026-10-15):
- **The Jersey Devil:** reads as a boxy hairy blob; needs a creature silhouette (hunched, long limbs).
- **The Flukeman:** reads as a pale marshmallow; needs to look more like a worm (segments, a longer body).
- **The Alien Bounty Hunter:** at the peak of his shape-shift he looks striped rather than clearly like Scrawly.
- **The Toothpick Man:** the toothpick is a few pixels and barely shows at desktop size.
- **The Well-Manicured Clawd and Kersh** have no weapon (as planned), so in a fight they stand holding a brandy glass or a file. Consider giving them something to do in a fight.
- **Smaller:** Skinnard's eye-rubbing hand is small, Einstine's folded arms read as a grey band, Lanky's T-shirt logo reads as a "+", Frohack's stubble is faint, the Grey's head tilt is one pixel, Tooms's legs merge into a line at the ends of his squeeze, Samantha's glow washes her out.
- **Phase 3 characters:** Yves Harlowe is almost all black (a silhouette with a face); Margaret's grey temples barely show; Spendr's shredder is small; the Wendigo looks giraffe-like when it rears and its claw swing doesn't show; Mr. Chuckleteeth's mask tilt shows a sliver of orange; Eve 6's hair frames her face like a helmet; the Colonist reads as a floating torso; the Crew-Cut Man's turtleneck sits where a mouth would be; Strughold's grey temples are tiny; Lord Kinbote may want `armoured`; Cecil L'ively and Luther Lee Boggs lean on Clawd orange (Luther's jumpsuit is close to it); the Robo-Roach's feelers get a busy outline; the Mothmen read a little like a leafy hut; the Trashman is busy at desktop size; Ronnie's resting fangs are two pixels; Tad's sound arcs and LIVE light are tiny; Daggoo's fish is small; the Conundrum's jigsaw reads as a grid; Clyde's kewpie doll is small and pale; Frank Blackclaw's collar reads like jowls; Pendrill's blush is subtle.
- **Phase 3 places:** the Antarctic saucer is in the moving layer, so transitions' still snapshots won't show it; the bee domes' and Ruskin Dam's screen-saver skies are plain stars; the Antarctic ice ridges are simple; the dam's fire is small in the window; the railcar's screen-saver ceiling is many repeated ribs; the lamp glow at Tooms's block reads grey; the Monument nearly touches the top of the window strip; the autopsy light's cone is faint; Gibsonton's banner strongman is crude and the Ferris wheel is thin; the lake is a big plain area on the screen saver and Big Blue is small on it; the farmhouse roof is shallow.
- **Places:** furniture in the indoor rooms is small next to the characters; the club's ceiling smoke is faint; Skinnard's office and the sewer vault have bare upper areas on the screen saver; the sewer outlet half-hides its pouring water.

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Fox Clawder"`;
  - `build/preview fight out.png "Fox Clawder" "The Cigarette-Smoking Clawd"`;
  - `build/preview place out.png "The Clawd Files"`.
- **In the app:**
  - Settings → Universe → The Clawd Files: new sessions are agents and allies, subagents can be villains or small fry.
  - The screen saver's Options include it.
  - Random and Clawd Royale reach it.
- **Missing time:** `/compact` in a Claude session.

## Open questions for you

- **Swaps:** any character you'd rather have in or out. The cast list is full, so a swap keeps the count.

## Transitions (`FilesTrip`, 10)

These are the ten chosen on 2026-10-15: your top five from your list, plus five I added. Each is weighted by who is on screen and where, like `DoctorTrip`.

**Style.** Every transition is drawn in the app's pixel art, not a painted comic. The palette is desaturated forest greens, cold blue-greys, deep black shadows and the odd eerie fluorescent green, with halftone dots and a little grain where it helps. There are no glossy or neon effects. Following the show, most of them stay restrained: something slightly unnatural happens to an ordinary picture.

**Ending.** Every transition ends with the **typewriter caption**: the new place's name and city type themselves in letter by letter in the corner (for example "FBI HEADQUARTERS / WASHINGTON, D.C."), the way every scene opens in the show. Typed captions also replace the usual place-name label in this universe.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Black Oil** | A pool of black oil spreads up from the floor against gravity, swallows the scene into a glossy black surface, ripples, then pulls back to reveal the new place. | Clawcek, the Black Oil, Marita; the Antarctic ice field |
| 2 | **The Blinking Eye** | A huge eye fades in with the old place reflected in its pupil. It blinks to black, and when it opens the new place is in the pupil; pull out until it fills the screen. | anyone (the credits' eye); Gibson Prays |
| 3 | **The Classified File** | The old place becomes a black-and-white photo clipped to a case file. Papers slide across with TOP SECRET stamps and redaction bars, and a folder opens on a photo of the new place, which zooms in and gets its colour back. | the FBI unit; the basement office, Skinnard's office |
| 4 | **Television Interference** | The old place is seen on a CRT. Scanlines roll, it loses sync, fragments of surveillance footage flash, it turns to static, and it clears on the new place before pushing through the screen. | the Lone Gunclawds; their den, Clawder's apartment |
| 5 | **The Opening Montage** | The full title sequence: the UFO, the eye, the distorted face, the ghostly silhouette in a corridor, the red-lit hand, then racing clouds and THE TRUTH IS OUT THERE; the clouds part on the new place. It's the longest and the rarest. | any time, rarely |
| 6 | **The UFO Abduction** | A saucer over a darkened scene. Its green-white cone widens until the panel washes out, with symbols flickering inside it, then fades to the new place under the same light, and the beam pulls back up. | the Grey, the Colonist, the Faceless Rebel; Area 51, the mothership |
| 7 | **The Flashlight Investigation** | The old place goes dark to faint outlines. Two flashlight beams sweep and cross in a white flash, then light up the new place as it comes back. | Clawder and Scrawly; night places (the woods, the sewers, Tooms's block) |
| 8 | **Cigarette Smoke** | A ribbon of smoke drifts in, thickens into grey spirals with brief silhouettes of figures and government buildings, then clears on the new place with a last wisp across the front. | the Cigarette-Smoking Clawd, the Syndicate; the club |
| 9 | **Surveillance Satellite** | The old place turns into a gridded green satellite image and pulls up to a dot on a map. The reticle moves and locks on, and the view dives through clouds into the new place. | trips between places far apart (Area 51 to the Antarctic) |
| 10 | **Paranormal Distortion** | The picture misbehaves: rows of pixels slide out of line and stretch, like the warped face in the credits, collapse to a thin line and open out on the new place. | the Pusher, Eve 6, Luther Lee Boggs; the paranormal monsters |

**Not used:** "The Truth Is Out There" and "The Mysterious Hand" (both are in the montage), "The Alien Silhouette" (overlaps the abduction), and "The Invisible Entity" and "The Alien Implant" (fine glass and circuit detail that won't read at pixel scale).

**Promo.** The opening montage (#5) is the trailer's title sequence: `REEL=files` opens on it before the scenes, the way Doctor Clawd's trailer opens on its time vortex.

**Check them** with `Tools/Transitions`, which renders all ten between two Clawd Files places.
