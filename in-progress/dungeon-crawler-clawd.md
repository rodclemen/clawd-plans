# Plan: a new universe, Dungeon Crawler Clawd (Dungeon Crawler Carl parody)
<!-- track: repo=rodclemen/clawd-clash branch=dungeon-crawler-clawd folder=DungeonCrawlerClawd title="Dungeon Crawler Clawd" source="Dungeon Crawler Carl, all eight books" cast=95 places=20 -->

## Context

Clawd Clash has seven universes on `main` (b5c6ab8, 2026-10-18). This plan adds a parody of Dungeon Crawler Carl: **all eight books** (through *A Parade of Horribles*). The Peacock series was ordered in June 2026 but hasn't aired, so the books, the wiki's descriptions and the official art are the only visual source. It clears the threshold comfortably, and its cast is the most varied in the app: a cat, a raptor, a goat on a hellgoat, a lava giant, a fish in a water helmet, a crab-taur talk-show host.

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
| Harry Clawder (planned)              |     45 |       40 |    85 |     22 |          12 |
| **Dungeon Crawler Clawd (proposed)**    | **51** | **44** | **95** | **20** | **12** + the System box |

(heroCount includes HEM and the agent-only Garret; villainCount includes the five agent-only small fry.)

- **Viability: comfortably over.** 49 drawn heroes and 39 drawn villains. The early worry that heroes would be thin didn't survive the research: the allies run well past Carl's crew.
- **Name: Dungeon Crawler Clawd** (chosen on 2026-10-18 as Dungeon Clawd Carl, renamed on 2026-10-22). The other alternatives were Dungeon Clawler Carl and The Royal Clawd of Princess Donut.
- **Code naming** avoids the franchise's trademark:
  - `case crawl` with key `"crawl"`.
  - Folder `Sources/App/Universes/DungeonCrawlerClawd/`, file prefix `Crawl` (`CrawlRoster.swift`, `CrawlHeroes1.swift`, `CrawlWipes.swift` …). No file in the repo uses `Crawl` as a prefix today. Top-level names start with `crawl` or are `private`, as `scripts/pr-guard.py` asks. Star Clawds' sandcrawler has locals called `crawlerLights` and `crawlerHigh`; don't name anything `crawler…`.
  - Place keys are prefixed `crawl…` (`crawlSafeRoom`); none clash with `main` or `buffy`.
  - Branch `dungeon-crawler-clawd`. Trailer `REEL=crawl`.
- **Raw value: next free when the build starts.** Check `main`, the open branches (`buffy` has `slayer = 7`), Henrik's fork (HEM42/clawd-clash) and the other plans (Harry Clawder's `wizards` among them). Read other branches with `git show <branch>:Sources/Shared/Universe.swift`, never by switching. Ids are rawValue*1000 and permanent.
- **Naming style:** everyone keeps the on-page name. The books' names are already jokes (Princess Donut, Gluteus Maxx, Splash Zone), and a pun on top would be forced. No narrators' or actors' names (Donut's announced voice actor included), and no character named after a real person.
- **Size:** 95 characters and 20 places, in the guide's 70 to 100 target.

### How the cast is split

Heroes are the Royal Court of Princess Donut, Meadow Lark, the allied crawlers, the Desperado Club's bouncers and dancers, the NPC allies, and the show's friendlier side (Odette, Zev, the anarchists, Princess Formidable). Villains are the bosses, the player killers and rivals, the Syndicate's showrunners and liaisons, and the gods. The grey ones:
- **Lucia Mar → villain.** She's a child, but the threat, never in harm's way, and drawn as her armoured or skull-faced adult Lajabless form.
- **Odette, Zev, Quasar → heroes**: they work for the show but side with Carl.
- **Emberus → villain**, Carl's patron god but a cruel one.
- **Tsarina Signet → villain.**
- **Juice Box → hero.**

### Tone: what's kept, softened and left out

The books are profane, gory and bawdy. Clawd Clash is a desktop toy, but at 72×52 pixels much of the bawdiness reads as plain comedy, so:
- **Kept:** the Desperado Club's dancers (Gluteus Maxx in his Speedo and hockey helmet, Dong Quixote, Splash Zone, Damascus Steel, Anaconda), decided by you: at this size it isn't too sexy. The club's stage is called **the Parade** in the app, never by its full name.
- **Samantha** is just a big doll's head with bone-white hair and smeared red lipstick. No barrette slogan, no "love doll". Her callout "I'll kill your mother!" stays, decided by you.
- **Crude item names are dropped:** Donut's crown is just a crown.
- **Left out entirely:** Carl's "You Monster!" goblin-children kill, Yvette's death, Vrah's trophy heads, the demon harem (Gash, Slit, Minge), Juice Box's job, the Hoarder's sores, gore in general.
- **Drawn eerie or sad, never gory:** Heather the Bear (clown hat, tutu, roller skates; no skinless face), the Hoarder, the Reminiscence Hydra (stitched, not raw), Lucia's skull face.
- **Profanity:** callouts stay clean apart from the ones you approved.
- **Lookalikes in Clawd Royale:** Mongo's pink feathers and collar keep him apart from Stevie Clawdberg's raptors; Big Tina's tutu and tiara apart from its T. rex; the Sledge's cowboy hat and boa apart from Bomo; Katia's combat form is pink, never Hulk green.
- **Music:** game-show brass and chiptune in our own notes.

## How a universe plugs in (the folder flow, since 2026-10-19)

Everything is in `Sources/App/Universes/DungeonCrawlerClawd/`, started from the template with `Tools/new-universe.sh DungeonCrawlerClawd Crawl crawl "Dungeon Crawler Clawd" 12` (2026-10-30, number 12 reserved in `NUMBERS` on `main`). Nothing outside the folder changes except `NUMBERS`; the guide's Step 7 and "Your folder" have the layout (`CrawlFacts`, `CrawlRoster`, `CrawlUniverse`, `CrawlHem`, `CrawlIcon`, `CrawlWipes`, `Art/`, `Places/`, `Promo/`). Shared drawing helpers go in `CrawlKit.swift` with `crawl`-prefixed names; never name anything `crawler…` (Star Clawds' sandcrawler has `crawlerLights`).

