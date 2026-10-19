# Plan: a new universe, Harry Clawder (Harry Potter parody)
<!-- track: repo=rodclemen/clawd-clash branch=harry-potter folder=HarryClawder title="Harry Clawder" cast=85 places=22 -->

## Context

Clawd Clash has seven universes on `main` (b5c6ab8, 2026-10-18). This plan adds a parody of Harry Potter: **the seven books and eight films only**. No Fantastic Beasts, no Cursed Child, no games. It clears the threshold easily: the hard part was choosing who to leave out, not finding enough people.

| Universe                             | Heroes | Villains | Total | Places | Transitions |
|--------------------------------------|--------|----------|-------|--------|-------------|
| Star Clawds                          |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds                     |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds                     |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd                         |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files                      |     36 |       46 |    82 |     20 |          11 |
| Stevie Clawdberg                     |     64 |       54 |   118 |     23 |          10 |
| Clawd of the Rings                   |     38 |       38 |    76 |     22 |           9 |
| Clawd Slayer (branch `buffy`)        |     36 |       48 |    84 |     20 |  in progress |
| Superclawdtural (planned)            |     35 |       45 |    80 |     20 |          12 |
| Battleclawd Galactica (planned)      |     26 |       25 |    51 |     17 |          10 |
| Stranger Clawds (planned)            |     29 |       16 |    45 |     16 |          10 |
| **Harry Clawder (proposed)**         | **45** | **40** | **85** | **22** |      **12** |

(heroCount includes HEM and Hedwig, who is agent-only; villainCount includes the four agent-only small fry.)

- **Viability: comfortably over.** 43 drawn heroes and 36 drawn villains, both well over 20.
- **Name: Harry Clawder** (chosen on 2026-10-18). The alternatives were Harry Clawter, Clawgwarts and The Boy Who Clawed. The Clawd Files already has Fox Clawder; the first names differ and the two look nothing alike, so they sit fine together in Clawd Royale.
- **Code naming** avoids the franchise's trademarks:
  - `case wizards` with key `"wizards"`.
  - Folder `Sources/App/Universes/HarryClawder/`, file prefix `Wand` (`WandRoster.swift`, `WandHeroes1.swift`, `WandWipes.swift` …). No file in the repo uses `Wand` as a prefix today. Top-level names start with `wand` or are `private`, as `scripts/pr-guard.py` asks.
  - Place keys are prefixed `wand…` (`wandGreatHall`), the way Clawd Slayer prefixes its own with `slayer`.
  - Branch `harry-potter`. Trailer `REEL=wand`.
- **Raw value: next free when the build starts.** Check before the skeleton commit: `main` uses 0 to 6 (`middleEarth = 6`); the `buffy` branch has `slayer = 7`; Henrik's Clawd Burton lives on his fork (HEM42/clawd-clash) with a value of its own; Superclawdtural (`hunters`), Battleclawd Galactica (`fleet`), Stranger Clawds (`hawkins`) and the older plans may have taken some by then. Read other branches with `git show <branch>:Sources/Shared/Universe.swift`, never by switching. Ids are rawValue*1000 and permanent.
- **Naming style:** light puns only where they read at a glance: **Harry Clawder**, **Hermione Clawnger**, **Lord Clawdemort**, **Draco Malclaw**. Everyone else keeps the on-screen name, because a forced pun is worse than none. Actors' names are never used, and the author isn't named anywhere in the app or the docs.
- **Size:** 85 characters and 22 places, in the guide's 70 to 100 target.

### How the cast is split

Heroes are the trio, the students, the Weasleys, the Hogwarts staff, the Order, the visiting champions and the creatures and ghosts on their side. Villains are Clawdemort and the Death Eaters, the Slytherin bullies, the Ministry and the press, the troublemakers (Lockhart, Peeves, Filch, the Dursleys) and the monsters. The grey ones go by how the story ends:
- **Snape, Slughorn, Kreacher, Percy → heroes.**
- **Draco, Narcissa, Fudge, Griphook → villains.**
- **The Boggart → villain**, shown as Snape in Neville's grandmother's clothes.

### Tone: what's left out, and why

The later books are dark. Clawd Clash is a desktop toy, so:
- **Left out entirely:** Voldemort's rebirth from the cauldron and the Little Hangleton graveyard, Cedric's death, Sectumsempra wounds, Bathilda Bagshot's snake reveal, Greyback biting children, the Astronomy Tower, the Cruciatus curse.
- **Drawn eerie, never gory:** the Dementor (hooded rags and frost), the Inferius (pale and drowned, rising and sinking), the cave.
- **Kept cartoonish:** Ron's slugs, Nick's head on its flap of skin, Aunt Marge swelling up.
- **Callouts checked:** Ron's "Bloody hell!" is kept (mild, and his line); Molly's is cut to "Not my daughter!". Nobody uses an in-universe slur.
- **Lookalikes in Clawd Royale:** Dumbledore is purple and silver with half-moon glasses so he never reads as Gandclawd the Grey; Dobby wears his pillowcase and has big green eyes so he never reads as Gollum; McGonagall's green tartan keeps her apart from the Marvel and DC sorcerers.
- **No real people, no actors' names, no author's name.**
- **Music:** a celesta-like lilt in our own notes, never the theme.

## How a universe plugs in (checked against the code on 2026-10-18, main b5c6ab8)

**New code: `Sources/App/Universes/HarryClawder/`**
- `WandRoster.swift`:
  - `enum WandHero` and `enum WandVillain`, append-only, with `hem` as the last hero.
  - The persona dictionaries, `.reduce([.hem: hemPersona(.wizards)])`.
  - `Location.wandHome(of:)` for heroes and villains, `wandNemeses`, the ride closure, `let wandTheme = Theme(...)`.
  - The `static let` place keys and `let wandPlaces` merged from the Places files.
