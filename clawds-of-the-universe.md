# Plan: a new universe, Clawds of the Universe (He-Man and the Masters of the Universe)
<!-- track: repo=rodclemen/clawd-clash branch=he_man folder=Eternia title="Clawds of the Universe" cast=85 places=21 -->

(The file keeps its old name, `masters-of-the-clawdiverse.md`, so links to it still work. The universe is called **Clawds of the Universe**.)

## Context

Clawd Clash has seven universes: Star Clawds, Marvelous Clawds, Detective Clawds, Doctor Clawd, The Clawd Files, Stevie Clawdberg and Clawd of the Rings. This plan adds He-Man and the Masters of the Universe as a full ensemble, built the same way as Doctor Clawd and The Clawd Files. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

- **Name: Clawds of the Universe** (decided 2026-10-16).
- **Scope: the 1983–1987 cast.** That's the 1983 Filmation cartoon and the 1982–87 toy line, plus **She-Ra: Princess of Power** (Filmation, 1985) and the **1987 live-action film**:
  - She-Ra brings the Great Rebellion and, more importantly, the Evil Horde. Without it the villain side would be thin (see Viability).
  - The film brings Gwildor, the Thenorian locksmith with the Cosmic Key, and Skeletor's mercenaries Blade, Saurod and Karg, plus his Dark Troopers. It also brings a place of its own, the small Earth town at night.
  - The 2002 series and Revelation stay out. The 2002 Snake Men are a possible add-on later, appended to the enums.
- **Code naming** avoids the franchise name, as the other universes do:
  - `case eternia` with key `"eternia"`.
  - Folder `Sources/App/Universes/Eternia/`, file prefix `Eternia…`.
  - Branch `he_man`. Trailer reel `REEL=eternia`.
- **Raw value:** the next free one when its build starts, checked against main and the open branches (Clawd of the Rings is `middleEarth = 6` on main, and the `buffy` branch also uses 6 today); ids are rawValue*1000 and permanent.
- **Naming style:** light puns on the on-screen names (He-Clawd, Skeleclawd, Man-At-Claws, Trap Claw, Tri-Klawps). Where no pun comes naturally, a near-spelling or the plain name (Bow, Glimmer, Kowl, Cringer). Actors' names are never used.
- **Size:** **85 characters**: 44 heroes including HEM and one agent-only, and 41 villains including 4 agent-only. Plus **21 places** and **12 transitions**.
- **Tone:** the show is already made for children, so very little needs leaving out. Fisto is renamed (his real name reads as adult slang); Mosquitor (a blood-sucker) and the cruelty of Vultak's Horde Zoo are left out. Anything else is just a matter of keeping fights cartoonish, which is how Filmation drew them anyway: nobody is ever hurt by a sword.

| Universe                    | Heroes | Villains | Total | Places | Transitions |
|-----------------------------|--------|----------|-------|--------|-------------|
| Star Clawds                 |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds            |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds            |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd                |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files             |     36 |       46 |    82 |     20 |          11 |
| Stevie Clawdberg            |     64 |       54 |   118 |     23 |          10 |
| Clawd of the Rings          |     38 |       38 |    76 |     22 |           9 |
| Clawds of the Universe (proposed) | 44 |   41 |    85 |     21 |          12 |

(heroCount includes HEM; villainCount includes agent-only.)

### Viability

It clears the bar comfortably: **42 heroes and 37 villains** who can lead a session (not counting HEM and the agent-only small fry).

Without She-Ra it would not. The 1983 cartoon alone gives about 22 good heroes but only about 18 villains, since the Evil Warriors are a small gang and most of Filmation's one-off foes (Kothos, the Dragon of Darksmoke's enemies, assorted wizards) aren't recognisable. That would be **a limited experience**: the same five villains every time. She-Ra adds 15 Horde villains and 19 rebels, all drawn in the same Filmation style, and Hordak is canonically Skeletor's old teacher, so the two halves meet naturally. The 1987 film adds one hero and three villains who lead, plus the Dark Troopers as small fry. They're drawn in the same flat cel style as everyone else, so they sit with the cartoon cast without looking out of place.

Left out of the film on purpose: Julie and Kevin, the Earth teenagers, and Detective Lubic. They're ordinary people in 1980s clothes, and none of them carries the show the way Gwildor's Cosmic Key does.

### Telling the barbarians apart

Half the heroic cast are muscled men in furry briefs and a harness, and many villains are green and scaly. At 72×52 pixels, **colour and headgear carry them**, so every character below is given a distinct colour pair and a helmet, hood or head shape. The risky clusters, and how each is split:
- **He-Clawd / Faker / Prince Addam:** He-Clawd is bronze with a blond pageboy and the iron-cross harness; Faker is the same build in **blue skin, orange armour and red hair** with glowing eyes; Addam wears a **pink vest and lavender sleeves**, paler, no harness.
- **He-Clawd / She-Clawd:** She-Clawd has the long blond hair, **winged golden tiara, red cape** and white tunic.
- **The scaly greens:** Mer-Clawd (teal-green, fish fins, blue armour), Kobra Khan (bright green, **yellow cobra hood**), Whiplash (olive-brown, long gator snout and **orange belly**, spear), Rattlor (**red-orange**, yellow belly, rattle tail), Tung Lashor (**purple**, long pink tongue), King Hiss (purple-and-gold armour, snake heads round his waist), Saurod (**grey-green** lizard in **silver plate armour**, sparks at the mouth).
- **The beasts:** Beast Clawd (**orange-red fur, blue face**), Grizzlor (dark brown shag, **Horde purple chest armour, red eyes**), Battle Kat (**green tiger, orange stripes, red helmet and saddle**), Cringer (the same tiger, no helmet, ears down), Panthor (**dark purple panther, gold saddle**). Katra no longer turns into a panther, so Panthor is the only purple cat.
- **The big hands:** Clawfist's **silver** right fist on blue and red armour; Jitsu's **gold** chopping hand on orange and black.
- **The film's mercenaries:** Blade (**black and silver**, a long sword), Karg (**wild white mane**, a hook for a hand, black fur cloak). Neither is a skull, so neither reads as Skeleclawd.
- **The fliers:** Stratos (grey fur, **blue wing-arms, red backpack**), Vultak (bald pink vulture head, black wings), Kowl (round grey koala-owl, little), Buzz-Off (yellow and black bee), Flutterina (butterfly wings), Swift Wind (white winged horse).

