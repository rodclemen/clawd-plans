# Plan: a new universe, Game of Clawds (Game of Thrones parody)
<!-- track: repo=rodclemen/clawd-clash branch=game_of_thrones folder=GameOfClawds title="Game of Clawds" cast=99 places=20 -->

## Context

Clawd Clash has seven universes on `main` (d270b63, 2026-10-17). This plan adds a Game of Thrones parody, the HBO series (eight seasons), as a full ensemble, built the same way as Doctor Clawd and The Clawd Files. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

| Universe                   | Heroes | Villains | Total | Places | Transitions |
|----------------------------|--------|----------|-------|--------|-------------|
| Star Clawds                |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds           |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds           |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd               |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files            |     36 |       46 |    82 |     20 |          11 |
| Stevie Clawdberg           |     64 |       54 |   118 |     23 |          10 |
| Clawd of the Rings         |     38 |       38 |    76 |     22 |           9 |
| **Game of Clawds (proposed)** | **63** | **36** | **99** | **20** | **12** |

(heroCount includes HEM and two agent-only pets; villainCount includes one agent-only creature.)

- **Viability: comfortably viable.** 63 heroes and 36 villains, both well over the 20 threshold, with no padding. The show's real problem isn't numbers, it's that nobody is cleanly good or bad. How the cast is split is set out below.
- **Name: Game of Clawds** (chosen on 2026-10-16). The alternatives were *A Song of Ice and Clawd* and *Clawds of Westeros*.
- **Code naming** avoids the franchise name, as the other universes do:
  - `case thrones` with key `"thrones"`.
  - Folder `Sources/App/Universes/GameOfClawds/`, file prefix `Thrones…` (`ThronesRoster.swift`, `ThronesHeroes1.swift`, `ThronesWipes.swift` …). Nothing in the repo uses `Thrones` today.
  - Branch `game_of_thrones`.