- `Art/WandHeroes1…5.swift` and `Art/WandVillains1…5.swift`, 8 to 10 personas per file, in the pattern of `RingsHeroes1.swift`. Shared helpers (robes, house scarves and ties, wands, pointed hats, the ghosts' pearly silver) go in one `WandKit.swift` with `wand`-prefixed names.
- `Places/WandScenes1…3.swift` as `let wandScenesN: [Location: Place]`.
- `WandIcon.swift`: the menu bar icon, 28×26, colour and mono. A lightning-bolt scar under round glasses, or a wand with a spark.
- `WandPensieve.swift`: the compaction mechanic (see Mechanics).
- `WandWipes.swift`: the twelve transitions, last.

**Wiring into the existing code.** Copy what `middleEarth` and `clawdberg` did. Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎.
- **`Sources/Shared/Universe.swift`:**
  - `:9–15` the case; `:17` `key`; `:25` `title`; `:33` `villainCount` (40); `:37` `heroCount` (45);
  - `:50` `agentOnly`: Hedwig (hero 43, so `base + StatusStore.heroBase + 43`) and the four small fry (villains 36 to 39, 0-based);
  - `:65` `claudeSide` (default false: Claude plays the heroes);
  - `:74` `guises`: Clawdemort and Tom Riddle are the same person (villains 0 and 10), never on screen together. Today it's `guard self == .middleEarth else { return [] }`, so it becomes a `switch` (Clawd Trek and Clawds of the Universe may already have done that), and its doc comment gains the pair;
  - `:83` `homebound`: the Basilisk (villain 28) only at `"wandChamber"`. Today it's `self == .middleEarth ? … : [:]`, so it becomes a `switch` too;
  - `:90` `abductees`: the four Pensieve users (see Mechanics), with a doc comment like the other two;
  - `:106` `isReleased`: return `false` for `.wizards` until phase 6 if it's built on `main`, as Clawd of the Rings was.
- **`Sources/App/Theme.swift:40–48`:** `Theme.of`. **`:89–90`** add `knightBus` and `fordAnglia` to `enum Ride`, and **`:93`** add `knightBus` to `Ride.drives` (it comes in along the ground; the Anglia flies). Check `boardingOffset` just below for both.
- **`Sources/App/Locations.swift:70–72`:** `.merging(wandPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift`:** in phase 1, add `.wizards` next to Star Clawds in `pick` (`case .starWars, .wizards: return nil`, `:49`). In phase 5, take it out of that line and add a `.wizards(WandTrip)` case to the enum (`:7–13`), `duration` (`:15–23`), `draw` (`:27–35`) and `pick` (`:47–68`), and the doc comment at `:3–6`.
- **`Sources/App/Universes/Hem.swift:31–32, 55–57, 76, 115, 130, 151–157, 174, 196, 203`:** HEM's persona and costume in every switch (Hogwarts robes, a yellow and black Hufflepuff scarf, a pointed hat, a wand). Several of those are `u == .middleEarth` checks for Rohan's helmet and shield; leave those alone.
- **`Sources/App/Rides.swift:18–34`:** the Knight Bus and the Ford Anglia in `drawRide` (phase 4), next to the others.
- ⚠︎ **`Sources/Saver/SaverView.swift`:** nothing to add; the Options list and the trip choice build themselves from `Universe.offered` (`:89`, `:208–212`).
- ⚠︎ **`Sources/App/Drills.swift:51`:** the meditation guard (`meditates`). Harry Clawder doesn't meditate, so it must stay out. **`:73`** and the bespoke-drill table: merge `wandBespokeDrills`.
- ⚠︎ **`Sources/App/Overlay.swift`:**
  - `:875–878` the Playground prompts (five, below), a `case .wizards:` next to `.clawdberg` and `.middleEarth`;
  - `:1271–1272` is where `OutaTime` is chosen for `clawdberg` (`MissingTime` is the fallback for everyone else in `abductees`); `WandPensieve` hooks in the same way;
  - the Peeves, Whiz-bang and Dementor's-chill habits hook into the tick;
  - the cast-size check is at `:180`.
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`**: decide per universe-specific `if`. Harry Clawder joins none of the existing ones; it adds its own habits.
- ⚠︎ **Compaction:** `Sources/Shared/StatusStore.swift:367` already marks any leader in `abductees`; check it picks up `.wizards` without changes. `HookInstaller.swift` already registers the hook.
- **Clawd Royale** picks the cast and places up through `Universe.allCases`. Check the menu bar icon and arch-enemies still behave when a scene is in a Harry Clawder place, and that the homebound Basilisk is recast anywhere but the Chamber.
- **Tools:**
  - `Tools/Preview/main.swift:7, 65` (the batch doc comments), `:87` (the universe lookup, `"wizards": Theme.of(.wizards).cast`), `:102–104` (the batch arrays `wandHeroes1…`, `wandVillains1…`, `wandHem`), and the enum lookups by case name.
  - `Tools/Transitions/main.swift:7, 15` (usage comments), a `shownWand` like `shownRings` at `:88–90`, and the branch at `:133` (phase 5).
  - Phase 6: `Tools/RenderPromo` (`REEL=wand`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts** (`Overlay.swift:875`):
1. "Solemnly swear you're up to no good, then run the tests."
2. "Send the build log by owl."
3. "Fix the merge conflict before Snape takes points."
4. "Expelliarmus the flaky test."
5. "Ask the Sorting Hat which branch this goes in."

## Cast

How the engine's weapons map onto the books and films. Nearly everyone fights with a wand, so the variety comes from **using every kind of spell the engine has**, each character with a colour of their own:

| Look | Who |
|---|---|
| **Steady ray** (`.lightning`, `jagged: false`) | Harry (red Expelliarmus). Clawdemort (green) and Dumbledore (gold) with `thick: true`, so their duel looks heavier than anyone else's. Harry's red against Clawdemort's green gives the films' Priori Incantatem lock for free. |
| **Forked lightning** (`jagged: true`) | Grindelwald only: the Elder Wand, blue-white. |
| **Sparkle ribbon** (`spell`) | McGonagall (gold, Transfiguration), Flitwick (blue, Charms), Ollivander (silver). |
| **Rings** (`rings`) | Snape's Legilimency, grey-violet. |
| **Waves** (`waves`) | Dobby's finger-snap elf magic, pale blue. |
| **Touch** (`touch`): no stream, a glow round the target | Tom Riddle drawing life away (pale green); the Dementor's Kiss (grey-blue). The eerie two. |
| **Beam** (`.blaster` + `.beam`) | Moody (blue), Kingsley (gold), Dolohov (purple flame), Umbridge (pink). |
| **Thrown** (spells that become things) | Ron's backfiring slug curse (green), Draco's Serpensortia (a little black snake), Ginny's Bat-Bogey bats (black), Sprout's Mandrakes, Trelawney's crystal balls, Wood's Quaffle, Peeves's water balloons. |
| **Fire** | Fred's Whiz-bangs, Seamus's blasts, Crabbe's Fiendfyre, the Horntail. |
| **Energy bolts** (`.blaster` + `.energy`) | Everyone else, each in a colour of their own (listed in the tables). No two the same within one group. |

- **`.saber`:** Neville's and Griphook's Sword of Gryffindor, Macnair's axe, Kreacher's cleaver, Petunia's frying pan, Greyback's claws, the monsters, fists.
- **`.arrow`:** Hagrid's crossbow, Firenze's bow. **`.bullet`:** Uncle Vernon's shotgun.
- **Motion:** `fly` for Buckbeak, Fawkes, Hedwig, the Horntail, Madam Hooch on her broom; `hover` and `canSit: false` for the ghosts, Peeves and the Dementor.
- **`bulk`:** Hagrid, Grawp, Buckbeak, Firenze, Vernon, Crabbe, Goyle, the Basilisk, Aragog, the troll, Fluffy, the Horntail. **`armoured`:** the Basilisk and the Horntail.
- **Ghosts** are drawn in solid pearly silver, so the outline holds; only a faint glow round them is see-through.
- Everyone, monsters included, is Clawd in costume on Clawd's four legs: the centaur's and hippogriff's horse legs are Clawd's legs.

### Heroes (45)

Enum order is the table order. Harry, Hermione and Ron come first for the skeleton.

**The trio (3)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Harry Clawder | round glasses, lightning scar, messy black hair, Gryffindor scarf | Expelliarmus (steady ray, red) | casts his silver stag Patronus | "Expelliarmus!" |
| 2 | Hermione Clawnger | bushy brown hair, an armful of books | wand (energy, electric blue) | spins the gold Time-Turner | "It's Levi-O-sa!" |
| 3 | Ron Weasley | red hair, freckles, maroon jumper with an R, Spellotaped wand | backfiring slug curse (thrown, green) | his wand sputters and he burps up a slug | "Bloody hell!" |

**Students (10)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 4 | Neville Longbottom | round face, cardigan, a Mimbulus plant | Sword of Gryffindor (saber) | pulls the sword out of the Sorting Hat | "Why is it always me?" |
| 5 | Luna Lovegood | straggly blonde hair, radish earrings | wand (energy, pale blue) | her lion-head hat roars | "Nargles." |
| 6 | Ginny Weasley | long red hair, Quidditch robes | Bat-Bogey Hex (thrown, little black bats) | none | none |
| 7 | Fred Weasley | red hair, jumper with an F | Whiz-bangs (fire) | lights a firework that bursts into a dragon | "Gred." |
| 8 | George Weasley | red hair, jumper with a G, an Extendable Ear | wand (energy, pink and gold) | dangles an Extendable Ear | "Forge." |
| 9 | Cedric Diggory | Hufflepuff yellow and black, Triwizard shirt | wand (energy, yellow) | lifts the glowing blue Triwizard Cup | none |
| 10 | Cho Chang | black hair, Ravenclaw blue scarf | wand (energy, silver-blue) | none | none |
| 11 | Seamus Finnigan | sandy hair, Gryffindor tie | blasting (fire) | his spell blows up in his face: soot and smoking hair | "Boom." |
| 12 | Colin Creevey | mousy hair, a big camera | none | takes a photo with a big flash | none |
| 13 | Oliver Wood | scarlet Quidditch robes and pads | Quaffle (thrown, red-brown) | spins the Quaffle on one finger | none |

**The Weasley grown-ups (4)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 14 | Molly Weasley | red curls, apron, knitted cardigan | wand (energy, hot red) | knitting needles knit a jumper on their own | "Not my daughter!" |
| 15 | Arthur Weasley | thinning red hair, Ministry robes | wand (energy, sky blue) | holds up a rubber duck, fascinated | none |
| 16 | Bill Weasley | long red ponytail, fang earring, scarred cheek, dragon-hide boots | wand (energy, orange) | none | none |
| 17 | Percy Weasley | horn-rimmed glasses, Head Boy badge | wand (energy, crimson) | polishes his badge | none |

**Hogwarts staff (10)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 18 | Dumbledore | purple and silver robes, half-moon glasses, long white beard | wand (steady ray, gold, `thick`) | clicks the Deluminator, and little lights fly into it | "Sherbet lemon?" |
| 19 | McGonagall | green tartan robes, pointed hat, tight bun, square glasses | Transfiguration (`spell`, gold) | turns into a tabby cat with spectacle markings, and back | "Ten points to Gryffindor!" |
| 20 | Snape | black robes, lank black hair, hooked nose | Legilimency (`rings`, grey-violet) | his cloak sweeps round, and a silver doe runs past | "Always." |
| 21 | Hagrid | huge (`bulk`), wild beard, moleskin coat | crossbow (arrow) | his pink umbrella sparks | "Yer a wizard!" |
| 22 | Flitwick | tiny, on a stack of books, white moustache | Charms (`spell`, blue); a former duelling champion | swish and flick, and a feather floats up | "Swish and flick!" |
| 23 | Sprout | patched hat, earthy robes, earmuffs | Mandrakes (thrown), as in the Battle of Hogwarts | pulls a screaming Mandrake from its pot | none |
| 24 | Slughorn | walrus moustache, plum velvet waistcoat | wand (energy, amber) | turns into an armchair, and back (re-check it reads at the audit) | none |
| 25 | Trelawney | enormous glasses, shawls, bangles | crystal balls (thrown), as in the book's battle | peers into a crystal ball, mist swirls, her eyes go wide | "The Grim!" |
| 26 | Lupin | shabby patched brown suit, faint scars | wand (energy, blue-white) | offers a bar of chocolate | "Chocolate?" |
| 27 | Madam Hooch | spiky grey hair, yellow hawk eyes, broom (`fly`) | none | blows her whistle | "Up!" |

**The Order of the Phoenix (5)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 28 | Sirius Black | long dark wavy hair, velvet coat | wand (energy, scarlet) | turns into Padfoot, a big black dog, and back | none |
| 29 | Mad-Eye Moody | blue magical eye, wooden leg, staff, scars | wand (beam, blue) | the magical eye spins round | "Constant vigilance!" |
| 30 | Tonks | spiky bubblegum-pink hair, punk jacket | wand (energy, pink) | her hair goes pink, blue, purple and back | "Wotcher!" |
| 31 | Kingsley | tall, purple and blue robes, small cap, gold earring | wand (beam, gold) | none | none |
| 32 | Aberforth | grubby beard, barman's apron | wand (energy, teal) | a silver goat Patronus trots past | none |

**Other schools (2)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 33 | Fleur Delacour | silvery-blonde hair, Beauxbatons blue silk and hat | wand (energy, powder blue) | tosses her hair, and it shimmers | none |
| 34 | Viktor Krum | shaved head, heavy brows, red Durmstrang fur cloak | wand (energy, dark red) | a Wronski Feint: hops up on his broom and dives | none |

**Allies and creatures (9)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 35 | Dobby | house-elf, pillowcase toga, big green eyes, bat ears | elf magic (`waves`, pale blue) | holds up the sock | "Dobby is free!" |
| 36 | Kreacher | old elf, loincloth, white ear tufts, Slytherin locket | cleaver (saber), leading the elves in the battle | clutches the locket and mutters | none |
| 37 | Buckbeak | hippogriff: eagle head and wings on horse legs (`fly`, `bulk`) | talons (saber) | bows | none |
| 38 | Firenze | centaur, palomino, blue eyes (`bulk`) | bow (arrow) | points up, and a red star glows | none |
| 39 | Grawp | Hagrid's giant half-brother, ragged (`bulk`) | fists (saber) | none | "Hagger!" |
| 40 | Fawkes | crimson and gold phoenix (`fly`) | talons (saber) | bursts into flame and is reborn as a chick | none |
| 41 | Nearly Headless Nick | ghost, ruff, Tudor doublet (`hover`, `canSit: false`) | none | tips his head off on its flap of skin, cartoonishly | "Nearly Headless!" |
| 42 | Moaning Myrtle | ghost girl, pigtails, round glasses (`hover`, `canSit: false`) | none | bursts into tears and dives with a splash | none |
| 43 | Ollivander | wild white hair, pale eyes, a tape measure | wand sparks (`spell`, silver) | a wand box flies open, and the wand sprays sparks | "Curious." |

**Agent-only, and HEM**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 44 | Hedwig (agent-only) | snowy owl (`fly`) | none | drops a letter |
| 45 | HEM | Hogwarts robes, a yellow and black Hufflepuff scarf, a pointed hat | wand (energy, yellow) | sweeps up on a broom and back |

HEM wears Hufflepuff so he never reads as Harry.

### Villains (40)

Clawdemort comes first for the skeleton.

**Clawdemort and the Death Eaters (12)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Lord Clawdemort | chalk-white, no nose, snake slits, black robes | wand (steady ray, green, `thick`) | the Dark Mark rises above him in green smoke and fades | "Harry Clawder…" |
| 2 | Bellatrix Lestrange | wild black curls, black corset dress, crooked wand | wand (energy, purple) | cackles and twirls her wand | "Hee hee hee!" |
| 3 | Lucius Malfoy | long platinum hair, black furs, snake-head cane | wand (energy, green) | draws the wand out of the snake-head cane | none |
| 4 | Narcissa Malfoy | two-tone hair, half black and half blonde, elegant | wand (energy, silver) | none | none |
| 5 | Wormtail | balding, ratty, a silver hand | wand (energy, sickly yellow-green) | turns into a rat, scurries, and comes back | none |
| 6 | Barty Crouch Jr | wild brown hair, Azkaban stripes | wand (energy, red) | swigs Polyjuice from a hip flask and grimaces | none |
| 7 | Fenrir Greyback | wolfish, shaggy grey hair, claws | claws (saber) | howls | none |
| 8 | Dolohov | long face, silver Death Eater mask | curse (beam, purple flame) | puts on the silver mask | none |
| 9 | Macnair | the executioner, hooded, with an axe | axe (saber) | spins the axe | none |
| 10 | Quirrell | purple turban, nervous | wand (energy, violet) | unwinds the turban partway, a face glimpses, and he rewinds it | "T-t-troll in the dungeon!" |
| 11 | Tom Riddle | sixteen, neat dark hair, Slytherin tie, the diary, lit pale | life drain (`touch`, pale green) | the diary's pages flip, and he flickers | none |
| 12 | Grindelwald (young) | blond curls, a 19th-century coat, the Elder Wand | Elder Wand (forked lightning, blue-white) | laughs and leaps backwards out of a window frame | none |

**Slytherins (4)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 13 | Draco Malclaw | slicked white-blond hair, Slytherin robes, a sneer | Serpensortia (thrown, a little black snake) | turns into a bouncing ferret, and back | "My father will hear about this!" |
| 14 | Crabbe | big (`bulk`), Slytherin | Fiendfyre (fire) | none | none |
| 15 | Goyle | big (`bulk`), Slytherin | fists (saber) | gobbles a cupcake | none |
| 16 | Pansy Parkinson | black bob, pug nose | wand (energy, emerald) | points | "Get him!" |

**The Ministry and the press (3)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 17 | Umbridge | pink cardigan, a bow, a kitten plate | wand (beam, pink) | coughs "hem hem", and a kitten plate mews | "Hem, hem." |
| 18 | Fudge | lime bowler hat, pinstripes | none | twiddles his bowler hat | "He is NOT back!" |
| 19 | Rita Skeeter | blonde curls, jewelled glasses, acid-green suit, Quick-Quotes Quill | none | turns into a beetle, and back | none |

**Troublemakers (9)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 20 | Gilderoy Lockhart | golden waves, lilac robes, gleaming smile | wand (energy, lilac), which misfires | winks and signs a photo of himself | "Obliviate!" |
| 21 | Peeves | poltergeist, belled hat, bow tie (`hover`, `canSit: false`) | water balloons (thrown, blue) | blows a raspberry and cartwheels | none |
| 22 | Filch | ragged, a lantern and keys | none | Mrs Norris winds round his legs, and he lifts the lantern | "Students out of bed!" |
| 23 | Uncle Vernon | huge (`bulk`), moustache, purple face | shotgun (bullet) | owl letters fly at him, and he flails | "There's no such thing as magic!" |
| 24 | Aunt Petunia | long neck, prim twinset | frying pan (saber) | cranes her neck over the hedge | none |
| 25 | Dudley | huge, blond, a toddler's tantrum | fists (saber) | a curly pig's tail sprouts | "Mum!" |
| 26 | Aunt Marge | tweed, with Ripper the bulldog | none | swells like a balloon, floats up and goes down again (kept inside the frame) | none |
| 27 | Griphook | goblin, Gringotts uniform | Sword of Gryffindor (saber), the one he takes | counts gold coins | none |
| 28 | Boggart | Snape in Neville's grandmother's clothes: vulture hat, green dress, red handbag | none | "Riddikulus!": a twirl into the outfit | none |

**Monsters (8)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 29 | Basilisk | great green serpent, yellow eyes (`bulk`, `armoured`); homebound in the Chamber | fangs (saber) | its eyes glow | none |
| 30 | Aragog | giant grey spider (`bulk`) | pincers (saber) | clicks his pincers | none |
| 31 | Dementor | hooded rags (`hover`, `canSit: false`) | the Kiss (`touch`, grey-blue), drawn eerie | frost spreads at its feet | none |
| 32 | Mountain troll | grey, a club (`bulk`) | club (saber) | swings the club and scratches its head | none |
| 33 | Fluffy | three-headed dog (`bulk`) | bites (saber) | falls asleep when a harp plays | none |
| 34 | Hungarian Horntail | black dragon, spiked tail (`fly`, `bulk`, `armoured`) | fire | curls round the golden egg | none |
| 35 | Nagini | huge snake | bite (saber) | coils and rises | none |
| 36 | Inferius | pale and drowned, grey-blue, eerie | grab (saber) | rises from black water and sinks | none |

**Agent-only small fry (4)**

| # | Name | Look | Weapon |
|---|---|---|---|
| 37 | Cornish pixie | electric blue, flapping (`fly`) | none |
| 38 | Blast-Ended Skrewt | armoured, sparking from its tail | fire |
| 39 | Howler | a red envelope with a paper mouth (`hover`) | none |
| 40 | Chocolate Frog | hops | none |

Rows are 1-based throughout this plan; the enum and the ids are 0-based. So the small fry are villains 36 to 39 (`agentOnly` lists `base + 36…39`), Hedwig is hero 43, Clawdemort and Riddle are villains 0 and 10, and the Basilisk is villain 28.

**villainCount is 40.** The gate 2 summary said 41; Mrs Norris was folded into Filch's signature and the count wasn't redone then.

### Telling them apart

- **Clawdemort and Tom Riddle** are the same person: `Universe.guises`, never on screen together. Riddle is a pale-lit sixteen-year-old with neat hair and the diary; Clawdemort is chalk-white and noseless.
- **Harry and Tom Riddle** are both dark-haired boys: Harry has round glasses, the scar and Gryffindor red; Riddle has no glasses and a Slytherin green tie.
- **Fred and George**: F and G on their jumpers, and different props (Whiz-bang, Extendable Ear).
- **The red-haired Weasleys** (Ron, Ginny, Fred, George, Molly, Arthur, Bill, Percy): told apart by jumper letters, Quidditch robes, apron, Ministry robes, ponytail and glasses.
- **Snape and the Boggart**: the Boggart wears the vulture hat, green dress and red handbag.
- **Moody and Barty Crouch Jr**: Moody has the blue eye, wooden leg and staff; Barty has wild hair and Azkaban stripes. Both have a hip flask, but only Barty's signature uses it.
- **Dumbledore and Gandclawd**, **Dobby and Gollum**: see Tone.

### Nemeses (19)

| Hero | Villain | Why |
|---|---|---|
| Harry | Clawdemort | the whole story |
| Hermione | Draco | she punches him, third year |
| Ron | Aragog | spiders |
| Neville | Nagini | he kills the snake |
| Ginny | Tom Riddle | the diary, second year |
| Luna | Rita Skeeter | the Quibbler against the Prophet |
| Fred | Filch | a rivalry since their first year |
| Molly | Bellatrix | "Not my daughter!" |
| Dumbledore | Grindelwald | their duel |
| McGonagall | Umbridge | fifth year |
| Snape | Lockhart | the Duelling Club |
| Hagrid | Uncle Vernon | the hut on the rock |
| Sirius | Wormtail | the betrayal |
| Lupin | Greyback | werewolves on both sides |
| Moody | Barty Crouch Jr | the impostor |
| Kingsley | Dolohov | the Department of Mysteries |
| Buckbeak | Macnair | the executioner |
| Fawkes | the Basilisk | the Chamber |
| Dobby | Lucius | the sock |

**Claude's side:** heroes. **Rivals:** none (Clawdemort and Riddle are guises instead).

### Left out of the cast

- **Lily and James:** they'd read as Ginny and Harry.
- **Too thin to carry a sprite:** Dean Thomas, Lavender Brown, Lee Jordan, Charlie Weasley, Yaxley, Scabior, the Carrows, Marcus Flint, Madam Pomfrey.
- **Mrs Norris:** part of Filch's signature instead.
- **Everything from Fantastic Beasts, Cursed Child and the games:** out of scope.

## Places (22)

| # | Key | Place | Still | Moving | Tall (screen saver) |
|---|---|---|---|---|---|
| 1 | `wandGreatHall` | **Great Hall** (default) | long house tables, banners, the staff table | floating candles flicker, clouds drift across the enchanted ceiling | the starry ceiling and its candles |
| 2 | `wandPlatform` | Platform Nine and Three-Quarters | the red steam engine, trunks, an owl cage | steam billows | the station's iron roof and clock |
| 3 | `wandGryffindor` | Gryffindor common room | red armchairs, fireplace, the Fat Lady's portrait | the fire crackles | tower windows and banners |
| 4 | `wandSlytherin` | Slytherin common room | green lamps, stone, windows under the lake | aquamarine water ripples; the giant squid's tentacle slides past | the lake rising above |
| 5 | `wandPotions` | Potions dungeon | cauldrons, jars on shelves | cauldrons bubble and puff | vaulted stone, more jars |
| 6 | `wandStaircase` | Grand Staircase | landings and portraits | a staircase swings round | staircases climbing out of sight |
| 7 | `wandHeadmaster` | Headmaster's office | Fawkes's perch, the Sorting Hat, the Pensieve, silver instruments | instruments whirr, the Pensieve glows | the gallery of old headmasters' portraits |
| 8 | `wandHagrid` | Hagrid's hut | pumpkin patch, the forest edge, daylight | chimney smoke | the castle on the hill behind |
| 9 | `wandForest` | Forbidden Forest | night, mist, cobwebs | glowing eyes blink, mist drifts | towering trunks |
| 10 | `wandPitch` | Quidditch pitch | the hoops, the house towers, blue sky | tiny players zip overhead | the stands and sky |
| 11 | `wandChamber` | Chamber of Secrets | serpent pillars, water, Slytherin's stone face | water drips and ripples | the great statue face |
| 12 | `wandShack` | Shrieking Shack | broken bed, boarded windows, dust | a loose board creaks, dust motes drift | the sagging roof |
| 13 | `wandHogsmeade` | Hogsmeade | snowy day: Honeydukes' bright window, the Three Broomsticks | snow falls | snowy rooftops, the castle far off |
| 14 | `wandDiagon` | Diagon Alley | crooked shops: Ollivanders, the Wheezes, Flourish and Blotts | owls flutter, a shop sign swings | leaning shopfronts, Gringotts at the top |
| 15 | `wandGringotts` | Gringotts | white marble hall, goblins at high desks | chandeliers glint, scales tip | the marble pillars |
| 16 | `wandPrivet` | Privet Drive | identical houses, a neat hedge | letters fly out of the fireplace and the letterbox | the street receding |
| 17 | `wandBurrow` | The Burrow | the crooked stacked house, the Ford Anglia, gnomes | the family clock's hands turn, a gnome scurries | the house leaning ever higher |
| 18 | `wandGrimmauld` | Grimmauld Place | dark hall, the family tapestry, a curtained portrait | gaslight flickers | the narrow stairwell |
| 19 | `wandMinistry` | Ministry Atrium | green-tiled walls, the golden fountain | green Floo flames, memo planes flutter | the dark ceiling and the floors above |
| 20 | `wandManor` | Malfoy Manor | long dining table, chandelier, white peacocks outside | candle smoke curls | the high dark windows |
| 21 | `wandGodrics` | Godric's Hollow | snowy night, the church, the war memorial | snow falls, church windows glow | the steeple |
| 22 | `wandCave` | The cave | black lake, the island, the green basin's glow | the water's surface ripples (no bodies until an Inferius rises) | the cave roof dripping |

**Kept apart:** Hogsmeade (bright snowy day, sweet-shop colours) and Godric's Hollow (blue snowy night); the Chamber (grey-green stone) and the Slytherin common room (lake aquamarine). None of the 22 keys clashes with an existing `Location("…")` on `main` or `buffy`.

**Left out:** the Astronomy Tower (too sad), the Room of Requirement (overlaps the common room and the Great Hall), Azkaban (grim, and the Dementor has the train), the Little Hangleton graveyard (its big moment is cut for tone).

### Homes

| Place | Heroes | Villains |
|---|---|---|
| Great Hall | McGonagall, Flitwick, Cedric, Cho, Fleur, Nearly Headless Nick, Hedwig, HEM | Quirrell, Howler |
| Platform 9¾ | Luna, Percy | Dementor, Chocolate Frog |
| Gryffindor common room | Harry, Hermione, Ron, Neville, Seamus, Colin | |
| Slytherin common room | | Draco, Crabbe, Goyle, Pansy |
| Potions dungeon | Snape, Slughorn | Boggart |
| Grand Staircase | Trelawney | Filch, Peeves, Fluffy, the troll, Cornish pixie |
| Headmaster's office | Dumbledore, Fawkes | |
| Hagrid's hut | Hagrid, Sprout, Buckbeak | Macnair, Blast-Ended Skrewt |
| Forbidden Forest | Firenze, Grawp | Aragog, Greyback |
| Quidditch pitch | Ginny, Oliver Wood, Madam Hooch, Krum | Horntail |
| Chamber of Secrets | Moaning Myrtle | Tom Riddle, the Basilisk (homebound) |
| Shrieking Shack | Lupin | Wormtail |
| Hogsmeade | Aberforth | Rita Skeeter |
| Diagon Alley | Fred, George, Ollivander | Lockhart |
| Gringotts | Bill | Griphook |
| Privet Drive | Dobby | Vernon, Petunia, Dudley, Marge |
| The Burrow | Molly, Arthur | |
| Grimmauld Place | Sirius, Moody, Tonks, Kingsley, Kreacher | |
| Ministry Atrium | | Umbridge, Fudge, Dolohov, Barty Crouch Jr |
| Malfoy Manor | | Clawdemort, Bellatrix, Lucius, Narcissa |
| Godric's Hollow | | Grindelwald, Nagini |
| The cave | | Inferius |

## Mechanics that make it its own universe

1. **The ride: the Knight Bus** (`Ride.knightBus`, in `Ride.drives`). A purple triple-decker bangs into the scene, lurches to a stop and squeezes everyone aboard, then bangs away. It picks up the heroes, except HEM, the creatures (Buckbeak, Firenze, Grawp, Fawkes, Hedwig) and the ghosts. **When it's a Weasley** (Ron, Ginny, Fred, George, Molly, Arthur, Bill, Percy), the flying **Ford Anglia** (`Ride.fordAnglia`) swoops in over the rooftops instead. Villains leave on foot. The theme's `ride: (Cast) -> Ride?` closure makes the choice, as `FilesRoster.swift:134` does.
2. **Compaction mechanic: the Pensieve** (`WandPensieve.swift`). For **Dumbledore, Snape, Harry and Slughorn**. When their session compacts, they raise the wand to their temple and draw out a silver thread of memory; a stone basin floats up beside them, the thread drops in and swirls, and the basin sinks away. Same session, same face, a lighter head. **Slughorn's** thread comes out foggy and patchy: the tampered memory. Losing context and setting memories aside fits compaction exactly. It reuses the missing-time clock (`SessionRecord.abducted`) as Clawdberg's `OutaTime` does: the four go in `Universe.abductees`, and the effect is chosen where the overlay picks `OutaTime` (`Overlay.swift:1271`).
3. **Habits** (`Habits.swift`, Overlay's tick):
   - **Peeves's ammunition:** while Peeves is on stage, now and then a water balloon drops on someone in the crew, and they shake themselves off.
   - **The twins' Whiz-bang:** while Fred or George is on stage, now and then a firework dragon zooms across above the crew and pops.
   - **The Dementor's chill:** while the Dementor is on stage, the crew nearest it show frosty breath. If Harry, Lupin or Snape is there too, they cast their Patronus at it and it drifts back.
4. **Bespoke drills** (`Drills.swift`): the students practise Wingardium Leviosa, a feather rising and falling (Seamus's explodes); Snape and Slughorn tend a little cauldron that puffs coloured smoke; the Quidditch players (Ginny, Wood, Krum, Hooch) toss and catch a Quaffle. **No meditation:** nobody floats cross-legged.

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one. A `CHANGELOG.md` entry each phase.

1. **Skeleton:**
   - settle the raw value first (see Context);
   - the universe case and all the wiring above;
   - Harry, Hermione and Ron, and Clawdemort (the enums' first cases);
   - the Great Hall, the menu icon, HEM's costume, Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with plain wipes (`case .starWars, .wizards: return nil` in `ComicTransition.pick`).
2. **Core ensemble.** About 35 characters:
   - the students, the Weasleys, Dumbledore, McGonagall, Snape, Hagrid, Sirius, Lupin, Moody, Dobby;
   - Bellatrix, Lucius, Wormtail, Draco, Crabbe, Goyle, Umbridge, Quirrell, Tom Riddle, Lockhart;
   - 8 places: the Great Hall, Gryffindor common room, Slytherin common room, Potions dungeon, Headmaster's office, Hagrid's hut, the Burrow, Malfoy Manor; with homes and nemeses for these.

   The enum cases can go in first as stand-ins and be drawn in a second commit, as The Clawd Files did.
3. **The rest:** all 85 characters and all 22 places, every home filled in, the guises pair and the homebound Basilisk. Ends with **the character audit**: every weapon, shot, magic family and colour, motion, signature and callout checked against the books and films and against this plan, a mismatches table for your OK. Re-check: **that every spell type in the Cast table is really used and no two in one group share a colour**; Slughorn's armchair reading at 72×52; Aunt Marge's swell staying in the frame.
4. **Mechanics:** the Knight Bus and the Ford Anglia, the Pensieve, the three habits, the bespoke drills.
5. **Transitions:** the twelve `WandTrip`s, through `ComicTransition`.
6. **Polish pass** (always before docs): every weak spot noted in phases 2 to 5, split by file and fixed in parallel, with before-and-after renders for your OK.
7. **Docs and release:**
   - README (the universe's own section under "The universes" with its collapsible cast-and-places pictures, the screen-saver paragraph, developer notes), `llms.txt` (universe list, folder and prefix, the Pensieve);
   - `Tools/RenderDocs`: a `wandLineup` desktop strip, `roster-harry-clawder.png`, the locations sheet and a social preview; `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - the trailer, `REEL=wand`;
   - flip `isReleased` if it was built on `main`;
   - the version: a new universe raises the middle number (the next `3.N.0`);
   - **needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

**Weak spots to expect** (note them as they come up, fix them in the polish pass): eight red-haired Weasleys blurring together; wands too thin to see at agent size; Hedwig and Fawkes too alike in flight; the ghosts' pearly silver against pale places (the Great Hall's candlelight, Gringotts' marble); the monsters' tails, wings and necks against the frame rule (the Basilisk, the Horntail, Fluffy's three heads); the Dementor's rags (see-through edges must be solid or faint, never half-opaque); the Chamber and the cave too dark for outlines; the Marauder's Map's ink lettering and the Daily Prophet's headline too small at window size.

## Verification

- **Build:** `./build.sh`. The cast-size `precondition` in `Overlay.swift:180` catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` for slow type-checks before calling a phase done.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Harry Clawder"`;
  - `build/preview fight out.png "Harry Clawder" "Lord Clawdemort"`: the red and green steady rays should lock;
  - `build/preview fight out.png "Dumbledore" "Grindelwald"`: the thick gold ray against forked lightning;
  - `build/preview place out.png "Harry Clawder"`;
  - `build/preview edges out.txt "Harry Clawder"`: everything it lists must be on purpose (shots, thrown slugs, bats, Mandrakes and crystal balls, Fred's fireworks, Krum's dive, Fawkes's flames, Aunt Marge's float);
  - and the batch sheets, one per Art file. Look at the PNGs before showing them.
- **Guises and homebound:** Clawdemort and Riddle are never on screen together; the Basilisk only appears in the Chamber and is recast anywhere else, including the desktop.
- **Pull request guard:** `python3 scripts/pr-guard.py main harry-potter` before any PR.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> wandGreatHall wandBurrow`.
- **In the app:**
  - Settings → Universe → Harry Clawder: sessions are heroes, subagents include villains, Hedwig and the small fry;
  - the screen saver's Options list it;
  - Random and Clawd Royale reach it.
- **The Pensieve:** `/compact` in a session led by Dumbledore or Harry, and once with Slughorn for the foggy memory.

## Transitions (`WandTrip`, 12)

| # | Name | What happens | Comes up more with |
|---|---|---|---|
| 1 | **The Opening** (signature, longest and rarest) | Storm clouds roll, an owl flies through them, and a gilded title rises out of the mist and swells. The camera pushes through the clouds into the new place. | rare for anyone · turf: Great Hall |
| 2 | **Floo Powder** | Green flames roar up and swallow the scene; the new place appears through a fireplace's flames as they die down. | the Weasleys · turf: the Burrow, Ministry Atrium, Grimmauld Place |
| 3 | **Apparition** | A sharp crack: the old scene twists and squeezes to a point, and the new one untwists. | Dumbledore, the Order, Dobby |
| 4 | **Death Eater Smoke** | Streaks of black smoke tear across and swirl, and clear on the new place. | **needs a Death Eater present** (`needsOwner`) · turf: Malfoy Manor |
| 5 | **Portkey** | An old boot glows blue, the scene spins round it in a whirl, and everything drops into the new place. | Cedric, Arthur · turf: Godric's Hollow |
| 6 | **Time-Turner** | The gold hourglass spins; the old scene blurs, runs backwards and settles as the new one. | Hermione |
| 7 | **The Marauder's Map** | Parchment unfolds over the screen, ink footprints walk across it to the new place's label, and the map folds away. | Harry, Fred, George, Lupin, Sirius, Wormtail · turf: the Hogwarts places |
| 8 | **The Daily Prophet** | A newspaper spins in, as in the films; its moving front-page photo is the new place, and it grows to fill the screen. | Rita Skeeter, Fudge, Umbridge · turf: Ministry Atrium |
| 9 | **Patronus** | A silver stag gallops across and its light floods the screen white, fading on the new place. With Snape on screen it's his doe. | Harry, Snape, Lupin |
| 10 | **The Deluminator** | Click: the old scene's lights fly into the lighter and it goes dark. Click: they fly out and light the new place. | Dumbledore, Ron |
| 11 | **Howler** | A red envelope shakes, opens a paper mouth and shouts, then tears itself to shreds that blow away off the new place. | Molly · turf: Great Hall |
| 12 | **Dementor Frost** | Frost creeps in from the edges and the colours drain; silver light cracks it open on the new place. | **needs the Dementor present** (`needsOwner`) |

**Finishing touch: none.** The Marauder's Map already labels the new place, and a caption on every trip would crowd it.

**Style:** pixel art in candle gold, Gryffindor scarlet, slate stone, Floo green, Patronus silver-blue and parchment, with a little grain on the Opening and the Prophet. Lettering big and blocky, never the films' logo or typeface. No fine detail that won't read at pixel scale.

**Left out:**
- The Pensieve dive: it's the compaction mechanic.
- The moving staircase: it's the Grand Staircase's moving layer.
- The flood of letters at Privet Drive: overlaps the Howler, and it's Vernon's signature.
- The Sorting Hat: too static.
- The Knight Bus: it's the ride.

## Promo: the trailer (`REEL=wand`)

Built on `doctorShots`, about 45 to 50 seconds, rendered with the app's own sprites, places and transitions. Storyboard first, for your OK.

- **Intro (~9 s): The Opening.** Dark storm clouds, thunder. An owl beats through the gloom; a gilded title, **HARRY CLAWDER** in our own lettering, rises out of the mist and swells, and the camera plunges through the clouds into the Great Hall's candles. Sound: a celesta-like lilt with low strings, our own notes.
- **Set piece (~9.5 s): the Battle of Hogwarts.** Night, the castle's shield dome shimmering. Death Eater smoke streaks in and cracks against it; Molly faces Bellatrix; Neville draws the sword from the Sorting Hat; Harry's red ray locks with Clawdemort's green. Caption: "Not my daughter!"
- **Hook (4 s):** shared.
- **Desktop (~4.6 s):** `brawl(ctx, .wizards, …)`: "Mischief managed."
- **Status (~4.2 s):** four characters, one per state; the aside: "Constant vigilance!"
- **Agents (4 s):** "Every subagent gets a Hogwarts letter."
- **Window (~4.8 s):** `windowShot(ctx, .wizards, …, at: .wandGreatHall)`: "It's bigger on the inside. No, wait, that's a tent."
- **AIs (~4.4 s):** the BRING YOUR OWN AI* line-up, one character per AI.
- **End card (~4.2 s):** the Great Hall, the crew lined up, the title lands in gold, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS", the app icon and the GitHub URL.

No logo or melody is copied: the title is our own lettering, and the music only evokes the sound (celesta, strings, brass swells).

## Decisions (2026-10-18)

All four gates are passed:
- **Scope:** the seven books and eight films only.
- **Name: Harry Clawder.** Puns: Clawder, Clawnger, Clawdemort, Malclaw; everyone else by name.
- **Code naming:** `case wizards`, prefix `Wand`, folder `HarryClawder/`, branch `harry-potter`, `REEL=wand`.
- **Raw value:** settled at build time, after checking `main`, the open branches, the forks and the other plans.
- **Roster:** approved as drafted: 45 heroes (with HEM and the agent-only Hedwig), 40 villains (with four agent-only small fry), 85 in all. Clawdemort and Riddle are guises; the Basilisk is homebound.
- **Spell variety:** your request at the roster gate. Every spell type the engine has is used (steady ray, forked lightning, `spell`, `rings`, `waves`, `touch`, beam, thrown, fire, energy bolts), each character with a colour of their own.
- **Places and homes:** the 22 approved.
- **Mechanics:** the Knight Bus (the Ford Anglia for the Weasleys), the Pensieve, the Peeves, Whiz-bang and Dementor's-chill habits, the drills, no meditation.
- **Transitions:** the twelve above, opening with the Opening, no finishing touch.

The plan is ready for phase 1 when you say start.
