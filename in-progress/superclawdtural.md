# Plan: a new universe, Superclawdtural (Supernatural parody)
<!-- track: repo=rodclemen/clawd-clash branch=superclawdtural folder=Superclawdtural title="Superclawdtural" source="Supernatural" cast=80 places=20 -->

## Context

Written 2026-10-17 (after 3.6.0); brought up to date 2026-10-23 for the universe-modules folder flow and the "clawd, never claw" naming rule, with Stranger Clawds (4.0.0) the newest universe on `main`. This plan adds a Supernatural parody, the fifteen seasons of the TV series (2005 to 2020), as a full ensemble, built the same way as Doctor Clawd and The Clawd Files. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

| Universe                        | Heroes | Villains | Total | Places | Transitions |
|---------------------------------|--------|----------|-------|--------|-------------|
| Star Clawds                     |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds                |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds                |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd                    |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files                 |     36 |       46 |    82 |     20 |          11 |
| Stevie Clawdberg                |     64 |       54 |   118 |     23 |          10 |
| Clawd of the Rings              |     38 |       38 |    76 |     22 |           9 |
| **Superclawdtural (proposed)**  | **35** | **45** | **80** | **20** | **12** |

(heroCount includes HEM and one agent-only pet, Miracle; villainCount includes three agent-only small fry.)

- **Viability: comfortably viable.** 33 drawn heroes and 42 drawn villains, both well over the 20 threshold. Fifteen seasons of monsters of the week, angels, demons and hunters leave more candidates than slots; the job was picking.
- **Name: Superclawdtural** (chosen on 2026-10-17). The alternatives were Supernaclawd, The Road So Clawd, Team Free Clawd, Carry On Clawd and others.
- **Code naming** avoids the franchise name, as the other universes do:
  - **number 10** in `Sources/App/Universes/NUMBERS` (8 is reserved for Clawd Burton, 9 is Stranger Clawds), so ids are 10000 and up;
  - key `hunters`, folder `Sources/App/Universes/Superclawdtural/`, prefix `Hunt` (`HuntRoster.swift`, `HuntHero`, `huntTheme`), reel `hunters`; no file, type or key in the repo uses any of them today;
  - branch `superclawdtural`, off `main`.
- **Naming style:** light puns on the on-screen names, kept where they read at a glance, and every pun says "clawd", never a bare "claw" (the rule from 2026-10-22; Crowley is Clawdley even though The Clawd Files has a Tad O'Clawdley, the owner's call on 2026-10-23): **Winclawdster** for the family, **Clawdstiel**, **Clawdley**, Bobby **Clawdsinger**, Garth **Fitzclawd** IV, Charlie **Clawdbury**, Rowena **MacClawd**, **Balthaclawds**. Where a pun would be forced, the real or near name (Metatron, Ruby, Jack Klyne). Actors' names are never used.
- **Scope:** the fifteen seasons only. The prequel *The Winchesters* and the *Wayward Sisters* pilot are left out.
- **Size:** 80 characters (about The Clawd Files' size) and 20 places.

### How the cast is split

The show is about hunters against monsters, so the split is mostly easy: hunters, their friends and the angels who side with them are heroes; demons, the angels who turn on humanity, the cosmic Big Bads, the human villains and the monsters of the week are villains. The rule for the grey ones is **where they end up**:
- **Rowena → hero.** A villain early on, but she ends as an ally, becomes Queen of Hell and gives her life for the boys.
- **Gabriel → hero.** The Trickster's pranks turn into his stand against Lucifer, and he comes back to fight alongside them.
- **Clawdley → the lead villain.** Fans love him and he helps now and then, but he's the King of Hell for most of the run.
- **Meg, Ruby → villains.** Both help the brothers for a while, as demons with their own plans.
- **Ketch, Lady Bevell → villains.** The British Men of Letters; Ketch comes round late, but the show frames them as the enemy.
- **Gordon Walker → villain.** A hunter who hunts Sam, then becomes a vampire.
- **Death and Billie → villains.** Neither is evil, but both stand against the brothers when it counts.
- **Demon Dean** is a villain of his own, separate from Dean.

### Tone: what's left out, and why

The show is full of gore, torture and dark themes. Clawd Clash is a desktop toy, so:
- **Left out entirely:**
  - the Benders, a human cannibal family (left out for the reason The Clawd Files left out the Peacocks);
  - real people: Hitler and the Thule episodes, Eliot Ness, Bonnie and Clyde;
  - "The French Mistake" and anything about the actors;
  - the Scooby-Doo crossover (a trademark).
- **Kept, but tamed:**
  - Alastair is a menace with white eyes, never a torturer; nothing of Hell's rack is shown;
  - Lilith is drawn as the pale woman in white, not her child vessel;
  - God (Chuck) and Lucifer are fictional characters, played the way the show plays them: a scruffy writer with a guitar, a smirking man in a grey jacket;
  - deaths are cartoonish: the compaction mechanic drags its leader off and brings them back, nothing worse;
  - the shapeshifter sheds its skin like a costume, never gory; Bloody Mary appears in her mirror, eerie rather than bleeding.
- **Not drawn, for too little on screen or no signature:** Hannah, Samandriel, Adam Milligan, Linda Tran, Kaia.
- **The Wendigo** is left out: The Clawd Files already has a character called The Wendigo, and the names would clash in Clawd Royale.
- **Overlaps with the other universes:** vampires, ghosts and a cemetery also show up in Clawd Slayer and The Clawd Files. This universe keeps its own look: flannel and denim hunters, black-eyed demons in suits, angels in trench coats, and a palette of rust, amber, Impala black and dusty denim blue. Its graveyard is flat Kansas Stull, not a gothic crypt.

## Your folder (the universe-modules flow, clawdify_guide.md Step 7)

Nothing outside `Sources/App/Universes/Superclawdtural/` changes, except the owner's `NUMBERS` line on `main`. It starts as the template, through `Tools/new-universe.sh Superclawdtural Hunt hunters "Superclawdtural" 10`.

| File | What it holds here |
|---|---|
| `universe.conf` | number 10, key `hunters`, title Superclawdtural, prefix `Hunt`, entry `HuntUniverse`, reel `hunters`, cask empty |
| `HuntFacts.swift` | `HuntHero` and `HuntVillain` (append-only, enum order as in Cast, `hem` last), agent-only (Miracle, the hellhound, the Leviathan blob, the demon smoke), Claude's side heroes, rivals Death and Billie, compaction `.away` for Dean, Sam, Clawdstiel, Bobby and Jack |
| `HuntUniverse.swift` | the module (below) |
| `HuntRoster.swift` | the persona dictionaries, `Location.huntHome(of:)`, nemeses, the ride closure, `huntTheme`, the place keys, `huntPlaces` |
| `HuntHem.swift` | HEM: flannel, a trucker cap, Dean's amulet on his chest, a rock-salt shotgun |
| `HuntIcon.swift` | the menu bar icon: a devil's trap, or the Impala's front end |
| `HuntKit.swift` | shared art helpers: flannel, leather jackets, trench coats, wing shadows, black demon eyes |
| `Art/HuntHeroes1…4.swift`, `Art/HuntVillains1…5.swift` | 8 to 10 personas a file |
| `Places/HuntScenes1…N.swift` | the 20 places |
| `HuntRides.swift` | Baby, the '67 Impala, a `Ride` that drives in |
| `HuntBackFromHell.swift` | the compaction look (`CompactionLook`) |
| `HuntDrills.swift` | the devil's trap and angel blade drills |
| `HuntWipes.swift` + `Hunt<Name>Trip.swift` | the twelve trips, one file each past a handful, as Slayer does |
| `Promo/HuntReel.swift`, `Promo/HuntShowcase.swift` | the trailer and the showcase pictures (phase 6) |

**The module's members:** `theme`, `places`, `hem`, `preview` (written); `transitions` (the template's one trip until phase 5); `playgroundPrompts` (below); `meditation: .never`; `compactionLook` (Back from Hell); `quirks.remark` for "Jerk." "Bitch."; `rides`; `drills`; `docs` (phase 6). Left at their defaults: `poseStyle`, `moonwalkers`, `swingLine`, `placeCaption`, `regeneration`, `shootOuts`.