- **Raw value:** the next free one when its build starts, checked against main and the open branches (main ends at `middleEarth = 6`, and the `buffy` branch still has `slayer = 6`); ids are rawValue*1000 and permanent.
- **Naming style:** light puns on the on-screen names, one per house so families read together: the Starks are **Stork**, the Lannisters **Lannclaw**, the Targaryens **Clawgaryen**, the Mormonts **Clawmont**, the Greyjoys **Greyjaw**, the Tyrells **Tyrose**, the Cleganes **Clawgane**. Where a pun would be forced, a near-spelling (Gendree, Syrio Foral). Actors' names are never used.
- **Scope:** the HBO series only. House of the Dragon is an option (see Open questions); it can be appended later without touching any ids.
- **Size:** 99 characters (Doctor Clawd's size) and 20 places.

### How the cast is split

The show is grey from top to bottom, so the split needs a rule rather than a feeling. The rule: **which side were they on when it counted?** Mostly that means the Long Night: who stood at Winterfell against the dead, or died redeemed on the way there. Where the Long Night doesn't decide it, the tiebreak is who the show asks us to root for.

- **Heroes:** the Starks and their direwolves, the North's loyalists, the Night's Watch, the free folk, Daenerys's court and dragons, the Brotherhood Without Banners, and the sympathetic rogues and turncloaks who come round.
- **Villains:** the Lannisters as the crown's antagonists (Cersei, Tywin, Joffrey, the Mountain, Qyburn, Pycelle) plus Littlefinger and the Faith, the rival kings and the Red Wedding's hosts (Stannis, the Greyjoy brothers Balon and Euron, Roose Bolton, Walder Frey), the Night's Watch mutineers and hostile wildlings, the Army of the Dead, the slavers and schemers of Essos, and Ellaria and the Sand Snakes.

**The grey ones, and where they land:**
- **Jaime → hero.** He spends three seasons as the face of the enemy, but his arc is the show's biggest turn: he loses his hand, saves Brienne, knights her, rides north alone and fights the dead at Winterfell. Fans remember the redemption.
- **Tyrion → hero.** Clearly the show's moral centre among the Lannisters, and Daenerys's Hand.
- **The Hound → hero.** Arya's reluctant guardian, the Brotherhood's ally, fights at Winterfell. Brutal, but the show is on his side by the end.
- **Theon → hero.** He betrays Robb, but his redemption is complete: he rescues Yara and dies defending Bran from the Night King. His torture by Ramsay is left out entirely; he is drawn as Theon the archer, not as Reek.
- **Bronn, Varys → heroes.** Sympathetic rogues: Bronn is Tyrion's friend and a sellsword with a grin; Varys says he serves the realm and is at Winterfell for the Long Night.
- **Melisandre → hero (debatable).** She lights the Dothraki arakhs and the trench in the Long Night, and she brought Jon back. Her worst act belongs to Stannis's story and is never referenced. See Open questions.
- **Stannis → villain.** He makes war on the realm, burns people for his god, and his story is framed as a tragic fall. He's a fair foe, not a monster.
- **Daenerys → hero, with a note.** She is the show's other lead for seven seasons and fights at Winterfell. The final season's turn ("The Bells") is never shown or referenced.
- **Jaqen → hero.** He saves Arya and teaches her; his menace is all charm.
- **Cersei → the lead villain.** She is the show's human antagonist to the very end, and refuses to help against the dead.

### Tone: what's left out, and why

The show has a lot of sexual violence, torture and gore. Clawd Clash is a desktop toy, so:
- **Left out entirely, because their whole point is torture, sexual violence or child harm:** Ramsay Bolton, Craster, Karl Tanner, Locke, the Tickler, Polliver, Rorge and Biter, Ser Meryn Trant, Styr and the Thenns (cannibals), Septa Unella (the walk of shame), Shae and Ros (their stories are sexualised), Tyene Sand (her one scene is a flashing gag).
- **Left out because their point is an execution:** Ser Ilyn Payne.
- **Kept, but tamed.** Nobody is shown dying, and the massacres (the Red Wedding, the Sept, King's Landing burning) are never referenced in moves, callouts or transitions:
  - the Mountain is a towering armoured brute, never skull-crushing;
  - Joffrey has his crossbow and his sulks, never his cruelty;
  - Walder Frey cackles and raises a goblet; that's all;
  - the dead are eerie (blue eyes, frost, shuffling), not rotting;
  - the Faceless Men's Hall of Faces is pale masks, never skin;
  - Lancel's seven-pointed star is a painted mark, not a carved wound;
  - Khal Drogo is the warrior with the braid and the bells, no more;
  - Roose's famous line is not used as his callout, and Jaime's "the things I do for love" (said before he pushes Bran) is not used either.
- **No sexualised names.** "Tart" was avoided for Brienne for this reason (she's Brienne of Tharth).

## How a universe plugs in (checked against the code on 2026-10-17, main d270b63)

**New code: `Sources/App/Universes/GameOfClawds/`**
- `ThronesRoster.swift`:
  - `enum ThronesHero` and `enum ThronesVillain`, append-only, with `hem` as the last hero.
  - The persona dictionaries, `.reduce([.hem: hemPersona(.thrones)])`.
  - `Location.thronesHome(of:)` for heroes and villains, `thronesNemeses`, the ride closure, `let thronesTheme = Theme(...)`.
  - The `static let` place keys and `let thronesPlaces` merged from the Places files.
- `Art/ThronesHeroes1…7.swift` and `Art/ThronesVillains1…4.swift`, 8–10 personas per file, in the pattern of `ClawdbergHeroes1.swift`. Shared helpers (fur cloaks, plate armour, the house sigils, dragon wings) go in one `ThronesKit.swift` with `thrones`-prefixed names.
- `Places/ThronesScenes1…3.swift` as `let thronesScenesN: [Location: Place]`.
- `ThronesIcon.swift`: the menu bar icon, 28×26, colour and mono. The Iron Throne's silhouette of swords, or a direwolf's head.
- `ThronesNoOne.swift`: the compaction mechanic (see Mechanics).
- `ThronesWipes.swift`: the transitions, last.

**Wiring into the existing code.** Copy what `clawdberg` did. Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎.
- **`Sources/Shared/Universe.swift`:**
  - `:8–40`: the case, `key`, `title`, `villainCount`, `heroCount`;
  - `:50–61`: `agentOnly` (Ser Pounce, the Lord Commander's raven, the crawling wight);
  - `:65`: `claudeSide` (default false: Claude plays the heroes);
  - `:68`: `rivals`, a one-liner today (`self == .starWars ? [0, 1] : []`), which has to take the Night Clawd and the White Stalker too (see Cast);
  - `:85–96`: `abductees`, which lists the Faceless (Arya, Jaqen, the Waif) the way Clawdberg lists its time travellers.
- **`Sources/App/Theme.swift:48`:** `Theme.of`.
- **`Sources/App/Locations.swift:72`:** `.merging(thronesPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift:3–6, 13, 15–24, 27–35, 40–63`:** `pick` lists every universe explicitly, so in phase 1 `.thrones` joins Star Clawds' line (`:42`, `case .starWars, .thrones: return nil`); in phase 5, a `.thrones(ThronesTrip)` case in the enum, `duration`, `draw` and `pick`, and the doc comment.
- **`Sources/App/Universes/Hem.swift:14, 62, 112, 123, 200`:** HEM's costume in every switch.
- **`Sources/App/Rides.swift`:** the rides (phase 4).
- ⚠︎ **`Sources/Saver/SaverView.swift:79–80`:** only the Options doc comment. The choices list (`:89`) and the trip pick (`:208`) build themselves from `Universe.offered`.
- ⚠︎ **`Sources/App/Drills.swift:54`:** the meditation guard. Game of Clawds doesn't meditate: nobody floats in the show (the Three-Eyed Raven sits in roots). **`:488`:** merge the bespoke drills.
- ⚠︎ **`Sources/App/Overlay.swift:868`:** the Playground prompts (five, below). Lines 1143 and 1271 show how `clawdberg` hooked in its set piece and its `OutaTime` effect; `ThronesNoOne` hooks in the same way. The habits hook into the tick here too (see Mechanics).
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`**: decide per universe-specific `if`. Game of Clawds joins none of the existing ones; it adds its own habits.
- ⚠︎ **Compaction:** `StatusStore.swift`'s PreCompact path already serves `abductees`; check it picks up `.thrones` without changes. `HookInstaller.swift` already registers the hook.
- **Clawd Royale** picks the cast and places up through `Universe.allCases`. Check the menu bar icon and arch-enemies still behave when a scene is in a Game of Clawds place.
- **Tools:**
  - `Tools/Preview/main.swift:63–120`: the batch names (`thronesHeroes1…`), the universe lookup, the enum lookups by case name.
  - `Tools/Transitions/main.swift:4–15, 129–133`.
  - Phase 6: `Tools/RenderPromo` (`REEL=thrones`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts** (`Overlay.swift:868`):
1. "Send a raven to Castle Black: the build is broken."
2. "Find out who poisoned the wine at the wedding feast."
3. "Count the dragonglass in the mines under Dragonstone."
4. "Refactor the line of succession so it compiles."
5. "Warm the dragon eggs and see if anything hatches."

## Cast

Each entry gives the parody name, look, weapon or motion, and signature move. How the engine's weapons map onto the show:
- **`.saber`** is the main weapon: this is a show of swords. Ice, Longclaw, Needle, Oathkeeper, Widow's Wail, Heartsbane, arakhs, axes, spears used up close, war hammers, whips. It deflects shots, which suits duellists like Syrio and Brienne.
- **`.blaster` + `.arrow`** for archers and crossbows: Ygritte, Theon, Bronn, Joffrey.
- **`.blaster` + `.thrown(colour)`** for things thrown: the Night King's ice spear, Obara's spear, Leaf's fire orbs.
- **`.lightning` + `Magic`** for the few true casters and for **dragonfire**. Dragonfire is a steady, wavering jet (`jagged: false`), each dragon its own colour. Magic is rare in the show, so it stays rare here.
- **`.none`** for the schemers and talkers: Varys, Cersei, Tywin, Sansa, Littlefinger's betters. Most of the show's power is talk.
- **`armoured: true`** for the unstoppable: the Mountain, the White Walkers and the Night King (steel shatters on them; only dragonglass and Valyrian steel bite, and dragonfire doesn't harm the Night King).
- **`bulk`** for the big bodies: the dragons, Wun Wun, the wight giant and wight bear, the Mountain, Hodor, Khal Drogo, Robert.
- **`motion: .fly`** for the dragons and the Lord Commander's raven. The dragons are drawn as young dragons that still fit the 72×52 canvas, wings half-folded on the ground and spread in flight, with `bulk` so duels stand back.
- Everyone, dragons and direwolves included, is Clawd in costume on Clawd's four legs, as in every universe. Bran is drawn as the climbing boy in his fur cloak, standing, not in his chair.

**Every caster looks different** (this universe and across the others):

| Caster | Look |
|---|---|
| Drawgon (Drogon) | steady jet, deep red glow, gold core, the thickest stream |
| Raygal (Rhaegal) | steady jet, orange-gold glow, pale yellow core, thinner, with a flicker |
| Viceserion (Viserion as a wight) | steady jet, ice-blue glow, white core: the only blue fire anywhere in the app |
| Melisandra | `spell` ribbon of red-and-gold embers twinkling, her ruby glowing as she casts |
| Pyat Three | `touch`: a blue-lipped fingertip and a violet glow round his target |
| Mirri Maz Dour | `waves`: ochre-and-maroon chant arcs pulsing out |
| Leif | `.thrown`, a small orange orb with a bright core (the Children's fire) |
| The Night Clawd | `.thrown`, a long pale-blue ice spear |

Checked against the other universes: Doctor Clawd's Ice Warrior is green and reptilian; Detective Clawds' Mr. Frost and Iceman throw ice streams, never a spear or blue flame; Marvelous Clawds' Fin Fang Fume is a green dragon in purple shorts with no wings, so Raygal keeps wings, a bronze belly and a horned western head.

### Heroes (63)

**House Stark (8)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Jon Snaw | black Night's Watch furs, dark curls, short beard | Longclaw (saber) | pulls his cloak round him and looks north; Ghost at his heel | "I don't want it." |
| 2 | Arya Stork | small, brown leather jerkin, hair tied back | Needle (saber) | flips her Valyrian dagger from one hand to the other and catches it | "Valar morghulis." |
| 3 | Ned Stork | grey furs, long brown hair, greatsword on his back | Ice, the greatsword (saber) | plants Ice point-down and rests both hands on the hilt | "Winter is coming." |
| 4 | Catelyn Stork | auburn hair, Tully blue-and-red dress | none | ties twigs into a little seven-pointed star (her prayer for Bran) | none |
| 5 | Robb Stork | crown of iron spikes, fur cloak | sword (saber) | raises his sword; "The King in the North!" | "The King in the North!" |
| 6 | Sansa Stork | auburn hair, dark grey northern gown | none | nibbles a lemon cake | "The North remembers." |
| 7 | Bran Stork | boy in a fur cloak, hood | none | eyes go milky white; a raven circles his head | "I'm the Three-Eyed Raven." |
| 8 | Benjen Stork | hooded Ranger, frost on his face | flaming flail (saber, a ball of fire on a chain) | swings the burning flail in a slow circle | none |

**The direwolves (4).** Four wolves are told apart by coat and by size: Ghost is the smallest and white; the others are grey, tawny and dark.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 9 | Ghost | white, red eyes | bite (saber) | silent: sits, ears up, never barks |
| 10 | Grey Wind | big, storm grey | bite (saber) | lunges with a growl |
| 11 | Summer | tawny grey-brown, lighter muzzle | bite (saber) | howls at the sky |
| 12 | Nymeria | dark grey, lean, a pack-leader's scruff | bite (saber) | lowers her head and stalks |

**The North (5)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 13 | Holdor | huge stable hand, wild beard, sheepskin | none, `bulk` | stands with his arms braced across a doorway | "Hodor!" |
| 14 | Maester Clawin | grey robe, maester's chain, brown beard | none | unrolls a scroll | none |
| 15 | Oshaw | wildling, ragged furs, tangled hair | spear (saber) | jabs the spear at nothing, warily | none |
| 16 | Meera Reid | green-brown cloak, net over her shoulder | spear (saber) | casts her net | none |
| 17 | Lyanna Clawmont | small girl, bear sigil, fierce frown | sword (saber) | folds her arms and glares | "I don't need permission." |

**The Night's Watch (5)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 18 | Samwell Tardly | round, black furs, a book under his arm | dragonglass dagger (saber, black) | opens a book; pages flutter | "I've read about this." |
| 19 | Jeor Clawmont | old Lord Commander, white beard, raven on his shoulder | sword (saber) | the raven hops up and squawks "Corn!" | none |
| 20 | Doleful Edd | lanky, black furs, long face | sword (saber) | a long sigh, shoulders drop | "Oh, good." |
| 21 | Maester Aemonn | very old, blind white eyes, black robe and chain | none | feels his way with a hand on a staff | none |
| 22 | Gillie | wildling girl, shawl, baby Sam in her arms | none | rocks the baby | none |

**The free folk and beyond the Wall (6)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 23 | Tormund Clawsbane | huge red beard, furs | axe (saber) | throws his head back and laughs | "Free folk!" |
| 24 | Ygrette | red hair, furs, bow | bow (`.blaster`, `.arrow`) | draws and looses an arrow at the sky | "You know nothing." |
| 25 | Mance Raider | grey furs, short dark beard | sword (saber) | raises a fist to the free folk | none |
| 26 | Won Won | giant, shaggy, a tree-trunk club | club (saber), `bulk` | lifts the club over his head and roars | none |
| 27 | Leif | Child of the Forest: small, bark-brown skin, leaves in her hair | fire orb (`.blaster`, `.thrown(orange)`) | a little orb of fire glows in her palm | none |
| 28 | The Three-Clawed Raven | old man in a weirwood throne of roots | none | roots creep up round him and settle | none |

**Daenerys's court (9)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 29 | Daenerys Clawgaryen | silver-white braids, blue gown or white winter coat | none | holds up a dragon egg that cracks and a hatchling peeks out | "Dracarys!" |
| 30 | Drawgon | black dragon, red wing membranes | dragonfire jet (`.lightning`), `.fly`, `bulk` | spreads his wings and roars | none |
| 31 | Raygal | green dragon, bronze belly and horns | dragonfire jet (`.lightning`), `.fly`, `bulk` | curls his neck and snorts smoke | none |
| 32 | Jorah Clawmont | weathered knight, leather and mail, bear sigil | Heartsbane (saber) | bows his head: "Khaleesi" | "Khaleesi." |
| 33 | Missandee | dark curls, gold-trimmed robe | none | speaks High Valyrian: a bubble of curly glyphs | none |
| 34 | Grey Wyrm | Unsullied leather, spiked helmet, shield | spear and shield (saber) | stamps his spear | "Unsullied!" |
| 35 | Barristan Selclaw | white-haired knight, white cloak | sword (saber) | a slow, perfect salute with the sword | none |
| 36 | Daario Nahairis | swaggering sellsword, long hair, blue coat | arakh (saber) | spins his stiletto and catches it | none |
| 37 | Khal Clawgo | long braid with bells, painted chest, arakh | arakh (saber), `bulk` | the bells on his braid jingle as he turns | none |

**The grey ones who came round (7)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 38 | Tyrion Lannclaw | short, golden hair, dark red doublet, Hand's pin | axe and shield (saber) | sips from a wine cup | "I drink and I know things." |
| 39 | Jaime Lannclaw | gold hair, gold hand, Lannister armour | Widow's Wail, left-handed (saber) | flexes the golden hand | "Kingslayer." |
| 40 | Sandor Clawgane | the Hound: dog's-head helm, burned cheek (one darker patch) | greatsword (saber) | tears a leg off a roast chicken | "Chicken." |
| 41 | Theon Greyjaw | dark hair, Ironborn leathers, kraken sigil | bow (`.blaster`, `.arrow`) | nocks an arrow; a gull cries | "What is dead may never die." |
| 42 | Yara Greyjaw | short dark hair, leather and salt | axe (saber) | leans on the axe with a grin | none |
| 43 | Brawn | sellsword, stubble, crossbow | crossbow (`.blaster`, `.arrow`) | flips a coin and pockets it | "That's what I do." |
| 44 | Varies | bald, silks, sleeves folded | none | a little bird flutters to his hand | "Little birds." |

**Knights, outlaws and the faithful (10)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 45 | Brienne of Tharth | very tall, short blonde hair, blue-tinted plate | Oathkeeper (saber) | taps her sword to her shoulders: knighted | "Ser Brienne." |
| 46 | Podrick Paine | young squire, mop of hair | sword (saber) | sings: little notes rise | none |
| 47 | Davos Seaclaw | grey beard, sailor's coat, glove with short fingers | none | whittles a little wooden stag | none |
| 48 | Gendree | blacksmith's apron, dark hair, bare arms | war hammer (saber) | hammers on an anvil; sparks | none |
| 49 | Beric Donderion | eyepatch, battered armour | flaming sword (saber, the blade on fire) | runs his hand down the blade and it bursts into flame | none |
| 50 | Thoros of Mire | shaved head, red robes, wineskin | sword (saber) | takes a long swig from the wineskin | none |
| 51 | Melisandra | red gown, red hair, ruby choker | fire `spell` (`.lightning`) | gazes into a brazier; the flames rise | "The night is dark…" |
| 52 | Syrio Foral | water dancer, Braavosi silks | wooden practice sword (saber) | a balanced water-dancer's stance on one leg | "Not today." |
| 53 | Jaqen H'gnar | red-and-white hair, ragged prisoner's coat | knife (saber) | his face blurs and becomes his own again | "A man has no name." |
| 54 | Hot Pie | baker's boy, flour-dusted apron | none | holds up a loaf shaped like a wolf | "Wolf bread!" |

**Lords and ladies of the realm (6)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 55 | Robert Beeratheon | big, black beard, crown, antlered helm | war hammer (saber), `bulk` | raises a wine cup | "Gods, I was strong then." |
| 56 | Oberyn Martial | Dornish robes, long dark hair | spear (saber) | twirls the spear round his back | none |
| 57 | Olenna Tyrose | old, sharp, rose-gold wimple | none | sips her wine and says it | "Tell Cersei." |
| 58 | Margaery Tyrose | green-gold gown, rose in her hair | none | offers a rose | none |
| 59 | Loras Tyrose | Knight of Flowers, green armour, rose crest | sword (saber) | polishes a rose-embossed shield | none |
| 60 | The Blackfish | grizzled Tully knight, fish sigil | sword (saber) | sheathes his sword and walks off | none |

**Small friends (agent-only, 2)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 61 | Ser Pounce | Tommen's black-and-white kitten | none | pounces on a falling feather |
| 62 | The Lord Commander's Raven | black raven, `.fly` | none | "Corn!" |

**HEM (1)**, last, as in every universe:

| # | Name | Look | Weapon |
|---|---|---|---|
| 63 | HEM | a black Night's Watch fur cloak, a raven on his shoulder, a leather jerkin | a sword |

### Villains (36)

**The Lannisters and King's Landing (9)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Cersei Lannclaw | gold hair (short in later seasons), crimson-and-gold gown, crown | none | swirls a goblet of wine | "You win or you die." |
| 2 | Tywin Lannclaw | bald, grey beard, crimson doublet, gold lion clasp | none | writes a letter with a quill and seals it | "A Lannister pays his debts." |
| 3 | Joffrey Brattheon | young, blond, crown, gold-and-red | crossbow (`.blaster`, `.arrow`) | tilts his crown and sneers | "I am the king!" |
| 4 | Gregor Clawgane | the Mountain: huge plate armour, flat helm | greatsword (saber), `armoured`, `bulk` | lifts the greatsword overhead, slowly | none |
| 5 | Quackburn | grey hair, black robes, pale hands | none | scribbles notes in a little book | "Your Grace." |
| 6 | Grand Maester Pyclaw | long white beard, great chain, hunched | none | shuffles bent double, then straightens up spry (see Habits) | none |
| 7 | Petyr Baelclaw ("Littleclaw") | trim beard, dark doublet, mockingbird pin | the catspaw dagger (saber) | a little ladder appears and he steps up a rung | "Chaos is a ladder." |
| 8 | Lancel Lannclaw | Faith Militant grey, painted star on his brow | cudgel (saber) | kneels and prays | none |
| 9 | The High Narrow | barefoot, grey sackcloth, cropped grey hair | none | a humble little bow, hands clasped | none |

**Rival kings and their men (6)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 10 | Stannis Sternatheon | close-cropped beard, dark armour, crown of flames | Lightbringer (saber, glowing) | grinds his teeth; "Fewer." | "Fewer." |
| 11 | Balon Greyjaw | old, grey beard, black-and-gold, kraken | none | stands in the wind and rain | "We do not sow." |
| 12 | Euron Greyjaw | dark kohl eyes, black leather coat | axe (saber) | laughs, arms wide | none |
| 13 | Roose Boltclaw | pale, cold eyes, black-and-pink | sword (saber) | a leech on his forearm (his bleeding habit) | none |
| 14 | Walder Fray | very old, tufts of hair, weasel grin | none | cackles and raises a goblet | none |
| 15 | Smalljon Umbrage | young, burly, giant-chains sigil | sword (saber) | cracks his knuckles | none |

**The Wall's enemies (4)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 16 | Alliser Scorn | sour face, grey hair, black furs | sword (saber) | a sneer and a slow clap | "Lord Snow." |
| 17 | Janos Slynk | balding, jowly, gold cloak gone black | sword (saber) | wrings his hands | none |
| 18 | Orrel | wildling warg, furs | axe (saber) | an eagle swoops down and lands on his arm | none |
| 19 | Rattleshirt | the Lord of Bones: armour of bones, a giant's skull helm | club (saber) | rattles: the bones clatter | none |

**The Army of the Dead (6, plus 1 agent-only)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 20 | The Night Clawd | bald ice-blue head, a crown of horns of ice, dark armour | ice spear (`.blaster`, `.thrown(pale blue)`), `armoured` | slowly raises both arms (raising the dead); frost spreads at his feet | none |
| 21 | A White Stalker | long white hair, ice-crackle armour, glowing blue eyes | ice sword (saber), `armoured` | tilts his head; his blade frosts over | none |
| 22 | A Wight | grey-blue skin, rags, glowing blue eyes | claws (saber) | shuffles in place, head jerking | none |
| 23 | The Wight Giant | giant, grey-blue, blue eyes | club (saber), `bulk` | stoops and sways | none |
| 24 | The Wight Bear | huge bear, frost-white fur, blue eyes, flames licking its back | claws (saber), `bulk` | rears up and roars | none |
| 25 | Viceserion | pale dragon with torn wings and blue eyes | blue dragonfire jet (`.lightning`), `.fly`, `bulk` | an icy roar; frost puffs from his jaws | none |
| 36 | A Crawling Wight (agent-only) | small, legless grey wight dragging itself | claws (saber) | none | none |

**Essos (7)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 26 | Viserys Clawgaryen | silver hair, pale robes | none | smooths his hair and demands his crown | "I am the dragon!" |
| 27 | Pyat Three | Qarth warlock, bald, blue lips | blue `touch` (`.lightning`) | splits into three of himself and back | none |
| 28 | Xaro Xhoan Daxclaws | jewelled Qartheen robes, gold | none | flips a gold coin; opens an empty vault | none |
| 29 | Kraznys mo Nakclaws | slaver's robes, oiled beard, tokar | whip (saber) | cracks his whip | none |
| 30 | Mirri Maz Dour | Lhazareen healer, shawl, beads | chant `waves` (`.lightning`) | sings over a steaming bowl | none |
| 31 | A Son of the Harpy | black robes, golden harpy mask | knife (saber) | the mask tilts, slowly | none |
| 32 | The Waif | plain grey dress, cropped hair | staff (saber) | a thin smirk; her face blurs into another and back | "A girl is no one." |

**Dorne (3)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 33 | Ellaria Sands | long dark hair, orange-gold Dornish silks | poisoned dagger (saber, green-tipped) | turns the dagger; a green drip | none |
| 34 | Obara Sands | leather armour, spear | thrown spear (`.blaster`, `.thrown(brown)`) | balances the spear on her palm | none |
| 35 | Nym Sands | dark curls, leathers | whip (saber) | cracks the whip in a loop | none |

The enum order follows the tables (heroes 1–63, villains 1–36 with the crawling wight last). The skeleton's characters, Jon Snaw, Arya Stork and Cersei Lannclaw, are the first cases. Agent-only global ids: heroes 61 and 62 (Ser Pounce, the raven), villain 36 (the crawling wight).

### Telling them apart

- **The blond Lannisters:** Jaime has the gold hand and armour; Joffrey the crown and a sneer; Lancel the grey Faith robe and the star; Cersei the gown. Tyrion is short and red-doubleted.
- **The robes:** Varys bald in silks; Pycelle the long white beard and great chain; Aemon blind-white eyes and black; Clawin grey with a brown beard; Qyburn black with grey hair; the High Narrow barefoot sackcloth.
- **The dead:** the Night Clawd has the ice crown and no hair; the White Stalker has long white hair; the Wight is grey and ragged; Rattleshirt (alive) is bone-armoured with warm skin.
- **The dragons:** black-red, green-bronze, pale ice-blue.
- **The direwolves:** white, storm grey, tawny, dark; Ghost smallest.
- **Jon vs Robb:** Jon black furs, Robb the iron crown and grey cloak.
- **Fire swords:** Beric has the burning blade and an eyepatch; Thoros has a plain blade, red robes and the wineskin; Benjen's fire is a ball on a chain.
- **Against the other universes:** Hound vs Ace the Batclawd Hound (a dog, no armour), the Night Clawd vs the Ice Warrior (green) and Mr. Frost (silver suit), Raygal vs Fin Fang Fume (no wings, shorts), Won Won vs the Frost Jötunn (blue-skinned) and Wun Wun's own shaggy brown.

### Nemeses

Each pair faces off first on the same stage:
- Jon Snaw ↔ the Night Clawd
- Arya Stork ↔ the Waif
- Ned Stork ↔ Littleclaw
- Catelyn Stork ↔ Walder Fray
- Robb Stork ↔ Roose Boltclaw
- Sansa Stork and Olenna Tyrose ↔ Joffrey Brattheon
- Daenerys ↔ Cersei
- Tyrion ↔ Tywin
- Jaime ↔ Ellaria Sands
- Sandor Clawgane and Oberyn Martial ↔ the Mountain
- Theon and Yara Greyjaw ↔ Euron Greyjaw
- Brienne of Tharth ↔ Stannis
- Samwell Tardly ↔ the White Stalker
- Jeor Clawmont ↔ the Wight
- Tormund Clawsbane ↔ Alliser Scorn
- Won Won ↔ the Wight Giant
- Beric and Thoros ↔ the Wight Bear
- Drawgon ↔ Viceserion
- Ghost ↔ Orrel
- Grey Wyrm ↔ a Son of the Harpy
- Missandee ↔ Kraznys
- Khal Clawgo ↔ Viserys
- Margaery and Loras Tyrose ↔ the High Narrow
- Brawn ↔ Nym Sands

**Rivals:** the Night Clawd and the White Stalker never lead two sessions back to back (they're the closest lookalikes).

**Claude's side:** the heroes (the default).

## Places (20)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. The palette swings between cold Northern blue-greys and snow, warm candlelit stone in the south, and the hot ochres and turquoise of Essos and Dorne. Keys are all Westerosi proper nouns, checked unique across the repo.

| # | Key | Place | Still | Moving | Tall-canvas extras |
|---|---|---|---|---|---|
| 1 | `ironThroneRoom` | **The Iron Throne room, the Red Keep** (default) | the jagged throne of melted swords at the top of its steps, pillars, crimson banners | shafts of light from the high windows with dust drifting in them; banners stir; candles flicker | the high windows climb, dragon skulls in the shadows up near the roof |
| 2 | `winterfellYard` | **Winterfell's courtyard** | grey stone, wooden walkways, archery butts, the direwolf banner | snow drifting; smoke from the forge chimney | the Broken Tower and the battlements above, crows on them |
| 3 | `winterfellGodswood` | **Winterfell's godswood** | the white heart tree with red leaves and a carved face, a black pool | red leaves falling; the pool rippling | the weirwood's crown and snowy pines |
| 4 | `castleBlackYard` | **Castle Black** | the yard, wooden stairs and the winch cage at the foot of the Wall | the lift cage rising and falling; snow | the Wall itself, sheer ice rising the whole height of the screen |
| 5 | `frozenLakeNorth` | **The frozen lake beyond the Wall** | a rock island on a white lake, mountains, grey sky | snow blowing sideways; cracks creeping across the ice | snow-capped peaks and a low, bruised sky |
| 6 | `hardhomeShore` | **Hardhome** | the wildling village of huts by a dark sea, longboats pulled up | sea-spray and dusk light; smoke | the cliffs above the village, snow clouds |
| 7 | `threeEyedRavenCave` | **The Three-Eyed Raven's cave** | a cavern of weirwood roots, a root throne | roots twitching; fire glow; embers rising | the roots climb into the dark, little lights of the Children |
| 8 | `blackwaterBay` | **Blackwater Bay** | King's Landing on its hill, the Red Keep, ships in the bay | waves; sails bobbing; gulls | the city climbing up, the Great Sept's dome |
| 9 | `greatSeptBaelor` | **The Great Sept of Baelor** | statues of the Seven, stained glass, rows of candles | candle flames flickering; coloured light shifting | the dome and its high stained glass |
| 10 | `dragonstonePaintedTable` | **Dragonstone: the Painted Table** | the carved map table of Westeros, braziers, the sea through arches | brazier flames; waves beyond | the dark volcanic towers and dragon carvings |
| 11 | `twinsCrossing` | **The Twins** | the two grey towers astride the river, the bridge between | rain; the river running; lantern light | the towers' upper storeys in cloud |
| 12 | `pykeBridges` | **Pyke** | the castle on sea stacks linked by rope bridges, the kraken banner | waves crashing; the bridges swaying | spray rising up the stacks, storm clouds |
| 13 | `meereenPyramid` | **Meereen's Great Pyramid** | the terrace, the city below, the harpy statue | Targaryen banners in the wind; a dragon circling far off | the pyramid's stepped top and the hot sky |
| 14 | `dothrakiSea` | **The Dothraki Sea** | endless grass at sunset, the horse gate of Vaes Dothrak | grass rolling in waves; a hawk circling | huge sky, the bronze horse statues |
| 15 | `titanOfBraavos` | **The Titan of Braavos** | the giant bronze statue straddling the harbour mouth | the beacon fire in his eyes; ships passing under | the Titan at full height, his sword raised |
| 16 | `houseBlackAndWhite` | **The House of Black and White** | the black-and-white doors, the pool, rows of pale masks on pillars | candle flicker; the pool rippling | the pillars of masks climbing into the dark |
| 17 | `qarthUndying` | **Qarth: the House of the Undying** | a doorless tower in the desert, blue-lit inside | blue candle flicker; doors appearing and fading | the tower rising, a Qartheen night sky |
| 18 | `dorneWaterGardens` | **Dorne: the Water Gardens** | Moorish arches, fountains, orange trees | fountains splashing; oranges swaying | arches and blue sky, a palm frond |
| 19 | `innAtTheCrossroads` | **The Inn at the Crossroads** | a timbered inn, a sign, a hitching post, roast chicken on the table inside | smoke from the chimney; the sign creaking | trees and a grey Riverlands sky |
| 20 | `citadelLibrary` | **The Citadel, Oldtown** | endless shelves of chained books, a reading desk | a great brass armillary turning slowly (a nod to the opening titles) | shelves rising into the vaults, ladders |

**Homes:**
- House Stark → Winterfell's courtyard (Bran → the godswood).
- The direwolves → the godswood.
- The North → Winterfell's courtyard (Lyanna Clawmont too).
- The Night's Watch → Castle Black (Sam → the Citadel).
- The free folk → Hardhome; Leif and the Three-Clawed Raven → the cave.
- Daenerys's court → Meereen; Khal Clawgo → the Dothraki Sea; Drawgon and Raygal → Dragonstone.
- Tyrion, Varys → Dragonstone (as Daenerys's council); Jaime → the throne room; the Hound → the Inn at the Crossroads; Theon, Yara → Pyke; Bronn → Blackwater Bay.
- Brienne, Pod → Winterfell's courtyard; Davos, Melisandra → Dragonstone; Gendree → Blackwater Bay; Beric, Thoros, Hot Pie → the Inn at the Crossroads; Syrio → the throne room (he taught in the Red Keep); Jaqen → the House of Black and White.
- Robert → the throne room; Oberyn → the Water Gardens; the Tyrells → the Great Sept; the Blackfish → the Twins.
- The Lannisters → the throne room; the High Narrow and Lancel → the Great Sept; Littleclaw → Blackwater Bay.
- Stannis → Dragonstone; Balon, Euron → Pyke; Roose, Walder, Smalljon → the Twins.
- The Wall's enemies → Castle Black (Orrel, Rattleshirt → Hardhome).
- The dead → the frozen lake (the Wight Giant → Hardhome).
- Viserys, Mirri → the Dothraki Sea; Pyat Three, Xaro → Qarth; Kraznys, the Son of the Harpy → Meereen; the Waif → the House of Black and White.
- Dorne → the Water Gardens.

## Mechanics that make it its own universe

1. **Rides** (`Rides.swift`, chosen in the theme's `ride:` closure):
   - **Daenerys's court** arrives on dragonback: a dragon's shadow sweeps over, it lands with a wingbeat, and leaves the same way.
   - **The Ironborn and Davos** row in on a longship with a striped sail.
   - **The dead** arrive in a blizzard: a swirl of snow thickens, and they're there when it clears; they leave by crumbling into snow.
   - **The Lannisters and the court** arrive in a gilded wheelhouse drawn by a horse (Cersei's from season 1).
   - **Everyone else** rides in on horseback, with their house banner on the lance.
2. **A girl is no one: Game of Clawds' compaction mechanic.** When a Claude Code or pi session led by one of **the Faceless** (Arya, Jaqen, the Waif) compacts its context, its leader becomes no one for a moment: their face lifts away like a pale mask, another face from the Hall of Faces (a random member of the current cast) looks out for a beat, then the mask slips back and they're themselves again, with a caption: "A GIRL HAS NO NAME" (Arya), "A MAN HAS NO NAME" (Jaqen), "A GIRL IS NO ONE" (the Waif). A session losing its memory and coming back as itself is exactly the Faceless trick. It reuses the clock Clawdberg's 88 mph uses: the three go in `Universe.abductees`, and `ThronesNoOne.swift` draws the effect where the overlay draws `OutaTime` (`Overlay.swift:1271`). The masks are pale porcelain, never skin. Everyone else ignores compaction.
3. **Habits** (`Habits.swift`, the Overlay tick):
   - **Wolves follow their Starks.** With both on stage, Ghost trails Jon, Grey Wind trails Robb, Summer trails Bran and Nymeria trails Arya.
   - **The Hound and fire.** When a fire-user is beside him (Beric, Melisandra, the dragons, Leif), he backs away a step.
   - **Winter is here.** While the Night Clawd is on stage, snow drifts across it, whatever the place.
   - **Pycelle's act.** Like the Weeping Angle, the other way round: with nobody near him he straightens up spry and stretches; when someone comes close, he hunches back over his cane.
   - **Warging** (decided 2026-10-16). Now and then, while idle, Bran's or Orrel's eyes go milky white, and a raven (for Bran) or an eagle (for Orrel) circles above them for a few seconds before they blink back. A habit rather than part of the compaction mechanic, which stays with the Faceless.
   - **Arya's list.** With a villain from her list on stage (Cersei, Joffrey, the Mountain, Walder Fray, Tywin), she whispers one name in a speech bubble now and then.
4. **Bespoke practice drills** (`Drills.swift:488`):
   - Arya water-dances with Needle, Syrio-style;
   - Bran shoots at the archery butt and misses; an arrow from off-stage hits the bullseye (the season 1 scene);
   - Jon drills on a straw dummy in the Castle Black yard;
   - Brienne and Pod's sword lesson (Pod gets knocked on his bottom);
   - Sam reads at the Citadel: books pile up beside him;
   - Hot Pie kneads wolf bread;
   - Daenerys sits her dragon eggs in the brazier.

   Nobody floats cross-legged in meditation (`Drills.swift:54`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one. A `CHANGELOG.md` entry each phase.

1. **Skeleton:**
   - the universe case and all the wiring above;
   - Jon Snaw, Arya Stork and Cersei Lannclaw (the enum's first cases);
   - the Iron Throne room, the menu icon, HEM's costume, the saver option and Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with plain wipes (`ComicTransition.pick` returns nil for it).
2. **Core ensemble.** About 37 characters:
   - House Stark, Ghost, the Night's Watch;
   - Daenerys, Drawgon, Jorah, Missandee, Grey Wyrm; Tyrion, Jaime, the Hound;
   - the Lannisters and King's Landing, and the Army of the Dead;
   - 8 places: the throne room, Winterfell's courtyard, Castle Black, the frozen lake, Blackwater Bay, the Great Sept, Dragonstone, Meereen; with homes and nemeses for these.

   The enum cases can go in first as stand-ins and be drawn in a second commit, as The Clawd Files did.
3. **The rest:** up to 99 characters and 20 places, every home filled in. Ends with **the character audit**: every weapon, shot, magic, motion, signature and callout checked against the show and this plan; a mismatches table for your OK.
4. **Mechanics:** the rides, A girl is no one, the habits and the bespoke drills.
5. **Transitions:** the twelve `ThronesTrip`s and the brass name-plate finishing touch (see below), through `ComicTransition`.
6. **Polish pass** (always before docs): every weak spot noted in phases 2–5, split by file and fixed in parallel, with before-and-after renders for your OK.
7. **Docs and release:**
   - README (universe table column, screen-saver paragraph, a collapsible cast-and-places section, developer notes), `llms.txt` (universe list, folder and prefix, the compaction mechanic);
   - `Tools/RenderDocs`: a `thronesLineup` desktop strip, `roster-game-of-clawds.png`, the locations sheet and a social preview; `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - the trailer, `REEL=thrones`;
   - **needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

**Weak spots to expect** (to note as they come up, and fix in the polish pass): the dragons' size against the 72×52 canvas; four direwolves reading as one wolf at agent size; Ser Pounce and the raven being tiny; Needle and Arya's dagger being a few pixels; the Wall's height in the window strip; the Hall of Faces reading as anything but masks.

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` for slow type-checks before calling a phase done.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Jon Snaw"`;
  - `build/preview fight out.png "Jon Snaw" "The Night Clawd"`;
  - `build/preview place out.png "Game of Clawds"`;
  - and the batch sheets, one per Art file. Look at the PNGs before showing them.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> ironThroneRoom winterfellYard`.
- **In the app:**
  - Settings → Universe → Game of Clawds: sessions are heroes, subagents include villains and small fry;
  - the screen saver's Options list it;
  - Random and Clawd Royale reach it.
- **A girl is no one:** `/compact` in a Claude session led by Arya.

## Transitions (`ThronesTrip`, 12)

Each is weighted by who is on screen and where, like `DoctorTrip`.

**Style.** Everything in the app's pixel art. The palette is the opening titles' brass, bronze, aged wood and parchment, with cold Northern blue-greys and snow-white, Lannister crimson and gold, wildfire green and ice blue as accents. No gloss: the opening's hand-made, clockwork feel, built from chunky pixels, gears with few teeth, and a little grain.

**Finishing touch.** Every trip ends with the new place's name on a small brass plate that clicks up from below on two turning cogs, the way towers rise out of the map in the titles.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Clockwork Map** (signature opening) | The full title sequence, our way: the armillary sun spins at the centre, the camera glides low over a brass-and-parchment map, and the new place's towers crank up out of the board on cogs; the camera dives in through the gates. The longest and rarest. | any time, rarely |
| 2 | **The Map Hop** | The short version: the old place folds down into a clockwork model on the map, the camera slides across to the new place's model, which cranks up and fills the screen. | trips between places far apart (Winterfell to Meereen) |
| 3 | **Dracarys** | A dragon's shadow sweeps over; a jet of fire roars across the screen, the old place burns to glowing embers, and the embers settle into the new place. | Daenerys, Drawgon, Raygal; Dragonstone, Meereen |
| 4 | **Winter Is Coming** | Frost creeps in from the corners, snow whites the picture out, then thaws away on the new place, dripping. | the Starks, the Night's Watch; Winterfell, Castle Black |
| 5 | **The Long Night** (`needsOwner`) | Darkness falls in a blizzard; pairs of blue eyes open one by one in the dark, then the storm clears on the new place. | the Night Clawd, the White Stalker, the wights; the frozen lake |
| 6 | **Wildfire** | A green jar tumbles in and bursts; a bloom of green fire fills the screen and dies down on the new place. | Cersei, Tyrion, Quackburn; Blackwater Bay |
| 7 | **The Raven** | A raven flies across with a scroll; the camera follows its flight, the scroll unrolls and the wax seal breaks on the new place. | Bran, the Three-Clawed Raven, Jeor Clawmont, the maesters; the Citadel |
| 8 | **Greensight** (`needsOwner`) | The picture goes milky white like Bran's eyes, rushes forward through weirwood branches as if flying, and lands on the new place. | Bran, the Three-Clawed Raven, Orrel; the cave, the godswood |
| 9 | **The Hall of Faces** | The old place turns into a pale mask on a pillar; it lifts away and the new place is behind it. | Arya, Jaqen, the Waif; the House of Black and White |
| 10 | **The Banners** | A house banner unfurls from the top and sweeps down over the screen, then lifts on the new place. The sigil is the leader's: the direwolf, the lion, the three-headed dragon, the kraken, the rose, the sun-and-spear. | everyone: the banner follows whoever leads |
| 11 | **The Lift** | The view rides the winch cage up the face of the Wall; at the top it looks out over the edge, and the new place is below. | the Night's Watch; Castle Black |
| 12 | **The Iron Fleet** | A wave crashes across the screen, a longship's prow cuts through, and the water falls away on the new place. | the Greyjaws, Davos; Pyke, Blackwater Bay |

**Not used:**
- **The Red Wedding, the Bells, the Sept exploding, Hold the Door:** each is a massacre or a death; not for a desktop toy.
- **The Iron Throne melting:** overlaps Dracarys, and belongs to the finale.
- **The Red Woman's fire visions:** overlaps Dracarys and Wildfire; Melisandra's flames live in her signature instead.
- **The walk of shame bell:** left out with Septa Unella.
- **Arya's coin ("Valar morghulis"):** too small to read at pixel scale.

**Promo.** The Clockwork Map (#1) is the trailer's title sequence.

## Promo: the trailer (`REEL=thrones`)

Built on `doctorShots`, about 45–50 seconds, rendered with the app's own sprites, places and transitions. Storyboard first, for your OK.

- **Intro (~9 s): the Clockwork Map.** A slow push in on the brass armillary sun spinning over a dark map. The camera glides north: King's Landing cranks up out of the board on cogs, then Winterfell, then the Wall rising in ice. The sun flares, **GAME OF CLAWDS** swells out of it in bronze letters, and the camera plunges through the Iron Throne room's doors into white. Sound: a driving cello-and-drums ostinato in a minor key in the *sound* of the theme, but our own notes; a clank of gears on each tower.
- **Set piece (~9.5 s): the Long Night at Winterfell.** Snow starts falling in Winterfell's courtyard (the Night Clawd's habit). Blue eyes open beyond the wall. Melisandra lifts her hands and a line of arakhs bursts into flame. Drawgon swoops down (the dragon ride) and breathes fire across the yard. The Night Clawd raises his arms; the wights rise. Then Arya leaps in from nowhere, the dagger flip, and he shatters into ice and snow. Dawn breaks pink over the battlements. Caption: "Not today."
- **Hook (4 s):** shared.
- **Desktop (~4.6 s):** `brawl(ctx, .thrones, …)`: "Winter is coming. So is your sprint review."
- **Status (~4.2 s):** four characters, one per state; the aside: "Hodor."
- **Agents (4 s):** "Every subagent gets to be a sworn sword."
- **Window (~4.8 s):** `windowShot(ctx, .thrones, …, at: .ironThroneRoom)`: "When you play the game of terminals, you ship or you die."
- **AIs (~4.4 s):** the BRING YOUR OWN AI* line-up, one character per AI.
- **End card (~4.2 s):** the Iron Throne room, the crew lined up, the title lands, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS", the app icon and the GitHub URL. A last brass cog clicks.

No logo or melody is copied: the title is our own lettering, and the music only evokes the theme's instruments and mood.

## Decisions (2026-10-16)

All the open questions are settled:
- **Name: Game of Clawds.**
- **House of the Dragon:** left out for now; it can be appended later as its own group without changing any ids.
- **Sides:** the Long Night rule holds for everyone. Melisandra, Daenerys and Jaime are heroes.
- **Ramsay Bolton** stays out.
- **Compaction:** "A girl is no one" stays with the three Faceless. The wargs get a white-eyed **warging** habit instead (Bran and Orrel).
- **The default place** is the Iron Throne room.
- **House Stork** stays, and the other names stand.
- **Swaps:** none; the cast stands as written.

The plan is ready for phase 1 when you say start.