What the old wiring list asked for now lives in the module and the facts:
- **Facts:** counts from the enums; agent-only Garret (hero 49) and the five small fry (villains 39 to 43); Claude plays the heroes; no guises; the Hoarder (villain 1) homebound at `crawlHoard`; compaction `.away` for the Earth crawlers (see Mechanics).
- **Module:** the monster truck in `rides` and `theme.ride`; New Achievement! as `compactionLook`; the habits through `quirks` where they fit (anything they can't do is an engine request); `drills` for the bespoke drills; `meditation: .never`; the five `playgroundPrompts` below; `transitions` in phase 5.
- **Engine requests**, if any turn up (built on `main` as their own commits first): check in phase 4 whether the fans' viewer ticker, Mongo nipping Donut, the crew jumping at Prepotente's scream and the petty-achievement toasts fit `StageQuirks`.

**Playground prompts** (`Overlay.swift:875`):
1. "Open the loot box the CI left us."
2. "Find the stairwell before the build collapses."
3. "Ping the map for failing tests."
4. "Get Mordecai to brew something for this stack trace."
5. "Ask the System AI why it gave this PR a bronze box."

## Cast

How the engine's weapons map onto the books. Every weapon type the engine has is used, each character with a colour of their own:

| Look | Who |
|---|---|
| **Saber** | Carl's War Gauntlet, swords, axes, maces, fists, claws, bites, chains, the Sledge's and Bomo's stone fists, Gluteus Maxx's butt crush |
| **Energy bolts** | Donut's Magic Missile (hot pink), Sister Ines's thrown white bolts, Rory (blue) and Lorelai (violet), Formidable's arm cannon (blue), Quan Ch (blue), Astrid (red sparkles), the Hydra (shifting colour) |
| **Ice** | Elle's icicles |
| **Notes** (`notes`) | Doctor Bones (gold), Chaco (orange) |
| **Forked lightning** | Ferdinand's turban (yellow), Dismember (sickly violet), Eris (magenta) |
| **Steady ray** | Big Tina's star wand (red); Emberus (orange, `thick`) |
| **Beam** | Splash Zone's water jet (blue) |
| **Waves** (`waves`) | Louis's Cloud of Exhaust (grey-green), the Krakaren's mist (green), Agatha's spray paint (silver) |
| **Rings** (`rings`) | Queen Imogen's telekinesis (gold) |
| **Spell** (`spell`) | Miss Quill (sickly green), Tsarina Signet's blood and ink (red-black) |
| **Touch** (`touch`) | Shi Maria's illusions (rainbow), Harbinger's dread (red) |
| **Thrown** | Mordecai's potions, Zhang's rocks, Rosemarie's coins, Rosetta's bombs, Tipid's poison vials, the Hoarder's Scatterer bugs, Mrs. Ghazi's sand, HEM's slingshot |
| **Fire** | Tserendolgor, Pater Coal, Amayon |
| **Arrow** | Langley, Osvaldo, Vrah's crossbow |
| **Bullet** | Florin's shotgun |

- **Motion:** `fly` for Ruckus, Quan Ch, Vrah, Astrid; `hover` for Elle.
- **`bulk`:** Katia (combat form), Chris, the Popov brothers, the Sledge, Bomo, Orthrus, Maestro, the Hoarder, the Krakaren, Ball of Swine, Big Tina, Shi Maria, Amayon, the Hydra, Emberus, Grull. **`armoured`:** Chris, the Sledge, Bomo, Damascus Steel (metal skin), Ruckus.
- Everyone is Clawd in costume on Clawd's four legs: Donut, Mongo, Ferdinand, Orthrus and the creatures included, which suits them; Odette's crab legs and Grull's horse body are drawn over the four.

### Heroes (51)

Enum order is the table order. Carl, Donut and Mongo come first for the skeleton.

**The Royal Court (8)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Carl | boxers, leather jacket with one sleeve burnt off, bare feet, toe rings, war gauntlet | War Gauntlet punch (saber) | lights a stick of goblin dynamite and lobs it off-screen; boom | "Donut!" |
| 2 | Princess Donut | tortoiseshell Persian, flat face, crown | Magic Missile (energy, hot pink) | poses for the cameras: a flash, and a viewer counter ticks up | "Carl!" |
| 3 | Mongo | pink-feathered raptor, a red feather stripe, black collar | claws (saber) | screeches and bobs his head | none |
| 4 | Katia Grim | pale, purple mohawk | fists in her combat form (saber, `bulk`) | swells into her hulking pink eight-foot form and back | none |
| 5 | Mordecai | golden-brown eagle Skyfowl, black vest, blue trousers, sandals | potions (thrown, green flasks) | stirs a bubbling flask, and it puffs | none |
| 6 | Samantha | a big doll's head: bone-white hair, wide unblinking eyes, smeared red lipstick, little fangs | bite (saber) | rages, and her hair catches fire for a moment | "I'll kill your mother!" |
| 7 | Prepotente | upright goat in a dark robe, curled black nails, riding Bianca (black, black-flamed, winged) | axe (saber) | throws his head back and screams | "AAAAAH!" |
| 8 | Louis | leather jacket over a "Donut Holes" fan T-shirt | Cloud of Exhaust (`waves`, grey-green) | takes a swig and hiccups | none |

**Meadow Lark (4)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 9 | Elle McGibbons | tiny pale-blue Frost Maiden, wild white hair, anti-slip socks (`hover`) | icicles from her palms (ice) | a little snow flurry swirls round her | none |
| 10 | Imani | skull face paint, monarch butterfly wings, longsword | longsword (saber) | her wings beat and glow (a buff) | none |
| 11 | Brandon Andrews | heavy winter jacket, a huge glittering hammer | hammer (saber) | lightning crackles off the hammer as he swings it onto his shoulder | none |
| 12 | Chris Andrews | black-and-red lava rock giant, metal skullcap (`bulk`, `armoured`) | fists (saber) | the lava cracks glow bright and fade | none |

**Crawlers (16)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 13 | Bautista | shirtless tiger-man, shaggy tail, bare clawed feet | orange-glowing curved sword (saber) | summons a little plushie that waddles about and vanishes | none |
| 14 | Tran | tired-looking man with a curved sword; later in Katia's mechanical crab rig | curved sword (saber) | tugs at his shirt, as if checking whether it's red | "Do you own a red shirt?" |
| 15 | Florin | crocodile, combat gear | endless shotgun (bullet) | racks the shotgun | "Good." |
| 16 | Ifechi | bald, red shirt, vest, Red Cross medic bag | none (healer) | opens the medic bag, and a green heal glows | none |
| 17 | Li Jun | street monk | kung fu (saber) | a flying spin kick | none |
| 18 | Li Na | tall pale Changbi demon, small black horns, wide mouth | chains (saber) | whirls a chain overhead | none |
| 19 | Zhang | warehouse worker, Cape of Odds | Earth Mover rocks (thrown, brown) | stamps, and the ground heaves | none |
| 20 | Sister Ines | cat-girl nun (dark brown Havana Brown), cloak, bracers, glowing trident | white bolts thrown like a baseball (energy, white) | recites a poem, and sparkles curl from the words | none |
| 21 | Tserendolgor | German Shepherd dog soldier, Vietnam-era helmet with ear holes, paw-print locket | Crisper fire (fire; re-check the class at the audit) | Garret rolls up giggling, and she pats him | none |
| 22 | Langley | stocky, greying blond, ice-blue eyes | bow (arrow) | nocks and sights | none |
| 23 | Gwendolyn Duet | chainmail, spear | spear (saber) | plants the spear | none |
| 24 | Jurgen | huge blond barbarian | fists (saber) | talks to his absent wife, and a little heart floats up | none |
| 25 | Osvaldo | barely five feet, dyed red hair, stone hawk Gimli on his shoulder | bow (arrow) | Gimli swoops, and a bug turns to stone | none |
| 26 | The Popov brothers | one seven-foot grey two-headed body, one head in a knitted beanie (`bulk`) | meteor hammer (saber) | the two heads argue | none |
| 27 | Miriam Dom | robe, hooked shepherd's staff | staff (saber) | a little goat trots past | none |
| 28 | Juice Box | changeling: a gum-chewing blonde; now and then her ratkin form in a purple jumpsuit | none | blows a bubble and flips into her ratkin form and back | none |

**The Desperado Club and its dancers (9)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 29 | The Sledge | seven-foot stone bouncer, tuxedo, cowboy hat, pink feather boa (`bulk`, `armoured`) | fists (saber) | adjusts the cowboy hat | "He buy spell with own money." |
| 30 | Bomo | stone bouncer in a tuxedo, no hat (`bulk`, `armoured`) | fists (saber) | cracks his knuckles | none |
| 31 | Doctor Bones | skeleton DJ with a gold crown | music (`notes`, gold) | scratches a record on a little turntable | none |
| 32 | Splash Zone | otter water mage, leather vest, little red boots | water jet (beam, blue) | "the Wet Spot": a spray of water round him | none |
| 33 | Gluteus Maxx | short, hairy, Speedo, hockey helmet | butt crush (saber) | flexes | none |
| 34 | Dong Quixote | elderly dancer with the heart of a knight | sword (saber) | sweeps a gallant bow | none |
| 35 | Damascus Steel | smoky Ifrit, white eyes, stubby goat horns, tattoos (`armoured`: metal skin) | fists (saber) | smoke curls off him | none |
| 36 | Anaconda | purple snake-man, shirtless, slit eyes | fists (saber) | a dancer's spin | none |
| 37 | Rosemarie | elderly dwarf with Bernie the mole on her shoulder | gold coins (thrown, gold) | flicks a coin at someone's eye | none |

**NPC allies (5)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 38 | Rory | goblin shamanka, black robe, forked tongue, pineapple-topped staff | anguish magic (energy, blue) | twirls the pineapple staff | none |
| 39 | Lorelai | goblin shamanka, piercings, bone necklace, pineapple-topped staff | anguish magic (energy, violet) | rattles the bone necklace | none |
| 40 | Pater Coal | tiny old cleric, long white hair, red robes | Emberus's fire (fire) | a little flame rises from his palm | none |
| 41 | Edgar | giant talking tortoise | none | pulls out a tattoo gun, and it buzzes | none |
| 42 | Ferdinand | yellow-orange tomcat in a gold turban | turban lightning (forked lightning, yellow) | phase-jumps: blinks out and back | none |

**The show's side (7)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 43 | Odette | crab-taur legs, black mantis helmet with mirrored eyes and huge antennae | none | an ON AIR light glows, and the antennae twitch | none |
| 44 | Zev | small fish alien, round glass helmet of bubbling water, white mesh spacesuit, backpack | none | bubbles rise in her helmet | none |
| 45 | Quasar | grey alien lawyer, huge eyes, bald bulbous head, silly tie | none | his upside-down pineapple tie blinks | none |
| 46 | Rosetta Thagra | bald Crest, a movable blob of hair, pantsuit | bombs (thrown, black) | the hair blob slides across her head and changes colour | none |
| 47 | Tipid | tall leathery Crest, scar across his bald head, sideways grin | poison (thrown, green vials) | the sideways grin, and a thumbs up | none |
| 48 | Princess Formidable | orc princess in a black and orange spacesuit | arm cannon (energy, blue) | the arm cannon powers up with a blue glow | none |
| 49 | Orthrus | huge, floppy-eared two-headed puppy (`bulk`) | bites (saber) | one head sniffs, the other licks | none |

**Agent-only, and HEM**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 50 | Garret (agent-only) | meatball-shaped Tummy Acher, one tooth | bite (saber) | giggles as he rolls |
| 51 | HEM | a crawler's patch jacket, a "Princess Posse" fan sash, a slingshot | slingshot (thrown, grey) | aims the slingshot and grins |

### Villains (44)

Maestro comes first for the skeleton.

**Bosses (20)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Maestro | boar-faced orc, black bristles, one gold tusk, gold chains, pink silk shirt half buttoned (`bulk`) | fists (saber) | a game-show host's grin and a microphone flourish | none |
| 2 | The Hoarder | huge, matted hair, PINK sweatpants, in a heap of junk (`bulk`); homebound in her lair | Scatterer bugs (thrown, brown) | rummages in her trash pile | none |
| 3 | The Juicer | steroid lizard-man, bulging veins, tiny black shorts | fists (saber) | curls a dumbbell | none |
| 4 | Krakaren clone | pink octopus, running mascara, a manager-mom hairdo (`bulk`) | green mist (`waves`, green) | her tentacles wag a finger | "Let me talk to your manager." |
| 5 | Ball of Swine | a rolling pink ball of tuxedoed warthog aristocrats (`bulk`) | rolling crush (saber) | bursts apart into Tusklings and rolls back together | none |
| 6 | Ralph | absurdly cute gerbil | the scream (saber) | its mouth opens wider than its whole body | none |
| 7 | Grimaldi | dwarf ringmaster in a top hat, pale-green vines sprouting from him | vines (saber) | cracks a ringmaster's whip | none |
| 8 | Heather the Bear | clown hat and ruff, pink tutu, roller skates; sad-eerie, not gory | glowing worm-paws (saber) | a wobbly roller-skate twirl | none |
| 9 | Miss Quill | elderly grey Skyfowl, cracked beak, sour face | dark cleric magic (`spell`, sickly green) | stamps a form | none |
| 10 | Big Tina | allosaurus in a pink tiara, feather boa and tutu, with a star wand (`bulk`) | wand (steady ray, red) | a ballerina pirouette | none |
| 11 | Gore-Gore | a train engineer with a second, smaller torso on top, blue warpaint, engineer's cap | four fists (saber) | both torsos flex | none |
| 12 | Dismember | silver-haired elf necromancer | necromancy (forked lightning, sickly violet) | raises a hand, and green wisps rise | none |
| 13 | Queen Imogen | gold-leaf make-up, piled-up hair, colour-shifting gown, claw nails | telekinesis (`rings`, gold) | her gown shimmers through colours | none |
| 14 | Shi Maria | huge spider with a haggard human head and a jewel eye (`bulk`) | illusions (`touch`, rainbow) | the jewel eye flashes | none |
| 15 | Amayon | lava-red demon lord, deer head with a fiery beak, four horns, pig legs (`bulk`) | fire | a column of fire up into the sky | none |
| 16 | The Reminiscence Hydra | stitched fleshy ball on stumpy legs, nine wobbling heads (`bulk`) | each head's attack (energy, shifting colour) | a head pops off and balloons back | none |
| 17 | Mrs. Ghazi | sand ooze | sand (thrown, tan) | slumps into a sand heap and rises | none |
| 18 | Ruckus | clockwork chicken hawk sentinel (`fly`, `armoured`) | talons (saber) | springs wind and clank | none |
| 19 | Denise | a feral goose | honk and bite (saber) | spreads her wings and hisses | "HONK!" |
| 20 | Station Mimic | a treasure chest with teeth | bite (saber) | the lid creaks open and snaps shut | none |

**Player killers and rivals (10)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 21 | Lucia Mar | yellow soccer jersey over silver armour, a mace; her beautiful form flips to her skull-faced one | mace (saber) | flips from beautiful to skull-faced and back | none |
| 22 | Frank Q | purple-skinned elf, Seahawks beanie, black jacket, one hand | battle axe (saber) | none | none |
| 23 | Maggie My | stealth field, black dagger with a purple halo | dagger (saber) | fades into her stealth field and back | none |
| 24 | Hekla | Amazon shieldmaiden, bodybuilder build, sapphire eyes | spear and shield (saber) | raises the shield | none |
| 25 | Eva | green opalescent, four arms, cobra head, twin swords in an X | swords (saber) | all four arms draw | none |
| 26 | Quan Ch | glowing robe, ethereal wings, blue-glowing left hand (`fly`) | blue energy (energy, blue) | the robe lifts him, and the wings flare | none |
| 27 | Burcu | badger-headed swashbuckler | curved sword (saber) | a fencer's salute | none |
| 28 | Agatha | wrinkled, scarves, red-checked trapper hat, shopping cart with a pink flamingo | silver spray paint (`waves`, silver) | sprays a smiley face and cackles | none |
| 29 | Tsarina Signet | luminous scaled skin covered in moving tattoos, glowing yellow hands | blood and ink (`spell`, red-black) | the tattoos swirl | none |
| 30 | Vrah | flying mantis hunter with a crossbow, no trophy heads (`fly`) | crossbow (arrow) | the mandibles click | none |

**The Syndicate (6)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 31 | Stalwart | tall orc, rings on his fists, gold crown | fists (saber) | punches his palm | none |
| 32 | Cascadia | tiny catfish alien with long whiskers and a rebreather, a tequila bottle | none | takes a swig | "Now get out there and kill, kill, kill!" |
| 33 | Loita | fish alien, rebreather round her neck, Bloom badge | none | polishes the Bloom badge | none |
| 34 | Harbinger | tall goat creature, two curled horns, a line of red bug eyes, silky black coat | dread (`touch`, red) | leans in and stares | none |
| 35 | Chaco | wolf-headed, bat-winged, brown and orange checked leisure suit, microphone | Song Bard (`notes`, orange) | runs in, grins with sharp teeth, and announces | none |
| 36 | Astrid | hand-sized fairy in a tuxedo, raven bun (`fly`) | blood boil (energy, red sparkles) | a trail of red sparkles | none |

**Gods (3)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 37 | Emberus | man-shaped mass of orange and red fire, a smoking horn, smoke where his eyes were (`bulk`) | fire (steady ray, orange, `thick`) | flares up, the horn smoking | none |
| 38 | Grull | black bull-headed centaur, gold nose ring, a molten axe (`bulk`) | axe (saber) | snorts steam | none |
| 39 | Eris | blonde, glowing Valkyrie armour, black and white striped long coat | chaos (forked lightning, magenta) | none | none |

**Agent-only small fry (5)**

| # | Name | Look | Weapon |
|---|---|---|---|
| 40 | Scatterer bug | the Hoarder's brown beetle | bite (saber) |
| 41 | Goblin | green, a stick of dynamite | dynamite (thrown, red) |
| 42 | Tuskling | short warthog aristocrat in a tuxedo | none |
| 43 | Pooka | fuzzy goblin-like thing that turns into a goat when hit | butt (saber) |
| 44 | Krakaren cloneling | a little pink tentacle blob | none |

Rows are 1-based; the enum and the ids are 0-based. So Maestro is villain 0, the Hoarder villain 1, the small fry villains 39 to 43, Garret hero 49 and HEM hero 50.

### Nemeses (15)

| Hero | Villain | Why |
|---|---|---|
| Carl | Maestro | Death Watch, and the grenade he bought to kill Carl |
| Donut | Lucia Mar | the insult to her dogs and the fight that followed |
| Mongo | Big Tina | dinosaur against dinosaur |
| Katia | Hekla | Brynhild's Daughters |
| Chris | Maggie My | she rode him like a suit |
| Brandon | Ball of Swine | Meadow Lark's First Floor fight |
| Florin | Queen Imogen | she wore Ifechi's face |
| Prepotente | Harbinger | working to remove him from the crawl |
| Samantha | Shi Maria | "MaeMae" |
| Mordecai | Chaco | Uzzi |
| Zev | Loita | the Bloom |
| Bautista | Grimaldi | the circus that killed his family |
| Sister Ines | Amayon | her charm on him |
| Langley | Vrah | the hunter who took him |
| Formidable | Stalwart | the succession |

**Claude's side:** heroes. **Rivals and guises:** none.

### Left out of the cast

- **Too thin, or overlapping:** Yolanda, Dr. Gracie, Firas, Fitz, Lexis, Bucket Boy, Clay-ton (a third stone bouncer), Corky and Porky, Darla No-Dentures, Grandma Sticky, Tuesday Two For One, Circe Took (too like Vrah), Orren, Hellik.
- **Tone, or a possible real name:** Rude-Dolph, "Author Steve Rowland", the demon harem.
- **The System AI** isn't a sprite: it's the voice of the compaction box, the petty achievements and the finishing touch.

## Places (20)

| # | Key | Place | Still | Moving | Tall (screen saver) |
|---|---|---|---|---|---|
| 1 | `crawlSafeRoom` | **A safe room** (default) | cosy dungeon pub: wooden bar, stools, a chalkboard, a TV on the wall | the TV flickers through the recap episode | stone ceiling, hanging lanterns |
| 2 | `crawlSeattle` | Carl's street, the night of the collapse | wet Seattle street, apartment block, a tree outside the window | rain, and a building slowly sinking into the earth | the apartment tower and night sky |
| 3 | `crawlCorridor` | First Floor tunnels | rough stone corridor, torches, a goblin graffiti tag | torches flicker, a System box blinks | the vaulted roof |
| 4 | `crawlGuild` | Mordecai's Tutorial Guild | alchemy bench, potion shelves, his cot | flasks bubble | shelves of jars and books |
| 5 | `crawlHoard` | The Hoarder's lair | a mountain of Earth junk: tyres, bags, a pink flamingo | flies buzz, a bag shifts | the junk pile towering |
| 6 | `crawlGym` | The Juicer's gym | weight racks, a turnstile, a "GAINS" poster | the lights pulse red when the boss music hits | the tall ceiling and banners |
| 7 | `crawlPersonal` | The Royal Court's personal space | couch, food synthesiser, Mongo's pet carrier, Donut's hat stand | the synthesiser's light blinks | a loft with the training room door |
| 8 | `crawlDesperado` | The Desperado Club casino | neon purple and gold, a Wheel of Fortune, velvet ropes | the wheel spins, the neon buzzes | the club's floors stacked above |
| 9 | `crawlParade` | The Parade (the club's dancers' stage) | stage, light rig, Doctor Bones's DJ booth, a disco ball | the disco ball scatters light | the light rig and balconies |
| 10 | `crawlOverCity` | The Over City | Skyfowl settlement, perches, the admin building | birds flit between perches | towers in the clouds |
| 11 | `crawlCircus` | Grimaldi's circus tent | striped big top, the centre ring choked with pale-green vines | the vines creep and sway | the tent's peak and trapezes |
| 12 | `crawlTangle` | Iron Tangle station | platform, tiled walls, a line map, the third rail | a train rushes through | girders and signs |
| 13 | `crawlHumpTown` | Hump Town | desert inn (the Toe), resting camels, a red sun | heat shimmer, a camel's tail swishes | the red sun over the dunes |
| 14 | `crawlCastle` | The High Elf castle ballroom | the Butcher's Masquerade: chandeliers, marble floor, masks on the walls | chandeliers glint, a masked couple waltzes far behind | high windows |
| 15 | `crawlHunting` | The Hunting Grounds | forest, ferns, a dinosaur footprint | ferns stir, a raptor's head peeks out | giant trees, a smoking volcano far off |
| 16 | `crawlStudio` | Odette's After Hours studio | cream sofa, the mantis set, studio lights | ON AIR glows, an APPLAUSE sign blinks | the lighting gantry |
| 17 | `crawlDeathWatch` | The Death Watch stage | Maestro's garish red and gold orc game show, a cage, a big wheel | spotlights sweep | the skull arch over the set |
| 18 | `crawlHavana` | Havana, Eighth Floor | pastel streets, vintage cars, the FOCSA tower | a column of demon fire far off, heat haze | the FOCSA tower |
| 19 | `crawlLarracos` | Larracos, Faction Wars | trenches, banners, a castle on the hill | smoke drifts, flags snap | the castle and siege towers |
| 20 | `crawlTemple` | Emberus's High Temple | molten floor, a boiling marble fountain, a charred stump | lava glows, the fountain boils | the smoky dome |

**Kept apart:** the safe room (warm wood) and the casino (neon purple); Odette's studio (calm cream) and Death Watch (garish red and gold); the corridor (bare stone) and the Hoarder's lair (junk).

**Left out:** the Necropolis of Anser and the other Fifth Floor bubbles (Hump Town stands for that floor), Shi Maria's swamp (she lives in Havana), the Nothing (no clear look), the Tenth Floor (too new to picture well).

### Homes

| Place | Heroes | Villains |
|---|---|---|
| Safe room | Tran, Florin, Ifechi, Langley, Gwendolyn, Jurgen, Osvaldo, HEM | |
| Carl's street | Ferdinand | Frank Q, Maggie My |
| First Floor tunnels | Elle, Imani, Brandon, Chris, Rory, Lorelai | Ball of Swine, Ralph, goblin, Tuskling |
| Tutorial Guild | Mordecai | |
| Hoarder's lair | | the Hoarder (homebound), Scatterer bug |
| Juicer's gym | | the Juicer |
| Personal space | Carl, Donut, Mongo, Katia, Samantha, Prepotente, Louis, Garret | |
| Desperado casino | the Sledge, Bomo, Rosemarie | Astrid |
| The Parade | Doctor Bones, Splash Zone, Gluteus Maxx, Dong Quixote, Damascus Steel, Anaconda | |
| Over City | Bautista | Miss Quill |
| Circus | | Grimaldi, Heather, Tsarina Signet |
| Iron Tangle | Li Jun, Li Na, Zhang, Tserendolgor | Gore-Gore, Krakaren clone, Dismember, Station Mimic, Hekla, Eva, Quan Ch, Grull, Pooka, cloneling |
| Hump Town | Juice Box, the Popov brothers | Mrs. Ghazi, Ruckus |
| Castle ballroom | | Queen Imogen, Lucia Mar, Vrah |
| Hunting Grounds | Miriam Dom | Big Tina, Denise |
| Odette's studio | Odette, Zev, Quasar, Rosetta | Cascadia, Loita, Harbinger |
| Death Watch stage | Formidable | Maestro, Stalwart, Chaco |
| Havana | Sister Ines | Amayon, Shi Maria, the Hydra |
| Larracos | Tipid, Edgar | Eris, Burcu, Agatha |
| Emberus's temple | Pater Coal, Orthrus | Emberus |

## Mechanics that make it its own universe

1. **The ride: Katia's monster truck** (`Ride.monsterTruck`, in `Ride.drives`). A giant-wheeled truck roars in, bounces to a stop, and the crawlers climb on. It picks up the heroes, except HEM, the creatures (Mongo rides along with Donut, Orthrus and Garret don't) and the NPCs tied to their posts (the Desperado staff, Rory, Lorelai, Pater Coal, Edgar, Odette, Zev, Quasar). Villains leave on foot.
2. **Compaction mechanic: "New Achievement!"** (`CrawlAchievement.swift`). When an Earth crawler's session compacts, a blue System box slams in over them: **NEW ACHIEVEMENT! You Forgot Everything!** A loot box drops at their feet, shakes and bursts open in light. Same session, same face. The box's tier is random: usually bronze, sometimes silver or gold, rarely legendary, now and then celestial. Limited to the **Earth crawlers among the heroes**: Carl, Donut, Katia, Prepotente, Louis, Elle, Imani, Brandon, Chris, Bautista, Tran, Florin, Ifechi, Li Jun, Li Na, Zhang, Sister Ines, Tserendolgor, Langley, Gwendolyn, Jurgen, Osvaldo, the Popov brothers, Miriam Dom (heroes 0, 1, 3, 6, 7 and 8 to 26, 0-based). It reuses the missing-time clock as Clawdberg's `OutaTime` does, chosen where the overlay picks `OutaTime` (`Overlay.swift:1271`).
3. **Habits** (`Habits.swift`, Overlay's tick):
   - **The fans:** while Donut is on stage, now and then a camera flashes and a little "+10,000 VIEWERS" ticker floats up over her.
   - **Mongo and Donut:** when both are on stage, now and then Mongo nips at Donut's tail and she swats his snout.
   - **Prepotente's scream:** when he screams (his signature), the crew next to him jump.
   - **The AI's petty achievements:** now and then a small System toast pops over whoever is idling ("Achievement: Professional Loiterer", "Achievement: Stood There"). Smaller and rarer than the compaction box, so the two never blur.
4. **Bespoke drills** (`Drills.swift`): Carl punches a training dummy and stomps (Smush); Donut fires Magic Missiles at a target; Katia swells and shrinks; Bautista and Tran spar together. **No meditation.**

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one. A `CHANGELOG.md` entry each phase.

1. **Skeleton:**
   - settle the raw value first (see Context);
   - the universe case and all the wiring above;
   - Carl, Donut and Mongo, and Maestro (the enums' first cases);
   - the safe room, the menu icon, HEM's costume, Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with plain wipes (`case .starWars, .crawl: return nil` in `ComicTransition.pick`).
2. **Core ensemble.** About 35 characters:
   - the rest of the Royal Court, Meadow Lark, Bautista, Florin, Ifechi, the Sledge, Bomo, Doctor Bones, Splash Zone, Odette, Zev, Rory, Lorelai;
   - the Hoarder, the Juicer, the Krakaren clone, Ball of Swine, Ralph, Lucia Mar, Frank Q, Maggie My, Hekla, Chaco, Cascadia, Emberus;
   - 8 places: the safe room, the First Floor tunnels, the Tutorial Guild, the Hoarder's lair, the Juicer's gym, the personal space, the Desperado casino, Odette's studio; with homes and nemeses for these.

   The enum cases can go in first as stand-ins and be drawn in a second commit, as The Clawd Files did.
3. **The rest:** all 95 characters and all 20 places, every home filled in, and the homebound Hoarder. Ends with **the character audit**: every weapon, shot, magic family and colour, motion, signature and callout checked against the books, the wiki and this plan, a mismatches table for your OK. Re-check: **Tserendolgor's Crisper class** (is fire right?), **Katia's weapon** (fists in combat form, or her crossbow bolts?), **Zhang's Earth Mover attack**, and that every weapon type in the Cast table is really used with no two shared colours in one group.
4. **Mechanics:** the monster truck, New Achievement!, the four habits, the bespoke drills.
5. **Transitions:** the twelve `CrawlTrip`s and the System-box finishing touch, through `ComicTransition`.
6. **Polish pass** (always before docs): every weak spot noted in phases 2 to 5, split by file and fixed in parallel, with before-and-after renders for your OK.
7. **Docs and release:**
   - README (the universe's own section under "The universes" with its collapsible cast-and-places pictures, the screen-saver paragraph, developer notes), `llms.txt` (universe list, folder and prefix, the compaction mechanic);
   - `Tools/RenderDocs`: a `crawlLineup` desktop strip, `roster-dungeon-crawler-clawd.png`, the locations sheet and a social preview; `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - the trailer, `REEL=crawl`;
   - flip `isReleased` if it was built on `main`;
   - the version: a new universe raises the middle number (the next `3.N.0`);
   - **needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

**Weak spots to expect** (note them as they come up, fix them in the polish pass): Donut, Ferdinand and Orthrus as four-legged animals still reading as Clawd in costume; Samantha's doll head on four legs reading as a head, not a ball; Prepotente and Bianca fitting in one 72×52 frame (Bianca's wings and black flames against the frame rule, and see-through flames never half-opaque at the edge); Elle so tiny she vanishes at agent size; the Sledge and Bomo telling apart at agent size; the big bosses (Big Tina, the Hydra's nine heads, Shi Maria's legs, Grull, Amayon) against the frame rule; the System box's lettering at window size; the corridor and the temple too dark or too red for outlines.

## Verification

- **Build:** `./build.sh`. The cast-size `precondition` in `Overlay.swift:180` catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` for slow type-checks before calling a phase done.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Princess Donut"`;
  - `build/preview fight out.png "Carl" "Maestro"`;
  - `build/preview fight out.png "Elle McGibbons" "Big Tina"`: ice against a steady red ray;
  - `build/preview place out.png "Dungeon Crawler Clawd"`;
  - `build/preview edges out.txt "Dungeon Crawler Clawd"`: everything it lists must be on purpose (shots, Carl's dynamite lob, Rosemarie's coins, thrown potions and bombs, Quan Ch's flight, Amayon's fire column);
  - and the batch sheets, one per Art file. Look at the PNGs before showing them.
- **Homebound:** the Hoarder only appears in her lair, and is recast anywhere else, including the desktop.
- **Pull request guard:** `python3 scripts/pr-guard.py main dungeon-crawler-clawd` before any PR.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> crawlSafeRoom crawlDesperado`.
- **In the app:**
  - Settings → Universe → Dungeon Crawler Clawd: sessions are heroes, subagents include villains, Garret and the small fry;
  - the screen saver's Options list it;
  - Random and Clawd Royale reach it.
- **New Achievement!:** `/compact` in a session led by Carl or Donut, several times, to see more than one box tier.

## Transitions (`CrawlTrip`, 12)

| # | Name | What happens | Comes up more with |
|---|---|---|---|
| 1 | **The Collapse** (signature, longest and rarest) | Night street, rain. The ground cracks and the buildings sink into the earth. A blue System box slams in: **WELCOME, CRAWLER!** A glittering game-show title, DUNGEON CRAWLER CLAWD in our own lettering, sweeps up, and the camera drops through the floor into the new place. | rare for anyone · turf: Carl's street |
| 2 | **Down the Stairwell** | The view spirals down a stone stairwell, a floor counter ticks over, and the bottom opens onto the new place. | Carl, Donut, Mordecai · turf: First Floor tunnels |
| 3 | **Loot Box** | A box thumps down, shakes, glows and bursts open, and its light becomes the new place. | the crawlers · turf: a safe room |
| 4 | **Recap Episode** | TV static, "PREVIOUSLY ON…", and the picture tunes in onto the new place. | Odette, Zev, Cascadia · turf: Odette's studio |
| 5 | **Floor Collapse** | A big red countdown ticks to 00:00:00, and the old floor crumbles away, revealing the new place below. | Mordecai, Cascadia |
| 6 | **The Iron Tangle** | A train screams across the screen, carrying the old scene away with it, and leaves the new one behind. | Gore-Gore, Li Jun, Li Na, Zhang · turf: Iron Tangle |
| 7 | **Ping** | A radar pulse rings out over a dungeon map grid, dots light up, and the map fades into the new place. | Carl (his spell), Elle (the scout) |
| 8 | **Goblin Dynamite** | A lit stick rolls in and fizzes. BOOM, and the smoke clears on the new place. | Carl, Rory, Lorelai, Rosetta · turf: First Floor tunnels |
| 9 | **The Club Doors** | Velvet doors swing open, neon spills out, and the new place is inside. | the Sledge, Bomo, the dancers · turf: the casino, the Parade |
| 10 | **The Death Watch Wheel** | Maestro's gaudy prize wheel spins, ticks, and lands on the new place's name. | Maestro, Chaco · turf: the Death Watch stage |
| 11 | **Hole** | Donut's Hole spell opens a black pit under the scene, everything drops through and lands in the new place. | Donut |
| 12 | **Emberus's Fire** | A wall of fire sweeps across, and ash drifts down onto the new place. | **needs Emberus present** (`needsOwner`) · turf: Emberus's temple |

**Finishing touch: the System box.** After every transition, a small blue System notification slides in with the new place's name ("ENTERING: The Over City"): the books' own interface, in the role The Clawd Files' typewriter caption plays there. Check the lettering reads at window size.

**Style:** pixel art in the System's electric blue, dungeon stone greys, Desperado neon purple and gold, and the red of boss music and countdowns. Lettering big and blocky like a game interface; nothing copied from the book covers.

**Left out:** Clockwork Triplicate (too fine to read), Magic Missile as a transition (only a flash, and it's Donut's weapon), Zerzura (teleporting a whole castle is too big for the frame), celestial ascension (no clear look).

## Promo: the trailer (`REEL=crawl`)

Built on `doctorShots`, about 45 to 50 seconds, rendered with the app's own sprites, places and transitions. Storyboard first, for your OK.

- **Intro (~9 s): The Collapse.** Rain on Carl's street; Donut darts out of a window and Carl follows in boxers and a leather jacket. The ground cracks, the buildings sink, the blue box slams in (**WELCOME, CRAWLER!**), and the glittering title **DUNGEON CRAWLER CLAWD** sweeps up as the camera drops into a safe room. Sound: a game-show brass sting and a chiptune pulse, our own notes.
- **Set piece (~9.5 s): from the sofa to the boss room.** Carl and Donut on Odette's cream sofa, ON AIR glowing; a trapdoor opens and drops them into the Juicer's gym as the lights go red. Carl's gauntlet punch, Donut's pink Magic Missiles from his shoulder, Mongo leaping in with a screech; the System box: "BOSS DEFEATED". Caption: "Mongo is appalled."
- **Hook (4 s):** shared.
- **Desktop (~4.6 s):** `brawl(ctx, .crawl, …)`: "Welcome to the dungeon. Your desktop is the dungeon."
- **Status (~4.2 s):** four characters, one per state; the aside: "Achievement: Professional Loiterer."
- **Agents (4 s):** "Every subagent gets a loot box."
- **Window (~4.8 s):** `windowShot(ctx, .crawl, …, at: .crawlSafeRoom)`, the System box naming the place: "Safe room. For now."
- **AIs (~4.4 s):** the BRING YOUR OWN AI* line-up, one character per AI.
- **End card (~4.2 s):** the safe room, the crew lined up, the title lands in System blue and game-show gold, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS", the app icon and the GitHub URL.

No cover art, logo or melody is copied.

## Sources

- [Dungeon Crawler Carl wiki, Category:Characters](https://dungeon-crawler-carl.fandom.com/wiki/Category:Characters): 424 character pages, read through the wiki's API for each character's look, weapon and home
- [WT Clients: Dungeon Crawler Carl ordered to series by Peacock](https://www.weintraub.com/2026/06/wt-clients-matt-dinnimans-dungeon-crawler-carl-ordered-to-series-by-peacock/)
- [TVLine: Dungeon Crawler Carl TV series ordered at Peacock](https://www.tvline.com/2197994/dungeon-crawler-carl-tv-adaptation-from-seth-macfarlane-ordered-at-peacock/)
- [Cinapse: Dungeon Crawler Carl TV show news](https://cinapse.co/dungeon-crawler-carl-tv-show/)

## Decisions (2026-10-18)

All four gates are passed:
- **Name: Dungeon Crawler Clawd.** Everyone keeps the on-page name.
- **Scope:** all eight books (confirmed by you after the plan was written).
- **Code naming:** `case crawl`, prefix `Crawl`, folder `DungeonCrawlerClawd/`, branch `dungeon-crawler-clawd`, `REEL=crawl`.
- **Raw value:** settled at build time.
- **Tone:** the Desperado dancers are in, your call (pixel art keeps them from being too sexy); Samantha is a doll's head with smeared red lipstick; Lucia Mar stays a villain (confirmed by you after the plan was written).
- **Roster:** approved as drafted: 51 heroes (with HEM and the agent-only Garret), 44 villains (with five small fry), 95 in all. Callouts "I'll kill your mother!" (Samantha) and Prepotente's scream approved.
- **Places and homes:** the 20 approved; the Hoarder is homebound in her lair.
- **Mechanics:** the monster truck, New Achievement!, the fans, Mongo and Donut, Prepotente's scream and petty-achievement habits, the drills, no meditation.
- **Transitions:** the twelve above, opening with the Collapse, finished with the System box.

The plan is ready for phase 1 when you say start.

## Status (2026-10-30, after phase 1)

Phase 1 is done on branch `dungeon-crawler-clawd` (1064d89; number 12 reserved on `main`): Carl, Princess Donut, Mongo and Maestro, HEM as a crawler fan with a slingshot, a safe room, the dynamite menu icon, the Playground prompts, no meditation, and the System's block letters (`crawlText` in CrawlKit). The template's one trip stays until phase 5. check.sh passes. Next: show phase 1, then phase 2 (core ensemble).

**Weak spots so far** (for the polish pass):
- Carl: the leather jacket's dark sides read a little like a moustache at 1×; the gauntlet is small.
- Donut: her split tortie face is busy, so the copper eyes and flat face don't read at once.
- Maestro: the snout and tusks are crowded together.
- Safe room: the "PREV" caption on the TV is cramped.

## Status (2026-10-30, after phase 2)

Phase 2 is drawn on branch `dungeon-crawler-clawd` (3458284 wiring, 62d58af art, 763144c fixes): 20 more heroes, 12 villains and 7 places. Donut is brown with a ginger saddle and a brown tail; Mongo is blue-grey under pink plumage (owner's picks, d76cbd4). Prepotente stands on his own now, without Bianca (owner's call). HEM sits just before the end of `CrawlHero`, so the plan's 0-based hero and villain numbers no longer apply; use the case names. Phase 2 homes stand in for places that come in phase 3 (see CrawlRoster.swift). Emberus is `.lightning` with a thick steady ray.

**Weak spots from phase 2** (for the polish pass):
- Mordecai reads as a brown bird more than an eagle.
- Ball of Swine: a tight cluster of tiny faces.
- The Hoarder: busy edges from the junk.
- Bautista's orange sword can read as his tail at rest.
- Lorelai's bone necklace and topknot.
- Odette's studio: the mantis emblem, and the tall version's empty top.
- Chaco's signature runs off the left edge on purpose.

## Handoff (2026-10-30, end of the day)

Everything is pushed: `main` (4f73e7b, number 12 reserved) and `dungeon-crawler-clawd` (763144c) on origin. To pick up at home: `git fetch && git checkout dungeon-crawler-clawd`, then `Tools/Preview/build.sh` (about 4 minutes).

- **Where it stands:** phases 1 and 2 done and shown; the owner approved Donut, Mongo, Prepotente and the guild fixes. No other phase 2 notes yet.
- **Next:** phase 3, the rest of the cast and places (see Phases). The enum cases go in first, before `hem` (HEM is always last), then the art.
- **How phase 2 was built:** the wiring commit first (cases, homes, nemeses, place keys, empty `CrawlHeroes2/3`, `CrawlVillains2/3`, `CrawlScenes2/3`), then six agents in parallel, one file each, in their own worktrees, with renders checked before merging. Worktree agents start from `main`, so each had to fast-forward to the branch first; say so in the brief. Builds run 4 to 7 minutes when several go at once.
- **Review renders:** `~/Desktop/dungeon-crawler-clawd-phase-2/` on the work machine only (not in git).
- **Preview names:** some clash with other universes; use `crawl:` in front (`crawl:rory`, `crawl:samantha`).
