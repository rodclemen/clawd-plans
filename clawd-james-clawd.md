# Plan: a new universe, James Clawd (the 007 films)
<!-- track: repo=rodclemen/clawd-clash branch=bond folder=SpyClawd title="James Clawd" cast=96 places=21 -->

## Context

Clawd Clash has six universes: Star Clawds, Marvelous Clawds, Detective Clawds, Doctor Clawd, The Clawd Files and Stevie Clawdberg. This plan adds the Eon 007 films, all twenty-five of them from Dr. No to No Time to Die, as one full ensemble. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

Bond is a strong fit. The heroes are a smaller, sharper crew (six Bonds, MI6, the CIA and the allies), and the villains are the franchise's real strength: sixty years of masterminds and memorable henchmen, each with one prop that reads instantly as pixels (a bowler hat, steel teeth, a golden gun, a white cat, a claw arm, a shoe blade).

- **Name: James Clawd** (chosen on 2026-10-16). The alternatives were *Licence to Clawd*, *00-Clawd* and *Clawdfinger*.
- **Code naming** avoids the franchise name, as the other universes do:
  - `case spy` with key `"spy"`.
  - Folder `Sources/App/Universes/SpyClawd/`, file prefix `Spy…` (`SpyRoster.swift`, `SpyHeroes1.swift`, `SpyWipes.swift`…).
  - Branch `bond`.
  - Place keys and top-level helpers all start with `spy` so they can't clash with the six sibling plans being written at the same time (Star Trek, Transformers, He-Man, Game of Thrones, Tim Burton, Buffy).
- **Raw value:** the next free one when its build starts, checked against main and the open branches (main has Clawd of the Rings as `middleEarth = 6`, and the Buffy branch also claims 6 today); ids are rawValue*1000 and permanent.
- **Naming style:** light puns on the on-screen names (Auric Goldclaw, Blowfeld, Dr. Know, Felix Lighter). The six Bonds get nicknames from their look, one per era (decided 2026-10-16): **Trilby Bond, Ski Bond, Safari Bond, Leather Bond, Tank Bond, Jumper Bond**, never the actors' names. Each era is named in this plan only by its films.
- **Size:** about **96 characters**: 45 heroes including HEM, and 51 villains including 4 agent-only. Plus **21 places** and **13 transitions**.
- **Tone:** a desktop toy, so the Bond films' sexualised names, the gore and the dated caricatures are left out or renamed (see *Tone, and what was left out*).

| Universe                | Heroes | Villains | Total | Places | Transitions |
|-------------------------|--------|----------|-------|--------|-------------|
| Star Clawds             |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds        |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds        |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd            |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files         |     36 |       46 |    82 |     20 |          11 |
| Stevie Clawdberg        |     64 |       54 |   118 |     23 |          10 |
| Clawd of the Rings      |     38 |       38 |    76 |     22 |           9 |
| **James Clawd (proposed)** | **45** | **51** | **96** | **21** | **13** |

(heroCount includes HEM; villainCount includes the 4 agent-only small fry.)

**Viability: clearly viable.** 44 good heroes and 47 good villains, more than double the 20-a-side threshold, without reaching for the non-Eon films, the novels or the games. This is not a limited experience.

**How the franchise is sorted.** Heroes are the six Bonds, MI6, the CIA, friends in the field, and the allies Bond works with on each mission (written as agents, pilots, scientists and fighters rather than as "Bond girls"). Villains are SPECTRE, then the masterminds and their henchmen grouped by decade, the way fans tend to rank them. Claude plays **the heroes** (MI6), as in every universe since Star Clawds.

### Tone, and what was left out