**Engine requests:** one, for phase 4. **Clawdstiel's personal space** (he vanishes with a flutter of wings and turns up right behind the nearest hero) needs a character to jump to a spot on stage, which no quirk can do. It goes on `main` as a general hook, its own commit, before the folder uses it. If it isn't built, the habit is dropped and his wing shadows stay his signature. The Impala's radio burst has no sound in the app; it lives in the trailer only.

**Playground prompts** (the module's `playgroundPrompts`):
1. "Salt the doorways before the build runs."
2. "Find out what's haunting the test suite and burn its bones."
3. "Check the lore in the Bunker's library for this stack trace."
4. "Gas up the Impala and drive the deploy to Kansas."
5. "Paint a devil's trap round the flaky test."

## Cast

Each entry gives the parody name, look, weapon or motion, signature move and callout. How the engine's weapons map onto the show:
- **`.blaster` + `.bullet`** is the hunters' main weapon: pistols and shotguns (rock salt is drawn as a pale tracer). Shotguns and pistols are told apart by the drawing, not the shot.
- **`.saber`** for angel blades, the First Blade, machetes, knives, fangs, claws, hooks and scythes.
- **`.blaster` + `.thrown(colour)`** for Jo's throwing knives (silver).
- **`.blaster` + `.fire`** for Dagon.
- **`.lightning` + `Magic`** for angels, demons and gods:
  - **smiting and touch powers** are `touch` (a glowing hand, and a glow round the target);
  - **demonic telekinesis and mind powers** are `rings` in the colour of the demon's eyes (yellow, red, white);
  - **archangels** get a full stream (Lucifer jagged, Michael steady);
  - **witchcraft and Trickster magic** are `spell` ribbons;
  - **Pestilence and Jack** are `waves`.
- **`.none`** for the talkers, psychics, prophets and nerds: Ash, Kevin, Missouri, Pamela, Becky, Henry, the Ghostfacers, Frank, Tessa, Eve, Famine, the Crossroads Demon.
- **`bulk`** for Ramiel.
- **`motion: .hover`, `canSit: false`** for the Woman in White.
- **Wing shadows:** angels show their wings only as a shadow cast behind them, the way the show does it.
- Everyone is Clawd in costume on Clawd's four legs, as in every universe.

**Every caster looks different** (this universe and across the others):

| Caster | Look |
|---|---|
| Clawdley | `touch`, red fingertip, red glow round his target |
| Azazel | `rings`, yellow |
| Alastair | `rings`, white |
| War | `rings`, deep red (normal speed: owner chose not to add a slow setting) |

| Lilith | jagged, white |
| Asmodeus | jagged, yellow |
| Lucifer | jagged, white core, red glow |
| Michael | steady, white core, gold glow |
| Raphael | jagged, white, thick forks |
| Zachariah | `touch`, blue-white |
| Naomi | `touch`, white, a needle-thin point |
| Chuck | `touch`, warm white |
| Death | `touch`, grey-black |
| Bloody Mary | `touch`, dark red |
| The Woman in White | `touch`, pale blue |
| The Djinn | `touch`, bright blue, his tattoos lit |
| Metatron | `spell`, gold |
| Rowena | `spell`, red sparks |
| Gabriel | `spell`, candy pink |
| Amara | steady, black-violet, wavering like smoke |
| Pestilence | `waves`, sickly green |
| Jack | `waves`, gold |

Checked against the other universes: Detective Clawds' Constantin has a gold `spell`, so Metatron's gold ribbon is thinner and paler; Doctor Clawd's and The Clawd Files' `touch` users are green and teal.

### Heroes (35)

**Team Free Will (4)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Dean Winclawdster | brown leather jacket over a flannel shirt, short hair, the amulet | Colt M1911, pearl grip (bullet) | pulls out a slice of pie and takes a huge bite | "Son of a…!" |
| 2 | Sam Winclawdster | tall, long brown hair, flannel over a hoodie | Ruby's demon knife (saber) | opens his laptop, types, sweeps his hair back | "Jerk." |
| 3 | Clawdstiel | beige trench coat, blue tie askew, dark hair | angel blade (saber) | his wing shadows spread across the wall, then fold | "Hello, Dean." |
| 4 | Jack Klyne | tan jacket, young face | Nephilim force (lightning, gold `waves`) | eyes glow gold, then he grins and eats nougat | "I'm Jack." |

**The Winclawdster family (3)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 5 | Mary Winclawdster | blonde, leather jacket | pistol (bullet) | pushes her hair back and checks the clip | "Angels are watching over you." |
| 6 | John Winclawdster | worn leather jacket, stubble | the Colt (bullet) | writes in his journal | "Take care of Sammy." |
| 7 | Henry Winclawdster | 1958 suit and fedora, the Men of Letters key | none | tips his fedora and shows the key | "Men of Letters." |

**Hunters (14)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 8 | Bobby Clawdsinger | trucker cap, grey beard, vest over flannel | shotgun with rock salt (bullet) | takes a swig from his flask of holy water | "Idjits." |
| 9 | Ellen Harvell | dark hair, Roadhouse apron over flannel | shotgun (bullet) | racks the shotgun | none |
| 10 | Jo Harvell | blonde, young, denim jacket | throwing knives (thrown, silver) | throws a knife into a dartboard | none |
| 11 | Rufus Turner | flat cap, older, cardigan | pistol (bullet) | pours a glass from a blue-label bottle | none |
| 12 | Garth Fitzclawd IV | very thin, big ears, a sock puppet | pistol (bullet) | Mr. Fizzles pops up on his hand and talks | "Mr. Fizzles says hi!" |
| 13 | Sheriff Jody Mills | tan sheriff's uniform, badge | service pistol (bullet) | holds up her badge | none |
| 14 | Sheriff Donna Hanscum | blonde, sheriff's parka, a box of donuts | service pistol (bullet) | eats a donut | "Oh, ya!" |
| 15 | Claire Novak | blonde, black leather jacket | machete (saber) | spins the machete | none |
| 16 | Alex Jones | dark hair, nurse's scrubs | pistol (bullet) | none | none |
| 17 | Eileen Leahy | dark hair, green jacket | pistol (bullet) | signs "hi" with a big wave of the hand | none |
| 18 | Charlie Clawdbury | red hair, geeky t-shirt, laptop | LARP sword (saber) | raises the sword as Queen of Moondoor | "Queen of Moondoor!" |
| 19 | Ed Zedmore | Ghostfacers jacket, camcorder | none | points the camcorder, its light blinking | "Ghostfacers!" |
| 20 | Harry Spangler | Ghostfacers jacket, EMF reader | none | waves the EMF meter, its lights jumping | none |
| 21 | Frank Devereaux | flat cap, paranoid glare, a stack of phones | none | snaps a SIM card in half | none |

**Friends and allies (12)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 22 | Ash | mullet, cut-off sleeves, laptop | none | his laptop lights blink "Dr. Badass" | "Dr. Badass." |
| 23 | Kevin Tran | hoodie, the glowing angel tablet | none | the tablet glows and its writing scrolls | none |
| 24 | Benny Lafitte | flat cap, Purgatory-dirty jacket | machete and fangs (saber) | grins, and his fangs drop | none |
| 25 | Missouri Mosley | purple blouse, beads | none | swats someone with the back of her hand | none |
| 26 | Pamela Barnes | dark curls, sunglasses | none | séance: candles flare round her | none |
| 27 | Becky Rosen | glasses, hugging a book | none | squeezes her favourite book series to her chest | "Sam!" |
| 28 | Victor Henriksen | FBI suit and tie | pistol (bullet) | holds up his FBI badge | none |
| 29 | Mick Davies | tidy British suit | pistol (bullet) | none | none |
| 30 | Tessa | dark hair, reaper's black coat | none | holds out a hand, softly | none |
| 31 | Gabriel, the Trickster | brown jacket, lollipop | Trickster magic (lightning, pink `spell`) | snaps his fingers and a candy bar appears | "Heya, Sammy!" |
| 32 | Balthaclawds | low V-neck, smug, wine glass | angel blade (saber) | sips wine, his wing shadows spreading | none |
| 33 | Rowena MacClawd | red hair, green velvet gown | spells (lightning, red `spell`) | throws a hex bag; red sparks fly | "Boys." |

**Agent-only and HEM (2)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 34 | Miracle (agent-only) | the shaggy dog from season 15 | none | wags, and chases its tail |
| 35 | **HEM** | flannel shirt, trucker cap, Dean's amulet, a rock-salt shotgun | shotgun (bullet) | spins the shotgun |

### Villains (45)

**Demons (13)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 1 | Clawdley | black suit and overcoat, goatee | power over Hell (lightning, red `touch`) | snaps his fingers with a red flash, and Juliet the hellhound appears at his heel (a shadow dog with red eyes, since hellhounds can't be seen in the show) | "Hello, boys." |
| 2 | Azazel | plain jacket, yellow eyes | telekinesis (lightning, yellow `rings`) | his eyes flash yellow | "Hey, Sammy." |
| 3 | Meg Masters | dark hair, leather jacket, black eyes | knife (saber) | her black eyes flick on | "Hey, Clarence." |
| 4 | Ruby | brunette, leather jacket | demon knife (saber) | twirls the knife | none |
| 5 | Lilith | the pale woman in white | white blast (lightning, white) | her eyes go white | none |
| 6 | Alastair | grey suit, white eyes | telekinesis (lightning, white `rings`) | his white eyes open slowly | none |
| 7 | Abaddon | red hair, black dress | telekinesis (lightning, red, steady) | purrs, eyes black | none |
| 8 | Cain | cardigan, beard, beekeeper | the First Blade (saber) | bees swirl round him | none |
| 9 | Asmodeus | white suit, cane, yellow eyes | lightning, yellow | twirls his cane | none |
| 10 | Dagon | black dress, yellow eyes | fire (fire) | a flame blooms in her palm | none |
| 11 | Ramiel | fisherman's vest, the Lance of Michael, `bulk` | Lance (saber) | casts a fishing line | none |
| 12 | Demon Dean | Dean with black eyes and the Mark of Cain glowing red | the First Blade (saber) | sings karaoke into a microphone | none |
| 13 | The Crossroads Demon | red dress, red eyes | none | buries a little box at the crossroads | "Do we have a deal?" |

**Angels (8)**

| # | Name | Look | Weapon | Signature | Callout |
|---|---|---|---|---|---|
| 14 | Lucifer | grey jacket, red eyes | archangel power (lightning, red glow, white core) | red-lit wing shadows spread | "Hello, Sam." |
| 15 | Michael | dark suit, white glow | archangel power (lightning, white-gold, steady) | a burst of light, and wing shadows | none |
| 16 | Zachariah | grey office suit, balding | smite (lightning, `touch`) | checks his watch | none |
| 17 | Uriel | stern, dark coat | angel blade (saber) | none | none |
| 18 | Raphael | dark suit, imposing | lightning, jagged white | thunder cracks behind him | none |
| 19 | Naomi | red hair, prim business suit | mind wipe (lightning, `touch`) | none | none |
| 20 | Metatron | sweater, glasses, typewriter | angel tablet (lightning, gold `spell`) | types on his typewriter | none |
| 21 | Gadreel | plain jacket | angel blade (saber) | none | none |

**Big Bads (9)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 22 | Dick Roman | slick business suit, a big smile | Leviathan bite (saber) | his smile splits into a huge Leviathan mouth |
| 23 | Eve | red hair, Mother of All | none | a little monster crawls out of her hand |
| 24 | Amara | dark hair, black dress | the Darkness (lightning, black-violet, steady) | black mist swirls round her |
| 25 | Chuck | scruffy beard, bathrobe, guitar | God's snap (lightning, `touch`) | strums the guitar |
| 26 | War | red suit | sows strife (lightning, red `rings`) | turns his ring |
| 27 | Famine | frail old man with a cane | none | breathes in a green mist |
| 28 | Pestilence | sickly, green tinge | plague (lightning, green `waves`) | coughs a green cloud |
| 29 | Death | tall, thin, black suit, cane | deadly touch (lightning, `touch`) | eats a chili dog with a knife and fork |
| 30 | Billie | reaper's long black coat, scythe | scythe (saber) | turns an hourglass |

**Human villains (4)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 31 | Lady Toni Bevell | British, tweed and pearls | pistol (bullet) | none |
| 32 | Arthur Ketch | black suit, a lot of weapons | pistol (bullet) | straightens his tie |
| 33 | Gordon Walker | hunter's jacket, later a vampire | machete (saber) | sharpens the machete |
| 34 | Bela Talbot | chic, short dark hair | pistol (bullet) | none |

**Monsters of the week (8)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 35 | The Alpha Vampire | 1800s coat, fangs | fangs (saber) | his fangs drop slowly |
| 36 | Bloody Mary | dark-haired ghost in a mirror frame | `touch` | appears in a mirror, then vanishes |
| 37 | The Woman in White | white dress, `hover`, `canSit: false` | `touch` | flickers out and back on the road |
| 38 | The Hookman | preacher's coat, a hook for a hand | hook (saber) | scrapes the hook |
| 39 | The Shapeshifter | silver-eyed lookalike | knife (saber) | his eyes flash silver, like on a camera |
| 40 | The Djinn | glowing blue tattoos | `touch`, blue | the tattoos ripple |
| 41 | The Clown | rainbow wig, red nose (the Rakshasa) | claws (saber) | honks its nose |
| 42 | The Scarecrow | the pagan god on its post, a scythe | scythe (saber) | its head turns slowly |

**Agent-only small fry (3)**

| # | Name | Look |
|---|---|---|
| 43 | Hellhound | a shadow dog with red eyes, low to the ground |
| 44 | Leviathan blob | a lump of black goo with a toothy grin |
| 45 | Demon smoke | a twisting wisp of black smoke, red flicker inside (`hover`, `canSit: false`) |

### Telling them apart

- **Dean and Demon Dean:** the same jacket; Demon Dean has black eyes, the glowing red Mark on his forearm and the jawbone blade.
- **The hunters with guns:** Dean's pearl-grip pistol, Bobby's cap and shotgun, Ellen's apron and shotgun, Jody's and Donna's uniforms (tan, and a parka with donuts), John's journal, Mary's blonde hair.
- **The Ghostfacers:** Ed's camcorder, Harry's EMF meter.
- **The suits:** Clawdley black with a goatee; Zachariah grey and balding; Dick Roman slick with the grin; Death tall and thin with a cane; Ketch black with weapons; Michael dark with a white glow.
- **The redheads:** Rowena in green velvet, Abaddon in black, Naomi in a prim suit, Charlie in a t-shirt, Eve barefoot and wild.
- **The reapers:** Tessa has no scythe; Billie carries one.
- **Against the other universes:** Clawdstiel and Detective Clawds' Constantin both wear beige trench coats: Constantin is blond with a cigarette; Clawdstiel has dark hair, a crooked blue tie and wing shadows. The Clown is not a Joker: a rainbow wig and a red nose, no purple. The Clawd Files' trench coats (Fox Clawder, HEM's costume there) are grey-brown with a lanyard.

### Nemeses

Each pair faces off first on the same stage:
- Dean Winclawdster ↔ Michael
- Sam Winclawdster ↔ Lucifer
- Clawdstiel ↔ Metatron
- Jack Klyne ↔ Chuck
- John Winclawdster ↔ Azazel
- Mary Winclawdster ↔ Lady Toni Bevell
- Bobby Clawdsinger ↔ Clawdley
- Charlie Clawdbury ↔ Dick Roman
- Kevin Tran ↔ Gadreel
- Gabriel ↔ Asmodeus
- Benny Lafitte ↔ Eve
- Victor Henriksen ↔ Lilith
- Henry Winclawdster ↔ Abaddon
- Mick Davies ↔ Arthur Ketch

**Rivals:** Death and Billie never lead two sessions back to back (two Deaths in a row).

**Claude's side:** the heroes (the default).

**Enum order** is as listed. Dean, Sam and Clawdstiel come first among the heroes and Clawdley first among the villains, so the skeleton is drawn first. `hem` is always the last hero.

## Places (20)

Each is a `Place` with a still picture and a moving layer, plus tall-canvas extras for the screen saver. The palette: rust, amber, Impala black, dusty denim blue, motel-sign neon, with red Hell, black Empty, orange Apocalypse and green Purgatory standing apart. Keys all start with `hunt`, like Slayer's `slayer…`, checked unique across the repo and the `buffy` branch.

| # | Key | Place | Still | Moving | Tall-canvas extras |
|---|---|---|---|---|---|
| 1 | `huntBunker` | **The Bunker's war room** (default) | the glowing map table, art deco lamps, library shelves, iron stairs up to the door | the map table's lights pulse, a lamp flickers | the shelves rise two levels, a balcony, the door at the top of the stairs |
| 2 | `huntSalvage` | **Singer Salvage**, at dusk | rusty cars stacked, Bobby's house and porch, the SINGER SALVAGE sign | the crane's hook sways, the porch light flickers | towers of cars, a water tower |
| 3 | `huntRoadhouse` | **Harvelle's Roadhouse** | a wooden bar, a pool table, the dartboard with knives in it | neon beer signs flicker, a ceiling fan turns | rafters with hanging lanterns |
| 4 | `huntMotel` | **A motel room** | wild patterned wallpaper, two beds, a line of salt at the door | the VACANCY sign blinks through the blinds, the TV glows | more wallpaper, duck paintings, a water stain |
| 5 | `huntLawrence` | **The house in Lawrence, Kansas**, at night | a two-storey house, the lawn, one lit window upstairs | the window light flickers, leaves blow | the old tree, the night sky |
| 6 | `huntCrossroads` | **The crossroads** | a dirt crossroads, one dead tree, flat fields | dust blows, a crow shifts on the branch | a big moon and stars |
| 7 | `huntStull` | **Stull Cemetery**, in a storm | the ruined stone church, headstones, the Impala parked | lightning flashes, a grave burns (salt and burn) | storm clouds |
| 8 | `huntHell` | **Clawdley's Hell** | the throne room in red stone, the throne, Crowley's endless queue | the queue shuffles forward, embers drift | a vaulted ceiling, chains |
| 9 | `huntHeaven` | **Heaven's garden** | white light, one great tree, a fountain, mid-green grass | leaves fall, the light shimmers | a blinding sky, a doorway of light |
| 10 | `huntPurgatory` | **Purgatory** | dark woods in mist | red and gold eyes blink between the trees | tall trees |
| 11 | `huntEmpty` | **The Empty** | a black void, pools of black goo, faint violet | goo drips | sleeping shapes in the dark |
| 12 | `huntRoad` | **The open road**, at night | a two-lane road's shoulder, the Impala's trunk open on the lit arsenal, telephone poles | headlights pass, the trunk light flickers | a big starry Kansas sky |
| 13 | `huntAsylum` | **Roosevelt Asylum** | a peeling green corridor, an old wheelchair | a flashlight beam sweeps, a door swings | a high cracked ceiling |
| 14 | `huntDiner` | **A roadside diner**, by day | the counter, booths, the pie case | the pie case turns, coffee steams | the menu board, ceiling fans |
| 15 | `huntRoman` | **Roman Enterprises** | the top floor of a glass tower, the city at night | city lights twinkle, a drip of black goo | the tower rising above |
| 16 | `huntApocalypse` | **Apocalypse World** | a burnt-out city, an orange sky | ash falls | smoke columns, a wing shadow in the clouds |
| 17 | `huntMoondoor` | **Moondoor**, the LARP field, sunny | tents, banners, a cardboard castle | flags flap | trees and clouds |
| 18 | `huntOrchard` | **The Burkitsville orchard**, at sunset | apple trees, the scarecrow on its post | crows hop, the scarecrow sways | the sunset sky |
| 19 | `huntChucks` | **Chuck's house** | a messy writer's study, empty bottles, a desk piled with manuscripts | the desk lamp, pages stirring | bookshelves |
| 20 | `huntSiouxFalls` | **Jody's house, Sioux Falls** | a cosy kitchen, family photos, a gun rack | the clock ticks, a curtain moves | the upstairs landing |

Rules from the guide's Look and style apply: the bottom `floorRows` and the band above stay plain and mid-to-dark so the crew and their labels read; busy detail goes high and to the sides; Heaven's grass and the diner's floor are kept mid-tone rather than white.

### Homes

| Place | Heroes | Villains |
|---|---|---|
| Bunker | Dean, Sam, Clawdstiel, Jack, Henry, Kevin, Eileen, Mick, Miracle, HEM | Ketch, Lady Bevell (both broke in; Ketch lived there later) |
| Singer Salvage | Bobby, Rufus, Garth, Frank | |
| Roadhouse | Ellen, Jo, Ash, Pamela | Demon Dean (a bar and a karaoke mic) |
| Motel room | Henriksen | Bela, Ruby |
| Lawrence | John, Mary, Missouri | Azazel |
| Crossroads | | the Crossroads Demon, Meg, Ramiel, the hellhound |
| Stull Cemetery | | Lucifer, War, Pestilence |
| Clawdley's Hell | Rowena (Queen of Hell) | Clawdley, Lilith, Alastair, Abaddon, Asmodeus, Dagon, the demon smoke |
| Heaven | Gabriel, Balthaclawds, Tessa | Zachariah, Uriel, Raphael, Naomi, Gadreel |
| Purgatory | Benny | Eve, the Alpha Vampire, the Djinn |
| The Empty | | Billie, Amara |
| Open road | | the Woman in White, the Hookman, Gordon |
| Roosevelt Asylum | Ed, Harry | Bloody Mary, the Shapeshifter, the Clown |
| Diner | | Death (chili dogs), Famine |
| Roman Enterprises | | Dick Roman, the Leviathan blob |
| Apocalypse World | | Michael |
| Moondoor | Charlie | |
| Orchard | | the Scarecrow, Cain (his farm and bees) |
| Chuck's house | Becky | Chuck, Metatron |
| Sioux Falls | Jody, Donna, Claire, Alex | |

## Mechanics that make it its own universe

1. **The ride: Baby, the '67 Impala** (`HuntRides.swift`, a `Ride` that drives in, listed in the module's `rides` and picked by the theme's `ride:` closure). It drives in along the ground, headlights on, windows down (the radio's classic-rock burst is the trailer's; the app has no sound). It stops, the crew gets in or out, and the trunk lid swings up on the arsenal for a moment as they go. Everyone rides it.
2. **Back from Hell: the compaction mechanic.** The Winchesters never stay dead. When a Claude Code or pi session led by **Dean, Sam, Clawdstiel, Bobby or Jack** compacts its context, its leader is dragged down by hellhound claws: red scratches across the ground, and they sink in a red glow. A moment later a fist punches up through the ground (Dean's grave, season 4), they climb out, dust themselves off, and the caption reads **BACK FROM HELL**. A session losing its memory and coming back as itself is exactly how the show treats death. It's `compaction: .away` for the five in `HuntFacts.swift`, on the same clock as Clawdberg's 88 mph, and `HuntBackFromHell.swift` is the module's `compactionLook` (its `caption`, `alpha`, `lift` and `layers`). Everyone else ignores compaction.
3. **Habits:**
   - **Clawdstiel's personal space.** Now and then he vanishes with a flutter of wings and turns up right behind the nearest hero, standing too close. **Engine request** (see Your folder): built on `main` first, or dropped.
   - **"Jerk." "Bitch."** With Sam and Dean both on stage and idle, now and then Sam says "Jerk." and Dean answers "Bitch." Done with the module's `quirks.remark`: Sam's line and Dean's answer timed off the same clock, so Dean answers a beat later.
4. **Bespoke practice drills** (`HuntDrills.swift`, the module's `drills`):
   - the hunters spray-paint a devil's trap on the floor and check it;
   - the angels practise with their angel blades, wing shadows flaring.

   Nobody floats cross-legged in meditation (`meditation: .never`): hunters, angels and demons don't, and Rowena is the only witch.

## Phases

Each phase builds, is checked with Preview sheets and `Tools/CheckUniverse/check.sh Superclawdtural`, and is shown to you before the next one. One commit per phase (or two: stand-ins, then the art), scoped `feat(hunters)`. The changelog and README text is gathered in the hand-off, not written into `CHANGELOG.md` until after the merge (guide Step 8).

1. **Skeleton:**
   - the owner's `10 hunters Superclawdtural reserved` line in `NUMBERS` on `main`, then the branch;
   - `Tools/new-universe.sh Superclawdtural Hunt hunters "Superclawdtural" 10`;
   - the template's samples turned into Dean, Sam and Clawdstiel, and Clawdley (the enums' first cases);
   - the Bunker's war room, the menu icon, HEM's costume, the facts.

   It runs end to end in the app, the window, the screen saver and Clawd Royale, with the template's one trip until phase 5.
2. **Core ensemble.** About 35 characters:
   - Team Free Will, the Winclawdster family, Bobby, Ellen, Jo, Ash, Charlie, Kevin, Gabriel, Rowena;
   - the demons, Lucifer, Michael, Zachariah, Metatron, Dick Roman, Chuck, the Horsemen and Death;
   - 8 places: the Bunker, Singer Salvage, the Roadhouse, the motel room, the crossroads, Stull, Clawdley's Hell, Heaven; with homes and nemeses for these.

   The enum cases can go in first as stand-ins and be drawn in a second commit, as The Clawd Files did.
3. **The rest:** all 80 characters and 20 places, every home filled in. Ends with **the character audit**: every weapon, shot, magic, motion, signature and callout checked against the show and this plan; a mismatches table for your OK.
4. **Mechanics:** the Impala, Back from Hell, the habits and the bespoke drills.
5. **Transitions:** the twelve `HuntTrip`s, through the module's `transitions`.
6. **Polish pass** (always before docs): every weak spot noted in phases 2 to 5, split by file and fixed in parallel, with before-and-after renders for your OK.
7. **Trailer and hand-off** (guide phase 6, once it's complete): the trailer `Promo/HuntReel.swift` (`REEL=hunters`, storyboard first), the showcase `Promo/HuntShowcase.swift`, the module's `docs` (the desktop line-up and the social preview), `check.sh` with no ✗, and the changelog and README text in the hand-off.
8. **The owner's steps, after the merge:** `CHANGELOG.md`, the README's universe section and table, `llms.txt`, the docs pictures (RenderDocs), the `cask` line, `NUMBERS` from `reserved` to `shipped`, and the release, 5.0.0 by the version rule. **Needs your OK first, since it's public:** pushing, a showcase repo, a cask, releasing.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

**Weak spots to expect** (note them as they come up, fix them in the polish pass): wing shadows reading as a dark smudge rather than wings; black demon eyes being two pixels; the Mark of Cain and Dean's amulet being tiny; Garth's sock puppet and Death's chili dog at agent size; the fourteen gunners' pistols and shotguns blurring together; the motel wallpaper fighting the crew for attention; the Empty and Purgatory being too dark for outlines; the Woman in White's flicker at the frame's edge.

## Verification

- **Build:** `./build.sh --no-install` (the copy in `build/`, leaving the installed app and hooks alone). `Tools/CheckUniverse/check.sh Superclawdtural` every phase; its "slow to type-check" line before calling a phase done.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Dean Winclawdster"`;
  - `build/preview fight out.png "Sam Winclawdster" "Lucifer"`;
  - `build/preview place out.png "Superclawdtural"`;
  - `build/preview edges out.txt "Superclawdtural"`: everything it lists must be on purpose (shots, thrown knives, the demon smoke leaving);
  - and the batch sheets, one per Art file. Look at the PNGs before showing them.
- **Pull request guard:** `python3 scripts/pr-guard.py main HEAD` before any PR.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions <outdir> huntBunker huntRoadhouse`.
- **In the app:**
  - Settings → Universe → Superclawdtural: sessions are heroes, subagents include villains and small fry;
  - the screen saver's Options list it;
  - Random and Clawd Royale reach it, and Settings → Universes can uncheck it and check it again.
- **Back from Hell:** `/compact` in a Claude session led by Dean.

## Transitions (`HuntTrip`, 12)

Each is weighted by who is on screen and where, like `DoctorTrip`.

**Style.** Everything in the app's pixel art. The palette is rust, amber, Impala black, dusty denim blue and motel-sign neon, with hellfire red, angel white and demon-smoke black as accents. Film grain on The Road So Far and the Ghostfacers Cam; nothing glossy.

**Finishing touch: none.** The show opens scenes with place captions ("LAWRENCE, KANSAS"), but The Clawd Files already ends every trip with exactly that, a typewritten place name, so it's left out.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Road So Far** (signature opening) | The picture turns to grainy film; **THE ROAD SO FAR** stamps on in big letters; the old place and others flash past as jumpy film stills; the title smoulders in on black like burning letters; then the card **NOW**, and the new place. The longest and rarest. | Dean, Sam |
| 2 | **Headlights** | Night falls on the old place, the Impala drives across, and its headlight beams sweep the new place into view. | Dean · turf: open road |
| 3 | **Salt and Burn** | Flames rise from the bottom like a grave set alight and burn the old place away; the new one shows through as the smoke clears. | Bobby, John, Ellen · turf: Stull |
| 4 | **Devil's Trap** | A red devil's trap paints itself on the screen and spins; the new place opens in the centre and grows to fill the frame. | Sam, Bobby · turf: Bunker |
| 5 | **Smoke Out** | A column of black demon smoke bursts up out of the old place the way it leaves a host's mouth, roaring and twisting. It fills the screen and thrashes, then funnels down in one tight stream and pours into the new place, which clears as the last wisp goes in. A red flash at the end, like demon eyes flicking on. | Clawdley, Meg, Ruby, Azazel, the demons · turf: Hell, Crossroads |
| 6 | **Angel Light** | The lights flicker and the bulbs pop; a blinding white light rises; huge wing shadows spread across the screen and fade on the new place. | Clawdstiel, Gabriel, the angels · turf: Heaven |
| 7 | **Hellhound** | Claw marks rip across the old place one after another, red eyes in the dark, and the tears open on the new place. | Clawdley, Lilith · turf: Crossroads |
| 8 | **Cold Spot** | The lights flicker, frost creeps in from the corners, breath-fog and all; the frost cracks and falls away onto the new place. | the ghosts (Woman in White, Bloody Mary, the Hookman) · turf: Asylum, Stull |
| 9 | **Ghostfacers Cam** | The camcorder's viewfinder with a red REC dot; static; a ghost flickers past the lens; the picture comes back on the new place. | Ed, Harry · turf: Asylum |
| 10 | **Motel Wallpaper** | The motel's wild wallpaper tiles across the screen in loud patterns, then peels away strip by strip onto the new place. | turf: motel room |
| 11 | **Leviathan Maw** (`needsOwner`) | A huge toothy grin splits the old place open, the jaws close, black goo drips, and they open on the new place. | Dick Roman |
| 12 | **Chuck's Rewrite** (`needsOwner`) | The old place becomes a page of the novels; a cursor types it out; Chuck crumples the page, and a fresh one types in the new place. | Chuck, Becky · turf: Chuck's house |

**Not used:**
- **The Empty's black goo:** too close to The Clawd Files' Black Oil.
- **John's journal page:** Clawd of the Rings' Red Book and The Clawd Files' case file already turn pages.
- **The Enochian banishing sigil:** drawn in blood, and Angel Light already covers the angels.
- **A separate exorcism:** Smoke Out covers the smoke both leaving and entering a host, and the Devil's Trap carries the exorcism's feel; two smoke wipes would look the same.
- **Crowley's snap:** too small for a transition; it's his signature.
- **Dean's cassette tape:** overlaps Headlights.

**Promo.** The Road So Far (#1) opens the trailer.

## Promo: the trailer (`REEL=hunters`)

Built on `doctorShots`, about 45 to 50 seconds, rendered with the app's own sprites, places and transitions. Storyboard first, for your OK.

- **Intro (~9 s): The Road So Far.** Film grain over black. **THE ROAD SO FAR** stamps on. Jumpy stills flash past: the house in Lawrence with its lit window, the Impala on the road, the crossroads under the moon, Stull in the storm, the Bunker's map table. The stills burn away and **SUPERCLAWDTURAL** smoulders in, letters glowing like embers, then **NOW**, and the camera plunges into the headlights. Sound: a chugging chiptune guitar riff and drums in the *sound* of seventies classic rock, our own notes, never the melody of any real song; a crackle of film; a big chord as the title burns in.
- **Set piece (~9.5 s): Smoke them out.** Night at the Roadhouse. The Impala pulls up (the ride). Sam and Dean come in; a black-eyed demon at the bar grins. It steps forward onto the rug; Dean kicks the rug aside and there's the devil's trap. It can't move. Sam reads the exorcism from his laptop; the demon thrashes, black smoke pours out of its mouth (the Smoke Out transition's look), funnels down into the floor in a red flash, and it's gone. Dean takes a bite of pie. Caption: "Saving people. Hunting things."
- **Hook (4 s):** shared.
- **Desktop (~4.6 s):** `brawl(ctx, .hunters, …)`: "Saving people. Hunting bugs. The family business."
- **Status (~4.2 s):** four characters, one per state; the aside: "Idjits."
- **Agents (4 s):** "Every subagent gets to be a hunter."
- **Window (~4.8 s):** `windowShot(ctx, .hunters, …, at: .huntBunker)`: "Driver picks the music. Claude picks the tasks."
- **AIs (~4.4 s):** the BRING YOUR OWN AI* line-up, one character per AI.
- **End card (~4.2 s):** the Bunker's war room, the crew lined up, the title lands, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS", the app icon and the GitHub URL. The Impala's engine turns over at the end.

No logo or melody is copied: the title is our own lettering, and the music only evokes classic rock's instruments and mood.

## Decisions (2026-10-17)

All the gates are passed:
- **Name: Superclawdtural.** Puns stay: Winclawdster, Clawdstiel, Clawdley, Clawdsinger, Fitzclawd, Clawdbury, MacClawd, Balthaclawds.
- **Scope:** the fifteen seasons only; no *The Winchesters*, no *Wayward Sisters*.
- **Raw value:** settled at build time, after checking `main`, the open branches and the forks.
- **Roster:** approved as written, 80 with HEM and the small fry. Rowena and Gabriel are heroes; Clawdley is the lead villain, and his signature brings Juliet the hellhound.
- **Places and homes:** the 20 approved; Demon Dean lives at the Roadhouse.
- **Mechanics:** the Impala, Back from Hell for the five, Clawdstiel's personal space and "Jerk." "Bitch.", the devil's trap and angel blade drills, no meditation.
- **Transitions:** the twelve above; #5 is **Smoke Out** (the demon smoke leaving one host and entering the new place), in place of a plain exorcism.

- **2026-10-23:** names get their "d" (Winclawdster, Clawdstiel, Clawdsinger, Balthaclawds, Clawdley); number 10; the plan follows the universe-modules folder flow.

Started 2026-10-23.

## Weak spots so far (for the polish pass)

Noted at the end of each phase, fixed together in the polish pass (guide Step 7).

**Phase 1:** Clawdstiel's wing shadow could be grander; Clawdley's goatee can read as a mouth; the Bunker's map table is small in the window strip.

**Phase 2, characters:**
- Jack: tan jacket a bit generic; his hair, like Dean's, reads as a rounded cap.
- Mary and Ellen: hair as full helmet shapes; Mary's clip check is small.
- Bobby: the flask is a 4×5 silver blob. Bobby's and Ellen's shotgun stocks hide behind the fist.
- Henry: lapel highlights a little blotchy.
- Jo: the top between her jacket halves can read as an open mouth; her dartboard and Rowena's hex bag pop in from nowhere.
- Gabriel: lollipop stick barely shows, jacket blocky. Kevin: hood reads as a lump. Charlie: laptop corner in her bag too small. Ash: black tee a flat band.
- Cain: grey hair and beard speckled; his bees' outlines heavy for their size. Ruby: knife at rest lost against her hair.
- Abaddon: signature only black eyes and a smile. Azazel and Asmodeus: same yellow eyes (costumes tell them apart). Lilith: hair a solid helmet.
- Dagon: black hair and dress run together, and her hair frames her face like a beard; her flame is small.
- Ramiel: hair a pale dome, face busy. Demon Dean: black eyes subtle on their own, the Mark of Cain tiny.
- The Crossroads Demon: box and mound small. Michael: his always-on glow barely registers. Zachariah: the watch is a 3×2 patch.
- Metatron: glasses read as a mask; typewriter small. Dick Roman and Death: grey hair reads as a helmet. Dick's bite tendril tiny.
- War: ring-turning subtle (rings stay at normal speed: owner decided against an engine request on 2026-10-24). Pestilence: combover dotted, green tint reads khaki. Famine: eyelids don't show, and the cane makes him read like a five-legged animal. Death: chili dog small. Chuck: beard blends into his hair.

**Phase 2, places:**
- A Motel Room: the orange wallpaper fills the band behind the crew's heads (and is Clawd's colour); the tall wall is one pattern all the way up.
- Clawdley's Hell: the queue of souls stands in the band just behind the crew, which should stay plain; the souls are a little robotic; the wall is small uniform brick; the tall zigzag queue is regular.
- Harvelle's Roadhouse: the fan sits at the very top in the window; the dartboard is small; the tall plank wall is plain.
- The Crossroads: the road reads a little like a mound; the wire steps; the crow is tiny.
- Singer Salvage: the tall car stacks can look as if they float.
- Stull Cemetery: clouds a little bubbly; the burning grave reads like a campfire.
- Heaven: the white light mostly shows on the screen saver; the tall green rise is a plain ellipse.

**Phase 3, characters:**
- Rufus: cardigan busy, shirt V reads as a bib. Garth: can't look "very thin", buzz cut like a cap; Mr. Fizzles sits above the hand. Donna, Jody, Claire: hair as helmets; Claire's hood a grey lump. Alex's pistol close to Mary's.
- Ed: camcorder small and close in tone to his face. Harry: signature only lights; mop close to Pamela's curls. Frank: phone stack small. Benny: hair tufts read as ear muffs. Missouri: the swat has no target. Pamela: curls a round afro.
- Becky: book small, hair close to Sam's. Balthaclawds: wine glass tiny. Mick: pocket square a blob. Tessa: hair hugs her face like a hood. Miracle: the spin is a flip, not quite tail-chasing.
- Amara: mist reads as scattered puffs. Eve: mane like a hood, the monster 7×4. Gadreel: jacket busy. Billie: hourglass small. Raphael: wing shadows faint.
- Ketch: hand covers the tie. Gordon: buzz cut like a headband, whetstone hand floats. Bela: bob a helmet. The Alpha: sideburns crowd the eyes, collar lost on the coat. Bloody Mary: hair dome reads as a hood. The Woman in White: reads a bit like a child.
- The Djinn: tattoos over the face hide it; reads as a pattern block. The Clown: wig is most of the sprite. Hookman: legs hidden by the coat. Shapeshifter: silver eyes subtle. Hellhound: leg pairs merge. Demon Smoke: wisps too faint.

**Phase 3, places:**
- The Open Road: the Impala's back end reads like a cabinet at window size; guns in the trunk half-read.
- The Empty: the window strip is the sparsest place (on purpose, but check). Purgatory: mist bands stripy, canopy forks at one height.
- Lawrence: the lawn a flat band. Asylum: ceiling beams thin. Diner: stools bright in the floor band, pie case small.
- Roman: goo small at window size. Apocalypse: the overpass break hard to see.
- Chuck's House: plain wall between the tall bookcases. Orchard: scarecrow small, Cain's veiled hat a grey box.
- Sioux Falls: counter doors uniform, the attic wall one brown area. Moondoor: the right oak cut by the frame.

**Phase 4, mechanics:**
- The Impala: the arsenal is small at 1× (the shotgun mostly a stock); the shotgun propping the lid was dropped (it turned to noise); the wound-down windows are a 3-row slit; the trunk stays up for the whole boarding (a ride only gets `ramp`); the grille shows only as an edge.
- Back from Hell: the pit's red glow is dim on dark; the tipping cross briefly reads as an X and vanishes in one frame; the fist is Clawd-orange for everyone, no sleeve; dirt specks are single pixels; the pit reaches about 4 rows under the feet (nothing clips it). Not checked on Sam, Bobby or Jack, on a ride, or with a coloured outline.
- Drills: the tipped spray can reads a bit like a pistol; the nods and the step back are 1 to 2 px; the paint fades rather than being scuffed; the angels all share one set of moves; the trap reaches x 70 and row 50. The drill hides the held weapon by erasing x 41 and beyond while the can is out.
- Wing shadows (HuntKit's `huntWingShadows`): next to the head they stop the app's outline being drawn, so the outline breaks where the wings meet the hair (the drill keeps a 1 px gap; the shared helper should too). Clawdstiel's flutter and signature wings are faint on a dark desktop; the drill adds a pale rim.
- Clawdstiel's visit: the feathers show only where he left, not at the other end when he goes home.
- Engine, for the owner: for a `.drives` ride the overlay draws a canvas `Ride.height + 1` tall and ignores `canvasHeight` (Overlay.swift, the second ride canvas), so Stranger Clawds' bikes, drawn two rows down on a taller canvas, may lose their bottom rows in the app.

**Phase 5, trips:**
- Speed, first: a frame at a Retina screen saver's 2560×1600 takes Ghostfacers Cam about 71 ms and The Road So Far about 53 ms, more than any Stranger Clawds trip (15 to 45 ms, Flip the slowest). The other ten take 10 to 29 ms. Bring those two down.
- The Road So Far: the title fills only 70% of the saver's width; the shared lettering's O reads like Ø at big sizes (HuntTrips.swift); every still opens on a washed-out flash frame; the yellow-eyed figure's hair reads as a bun; the burn starts with specks that look like a glitch.
- Headlights: night onto a night place (the Road) is less dramatic; the beam's three steps show as rings.
- Ghostfacers Cam: the ghost is cartoon-scream and her hair a flat block; NIGHT SHOT and LOW BATTERY are tiny in the window.
- Salt and Burn: round billows can look like balls; orange-lit puffs under the flames like blobs.
- Cold Spot: frost covers the window strip early; shards slide but don't turn; the breath fog is small.
- Smoke Out: the funnel is a straight V in the window and the stream thin; red sparks like lava specks; the eyes tiny; the flash subtle over Hell.
- Devil's Trap: sigils barely legible in the window; its glow leans neon.
- Angel Light: the blown-up wing reads a little bat-like and the body hides behind it; the wings are stretched sideways in the window; the rays like a picket fence; bulbs small; on Heaven the dimming goes flat grey.
- Hellhound: the last tears close fast; the eyes sit at fixed spots and can land on busy art.
- Motel Wallpaper: the peel is a rolling bar, not a curl; the patterns are huge in the window.
- Leviathan Maw: the old place warps column by column; the slit jumps as it spreads; fangs small in the window; snapped goo thin over Roman's lights.
- Chuck's Rewrite: the page comes and goes as a crossfade; the hand is a mitten; the ball small in the window; the new chapter types very fast; body text tight.

## Character audit (phase 3, 2026-10-24)

Every weapon, shot, magic family, motion, signature and callout checked against the Cast tables and the caster table. Everything matches except:

| Who | Plan | As drawn | Why |
|---|---|---|---|
| Michael | steady, white-gold | steady **thick** beam | owner asked for it to differ from Abaddon (phase 2) |
| Abaddon | steady ray, red | the engine's new `grip`: her foe lifted and choked inside a pink and crimson coil, her orange fist out | owner chose an engine request (2026-10-24), built on main as d7eabd2 |
| War | `rings`, slower | `rings`, normal speed | owner chose no engine request |
| Bloody Mary | appears in a mirror | carries her standing mirror everywhere; her face swims up in it in the signature | needs owner's OK |
| Gordon Walker | machete | machete, two small fangs show while he swings | a nod to "later a vampire"; needs owner's OK |
| The Scarecrow | on its post | carries his post and crossbar with him | how "on its post" reads on a walker; needs owner's OK |
| Hellhound | shadow dog | solid black (not see-through), never sits | so it isn't a copy of Juliet; needs owner's OK |