**Against the other seven universes** (they all meet in Clawd Royale):
- **Thorr** and **Herakles** (Marvel) and **Captain Thunderbolt** (DC, red and gold with lightning): He-Clawd's lightning is white-gold from the sword tip, and he's bronze and blond with no cape.
- **Cyclopz** (Marvel, red visor): Tri-Klawps is green with a **three-eyed rotating drum** on his helmet.
- **The Beest** (Marvel, blue fur) and **Sabreclawd**: Beast Clawd is orange-red with a blue face.
- **Chewbacca** (Star Clawds): Grizzlor needs his Horde armour and red eyes to stay apart from him.
- **Black Panthah** and **Black Kat** (Marvel): Katra's red cat-mask headdress and long black hair. She stays a woman in a mask throughout; no panther form.
- **The Horde Trooper and the Dark Troopers:** grey robot with the red bat emblem, against black armour with a narrow visor and no emblem.
- **Fin Fang Fume** (Marvel's green dragon): Granamyr is grey-green, old, with a long white beard and horns, and mostly sits.
- **Hawk-Warrior** and **Hawk-Maiden** (DC): Stratos has no helmet or mace; blue wing-arms on grey fur.
- **Aquamarine** (DC): Mermista has a blue-green tail and white-blonde hair; Mer-Clawd is a fish-man, not a man.
- **Killer Gator** (DC): Whiplash is olive-brown with a spear and a long tail.
- **The Thingamajig** (Marvel, orange rock): Stonedar is grey-brown stone.
- **Red Skulk** (Marvel): Skeleclawd's skull is **yellow under a purple hood**, his body blue.
- **The Emperor's Royal Guards** (Star Clawds, red robes): Shadow Weaver's red robe has a black face and glowing eyes, and she casts.
- **Names:** DC already has a **"Sorceress"** and **"The Leech"**, and Marvel has **"The Scorpyon"** and **"Iron Fyst"**. So it's *The Sorceress of Greyskull*, *Leach*, *Scorpia* and *Clawfist*.

## How a universe plugs in (checked against the code on 2026-10-17, main at d270b63)

**New code: `Sources/App/Universes/Eternia/`**
- `EterniaRoster.swift`:
  - `enum EterniaHero` and `enum EterniaVillain`, append-only, with `hem` as the last hero.
  - The persona dictionaries, `.reduce([.hem: hemPersona(.eternia)])`.
  - `Location.eterniaHome(of:)`, `eterniaNemeses`, the ride closure, `let eterniaTheme = Theme(...)`.
  - The `static let` place keys, and `let eterniaPlaces` merged from the Places files.
- `Art/EterniaHeroes1…N.swift` and `Art/EterniaVillains1…N.swift`, about 8–10 personas per file, in the pattern of `ClawdbergHeroes1.swift`. Shared helpers (the harness, the furry briefs, the Horde emblem) go in `EterniaKit.swift` with `eternia`-prefixed names.
- `Places/EterniaScenes1…N.swift` as `let eterniaScenesN: [Location: Place]`.
- `EterniaIcon.swift`: the menu bar icon, 28×26, colour and mono. Castle Greyskull's skull face, or the Power Sword with a spark at its tip.
- `EterniaRides.swift`: the Wind Raider, Swift Wind, the Roton and the Horde skiff (see Mechanics).
- `EterniaPower.swift`: the transformation on compaction (see Mechanics).
- `EterniaDrills.swift`: bespoke drills.
- `EterniaWipes.swift`: the transitions, last.

**Wiring into the existing code.** Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎. Copy what `clawdberg` did at each spot.
- **`Sources/Shared/Universe.swift`:**
  - `:8–40`: the case, `key`, `title`, `villainCount`, `heroCount`.
  - `:50–61`: `agentOnly` (Loo-Kee, Imp, the Horde Trooper, Screeech, the Dark Trooper: table rows hero #42 and villains #34, #35, #36 and #41, which are the 0-based enum ids hero 41 and villains 33, 34, 35 and 40).
  - `:65`: `claudeSide` (Claude plays the heroes, the default `false`).
  - `:68`: `rivals` (Skeleclawd and Hordakk, see Nemeses). Today it's a one-liner, `self == .starWars ? [0, 1] : []`, so it becomes a `switch` or gains an Eternia branch.
  - `:70–78`: `guises` gets the four Eternia pairs (see Mechanics). Today it's `guard self == .middleEarth else { return [] }`, so it becomes a `switch`, and its doc comment gains the Eternia pairs. The `Roster`'s union at `:141` and `ruledOut(by:)` at `:143–145` pick them up with nothing added.
  - `:100–102`: next to `regenerations`, a one-line flag, `var guisesSwapOnCompaction: Bool { self == .eternia }`, with a doc comment like the others (see Mechanics).
- ⚠︎ **`Sources/Shared/StatusStore.swift`:**
  - `:336–349` (`PreCompact`): a transformation branch after the abductee one (`:341`), before the regeneration lookup (`:342`).
  - Nothing for the secret identity rule: the casting already keeps to `guises` (see Mechanics).
  - `"Stop"` (`:350`): the moral's roll (see Mechanics).
- **`Sources/App/Theme.swift:40`:** `Theme.of`.
- **`Sources/App/Locations.swift:72`:** `.merging(eterniaPlaces)`.
- **`Sources/App/Universes/ComicTransition.swift:42`:** `pick` now lists every universe explicitly, and Star Clawds is the only one left on plain wipes, so in phase 1 Eternia joins its line: `case .starWars, .eternia: return nil`. In phase 5 it comes out of that line, and a `.eternia(EterniaTrip)` case goes in the enum (`:8–13`), `duration` (`:15`), `draw` (`:27`) and `pick` (`:40`), plus the doc comment (`:3–5`).
- **`Sources/App/Universes/Hem.swift:29, 104, 119, 146, 172, 228`:** HEM's costume in every switch (below).
- **`Sources/App/Rides.swift`:** the rides (phase 4).
- **`Sources/Saver/SaverView.swift`:** nothing to add. The Options list (`:89`) and the trip choice (`:208`) build themselves from `Universe.offered`.
- ⚠︎ **`Sources/App/Drills.swift:54`** (the meditation guard: no, see Mechanics) and **`:488`** (the bespoke drills merge).
- ⚠︎ **`Sources/App/Overlay.swift:868`:** five Playground prompts, a `case .eternia:` in the `prompts` switch. Lines 1143 and 1271 show how clawdberg hooked its set piece and its OutaTime effect into the tick; the transformation effect and Skeleclawd's retreat hook in the same places. The moral's speech bubble reuses the callout bubble at `:1339`.
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`:** decide whether Eternia joins each universe-specific `if`.
- ⚠︎ **`HookInstaller.swift`:** nothing new. The transformation reuses Doctor Clawd's `PreCompact` hook and the moral reuses `Stop`, both already registered.
- **Clawd Royale** picks up the cast and places through `Universe.allCases`. Check the menu bar icon and arch-enemies when a scene is an Eternia place.
- **Tools:**
  - `Tools/Preview/main.swift:64–120`: batch names (`eterniaHeroes1…`), the universe lookup and the enum lookups.
  - `Tools/Transitions/main.swift:7, 15, 133`.
  - Phase 6: `Tools/RenderPromo` (`REEL=eternia`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

## Cast

Each entry gives the parody name, its look as pixels, its weapon or motion, and its signature move. How the engine's weapons map onto the show:
- **`.saber`** is the main weapon on both sides. Eternia is swords, axes, staffs, maces, claws and fists. Filmation's He-Man barely swings his sword at people (he throws things, lifts things and deflects blasts), and `.saber` deflecting shots is exactly that.
- **`.blaster`** is for the few who shoot: Bow's arrows, Hordak's arm cannon, Trap Jaw's arm laser, Mantenna's eye beams, Saurod's mouth sparks, Roboto, Zodac, the Horde Troopers and the Dark Troopers. Frosta (`.ice`), Granamyr (`.fire`), Netossa's net (`.thrown`) and Perfuma's flowers (`.thrown`) use other shot styles.
- **`.lightning` + `Magic`** is for the sorcerers. Every caster gets its own family and colour (table below), so no two look alike here or elsewhere.
- **`motion: .fly`** for Stratos, Buzz-Off, Swift Wind, Kowl, Flutterina, Vultak, Granamyr and Queen Angella; **`.hover`** for Orkko, Light Hope and Horde Prime; **`.swing`** for Webstor.
- **`armoured: true`** for robots, rock and plate: Roboto, Multi-Bot, Clawful, Stonedar, Saurod, the Horde Trooper and the Dark Trooper.
- **`bulk`** for Battle Kat, Panthor, Granamyr, Ram Clawd, Two Bad and Clawful.

### Magic, one look per caster

| Caster | Family | Core / glow | What it looks like |
|---|---|---|---|
| Skeleclawd | jagged | sickly yellow / violet | forked bolts from the ram's-skull Havoc Staff |
| Count Marzo | jagged | orange / blood red | short crackling forks from his amulet |
| Horde Prime | jagged | acid green / black | a bolt out of the smoke round his hand |
| Evil-Lynn | spell | teal / deep blue | a twinkling ribbon from the orb on her staff |
| Orkko | spell | lemon / magenta | a sparkly ribbon that ends in a puff of the wrong thing |
| Clawstaspella | rings | lilac / violet | hypnotic rings, she spins as she casts |
| Queen Angella | rings | white / gold | golden rings from her wing-tips |
| The Sorceress of Greyskull | steady | white / sky blue | a calm, steady ray |
| Glimmer | steady | white / pink | a bright ray of light, a glow at the hand |
| Shokoti | steady | gold / black | a wavering gold ray |
| Sy-Klawne | waves | white / pale blue | wind arcs as he spins |
| Kobra Khan | waves | pale green / green | sleep mist pulsing out of his hood |
| Mermista | waves | aqua / blue | water arcs |
| Shadow Weaver | waves | dark crimson / black | shadow pulses from her sleeves |
| Madame Razz | touch | pink / purple | a glowing fingertip; the target glows (often the wrong one) |
| Leach | touch | yellow-green / green | his suckers glow; the target's glow drains to him |

Check every colour against the other seven universes' casters (`magicVariants`, `Theme.swift:55`) when drawing.

### Heroes (44)

**The Masters of the Universe: Eternia's heroes (22)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | He-Clawd (He-Man) | bronze, blond pageboy, iron-cross harness, furry briefs | the Power Sword (`.saber`) | raises the sword overhead; a fork of white-gold lightning hits its tip |
| 2 | Orkko (Orko) | floats; floppy orange hat, magenta robe with a black O, purple scarf hiding all but two eyes | bungled magic (`spell`, lemon/magenta), `.hover`, `canSit: false` | a trick goes wrong: a little rain cloud forms over his own hat |
| 3 | Prince Addam (Prince Adam) | paler, blond, pink vest, lavender sleeves and tights | none (the lazy prince) | yawns and stretches; the Power Sword peeks over his shoulder |
| 4 | Battle Kat (Battle Cat) | green tiger, orange stripes, red helmet and saddle | claws (`.saber`), `bulk` | rears and roars |
| 5 | Cringer | the same green tiger, no armour, ears flat | none | covers his eyes with both paws and trembles |
| 6 | Teelah (Teela) | auburn ponytail, white and gold, snake-crest headpiece | staff (`.saber`) | twirls her staff and plants it |
| 7 | Man-At-Claws (Man-At-Arms) | moustache, orange helmet, green and orange armour | mace (`.saber`) | pulls out a spanner and tinkers with his gauntlet; sparks |
| 8 | The Sorceress of Greyskull | white feathered falcon costume, falcon headdress, wings | `steady`, white/sky blue | spreads her wings, becomes Zoar the falcon for a beat, and back |
| 9 | King Randor | crown, brown beard, blue and gold royal robe | sword (`.saber`) | raises his sceptre (holding court) |
| 10 | Queen Marlena | crown, long gown | none | puts on her old astronaut's helmet (she crashed on Eternia from Earth) |
| 11 | Stratos | grey fur, blue feathered wing-arms, red backpack, goggles | fists (`.saber`), `.fly` | flaps up, hangs in the air, lands |
| 12 | Ram Clawd (Ram Man) | short, red-brown ram helmet, green armour | headbutt and axe (`.saber`), `bulk` | crouches and springs, head first |
| 13 | Man-E-Claws (Man-E-Faces) | helmet with a turning drum of faces, red and green armour | fists (`.saber`) | turns his faces: man → robot → monster → man |
| 14 | Mekaneck | blue armour, orange body, periscope visor | club (`.saber`) | his neck telescopes up, looks round, comes down |
| 15 | Buzz-Off | yellow and black bee, clear wings, antennae | axe (`.saber`), `.fly` | buzzes a little loop |
| 16 | Clawfist (Fisto) | big black beard, huge silver right fist, blue and red armour | the fist (`.saber`) | thumps his metal fist into his palm |
| 17 | Roboto | robot with a see-through chest of gears, snapping jaw | arm laser (`.blaster`, cyan energy), `armoured` | his chest gears spin faster |
| 18 | Moss Clawd (Moss Man) | shaggy green moss, brown face | vine lash (`.saber`) | a flower blooms on top of his head |
| 19 | Sy-Klawne (Sy-Klone) | blue and red armour, yellow radar fin on his head | whirlwind (`waves`, white/pale blue) | spins like a top |
| 20 | Snout Spout | elephant-trunk robot head, blue and red fire-fighter armour | water jet (`.blaster`, white/blue beam) | trumpets a fountain into the air |
| 21 | Zodac | the Cosmic Enforcer: red armour, black helmet, beard | laser pistol (`.blaster`, violet energy) | sits down in mid-air on his floating cosmic chair |
| 22 | Granamyr | old grey-green dragon, long white beard, horns | breath (`.blaster`, `.fire`), `.fly`, `bulk` | puffs a smoke ring, unimpressed |

**She-Ra and the Great Rebellion (19)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 23 | She-Clawd (She-Ra) | long blond hair, winged gold tiara, white tunic, red cape | the Sword of Protection (`.saber`) | the sword's jewel glows and it turns into a shield, then back |
| 24 | Princess Adorra (Adora) | blond, white tunic, red skirt, brown boots | sword (`.saber`) | holds the sword up to the light, thinking |
| 25 | Spirit | white horse, short mane | none | paws the ground, tosses his mane |
| 26 | Swift Wind | white winged unicorn, pink mane | horn charge (`.saber`), `.fly` | rears, wings wide |
| 27 | Bow | moustache, red shirt with a heart, blue cape | bow (`.blaster`, `.arrow`) | plucks his bow like a harp |
| 28 | Glimmer | pink and purple, long dark-red hair | `steady`, white/pink | lights a glowing ball of light in her palm |
| 29 | Queen Angella | white feathered wings, lilac gown, tall crown | `rings`, white/gold, `.fly` | folds and opens her wings |
| 30 | Clawstaspella (Castaspella) | purple robe, tall stiff collar, gold circlet | `rings`, lilac/violet | the hypno-spin: twirls on the spot |
| 31 | Frosta | white and ice-blue gown, icicle crown, white hair | ice (`.blaster`, `.ice`) | freezes the floor and skates a little circle |
| 32 | Madame Razz | small Twigget witch, purple pointed hat, green shawl, Broom at her side | `touch`, pink/purple | climbs on Broom, wobbles, falls off |
| 33 | Kowl | round grey koala-owl, big ears, little wings | none, `.fly` | folds his arms and rolls his eyes |
| 34 | Sea Hawk | pirate: red bandana, open waistcoat, boots | cutlass (`.saber`) | swings in on a rope |
| 35 | Mermista | blue-green fish tail (legs on land), white-blonde hair, shell crown | `waves`, aqua/blue | a little wave curls up beside her |
| 36 | Perfuma | flowers in her hair, pink and green petal dress | flowers (`.blaster`, `.thrown`, pink) | sniffs a flower; petals drift up |
| 37 | Peekablue | blue and white, a folded peacock tail | none | fans out her tail, every "eye" opening |
| 38 | Netossa | dark hair, white cape that's a net | net (`.blaster`, `.thrown`, silver) | swirls her cape out into a net |
| 39 | Flutterina | blonde, orange and yellow butterfly wings | none, `.fly` | flutters up and settles |
| 40 | Light Hope | a pillar of rainbow light with a calm face in it | none, `.hover`, `canSit: false` | the light cycles through the rainbow |
| 41 | Stonedar | grey-brown rock warrior, Comet Warrior armour | fists (`.saber`), `armoured` | curls into a boulder and rolls a little way |

**Agent-only small fry (1)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 42 | Loo-Kee | small yellow Kon-Seal, big eyes | none | hides behind the scenery and peeks out (She-Ra's "did you find me?") |

**From the 1987 film (1)**, appended after the small fry since ids are append-only

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 43 | Gwildor | small and stooped, wrinkled grey-brown face, wild red-brown hair and beard, brown robes, a tool belt | none (a locksmith, not a fighter; he ducks behind the nearest Master) | holds up the Cosmic Key: its lights blink in a row and a little run of music notes floats up |

**HEM (1)**, as in every universe, last: a blond pageboy wig, a leather chest harness with an iron cross, and a foam Power Sword.

Callouts (`Persona.callout`) for the leads:
- He-Clawd: "I have the power!"
- Prince Addam: "By the power of Greyskull!"
- Princess Adorra: "For the honour of Greyskull!"
- She-Clawd: "I am She-Clawd!"
- Orkko: "Oops!"
- Cringer: "Do I have to?"
- Battle Kat: "Rrrowr!"
- Teelah: "Where's Adam?" (she's always asking, which is the joke)
- Man-At-Claws: "Leave it to me."
- The Sorceress of Greyskull: "Hurry, He-Clawd!"
- Bow: "Here's Bow!"
- Kowl: "Typical."
- Gwildor: "Have key, will travel!"

### Villains (41)

**Skeleclawd and the Evil Warriors (15)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Skeleclawd (Skeletor) | yellow skull face, purple hood, blue body, black harness | Havoc Staff (`jagged`, yellow/violet) | shakes his fist and cackles, staff raised |
| 2 | Evil-Lynn (Evil-Lyn) | pale, black skullcap with fins, blue and purple robes | orb staff (`spell`, teal/deep blue) | gazes into the orb on her staff; it swirls |
| 3 | Beast Clawd (Beast Man) | orange-red fur, blue face, blue armour pieces | whip (`.saber`) | cracks the whip and roars |
| 4 | Trap Claw (Trap Jaw) | blue skin, metal jaw, black helmet, purple, a hook-arm | arm laser (`.blaster`, orange/yellow energy, `handGun: false`) | chomps his metal jaw open and shut |
| 5 | Tri-Klawps (Tri-Klops) | green armour, helmet with a turning drum of three eyes | sword (`.saber`) | the eye drum turns, each eye glowing as it comes round |
| 6 | Mer-Clawd (Mer-Man) | teal-green fish face, fins, blue armour | sword (`.saber`) | a fish leaps past behind him |
| 7 | Kobra Khan | bright green, yellow cobra hood | sleep mist (`waves`, pale green) | his hood flares open |
| 8 | Clawful | big red crab, yellow boots | claws (`.saber`), `armoured`, `bulk` | snaps both claws |
| 9 | Webstor | blue skin, orange armour, spider pack | grapple line (`.blaster`, `.web`), `.swing` | dangles upside down on a line |
| 10 | Whiplash | olive-brown alligator, long snout, orange belly | spear and tail (`.saber`) | swishes his tail |
| 11 | Spikor | blue-purple, orange spikes, trident arm | trident (`.saber`) | his spikes stand up all over |
| 12 | Two Bad | two heads (blue and green), one body | fists (`.saber`), `bulk` | the heads turn and argue |
| 13 | Faker | He-Clawd's double: blue skin, orange armour, red hair, glowing eyes | sword (`.saber`) | strikes He-Clawd's sword-up pose, but sparks fizz out of his ear |
| 14 | Panthor | dark purple panther, gold saddle | claws (`.saber`), `bulk` | snarls and swishes his tail |
| 15 | Stinkor | black and white skunk man, orange armour | none | lifts his tail: a green stink cloud drifts up (everyone near steps away) |

**Other foes of Eternia (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 16 | King Hiss | purple and gold armour, snake heads round his waist | snake bites (`.saber`) | his human face peels away to show the snakes, then back |
| 17 | Count Marzo | old red-bearded sorcerer, purple robe, amulet | `jagged`, orange/red | rubs his hands over his glowing amulet |
| 18 | Shokoti | the priestess: gold headdress, black and gold robes | `steady`, gold/black | raises both arms; her headdress glows |

**Hordakk and the Evil Horde (15)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 19 | Hordakk (Hordak) | white mask-like face, red eyes, bony cowl, dark blue suit, red bat emblem | arm cannon (`.blaster`, white/crimson energy, `handGun: false`) | his arm turns into a cannon, then back; snorting laugh |
| 20 | Shadow Weaver | red hooded robe, black face, glowing eyes | `waves`, dark crimson/black | weaves her hands; shadows curl round them |
| 21 | Katra (Catra) | long black hair, red cat-mask headdress, black and red | claws and whip (`.saber`) | pulls the cat mask down over her eyes and cracks her whip (no panther form: Panthor is the purple cat) |
| 22 | Scorpia | red and black, pincers, a stinger tail over her head | pincers (`.saber`) | clacks her pincers, tail flicks |
| 23 | Mantenna | four-legged brown bug, eyes on stalks | eye beams (`.blaster`, red beam, `handGun: false`) | his eyes pop out on their stalks |
| 24 | Leach (Leech) | green, suckers on his hands and mouth | `touch`, yellow-green | sticks to the wall with a sucker |
| 25 | Grizzlor | dark brown shag, Horde purple chest armour, red eyes | claws (`.saber`) | beats his chest |
| 26 | Modulok | red skin, two heads, extra limbs | fists (`.saber`) | pops a head off and puts it on the other way |
| 27 | Multi-Bot | two-headed, four-armed grey robot | fists (`.saber`), `armoured` | its heads spin round |
| 28 | Entrapta | purple outfit, long golden braids | hair lasso (`.saber`) | her braids lash out like ropes |
| 29 | Octavia | blue octopus woman, four tentacles | tentacles (`.saber`) | waves all four tentacles |
| 30 | Rattlor | red-orange snake, yellow belly, extending neck | bite (`.saber`) | rattles his tail |
| 31 | Tung Lashor | purple snake, a long pink tongue | tongue lash (`.saber`) | flicks his tongue out far |
| 32 | Vultak | bald pink vulture head, black wings | talons (`.saber`), `.fly` | hunches and croaks |
| 33 | Horde Prime | smoke clouds with a huge green hand | `jagged`, acid green/black, `.hover`, `canSit: false` | the hand reaches out of the smoke and points |

**Agent-only small fry (3)**
- Imp (34): Hordak's tiny purple bat-winged spy. Turns into an everyday object now and then (a vase, a stool).
- Horde Trooper (35): grey robot with a red bat emblem, `.blaster` red energy, `armoured`. Marches in step.
- Screeech (36): Skeleclawd's purple-and-green bird, `.fly`.

**Appended in phase 3 (5).** Ids are append-only, so these come after the small fry above, at the end of the villain enum.

*From the bench (1):*

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 37 | Jitsu | black hair, orange and black martial-arts armour, a huge golden right hand | the chopping hand (`.saber`) | karate-chops a plank clean in two |

*From the 1987 film (3 leaders, 1 small fry):*

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 38 | Blade | the mercenary swordsman: black and silver armour, slicked-back black hair, a scar | long sword (`.saber`) | a fencing salute, then a quick flourish |
| 39 | Saurod | armoured lizard man: grey-green scales, silver plate armour, red eyes | sparks from his mouth (`.blaster`, orange/yellow energy, `handGun: false`), `armoured` | opens his jaws and a shower of sparks sprays out |
| 40 | Karg | wild white mane, pale face, a hook for a left hand, black fur cloak over bronze armour | hook and sword (`.saber`) | slashes the air with his hook and bares his teeth |

- Dark Trooper (41), agent-only: Skeletor's foot soldiers in the film. Black armour, a helmet with a narrow visor, a laser rifle (`.blaster`, red energy), `armoured`. They march in a line, rifles up.

### Nemeses

Each pair faces off on the same stage:
- He-Clawd ↔ Skeleclawd
- She-Clawd ↔ Hordakk
- Prince Addam ↔ Beast Clawd
- Princess Adorra ↔ Katra
- Teelah ↔ Evil-Lynn
- Man-At-Claws ↔ Trap Claw
- Battle Kat ↔ Panthor
- Orkko ↔ Count Marzo
- The Sorceress of Greyskull ↔ Shokoti
- Mekaneck ↔ Tri-Klawps
- Man-E-Claws ↔ Faker
- Ram Clawd ↔ Clawful
- Buzz-Off ↔ Webstor
- Clawfist ↔ Jitsu (the fist and the chopping hand; their toys were sold as rivals)
- Moss Clawd ↔ Stinkor (the toys shared a mould)
- Roboto ↔ Multi-Bot
- King Randor ↔ King Hiss
- Stratos ↔ Vultak
- Mermista ↔ Mer-Clawd
- Sea Hawk ↔ Octavia
- Clawstaspella ↔ Shadow Weaver (once friends)
- Bow ↔ Mantenna
- Frosta ↔ Scorpia
- Glimmer ↔ Entrapta
- Light Hope ↔ Horde Prime
- Gwildor ↔ Karg (Karg leads the hunt for the Cosmic Key)
- Snout Spout ↔ Saurod (the fire-fighter and the spark-spitter)
- Stonedar ↔ Blade (a sword is no use against stone)

That's 28 pairs, three over the guide's usual 25, all for the film. Two Bad no longer has a nemesis; his two heads argue with each other instead.

**Rivals:** Skeleclawd and Hordakk never lead two sessions back to back. They are the two big bads, and the old pupil and teacher; two cackling skull-faces in a row would feel repetitive.

**Claude's side:** the heroes (the default).

## Places (21)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. Places 1–14 are on Eternia, 15–20 on Etheria, and the last is the film's Earth town. Keys are flavoured so they won't clash with the sibling plans: the proper nouns are unique already, and the generic ones carry `eternia`.

| # | Place (key) | Still | Moving layer | Tall-canvas extras |
|---|---|---|---|---|
| 1 | **Castle Greyskull** (`castleGreyskull`), the default | the skull-faced castle over a chasm, the jawbridge down, a purple-orange Filmation dusk | green mist curling up out of the chasm; the jawbridge chains sway | the full tower and its twin turrets; Zoar circling; distant lightning |
| 2 | **The Sorceress's chamber** (`greyskullChamber`) | the stone throne room inside Greyskull, the glowing pool, falcon carvings | the pool's light ripples on the walls | the vaulted ceiling and its hanging braziers |
| 3 | **The Royal Palace of Eternos** (`eterniaPalace`) | the throne room: two thrones, red banners, guards with spears | torches flicker, banners ripple | the palace towers outside the tall windows, a Wind Raider passing |
| 4 | **Man-At-Claws's workshop** (`eterniaWorkshop`) | benches, half-built gadgets, a Battle Ram on blocks | welding sparks, a cog turning | racks of tools and a skylight |
| 5 | **Snake Mountain** (`snakeMountain`) | the peak with a giant stone snake coiled round it, its mouth the door | the snake's eyes glow on and off; bats | the whole mountain and the snake's head at the top, a red sky |
| 6 | **The Vine Jungle** (`eterniaVineJungle`) | hanging vines, giant ferns | vines sway, fireflies drift | the canopy far overhead |
| 7 | **The Mystic Mountains** (`eterniaMysticMountains`) | jagged violet peaks | rocks float and bob in the air | more floating peaks up into a green sky |
| 8 | **Avion** (`avion`) | Stratos's city of the bird people, white towers on clouds | clouds drift past; a bird-man glides | towers above the cloud line, the sun |
| 9 | **Andreenos** (`andreenos`) | the bee people's honeycomb hive | bees zip about; honey drips | the hive's tiers rising |
| 10 | **Darksmoke** (`darksmoke`) | Granamyr's black cliffs, dragon caves | smoke rises, embers float | dragons' silhouettes against the smoke |
| 11 | **Trolla** (`trolla`) | Orko's home: little domed houses on a floating moon | the other moons orbit; sparkles | the sky full of moons |
| 12 | **Mer-Clawd's undersea kingdom** (`eterniaUndersea`) | coral, a sunken arch, seaweed | bubbles rise, fish swim by | the surface light far above |
| 13 | **Beast Island** (`beastIsland`) | foggy rocks, twisted trees, a smoking volcano | fog rolls, red eyes blink in the dark | the volcano's peak and its smoke |
| 14 | **The Temple of Shokoti** (`shokotiTemple`) | the pyramid temple in the desert, a gold idol | heat shimmer; the idol's eyes glow | the pyramid's tip and the stars |
| 15 | **The Fright Zone** (`frightZone`) | the Horde's fortress: smokestacks, dead trees, the bat emblem | smoke belches, red windows flicker | the fortress's tower and the bat emblem high up |
| 16 | **Bright Moon** (`brightMoon`) | Glimmer's crystal palace, a huge moon behind | the crystals twinkle | the palace spires and the moon |
| 17 | **The Whispering Woods** (`whisperingWoods`) | the rebels' forest of giant trees | leaves fall; Loo-Kee peeks out from behind a trunk now and then | tree trunks up into the canopy |
| 18 | **The Crystal Castle** (`crystalCastle`) | Light Hope's castle of crystal on a hill | a rainbow column of light inside | the castle's peak, beams of light |
| 19 | **Mystacor** (`mystacor`) | Castaspella's city of sorcerers, buildings on floating rocks | the islands bob; magic sparks | more islands up the sky |
| 20 | **Castle Chill** (`castleChill`) | Frosta's ice palace, icicles | snow falls | the ice towers and the aurora |
| 21 | **Earth, a small town at night** (`eterniaEarthTown`), from the 1987 film | a little American main street after dark: a diner with a neon sign, a music shop window full of keyboards, the high school across the road | the neon flickers; now and then the Cosmic Key's portal shimmers open in the alley and closes | a water tower against a starry sky, one star brighter than the rest (Eternia) |

Interiors (the chamber, the palace, the workshop) sit among plenty of outdoor scenes, and the palettes change a lot: Greyskull's dusk, the jungle's greens, Snake Mountain's reds, the undersea blues, Etheria's pastels, the Fright Zone's grey and red, and the Earth town's streetlight orange and neon pink against a navy night.

**Homes:**
- He-Clawd, the Sorceress, Battle Kat: Castle Greyskull (the Sorceress in her chamber).
- The royal family, Addam, Cringer, Teelah, Orkko and the Masters with no realm: the Royal Palace. Man-At-Claws, Roboto and Snout Spout: the workshop.
- Stratos: Avion. Buzz-Off: Andreenos. Granamyr: Darksmoke. Moss Clawd, Clawfist: the Vine Jungle. Zodac, Sy-Klawne: the Mystic Mountains. Orkko also counts Trolla as home.
- Skeleclawd and the Evil Warriors, Jitsu included: Snake Mountain (Mer-Clawd in the undersea kingdom; Beast Clawd and Panthor on Beast Island; Kobra Khan and King Hiss in the Vine Jungle; Count Marzo and Shokoti at the temple).
- The Horde: the Fright Zone. Horde Prime appears there too.
- The Great Rebellion: the Whispering Woods. Glimmer and Angella: Bright Moon. Light Hope, She-Clawd, Swift Wind: the Crystal Castle. Clawstaspella: Mystacor. Frosta: Castle Chill. Mermista: the undersea kingdom. Sea Hawk: the Whispering Woods (his ship moors on the coast).
- The film's cast: the Earth town. Gwildor, and the mercenaries sent after his key (Blade, Saurod, Karg and the Dark Troopers). Queen Marlena also counts it as home, since she came from Earth.

## Mechanics that make it its own universe

1. **Rides.** These replace ships flying in:
   - **Eternia's heroes, Gwildor included:** the Wind Raider (green and orange, with its tail fin) swoops in and lands.
   - **She-Ra and the rebels:** Swift Wind flies in with a rider on his back.
   - **Skeleclawd and the Evil Warriors, Jitsu and the film's mercenaries included:** the Roton rolls in, its blades spinning.
   - **The Horde:** a bat-winged Horde skiff. Hordakk himself arrives as a rocket (he turns into one in the show) and turns back into himself on landing.
2. **The transformation, which is Eternia's regeneration: "By the power of Greyskull!"** When a Claude Code or pi session led by one of these compacts its context, they change into their other self:
   - **Prince Addam → He-Clawd:** he raises the sword, lightning hits it, a white-out, and He-Clawd stands there. "I have the power!"
   - **Cringer → Battle Kat:** He-Clawd's stray bolt hits him, and he grows armour.
   - **Princess Adorra → She-Clawd:** "For the honour of Greyskull!", a gold-and-rainbow spiral.
   - **Spirit → Swift Wind:** wings and a horn appear in a rainbow.
   - The next compaction changes them back, with a soft glow (no lightning). It's the secret identity: he can't stay He-Clawd forever.

   Nobody else changes. Decided: these are **two characters per pair**, each with its own id, and compaction swaps one for the other.

   **The secret identity rule (decided): a pair is never on stage at once.** Prince Addam and He-Clawd are never both on screen, nor Adorra and She-Clawd, Cringer and Battle Kat, or Spirit and Swift Wind. The engine already has this rule for Clawd of the Rings (Gandclawd the Grey and the White, Arrogorn and Stride-r, Sarumanual and Sharkey, Sourun and the Necro-maintainer): `Universe.guises` (`Universe.swift:70–78`), "one character in two guises, as global ids: never on screen together". So the four pairs go in `guises`, as global ids from the table rows (0-based enum ids, heroes offset by `StatusStore.heroBase`):
   - He-Clawd and Prince Addam: hero rows #1 and #3, enum ids 0 and 2;
   - Battle Kat and Cringer: rows #4 and #5, ids 3 and 4;
   - She-Clawd and Princess Adorra: rows #23 and #24, ids 22 and 23;
   - Swift Wind and Spirit: rows #26 and #25, ids 25 and 24.

   That gives the rule for free, through code that's already there:
   - **New sessions:** `nextLeader` (`StatusStore.swift:476`) rules out the other guise of every leader and agent on screen (`Roster.ruledOut(by:)`, `Universe.swift:143–145`), and `pickLeader` (`:519`) drops them from the pool.
   - **New agents:** `nextAgentCast` (`:504–506`) does the same against `onScreen`, which covers both session leaders and agents.
   - **The backstop:** `snapshot` (`:762–789`) shows whoever comes later as someone else on the same side, the same someone on every refresh, for the cases the casting can't see coming (the universe switched with sessions open).
   - `Roster.recast` (`Universe.swift:153`) keeps to it too, though no Eternia character is homebound.

   **How the transformation works in the engine.** `guises` only keeps the pairs apart; nothing in the engine turns one guise into the other (Clawd of the Rings never swaps: Gandclawd is cast as the Grey or the White and stays that way). So the swap is the one new piece, and it reuses Doctor Clawd's `PreCompact` path:
   - **Which pairs swap:** derived from `guises`, not a second map. The flag `guisesSwapOnCompaction` (`self == .eternia`, next to `regenerations` at `Universe.swift:100–102`) says this universe's guises swap on compaction, so Clawd of the Rings' pairs never do. The other self is `Universe.of(leader).guises.first { $0.contains(leader) }`, minus the leader.
   - **The swap:** in `StatusStore`'s `PreCompact` case (`:336–349`), after the abductee check (`:341`): if the leader's universe has the flag and the leader has another self, set the session's leader to it and stamp the time (a new `transformed` field, or `regenerated` reused if the overlay can tell them apart by universe).
   - **Not when the other self is on stage:** if the other self already leads another session or works as an agent, the lightning plays and the leader stays as they are. Nobody ever meets their own secret identity. The existing code doesn't give this: Doctor Clawd's regeneration (`:344`) only skips faces leading *other* sessions, and ignores agents. Normally the casting means the other self can't be on stage at all while this one leads, so the check only matters after a universe switch, but without it the `snapshot` backstop would turn the newly swapped leader into a stand-in. The check: the other self isn't among the other sessions' leaders or any agent's cast (`a.cast ?? heroBase + a.character`), each through `s.roster.adopt`. `ruledOut(by:)` can't be used as it is here, since the session's own leader would rule out its own other self.
   - Its own effect in `EterniaPower.swift`, drawn where the overlay draws Clawdberg's OutaTime (`Overlay.swift:1271`).

   Helpers in `Preview` and `Transitions` that pick casts directly don't need the rule; it's a casting rule, not a drawing one.
3. **Habits:**
   - **Orkko's magic goes wrong** now and then: a rain cloud over his own hat, a rubber fish, his scarf tangling him up.
   - **Skeleclawd's retreat:** when he loses a fight he vanishes in a purple puff with "I'll get you for this, He-Clawd!" (hooked into the overlay's tick the way Clawdberg's Indy moment is, `Overlay.swift:1143`).
   - **Cringer hides** behind the nearest hero when a villain is on stage.
   - **Loo-Kee hides** behind scenery and peeks out.
   - **Imp** turns into an object for a few seconds.
   - **Two Bad's** heads argue when idle.
   - **Stinkor's** cloud makes characters near him shuffle away.
   - **Gwildor** ducks behind the nearest hero when a villain is on stage, clutching the Cosmic Key.
   - **The Dark Troopers** march in step when more than one is on stage.
4. **The moral (decided).** Every Filmation episode ended with a character stepping forward to give the audience a short lesson. Here, when a session finishes its work, its leader **now and then** steps forward and gives one in a speech bubble, in the Filmation voice with a coding twist. It's short and rare, so it stays a treat rather than chatter:
   - **When:** on `Stop` (the session has finished and gone idle), about one finish in eight, and never twice within half an hour for the same session.
   - **Who:** heroes only (Skeleclawd doesn't do lessons). Orkko, the Sorceress and Man-At-Claws get the most.
   - **Engine:** a small change. `StatusStore` rolls the dice on `Stop` and stamps the session with a `moral` time. The overlay shows the line in the done state through the callout bubble (`Overlay.swift:1339`) for about four seconds, the leader facing the front.
   - **The lines** (about ten, written so no single one gets stale):
     - "Remember, kids: always write your tests!"
     - "Remember, kids: read the error message before you ask for help."
     - "Sharing your code is good, but never share your passwords!"
     - "Commit before you refactor. Even He-Clawd saves his work."
     - "Never run a script from a stranger without reading it first."
     - "Nobody's code is perfect. Even Man-At-Claws asks for a review."
     - "Bullies force-push. Friends open a pull request."
     - "Stuck on a bug? Take a break. It'll still be there, and so will you."
     - "Orkko learned today that magic numbers cause trouble. Give them names!"
     - "Back up your files. Castle Greyskull didn't last this long by luck."
5. **Practice drills, which are bespoke:**
   - He-Clawd lifts a boulder over his head and puts it down;
   - Teelah spins her staff through a kata;
   - Man-At-Claws tinkers (sparks fly);
   - Orkko practises a trick, and juggles three glowing balls until one turns into a fish;
   - Ram Clawd charges a wall and bounces off;
   - Bow shoots at a target;
   - Jitsu chops a stack of planks;
   - Gwildor tunes the Cosmic Key, one note at a time;
   - Hordakk's Horde Troopers drill in step;
   - Skeleclawd practises his cackle on Screeech.

   **No meditation float** (`Drills.swift:54`). Orkko already floats; nobody in the show sits cross-legged in the air.

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one.

1. **Skeleton:**
   - the universe case, theme and Universe wiring;
   - He-Clawd, Orkko and Skeleclawd (the first cases of the enums);
   - Castle Greyskull, the menu icon, HEM's costume, the saver option and Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with plain wipes for now (`ComicTransition.pick` returns nil for it).
2. **Core ensemble.** About 38 characters:
   - heroes 1–16 (the Masters up to Clawfist) and She-Ra's core: She-Clawd, Adorra, Spirit, Swift Wind, Bow, Glimmer, Madame Razz, Kowl;
   - villains: the Evil Warriors 1–8 and the Horde's core: Hordakk, Shadow Weaver, Katra, Scorpia, Mantenna, plus the three agent-only;
   - 8 places (Castle Greyskull, the palace, the workshop, Snake Mountain, the Vine Jungle, the Fright Zone, the Whispering Woods, the Crystal Castle), with the nemeses for these.

   It's fine to commit the enum cases first, as stand-ins, and draw them in a second commit.
3. **Rest of the cast and places.** Up to 85 characters and 21 places, with every home filled in: the rest of the Masters, the rebels and the Horde, then the appended five (Jitsu, Blade, Saurod, Karg, the Dark Trooper) and Gwildor, and the Earth town. Ends with **the character audit**: every weapon, shot, magic colour, motion, signature and callout checked against the show, and a table of only the mismatches.
4. **Mechanics:** the rides, the transformation and the secret identity rule, the habits (Skeleclawd's retreat included), the moral, the bespoke drills.
5. **Transitions:** the twelve `EterniaTrip`s and the stone caption (see below).
6. **Docs and release:**
   - the README, roster and location sheets (`roster-clawds-of-the-universe.png`, `places-clawds-of-the-universe.png`), a desktop line-up (`eterniaLineup`) and a social preview;
   - `llms.txt`, and a `CHANGELOG.md` entry each phase;
   - a trailer, `REEL=eternia`, opening on "By the Power of Greyskull" as its title sequence.
   - **Needs your OK first, since it's public:** a showcase repo and a cask in `release.sh` (`write_cask`, the `others` list and its `preflight_steps` universe preset).

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

## Polish pass (after phase 5, before phase 6)

The weak-spot list is kept here as the phases go: anything that doesn't read in the Preview sheets (a prop too small, an outline gap, a bare area on the screen saver, a caption too small at window size). It's fixed in one go after the transitions, before any docs, sheets or the trailer are rendered, split by file across helpers in worktrees, with before-and-after renders as the approval gate.

Spots to watch from the start:
- He-Clawd, Faker and Prince Addam side by side; She-Clawd and Adorra side by side.
- The scaly greens (Mer-Clawd, Kobra Khan, Whiplash, Saurod) in one sheet.
- Clawfist's and Jitsu's big hands: silver against gold must read at a glance.
- Gwildor's Cosmic Key: a few pixels, so its lights need to be bright.
- Man-E-Claws's and Tri-Klawps's turning drums: a few pixels each, so the faces and eyes must be bold.
- Orkko's eyes in the dark under his hat; Loo-Kee's size as an agent.
- Light Hope and Horde Prime: neither has a body, so each must still read as a character on Clawd's legs (a rainbow robe; a smoke cloak with the hand).

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` before calling a phase done (dense drawing code can trip Swift's type-checker).
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "He-Clawd"`;
  - `build/preview fight out.png "He-Clawd" "Skeleclawd"`;
  - `build/preview place out.png "Clawds of the Universe"`;
  - and the batch sheets, one per Art file. Look at every PNG for lookalikes, inside the universe and against the seven others.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> castleGreyskull frightZone` (an Eternia-to-Etheria trip, so the portal shows).
- **In the app:**
  - Settings → Universe → Clawds of the Universe: new sessions are heroes, subagents can be villains or small fry.
  - The screen saver's Options include it.
  - Random and Clawd Royale reach it.
- **The transformation:** `/compact` in a Claude session led by Prince Addam (he becomes He-Clawd), then again (back to Addam). Check the secret identity rule: with Addam leading one session, start a second and spawn agents, and He-Clawd must never appear (the `guises` casting). For the guard on the swap, switch the universe to Clawds of the Universe with sessions open so that He-Clawd and Addam both come through `adopt`, then `/compact` Addam's session: he should only play the lightning.
- **The moral:** finish a few sessions led by heroes and check one in eight or so ends with a line, never from a villain, never twice in half an hour.

## Transitions (`EterniaTrip`, 12)

Each is weighted by who is on screen and where, like `DoctorTrip`.

**Style.** Everything is drawn in the app's pixel art, not painted. The palette is Filmation's: flat, saturated cel colours with dark outlines, painted dusk skies of purple, orange and teal, Eternia's earthy greens and sandstone, Etheria's pinks and lavenders, and the villains' purples and sickly yellows (Skeleclawd) or black, grey and red (the Horde). No glossy or neon effects; lightning is chunky white-gold pixels.

**Ending.** Every transition ends with a **stone caption**: the new place's name in chunky carved-stone letters, rising into the corner with a little dust, the way Eternia's places look hewn from rock. These are our own letters, not the show's logo.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **By the Power of Greyskull** (the signature opening) | Dusk; Castle Greyskull in silhouette. A hand raises a sword against the sky, lightning forks down into its tip, the sword blazes, bolts crackle out to the edges and the screen whites out; it clears on the new place. The longest and rarest. | He-Clawd, Prince Addam; Castle Greyskull |
| 2 | **The Jawbridge** | The scene becomes Greyskull's stone face; the jawbridge drops like a mouth opening, and the new place is through the doorway, rushing up to fill the screen. | the Sorceress, He-Clawd; Greyskull and its chamber |
| 3 | **Zoar's Flight** | A falcon swoops across; its wings sweep over the scene as a wipe, and the new place is behind it. | the Sorceress of Greyskull (`needsOwner`) |
| 4 | **Orkko's Trick** | Orkko waves; a puff of pink and yellow smoke. Two wrong places flash up first (a beach, a field of rubber chickens), "Oops!", then the right one. | Orkko (`needsOwner`) |
| 5 | **The Havoc Staff** | The ram's skull's eyes glow, yellow-and-violet bolts crack the scene like glass, and the shards fall away to the new place. | Skeleclawd, the Evil Warriors; Snake Mountain |
| 6 | **The Crystal Orb** | The scene shrinks into a crystal orb; mist swirls inside, the new place forms in it, and it grows to fill the screen. | Evil-Lynn, Count Marzo; Snake Mountain |
| 7 | **The Wind Raider** | The Wind Raider swoops across trailing cloud, the cloud covers the scene and blows away on the new place. | the Masters; trips between places far apart |
| 8 | **For the Honour of Greyskull** | She-Ra's transformation: a sword held high, a gold-and-rainbow spiral climbs up it and floods the screen, and the colours settle into the new place. Second-rarest. | She-Clawd, Adorra; the Crystal Castle |
| 9 | **The Horde Bat** | The red bat emblem flies at the screen, its wings close over the scene, and open on the new place. | Hordakk, the Horde; the Fright Zone |
| 10 | **Shadow Weave** | Dark crimson strands weave across the scene into a cloth, then unravel strand by strand to show the new place. | Shadow Weaver (`needsOwner`) |
| 11 | **The Portal** | A swirling blue-white tunnel between worlds opens in the middle of the scene and widens; the new place is at its end. | trips between worlds (Eternia, Etheria, the Earth town); Gwildor, whose Cosmic Key opens it |
| 12 | **Light Hope's Rainbow** | A column of rainbow light rises in the middle, splits into prism bands that sweep across, and fades on the new place. | Light Hope, the rebels; Etheria's places |

**Not used:**
- **Battle Kat's leap** overlaps the Wind Raider fly-by and the ride.
- **Snake Mountain's mouth** overlaps the jawbridge.
- **Hordak's rocket** is his ride, not a transition.
- **Filmation's reused stock zooms** read as a plain zoom at pixel scale.
- **The end-of-episode moral** suits a habit better (Mechanics), since it's a line, not a picture.
- **The Cosmic Key** as a transition of its own would be the Portal again; it's folded into the Portal instead.

**Check them** with `Tools/Transitions`, which renders all twelve between two Eternia places.

## Promo

**"By the Power of Greyskull" (#1) is the trailer's title sequence.** `REEL=eternia` opens on it before the scenes, the way Doctor Clawd's trailer opens on its time vortex.

**Intro (~9 s):**
- Dusk over Castle Greyskull, mist in the chasm.
- Prince Addam rides in on a trembling Cringer and stops at the edge.
- He draws the sword and raises it: "By the power of Greyskull!" in a speech bubble.
- Lightning forks down into the blade, the screen whites out in crackling bolts.
- He-Clawd stands where Addam was, sword high; Cringer has become Battle Kat, who roars. "I HAVE THE POWER!"
- The title, CLAWDS OF THE UNIVERSE, rises in carved-stone letters (our own, not the logo), and the camera plunges through the jawbridge into white.

**Set piece (~9.5 s):**
- Snake Mountain under a red sky. Skeleclawd, Beast Clawd and Trap Claw roll out on the Roton.
- They pull up at Greyskull's jawbridge. Skeleclawd raises the Havoc Staff.
- Orkko pops up to help: his spell misfires and a rain cloud opens over Skeleclawd.
- He-Clawd and Battle Kat leap in, He-Clawd lifts the Roton over his head and the crew scatters.
- Skeleclawd vanishes in a purple puff: "I'll get you for this, He-Clawd!"
- Orkko turns to the camera: "Remember, kids: always write your tests!" (the moral).

**The rest:**
- **desktop:** `brawl(ctx, .eternia, …)` with "The battle for Greyskull, right on your desktop."
- **status:** He-Clawd working, Cringer waiting (hiding), Orkko erroring ("Oops!"), Teelah done ("Where's Adam?").
- **agents:** "Every subagent gets to be a Master of the Universe."
- **window:** `windowShot(ctx, .eternia, …, at: .castleGreyskull)` with "It has the power."
- **endcard:** Castle Greyskull, the crew lined up, CLAWDS OF THE UNIVERSE lands in stone letters, then the shared lines.

**Sound:** a brassy, heroic synth march in the spirit of the 80s cartoon but **our own notes**, a big thunderclap on the lightning, a sword shing as the title lands, Skeleclawd's cackle as a pitched-down blip, and a bright fanfare sting on the end card.

**Playground prompts** (`Overlay.swift:868`):
- "Skeleclawd stole the castle keys: rotate the secrets"
- "Orkko broke the build again, find out what he did"
- "By the power of Greyskull, fix the flaky test"
- "Gwildor's Cosmic Key plays the wrong notes: fix the tune parser"
- "Hordakk needs a dashboard for the Fright Zone's smokestacks"

## Decisions (2026-10-16)

1. **Name: Clawds of the Universe.** The code naming stays as it was: `case eternia`, key `"eternia"`, folder `Sources/App/Universes/Eternia/`, prefix `Eternia…`, branch `he_man`, `REEL=eternia`. This file keeps its old path.
2. **Scope: the 1983–1987 cast.** The 1983 Filmation cartoon, She-Ra (1985) and the 1987 live-action film. The film adds Gwildor (hero 43), the villains Blade (38), Saurod (39) and Karg (40), appended after Jitsu, with the Dark Troopers (41) as agent-only small fry, and a 21st place, the small Earth town at night. Nemeses: Gwildor ↔ Karg, Snout Spout ↔ Saurod, Stonedar ↔ Blade. Julie, Kevin and Detective Lubic stay out. The 2002 series and Revelation stay out; the 2002 Snake Men could come later as an add-on, appended to the enums.
3. **The transformation: approved.** Two characters per pair (Prince Addam/He-Clawd, Adorra/She-Clawd, Cringer/Battle Kat, Spirit/Swift Wind), swapping on compaction. **The secret identity rule: approved.** A pair is never on stage at once, through `Universe.guises` and a guard on the `PreCompact` swap (see Mechanics and the 2026-10-17 note below).
4. **The moral: approved.** Short and rare end-of-episode morals when a session finishes, heroes only, in the Filmation voice with a coding twist. A small engine change: a roll on `Stop` and a line in the done state (see Mechanics).
5. **Swaps:** none beyond item 6.
6. **Katra's panther form is dropped; Panthor stays.** Jitsu (villain 37), Skeletor's martial artist with the golden chopping hand, comes in from the bench, at home in Snake Mountain, facing Clawfist (Two Bad loses that pairing).
7. **Names:** the plain ones (Bow, Glimmer, Kowl, Webstor, Whiplash, Faker) stay as they are.

**2026-10-17: uses `Universe.guises`, decided by the user.** The four pairs (Prince Addam/He-Clawd, Adorra/She-Clawd, Cringer/Battle Kat, Spirit/Swift Wind) go in the engine's existing `guises`, which already keeps Clawd of the Rings' pairs off the stage together, instead of a new `transformations: [Int: Int]` map and changes to `pickLeader` and `nextAgentCast`. What's left to build is the compaction swap: the `guisesSwapOnCompaction` flag, the `PreCompact` branch with its guard against the other self being on stage, and its effect.

**The counts now:** 44 heroes (42 who lead, Loo-Kee, HEM) and 41 villains (37 who lead, 4 agent-only), so 85 in all, with `heroCount` 44 and `villainCount` 41. Agent-only: table rows hero #42 and villains #34, #35, #36, #41 (0-based enum ids hero 41; villains 33, 34, 35, 40). 21 places, 12 transitions, 28 nemesis pairs.

The plan is ready for phase 1 when you say start.