- **Sexualised names are renamed or dropped.** Renamed, because the character carries a film: Pussy Galore → **Captain Galore** (she leads the Flying Circus); Holly Goodhead → **Dr. Holly Goodheart**; Xenia Onatopp → **Xenia Helicopp** (she steals the Tiger helicopter; her thigh-crushing is left out entirely, she's a laughing gunner); Octopussy → **Octoclawd**; Honey Ryder → **Shelley Ryder** (she dives for shells); Christmas Jones → **Dr. Christmas Joules** (the pun is on the physicist, not the line about Christmas); Anya Amasova keeps her name as **Major Anya Amaclawva**, never "Triple X". Dropped, because the name *is* the joke and they're bit parts: Plenty O'Toole, Molly Warmflash, Chew Mee, Bibi Dahl, Strawberry Fields, Kissy Suzuki (Tiger Tanaclaw covers You Only Live Twice).
- **Gore and cruelty:** no blood in the gun barrel (a red curtain wash instead); no golden-paint death; no torture chair (Le Cypher is in for the poker, inhaler and chips, not the rope); no shark tank maiming in Licence to Kill; Dario left out (his whole point is sadism); Zao's diamonds stay a sparkle on his cheek; piranhas and sharks splash but never eat anyone.
- **Children:** Mathilde (No Time to Die) is left out.
- **Dated caricatures:** the "Bond in Japanese disguise" and the voodoo stereotyping of Live and Let Die are not used. Mr. Bigg, Tee Hee and Baron Samedee are drawn as their characters (a rubber mask, a claw arm, a top hat and skull face paint), nothing more. Nick Knack is drawn as Scaramangle's scheming butler with a tray, with no jokes about his height.
- **No real people:** no politicians or real spies; real places (Fort Knox, the Golden Gate) appear only as backdrops.

## How a universe plugs in (checked against the code on 2026-10-17, main at d270b63)

**New code: `Sources/App/Universes/SpyClawd/`**
- `SpyRoster.swift` (the pattern is `StevieClawdberg/ClawdbergRoster.swift`):
  - `enum SpyHero` and `enum SpyVillain`, append-only, with `hem` as the last hero and the agent-only small fry as the last villains.
  - The persona dictionaries, `.reduce([.hem: hemPersona(.spy)])`.
  - `Location.spyHome(of:)` for heroes and villains, `spyNemeses`, the ride closure, `let spyTheme = Theme(...)`.
  - The `static let spy…` place keys, and `let spyPlaces` merged from the Places files.
- `Art/SpyHeroes1…5.swift` and `Art/SpyVillains1…6.swift`, 8–10 personas per file.
- `SpyKit.swift`: shared drawing helpers with `spy` names (the tuxedo, the Walther, the bow tie, the Nehru collar), since Preview compiles every universe together.
- `Places/SpyScenes1…3.swift`.
- `SpyIcon.swift`: the menu bar icon, 28×26, colour and mono. A gun-barrel circle with a tiny Clawd silhouette standing in it (no logo).
- `SpyRides.swift`: the Aston Martin and the flying car (phase 4).
- `SpyRecast.swift`: the compaction effect, the gun barrel closing on one Bond and opening on the next (phase 4).
- `SpyDrills.swift`: `spyBespokeDrills` (phase 4).
- `SpyWipes.swift`: `SpyTrip`, the transitions (phase 5).

**Wiring into the existing code.** Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎. Copy what `clawdberg` did in each spot.
- **`Sources/Shared/Universe.swift`:**
  - `:8–40` the case, `key`, `title`, `villainCount`, `heroCount`.
  - `:50–61` `agentOnly` (the white cat, the tarantula, the piranha, the iguana).
  - `:65` `claudeSide` stays the default (heroes). `:68` `rivals` (today the one-liner `self == .starWars ? [0, 1] : []`): none.
  - `:100–102` `regenerations`: the six Bonds in order (see Mechanics). Today it's `self == .doctor ? … : []`; it becomes a switch.
- **`Sources/App/Theme.swift:40–49`:** `Theme.of` → `spyTheme`.
- **`Sources/App/Locations.swift:70–72`:** `.merging(spyPlaces)` in `places`.
- **`Sources/App/Universes/ComicTransition.swift`:** `pick` (`:40–62`) now lists every universe explicitly, so in phase 1 James Clawd joins Star Clawds' line (`:42–43`, which becomes `case .starWars, .spy: return nil`). In phase 5 it leaves that line and gets a `.spy(SpyTrip)` case in the enum (`:8–13`), `duration` (`:15–24`), `draw` (`:27–36`) and `pick`, and the doc comment (`:3–6`) is updated.
- **`Sources/App/Universes/Hem.swift:29, 104, 119, 146, 172, 228`:** HEM's costume in every switch (see Cast).
- **`Sources/App/Rides.swift`** (and `Theme.swift:89`'s `enum Ride`): `.astonMartin`, `.flyingCar`. The Aston Martin drives in along the ground, so it also goes in `Ride.drives` (`Theme.swift:93`).
- **`Sources/Saver/SaverView.swift`:** nothing to add. The Options list (`:88–90`) and the trip choice (`:207–215`) build themselves from `Universe.offered`.
- ⚠︎ **`Sources/App/Drills.swift:54`:** add `.spy` to the no-meditation guard. `:488`: merge `spyBespokeDrills`.
- ⚠︎ **`Sources/App/Overlay.swift:869`:** five Playground prompts (below), a `case .spy:` in the `switch Universe.shown`. `:1143` shows how `clawdberg` hooked its set piece (Indy shoots first) into the Han-and-Greedo moment: the Golden Gun duel goes in the same way. `:1224` draws the Doctor's golden flare for *any* regenerated leader: wrap it so a `.spy` leader gets the gun-barrel recast instead. `:1271` is where OutaTime was hooked, for reference.
- ⚠︎ **`Sources/Shared/StatusStore.swift:336–349`:** the PreCompact path already walks `Universe.regenerations` for any universe, so no change is needed. Check the comment still reads right.
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`:** decide whether `.spy` joins each universe-specific `if`.
- **Clawd Royale** picks up the cast and places through `Universe.allCases`. Check the menu icon and arch-enemies in a Spy place.
- **Tools:**
  - `Tools/Preview/main.swift:63–120`: the batch names (`spyHeroes1…`, `spyVillains1…`), the universe lookup, the enum lookups by case name.
  - `Tools/Transitions/main.swift:13, 132–133`: the branch that renders `SpyTrip`s.
  - Phase 6: `Tools/RenderPromo` (`REEL=spy`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts** (`Overlay.swift:869`): "Run a background check on Auric Goldclaw", "Decrypt the Lektor before the train reaches Venice", "Q, what does this button do?", "Find the leak inside MI6", "Track the GoldenEye satellite's next pass".

## Cast

How the engine's weapons map onto the films. Each character's weapon was looked up, not assigned by group.
- **`.blaster` + `.bullet`** is the Walther PPK and its cousins: every Bond, most agents, most henchmen with a gun. It's the franchise's main weapon.
- **`.blaster` + `.thrown(colour)`** for the thrown gadgets and props: Oddjob's bowler, Necros's exploding milk bottles, Le Cypher's poker chips, Tiger's shuriken, Holly's dart pen.
- **`.blaster` + `.arrow`** for crossbows and spearguns (Melina, Domino, Largclaw).
- **`.blaster` + `.energy` / `.beam`** for the films' laser guns: Draks's Moonraker laser rifle (blue-white streak), Blowfeld's diamond-satellite laser (an ice-cyan beam), Scaramangle's golden gun (a short gold streak, one shot).
- **`.saber`** (melee) for the brawlers and blades: Jaws's teeth, Rosa Klebb's shoe blade, Grant's garrotte watch, Tee Hee's claw, Changg's kendo stick, Miranda's foil, Grean's axe, the judo and kung fu fighters.
- **`.lightning` + `Magic`** only for the handful of real "powers" and lasers: Goldclaw's laser, Gravez's Icarus beam, Baron Samedee's voodoo, Solitaire's tarot, Q's remote-control car. Each looks different (below).
- **`armoured: true`** for the unstoppable: Jawz, Renarde (a bullet in his brain, he feels no pain), Dr. Know's metal hands, Mayday.
- **`.none`** for those who never fight on screen: M, Moneypenny, Kronstine, Craver, the scientists.

**Magic and energy users, each with its own look** (nobody else in this universe or any other draws the same):

| Caster | Family | Colours and style |
|---|---|---|
| Auric Goldclaw (the laser table) | steady ray | thin ruby-red core, deep red glow; creeps forward slowly and throws molten-gold sparks where it lands |
| Gustav Gravez (Icarus) | steady ray | a wide pale-gold sunbeam slanting down from above, with heat shimmer along its edges |
| Baron Samedee (voodoo) | spell | violet and bone-white sparkle ribbon, with tiny skull-shaped twinkles |
| Solitaire (tarot) | touch | a teal-and-gold glowing tarot card at her fingertip; the target glows teal |
| Q (the remote BMW) | rcCar | a little silver saloon on twin blue-white exhaust trails (not fire, so it differs from the existing rcCar) |

`Theme.persona` numbers each caster's `variant` automatically; check in Preview that Goldclaw's red ray doesn't sit too close to any existing red ray (Marvel's Cyclops is a beam, not magic, so that's fine).

### Heroes (45)

**The Bonds (6).** One per era, each nicknamed for his look. All carry the Walther PPK; what tells them apart is the outfit and the signature. All six share the callout **"Clawd. James Clawd."**; their own lines are below.

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Trilby Bond (Dr. No to Diamonds Are Forever) | dark three-piece suit, narrow tie, trilby | Walther PPK | tosses his trilby onto a hatstand | "Shaken, not stirred." |
| 2 | Ski Bond (On Her Majesty's Secret Service) | a pale blue ski suit, goggles pushed up, skis over his shoulder | Walther PPK | turns and looks straight out at us, a hand on his chin | "This never happened to the other fellow." |
| 3 | Safari Bond (Live and Let Die to A View to a Kill) | cream safari suit, wide lapels | Walther PPK | the Union Jack parachute pops open behind him | "Clawd. James Clawd." (one eyebrow up) |
| 4 | Leather Bond (The Living Daylights, Licence to Kill) | black leather bomber jacket | Walther PPK | wolf-whistles, and his key ring puffs a little cloud of gas | "Clawd. James Clawd." |
| 5 | Tank Bond (GoldenEye to Die Another Day) | navy suit, crisp tie | Walther P99 | straightens his tie, as he did driving a tank through St Petersburg | "Clawd. James Clawd." |
| 6 | Jumper Bond (Casino Royale to No Time to Die) | navy knit jumper, shoulder holster, cropped blond hair | Walther PPK | a parkour leap up and down, then fixes a cufflink | "Do I look like I give a damn?" |

**MI6 (7)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 7 | Admiral M | grey suit, pipe | none | puffs his pipe, taps a dossier | "Oh, and 007…" |
| 8 | Dame M | short white hair, pearls, dark jacket | none | a dry, level stare over her glasses | "Don't be flippant." |
| 9 | Q (Major Boothclawd) | tweed jacket, grey hair, glasses | rcCar (the remote BMW) | a gadget goes off in his hands: "Don't touch that!" | "Pay attention, 007!" |
| 10 | Young Q | parka, cardigan, glasses, laptop | none | types; a little green progress bar fills | "Were you expecting an exploding pen?" |
| 11 | Miss Moneypinny | 1960s up-do, twinset, desk | none | catches a hat and hangs it on the hatstand | "Flattery will get you nowhere." |
| 12 | Eve Moneypinny | field agent, dark coat, rifle | rifle (bullet) | sights down her rifle, then a cut-throat razor glints | none |
| 13 | Nomee | the new 007: short hair, tactical black | pistol | taps the "007" on her ID card | "It's just a number." |

**The CIA (3)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 14 | Felix Lighter | light suit, CIA badge | pistol | a handshake and a grin | "Felix Lighter, CIA." |
| 15 | Jack Wayde | Hawaiian shirt, baseball cap | none | a cheery wave from a car window | none |
| 16 | Palomah | black evening dress, nervous smile | pistol, high kicks (melee) | downs a shot of vodka, then a spinning kick | "Three weeks' training!" |

**Friends in the field (8)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 17 | Quarrell | fisherman, cap, boat pole | none | poles a little boat |
| 18 | Kerim Bay | moustache, white suit | rifle | peers through a periscope |
| 19 | Tiger Tanaclaw | dark suit, Japanese secret service | shuriken (thrown) | ninjas drop in on ropes behind him |
| 20 | Marc-Ange Drako | silver hair, Corsican crime boss | pistol | raises a toast |
| 21 | Milos Colomboh | smuggler, cap, pistachios | machine gun (bullet) | cracks a pistachio, shells fly |
| 22 | Valentin Zukclawsky | big coat, cane, gold tooth | cane gun (one shot) | taps his cane; a single shot pops out |
| 23 | René Mathiss | silver-haired, cravat | none | sips a coffee, shrugs |
| 24 | Sheriff J.W. Peppah | stetson, belly, chewing tobacco | none | spits, then squints: "Boy!" |

**Allies on the mission (20).** Agents, pilots, scientists and fighters in their own right.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 25 | Shelley Ryder | white swimsuit, knife belt, conch | knife (melee) | holds up a conch shell and hums |
| 26 | Tatiana Romanclawva | Soviet cipher clerk, ribbon, headscarf | none | clutches the Lektor decoder |
| 27 | Captain Galore | pilot's flying suit, short blonde hair | judo (melee) | a judo throw |
| 28 | Domino Dervaul | black-and-white swimsuit, snorkel | speargun (arrow) | flips her snorkel mask up |
| 29 | Contessa Tracy | ski suit, long dark hair | skis (melee) | slaloms on the spot |
| 30 | Tiffany Kase | changing wigs | pistol | her hair colour switches: blonde, red, brunette |
| 31 | Solitaire | tall crown headdress, robes | tarot (touch magic) | turns over a tarot card: the Lovers |
| 32 | Mary Goodnite | blonde, sundress, MI6 field officer, flustered | none | backs into a button; something whirs up |
| 33 | Major Anya Amaclawva | Soviet uniform, cigarette-holder dart | pistol | blows a dart from the holder |
| 34 | Dr. Holly Goodheart | NASA scientist, white jumpsuit | dart pen (thrown) | her perfume bottle shoots a little flame |
| 35 | Melina Havelclawk | hair up, leather jerkin | crossbow (arrow) | loads a bolt, sights |
| 36 | Octoclawd | silk robes, octopus emblem | none | an octopus tattoo glows; her circus women cartwheel past |
| 37 | Kara Milovee | cellist, fur hat | none | plays her cello, then rides its case like a sled |
| 38 | Pam Bouviay | pilot, short hair, shotgun | shotgun (bullet) | racks the shotgun |
| 39 | Natalya Simoclawva | programmer, cardigan | none | types; a satellite glyph spins |
| 40 | Wai Linn | black catsuit, Chinese intelligence | kung fu (melee) | a flurry of kicks |
| 41 | Dr. Christmas Joules | tank top, cargo shorts, Geiger counter | none | the Geiger counter clicks and glows |
| 42 | Jinx Johnsun | orange swimsuit, dive knife | pistol | a backwards dive off a cliff (Jinx's orange is pushed towards coral so she doesn't melt into Clawd) |
| 43 | Vesper Lind | evening gown, Algerian love-knot pendant | none | twists her pendant |
| 44 | Madeleine Swan | white coat, psychologist | pistol | lowers a pistol, shaking |

**HEM (1)**, last as always:

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 45 | HEM | the white dinner jacket, black bow tie and a red carnation; a Walther | pistol | adjusts the carnation |

The white jacket keeps him apart from all six Bonds (none of them wears it in this cast).

### Villains (51)

**SPECTRE (13)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Ernst Stavro Blowfeld | bald, scar over one eye, grey Nehru suit, white cat | diamond-satellite laser (beam, ice-cyan) | strokes the white cat | "We meet again, Mr. Clawd." |
| 2 | Dr. Know | grey Nehru suit, black metal hands | metal hands (melee), `armoured` | clacks his metal fingers together | "A clever man." |
| 3 | Rosa Klawb | tight bun, glasses, khaki uniform | shoe blade (melee) | the blade flicks out of her shoe toe | none |
| 4 | Red Granite | blond crew cut, Orient Express waiter's jacket | garrotte watch (melee) | pulls the wire out of his wristwatch | "Red wine with fish." |
| 5 | Kronstine | chess master, dark suit | none | moves a knight on a floating chessboard | none |
| 6 | Emilio Largclaw | eyepatch, white shirt, No. 2 | speargun (arrow) | his sharks circle; a fin passes behind him | none |
| 7 | Fiona Volpeh | red hair, black leathers, motorbike helmet | rocket bike (fire) | revs the bike; a rocket whooshes | none |
| 8 | Irma Blunt | cropped hair, severe suit, clipboard | pistol | checks her clipboard, sniffs | none |
| 9 | Mr. Wynt | balding, thin, bow tie | bomb in a cake (thrown, pink) | sniffs the air, smiles | "Very sad, Mr. Kydd." |
| 10 | Mr. Kydd | curly hair, glasses | flaming kebabs (fire) | lights a kebab | "Very sad, Mr. Wynt." |
| 11 | Mr. Whyte | grey beard, glasses, tailored grey | pistol | a soft knowing smile; checks his phone | none |
| 12 | Hinxx | huge, dark suit, metal thumbnails | thumbnails (melee), `bulk` | flexes his metal thumbs | "Shh." |
| 13 | Primo | dark suit, glowing bionic eye | pistol | his bionic eye flickers blue | none |

**The masterminds and their muscle: the Sixties and Seventies (11)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 14 | Auric Goldclaw | gold suit, ginger hair | laser (magic, ruby red) | rubs his hands over a bar of gold | "No, Mr. Clawd, I expect you to die!" |
| 15 | Oddjobb | black bowler, grey suit | bowler hat (thrown, black) | crushes a golf ball in one hand | none |
| 16 | Mr. Bigg | sharp suit, rubber mask | pistol | peels the mask off his face | "Names is for tombstones." |
| 17 | Tee Hee Johnstone | big grin, metal claw arm | claw (melee) | his claw snips, he laughs | none |
| 18 | Baron Samedee | top hat, skull face paint, tails | voodoo (magic, violet) | a booming laugh; vanishes and reappears | none |
| 19 | Francisco Scaramangle | white suit, golden gun | golden gun (gold streak, one shot) | assembles the gun from pen, lighter, cufflink and case | "A duel between titans." |
| 20 | Nick Knack | butler's jacket, bow tie, tray | champagne cork (thrown) | pops a cork, grins | none |
| 21 | Karl Stromclawberg | grey Nehru jacket, webbed fingers | none | presses a button; a trapdoor opens under someone | none |
| 22 | Jawz | very tall, steel teeth | bite (melee), `armoured`, `bulk` | bites through a chain, then grins | "Well, here's to us." |
| 23 | Hugo Draks | black beard, Mao collar, NASA tie | laser rifle (energy, blue-white) | an orchid in his lapel; checks his watch | "Look after Mr. Clawd." |
| 24 | Changg | kendo armour, bamboo shinai | kendo stick (melee) | a kendo kiai stance | none |

**The Eighties (8)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 25 | Aris Kristaclaws | tweed, moustache, smuggler | pistol | sips ouzo | none |
| 26 | Emile Locke | round glasses, trench coat | pistol | polishes his glasses | none |
| 27 | Kamal Khaan | silk Nehru coat, Afghan exile | pistol | rolls dice that always come up sixes | none |
| 28 | Gobindah | turban, huge, stern | melee, `bulk` | crushes a pair of dice in his fist | none |
| 29 | Max Zorrin | platinum blond, black overcoat | machine gun (bullet) | a high giggle | "More!" |
| 30 | Mayday | flat-top hair, big jewellery | strength (melee), `armoured` | lifts a man over her head | none |
| 31 | Necross | milkman's white coat, Walkman headphones | exploding milk bottles (thrown, white) | puts on his headphones; the wire becomes a garrotte | none |
| 32 | Franz Sanclaws | moustache, open shirt, iguana with a diamond collar | pistol | strokes his iguana | "Loyalty is more important to me than money." |

**The Nineties and Noughties (10)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 33 | Alec Trevellion | 006: scarred cheek, dark coat | pistol | touches the scar | "For England, James?" |
| 34 | Xenia Helicopp | black fighter-pilot gear, red lipstick | machine gun (bullet) | fires wildly, laughing | none |
| 35 | Boris Grishenkko | computer nerd, polo shirt | none | clicks his pen three times; arms up | "I am invincible!" |
| 36 | Elliot Craver | black Mao suit, glasses | none | holds up a newspaper headline | "Give the people what they want." |
| 37 | Stampah | blond, huge, white tunic | melee, `bulk` | cracks his knuckles | none |
| 38 | Elektra Kingg | fur coat, oil heiress | none | a cold smile; tightens a strap | "I could have given you the world." |
| 39 | Renarde | bald, a bullet scar on his head | pistol, `armoured` | holds a hot stone with no pain | none |
| 40 | Gustav Gravez | polar fleece, then the Icarus power suit | Icarus beam (magic, pale gold) | his suit crackles with power | "Time to face gravity." |
| 41 | Zaoh | bald, diamonds on his cheek | pistol | his cheek sparkles | none |
| 42 | Miranda Frosst | fencing whites, ice-blonde | fencing foil (melee) | a fencing salute | none |

**The new century (5).** Mr. Whyte, Hinxx and Primo from these films are in SPECTRE.

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 43 | Le Cypher | scarred eye, black suit, inhaler | poker chips (thrown, red) | riffles a stack of chips, puffs his inhaler | none |
| 44 | Mollacka | bomb-maker, vest, parkour | thrown bomb | leaps up a crane and down | none |
| 45 | Dominic Grean | white linen suit, glasses | axe (melee) | adjusts his glasses, then a sudden wild swing | none |
| 46 | Raoul Silvah | bleached blond hair, white shirt | pistol | flicks his fringe; a toothy smile | "Hello, James." |
| 47 | Lyutsifer Saffin | cracked white Noh mask, scarred skin | pistol | lifts the Noh mask, kneels in his poison garden | none |

**Agent-only small fry (4).** Like the MSE-6, these only ever appear as agents:

| # | Name | Look | Motion |
|---|---|---|---|
| 48 | The white cat | Blowfeld's Persian, jewelled collar | walks, curls up |
| 49 | A tarantula | Dr. No's, from the hotel bed | scuttles |
| 50 | A piranha | from Blowfeld's pool | `.hover`, `canSit: false` |
| 51 | An iguana | Sanclaws's, diamond collar | walks |

Kananga's crocodiles are left out of the cast: Stevie Clawdberg's Croc Clock is already a crocodile. They stay in the scenery of the croc farm.

### Nemeses (25)

Each pair faces off first when both are on stage:
- Trilby Bond ↔ Blowfeld
- Ski Bond ↔ Irma Blunt
- Safari Bond ↔ Scaramangle
- Safari Bond ↔ Max Zorrin
- Leather Bond ↔ Franz Sanclaws
- Tank Bond ↔ Alec Trevellion
- Jumper Bond ↔ Le Cypher
- Dame M ↔ Raoul Silvah
- Young Q ↔ Boris Grishenkko (a hacking duel)
- Felix Lighter ↔ Auric Goldclaw
- Captain Galore ↔ Oddjobb
- Shelley Ryder ↔ Dr. Know
- Tatiana Romanclawva ↔ Rosa Klawb
- Kerim Bay ↔ Red Granite
- Domino Dervaul ↔ Emilio Largclaw
- Solitaire ↔ Baron Samedee
- Sheriff J.W. Peppah ↔ Mr. Bigg
- Major Anya Amaclawva ↔ Jawz
- Dr. Holly Goodheart ↔ Hugo Draks
- Melina Havelclawk ↔ Emile Locke
- Octoclawd ↔ Kamal Khaan
- Kara Milovee ↔ Necross
- Wai Linn ↔ Stampah
- Jinx Johnsun ↔ Miranda Frosst (their fencing-and-fists fight)
- Madeleine Swan ↔ Lyutsifer Saffin

**Rivals:** none. **Claude's side:** heroes.

### Lookalike check

- **Inside the universe:** a lot of suits. Each suited villain gets one loud prop: Blowfeld's cat and scar, Dr. Know's black metal hands, Stromclawberg's webbed fingers and the Nehru collar in a different colour (Blowfeld grey, Stromclawberg navy, Dr. Know charcoal with a white shirt), Craver's glasses and black Mao suit, Whyte's grey beard, Grean's white linen, Le Cypher's scarred eye and chips. The six Bonds differ by outfit: suit-and-trilby, kilt, safari, leather, navy suit, knit jumper. The three big henchmen (Jawz, Stampah, Hinxx) differ by colour and prop: steel teeth, white tunic, metal thumbs.
- **Across universes:** Blowfeld vs Detective Clawds' Lex Lugar (both bald): the cat, the scar and the Nehru suit separate them. Baron Samedee vs Marvel's Doctor Hoodoo: Samedee's top hat, tails and violet spell. Jawz vs Marvel's Lockjaws and Ebony Jaw (names only). Domino Dervaul vs Marvel's Dominoe: always written with her surname. Miranda Frosst vs DC's Mr. Frost and Marvel's Emma Frosty: different look entirely. Red Granite was chosen over "Red Grunt" because Doctor Clawd has Jo Grunt. Tee Hee is *Johnstone*, not *Johnsun*, so he doesn't share a surname with Jinx. Hugo Draks vs Marvel's Drex the Destroyer: different spellings and nothing alike in looks. Clawd Files' Jimmy Bondd stays as he is.

## Places (21)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. Keys all start with `spy`, so no clash with the existing ones (checked against every `static let … = Location` on main) or the sibling plans.

| # | Key | Place | Still | Moving layer | Tall-canvas extras |
|---|---|---|---|---|---|
| 1 | `spyMI6` | **MI6: Moneypenny's office** (the default) | the padded door to M's office, the hatstand, Moneypenny's desk and typewriter, a window on the Thames | rain on the window, a desk lamp's warm pool, the typewriter carriage | the Vauxhall Cross building's terraces and the river at night |
| 2 | `spyQBranch` | **Q Branch** | workbenches, a rocket-firing leg cast, an umbrella-shield, a dummy on a stand | a gadget test: a briefcase puffs smoke, a dummy gets zapped, a conveyor rolls | ducts and a parachute hanging from the ceiling |
| 3 | `spyCrabKey` | **Crab Key** | a white beach, palms, the "dragon" tank on the sand, Dr. No's reactor building | waves, the dragon's flame puff | a tropical sky with a seaplane |
| 4 | `spyOrientExpress` | **The Orient Express** | a wood-panelled sleeper compartment | the countryside streaming past the window, the lamp swaying | the carriage roof and mountains |
| 5 | `spyFortKnox` | **Fort Knox** | stacks of gold bars behind bars, the atomic bomb on a trolley | the bomb's timer counting down (it stops at 007) | the vault's tall gold shelving |
| 6 | `spyVolcano` | **The volcano lair** | the crater's steel floor, a monorail, a rocket on its gantry | the crater lid sliding, the monorail gliding, steam | the rock walls rising to a sky-lit lid |
| 7 | `spyPizGloria` | **Piz Gloria** | the revolving mountaintop restaurant, the cable car, snowfields | the cable car sliding, falling snow | Alpine peaks and stars |
| 8 | `spyCrocFarm` | **The crocodile farm** | a bayou hut, a TRESPASSERS sign, a pond | crocodile backs drifting, lily pads bobbing, fireflies | cypress trees and Spanish moss |
| 9 | `spyScaramangaIsle` | **Scaramangle's island** | karst towers rising out of the sea, the solar array, a funhouse door | the solar panels tilting, a mirror flicker | the karst towers soaring |
| 10 | `spyAtlantis` | **Atlantis** | the spider-legged sea base out on the water, a submarine pen | waves, the base rising and settling, a fin in the shark tank | a deep-sea window with fish |
| 11 | `spySpaceStation` | **Draks's space station** | white modules, a docking shuttle, a black sky | the Earth turning below, blue laser streaks far off | more of the station's spokes and stars |
| 12 | `spyStCyrils` | **St Cyril's monastery** | a monastery on a sheer rock pillar, a basket on a rope | the basket winching up, crows | the rock pillar's full height |
| 13 | `spyFloatingPalace` | **Octoclawd's floating palace** | a white marble palace on a lake, a barge | water shimmering, an octopus banner flapping | hills and a hilltop palace beyond |
| 14 | `spyGoldenGate` | **The Golden Gate and the airship** | the red bridge, fog | Zorrin's airship drifting past the tower, fog rolling | the tower's top and the airship's full length |
| 15 | `spyCasino` | **The casino** | a chandelier, a baccarat table, a roulette wheel | the roulette wheel spinning, chips sliding, the chandelier glinting | a gilded ceiling and a terrace over the harbour |
| 16 | `spyCubaDish` | **The satellite dish** | a giant dish in the jungle, a lake | the antenna rising out of the lake, birds | the dish's full curve and the jungle canopy |
| 17 | `spyStealthShip` | **Craver's stealth ship** | a black angular ship in a misty bay of karst islands | the ship's hull shimmering out of sight, junks drifting | the karst islands in mist |
| 18 | `spyMaidensTower` | **The Maiden's Tower** | a small tower on an island in the Bosphorus, a domed skyline | the water, a submarine's periscope cutting past | minarets and a sunset |
| 19 | `spyIcePalace` | **The ice palace** | a palace of ice in Iceland, ice sculptures | shimmering facets, the Icarus satellite's beam in the sky | auroras |
| 20 | `spySkyfall` | **Skyfall** | a stone lodge on a misty Scottish glen, the old Aston in the drive | mist, a flickering lamp | the glen and the hills |
| 21 | `spyPoisonGarden` | **The poison garden** | a concrete bunker garden, pools, Noh-style stone | still water rippling, drifting mist | the bunker's slanting concrete roofs |

Prefer variety: there are interiors (MI6, Q Branch, the train, the casino, Fort Knox), the sea and islands (Crab Key, Atlantis, Scaramangle's island, the floating palace, the Maiden's Tower), snow and ice (Piz Gloria, the ice palace), space (the station), and night (the croc farm, Skyfall, the Golden Gate in fog).

**Homes:**
- **MI6:** all six Bonds, Admiral M, Dame M, Miss Moneypinny, Eve Moneypinny, Nomee, HEM.
- **Q Branch:** Q, Young Q.
- **Crab Key:** Felix Lighter, Quarrell, Shelley Ryder, Dr. Know, the tarantula.
- **The Orient Express:** Kerim Bay, Tatiana, Rosa Klawb, Red Granite, Kronstine, Hinxx.
- **Fort Knox:** Captain Galore, Goldclaw, Oddjobb.
- **The volcano lair:** Tiger Tanaclaw, Domino, Blowfeld, Largclaw, Fiona Volpeh, the white cat, the piranha.
- **Piz Gloria:** Drako, Contessa Tracy, Kara Milovee, Irma Blunt, Necross (The Living Daylights' cello-case slide across the snowy border lives here too).
- **The crocodile farm:** Sheriff Peppah, Solitaire, Mr. Bigg, Tee Hee, Baron Samedee.
- **Scaramangle's island:** Mary Goodnite, Scaramangle, Nick Knack.
- **Atlantis:** Anya Amaclawva, Stromclawberg, Jawz.
- **The space station:** Holly Goodheart, Hugo Draks, Changg.
- **St Cyril's:** Colomboh, Melina, Kristaclaws, Locke.
- **The floating palace:** Octoclawd, Kamal Khaan, Gobindah.
- **The Golden Gate:** Max Zorrin, Mayday.
- **The casino:** René Mathiss, Vesper Lind, Pam Bouviay, Mr. Wynt, Mr. Kydd, Mr. Whyte, Sanclaws, Le Cypher, Mollacka, the iguana.
- **The satellite dish:** Jack Wayde, Zukclawsky, Natalya, Trevellion, Xenia, Boris.
- **The stealth ship:** Wai Linn, Craver, Stampah.
- **The Maiden's Tower:** Christmas Joules, Elektra Kingg, Renarde.
- **The ice palace:** Jinx, Gravez, Zaoh, Miranda Frosst.
- **Skyfall:** Raoul Silvah.
- **The poison garden:** Palomah, Madeleine Swan, Saffin, Primo, Dominic Grean.

## Mechanics that make it its own universe

1. **Rides** (`Sources/App/Rides.swift`, `SpyRides.swift`):
   - **Heroes:** the **silver Aston Martin DB5** pulls up, the door swings open. Now and then, as a gag, a departing *villain* who hitched a lift is fired out through the roof on the ejector seat.
   - **Villains:** **Scaramangle's flying car**: a 1970s coupé that sprouts wings and a tail fin and lifts off.
   - Q could have Little Nellie, the yellow autogyro, as his own ride (open question: one more ride or keep it to two).
2. **The new face: Bond's recast (compaction).** When a session led by one of the six Bonds compacts, he's **recast**: the gun barrel's white circle closes in on him like an iris, holds on black for a beat, and opens on the next Bond in the same spot, with **"JAMES CLAWD WILL RETURN"** typing out underneath, the line every film's end credits promise. Order One → Two → Three → Four → Five → Six → One, skipping any Bond already leading another session.
   - Recasting is how Bond really "regenerates", and it's the franchise's own running joke (Ski Bond's line, "This never happened to the other fellow"), so it fits.
   - It reuses the Doctor's path whole: `Universe.regenerations` lists the six Bonds (`[0, 1, 2, 3, 4, 5].map { base + StatusStore.heroBase + $0 }`), and `StatusStore.swift:336–349` already handles any universe. The only new code is the effect, `SpyRecast.swift`, drawn at `Overlay.swift:1224` instead of the golden flare when the leader is a Spy character.
   - Only the Bonds recast; everyone else ignores compaction, like non-Doctors.
3. **Set piece: the Golden Gun duel.** Hooked in like Indy shoots first (`Overlay.swift:1143`): when Safari Bond and Scaramangle face off, now and then they turn back to back, walk ten paces apart, turn and fire. Scaramangle's one gold shot misses; Safari Bond's doesn't.
4. **Habits** (`Habits.swift`, the Overlay tick):
   - **Trilby Bond's hat:** at MI6 he tosses his trilby onto the hatstand when he arrives, and takes it back when he leaves.
   - **Jawz gets up:** knocked down, he lies still a moment, then sits up, dusts himself off and grins. He always comes back.
   - **Oddjobb's bowler comes back** to his hand like a boomerang after he throws it.
   - **Nick Knack follows Scaramangle** a step behind, carrying his tray, whenever both are on stage.
   - **Baron Samedee won't stay down:** when he loses a fight he vanishes in violet sparkles and reappears at the edge of the stage, laughing (the last shot of Live and Let Die).
   - **Q's lab:** anyone idling in Q Branch near Q sets off a gadget; a little puff and "Don't touch that!".
5. **Bespoke practice drills** (`SpyDrills.swift`):
   - the Bonds on Q Branch's firing range, at a paper target;
   - Trilby Bond shakes a martini;
   - Q tests a gadget (the briefcase puffs, the umbrella opens);
   - Oddjobb slices a statue's head off with his bowler;
   - Jawz chews through a length of chain;
   - Changg practises kendo strikes;
   - Mayday lifts a barbell;
   - Moneypenny types at her desk.

   Nobody floats cross-legged in meditation (`Drills.swift:54`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one. Commit at the end of each phase (`feat(spy): …`), with a `CHANGELOG.md` entry each phase. Ids are append-only, so **the enum order is the order characters are added**: the tables above are grouped the way fans think of the films, and the enums are appended phase by phase in the order below, with a comment naming each group.

1. **Skeleton:**
   - the `Universe` case and all the wiring (with `ComicTransition.pick` returning nil for plain wipes);
   - **Trilby Bond** (the first hero case) and **Blowfeld** and **Dr. Know** (the first villain cases);
   - MI6 (`spyMI6`), the menu icon, HEM's white dinner jacket, the screen-saver option, Preview support.

   It runs end to end in the app, the window, the screen saver and Clawd Royale.
2. **Core ensemble.** About 36 characters, appended in this order:
   - heroes: Ski Bond to Jumper Bond, Admiral M, Dame M, Q, Miss Moneypinny, Felix Lighter, Shelley Ryder, Captain Galore, Tatiana, Solitaire, Anya, Natalya, Vesper;
   - villains: Rosa Klawb, Red Granite, Largclaw, Goldclaw, Oddjobb, Mr. Bigg, Tee Hee, Baron Samedee, Scaramangle, Nick Knack, Jawz, Hugo Draks, Max Zorrin, Trevellion, Xenia, Le Cypher, Silvah;
   - 8 places: Q Branch, Crab Key, the Orient Express, Fort Knox, the volcano lair, Scaramangle's island, the casino, the satellite dish;
   - homes and nemeses for these.

   It's fine to commit the enum cases first (they show as stand-ins) and draw them in a second commit, as The Clawd Files did.
3. **The rest.** The remaining characters in table order, up to 96, and the other 12 places, with every home filled in. Ends with **the character audit**: every Persona and drawing against the films and this roster, and a mismatches table for you.
4. **Mechanics:** the DB5 and the flying car, the recast, the Golden Gun duel, the habits and the drills.
5. **Transitions:** the 13 `SpyTrip`s (below), wired through `ComicTransition`.
6. **Polish pass** (always before phase 7): the weak-spot list from phases 2–5, split by file and run in parallel, with before-and-after renders for you.
7. **Docs and release:**
   - the README (universe table: the DB5, the recast, the Golden Gun duel; the screen-saver paragraph; a collapsible cast-and-places section; developer notes);
   - `llms.txt` (universe list, `SpyClawd/` and `Spy…`, the recast as a magic variant of regeneration);
   - `Tools/RenderDocs` (`spyLineup`, `roster-james-clawd.png`, `locations-james-clawd.png`, a social preview), `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - the trailer, `REEL=spy` (see Promo);
   - **needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

**Weak-spot list:** started in phase 2 and kept in this plan; nothing is fixed mid-phase. Things to watch from the start: Trilby Bond's trilby vs Q Branch's dummy hat, the kilt's tartan at 72×52 (may need a bold red tartan rather than a fine one), Jinx's orange against Clawd's orange, Le Cypher's scarred eye (tiny), Necross's headphone wire, Dr. Know's metal hands (black gloves can vanish against his suit), the white cat against pale floors.

## Verification

- **Build:** `./build.sh`. The cast-size `precondition` in `Overlay.swift` (`:180`, checked at launch) catches a wrong `heroCount` or `villainCount`. Check `./build.sh --release <version>` before calling a phase done; split any dense `sin`/`cos` expression the type-checker chokes on (`-Xfrontend -warn-long-expression-type-checking=300`).
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Trilby Bond"`;
  - `build/preview fight out.png "Safari Bond" "Francisco Scaramangle"`;
  - `build/preview place out.png "James Clawd"`;
  - the batch sheets, one per Art file. Look at every PNG before showing it: each character reads as who it is, nobody is confusable, no outline gaps.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> spyMI6 spyVolcano`.
- **In the app:**
  - Settings → Universe → James Clawd: new sessions are Bonds, MI6 and allies; subagents include villains and the small fry.
  - The screen saver's Options list it.
  - Random and Clawd Royale reach it, and the menu icon and arch-enemies hold in a Spy place.
- **The recast:** `/compact` in a Claude session led by a Bond: the barrel closes, the next Bond appears, "JAMES CLAWD WILL RETURN" types out. A non-Bond leader doesn't change.

## Transitions (`SpyTrip`, 13)

Each is weighted by who is on screen and where, like `DoctorTrip`.

**Style.** Pixel art throughout, not painted or glossy. The palette is the films' title-designer look: hard black, clean white, a deep gun-barrel red, rich gold, Riviera teal and midnight navy, with flat duotone washes and a little halftone where a wash needs texture. Big bold shapes: circles, silhouettes, spinning wheels. Nothing fine that won't read at window size.

**Ending.** No universe-wide caption: The Clawd Files already has the typewriter, and Bond films don't caption every scene. The place's own label stays.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Gun Barrel** (signature) | White dots slide across black from left to right; the last becomes a circle that opens into a rifled gun barrel framing the old place. A Clawd silhouette walks in, turns and fires; a deep red wash slides down the screen like a curtain (no blood); the barrel wobbles and drops, and the circle opens out on the new place. Longest and rarest. | any time, rarely; the six Bonds |
| 2 | **The Title Sequence** | The old place darkens to silhouettes; duotone colour gels sweep across (teal, magenta, gold), spinning revolver cylinders and a kaleidoscope of the old place turn, a Clawd silhouette tumbles past in slow motion, smoke curls, and the colours drain into the new place. | any time; HEM |
| 3 | **The Revolving Wall** | The scene is a wall panel; it swivels on a centre pivot, showing a moment of secret corridor, and the other side is the new place. | villains in their lairs; the volcano, Atlantis, the stealth ship |
| 4 | **The Crater Lid** | The old place turns into a still lake that slides open like the volcano's steel lid; a rocket rises through the gap and the camera drops into the new place below. | Blowfeld, Largclaw, Tiger Tanaclaw; the volcano lair |
| 5 | **The Ejector Seat** | The DB5's roof pops off and a seat rockets up out of frame; the view follows it up into sky and down, a parachute blooms, and it lands in the new place. | Q, the Bonds; car-friendly places (Skyfall, the Golden Gate) |
| 6 | **The Union Jack Parachute** | A skier sails off a cliff over the old place, freefalls, and a huge Union Jack canopy opens, filling the screen; it floats away to show the new place. | Safari Bond, Anya; snow (Piz Gloria, the ice palace) |
| 7 | **The Laser Table** | A thin red laser creeps across the old place from one side, splitting it; the two halves part like doors on the new place, a little molten gold glinting along the cut. | Goldclaw (needs owner); Fort Knox |
| 8 | **The Roulette Wheel** | The old place shrinks into the bowl of a spinning roulette wheel; the ball clatters round and drops into a pocket, which grows into the new place. | Le Cypher, Mathiss, Vesper, Kamal Khaan; the casino |
| 9 | **The Bowler Hat** | Oddjob's bowler spins across the screen on a curve, slicing the old place in a line; the top half slides off and falls away, the hat comes back the other way. | Oddjobb (needs owner) |
| 10 | **The Hall of Mirrors** | The old place multiplies in a funhouse maze of mirror panels; the panels shatter one by one into glinting shards, each shard showing a bit of the new place, until it's whole. | Scaramangle, Nick Knack; Scaramangle's island |
| 11 | **The Submarine Car** | The white sports car races along the bottom of the old place and drives off a jetty into the sea; the view follows it under, its wheels fold in and fins flick out, it cruises through a blur of bubbles past a fish or two, then surfaces on the new place's shore and the water drains off the screen. | Safari Bond, Q, Stromclawberg; Atlantis, the Maiden's Tower |
| 12 | **The Satellite Beam** | The view pulls up to orbit: a satellite (diamond, GoldenEye or Icarus, by owner) turns its dish, a beam sweeps across a dotted world map, locks on and zooms down through clouds into the new place. | Blowfeld, Trevellion, Boris, Gravez; trips between far-apart places |
| 13 | **The Briefing Slide** | The old place becomes a slide on MI6's briefing screen, projector light flickering; a click, the slide carousel shunts, and the next slide is the new place, which grows to fill the screen. | M, Moneypenny, Q; MI6, Q Branch |

**Left out:**
- **The blood in the gun barrel:** turned into a red curtain wash (tone).
- **The title sequences' dancing silhouettes:** too often nude or suggestive; the title-sequence transition keeps the guns, smoke, gels and kaleidoscope instead.
- **The iris closing on its own:** it's part of the gun barrel and the recast; a third use would wear it out.
- **Jaws biting through the frame:** a fun idea, but it overlaps the bowler hat's slice and works better as his habit.
- **The piranha pool:** swapped out for the submarine car (decided 2026-10-16): more iconic, and a death trap is grimmer than a car that turns into a submarine.
- **The DB5's revolving number plate:** too fine to read at pixel scale.
- **The space-shuttle launch:** overlaps the crater lid's rising rocket.

**Promo.** The Gun Barrel (#1) opens the trailer.

**Check them** with `Tools/Transitions`, which renders all thirteen between two Spy places.

## Promo: the trailer (`REEL=spy`)

Built on `doctorShots` in `Tools/RenderPromo/main.swift`, about 48 seconds.

- **Intro (~9 s): the gun barrel.** Silence, then white dots tick across a black screen with a twangy guitar note on each. The last dot opens into the rifled barrel; Trilby Bond walks in, turns and fires; the red curtain wash slides down; the barrel wobbles and drops. Out of the closing circle, **JAMES CLAWD** swells up in clean white capitals (our own lettering; no gun logo), held on a brass stab, then the circle opens on white.
- **Set piece (~9.5 s): Fort Knox.** Goldclaw's bomb ticks on its trolley among the gold bars; Oddjobb's bowler flies across the shot; the silver DB5 skids in and its ejector seat sends a henchman (Red Granite) through the roof; Trilby Bond squares up to Oddjobb while the timer runs down, and it stops on **0:07**. Goldclaw: "No, Mr. Clawd, I expect you to die!" Trilby Bond straightens his tie.
- **Hook (4 s):** shared, three busy terminals.
- **Desktop (~4.6 s):** `brawl(ctx, .spy, …)`: "Licensed to code."
- **Status (~4.2 s):** Trilby Bond working, Q waiting ("Pay attention!"), Jawz idle (grinning), Blowfeld finished (stroking the cat).
- **Agents (4 s):** "Every subagent gets a licence."
- **Window (~4.8 s):** `windowShot(ctx, .spy, …, at: .spyMI6)`: "Shaken, not stirred." as Trilby Bond's hat lands on the hatstand.
- **AIs (~4.4 s):** the BRING YOUR OWN AI* line-up, one Bond-universe character per AI.
- **End card (~4.2 s):** MI6, the crew lined up, the title lands, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS", the icon and the URL.

**Music:** a twangy surf-guitar riff, big-band brass stabs, a walking bass and a sting on the title, in the sound of a 1960s spy score but entirely **our own notes**. The famous theme's melody, the gun logo and the title-song tunes are never reproduced; their sound is only evoked. Hits land on the dots, the gunshot, the title, the DB5's skid and the end card.

## Decisions (2026-10-16)

All the open questions are settled:
- **Name: James Clawd.**
- **The Bonds:** all six stay, nicknamed for their look: Trilby Bond, Ski Bond (in his ski suit, not the kilt), Safari Bond, Leather Bond, Tank Bond, Jumper Bond.
- **The recast** on compaction stays: the gun barrel closes on one Bond and opens on the next.
- **Scope:** the Eon films only.
- **Renames** (Captain Galore, Dr. Holly Goodheart, Xenia Helicopp, Octoclawd, Shelley Ryder, Dr. Christmas Joules) are all fine.
- **Rides:** just the DB5 and the flying car; no Little Nellie.
- **Transitions:** the submarine car replaces the piranha pool. The Gun Barrel, with the silhouette walking in and firing, stays the signature transition and opens the trailer; the user wants it for sure.
- **Swaps:** none; the cast stands as written.

The plan is ready for phase 1 when you say start.