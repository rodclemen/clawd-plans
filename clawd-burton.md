# Plan: a new universe, Clawd Burton (Tim Burton's films)

## Context

Clawd Clash has six universes: Star Clawds, Marvelous Clawds, Detective Clawds, Doctor Clawd, The Clawd Files and Stevie Clawdberg. This plan adds a director universe for Tim Burton, built the way Stevie Clawdberg was: one ensemble drawn from a handful of films, grouped by film. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

- **Name: Clawd Burton** (proposed; alternatives are in Open questions). It reads at a glance, it's a light pun on the director, and it sits next to "Stevie Clawdberg" as a pair.
- **Code naming** avoids the director's name in code, as the other universes avoid theirs:
  - `case clawdBurton` with key `"clawdBurton"`.
  - Folder `Sources/App/Universes/ClawdBurton/`, file prefix `Burton…` (`BurtonRoster.swift`, `BurtonHeroes1.swift`, `burtonTheme`, `BurtonTrip`, `REEL=burton`).
  - Branch `tim_burton`.
  - Six other universes are being planned at the same time (Star Trek, 007, Transformers, He-Man, Game of Thrones, Buffy), so every top-level name and place key carries the `burton` prefix or a name only this universe would use.
- **Raw value:** the next free one when its build starts (Buffy is planned as 6); ids are rawValue*1000 and permanent.
- **The films (proposed default, nine, like Clawdberg):** Beetlejuice and Beetlejuice Beetlejuice (counted as one), Edward Scissorhands, The Nightmare Before Christmas, Corpse Bride, Sleepy Hollow, Mars Attacks!, Charlie and the Chocolate Factory, Alice in Wonderland (2010), Frankenweenie (2012). The final pick is yours (see Open questions).
  - **Left out on purpose:** Batman and Batman Returns (Batclawd, the Jester, Cat Burglar and the Puffin already live in Detective Clawds, and they'd look like doubles in Clawd Royale); Sweeney Todd (the whole film is murder and cannibal pies; there's no desktop-toy version of it); Ed Wood and Big Eyes (real people); Dark Shadows (Barnabas's appetite is the point of him); Planet of the Apes (2001) (overlaps Gorilla Grudd's Gorilla City). Wednesday is The Addams Family, its own franchise, so it's out by default.
  - **Ready to add if you want them:** Big Fish, Pee-wee's Big Adventure and Miss Peregrine's Home for Peculiar Children. Mini-rosters are in Open questions, so a yes needs no new research.
- **Naming style:** light puns on the on-screen names (Jack Skullington, Edward Scissorclaws, Sandy Clawz, Violet Bluregarde, the Jabberclawky). A near-spelling where no pun fits (Ichabod Craine, Katrina Van Tassle). Actors' names are never used, and the real people who play themselves (Mars Attacks!' singer cameo) are left out.
- **Size:** about **100 characters**: 51 heroes including HEM and one agent-only, 49 villains including four agent-only. Plus **22 places** and **12 transitions**.
- **Tone:** Burton is gothic but warm: his monsters are the misunderstood ones. That suits a desktop toy well. Where a film goes darker it's tamed to eerie (see "What's tamed" under Cast).

| Universe              | Heroes | Villains | Total | Places | Transitions |
|-----------------------|--------|----------|-------|--------|-------------|
| Star Clawds           |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds      |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds      |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd          |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files       |     36 |       46 |    82 |     20 |          10 |
| Stevie Clawdberg      |     64 |       54 |   118 |     23 |          10 |
| Clawd Burton (proposed) |   51 |       49 |   100 |     22 |          12 |

(heroCount includes HEM; villainCount includes agent-only.)

**Viability: a full experience, not a limited one.** 49 heroes can lead a session and 45 villains can, well past the 20-a-side threshold. One thing to know: many Burton heroes don't fight (Sally, Kim, Charlie, the White Queen), so a lot of the hero side is `.none` or throws something silly. That's in keeping with the films, and fights stay fun because the villain side is full of monsters with claws, swords and ray guns.

**How the sides are sorted.** Heroes are the films' protagonists and their friends. Villains are the antagonists, the monsters and the troublemakers. Two calls need care:
- **Beetlejuice is a villain**, and the villain side's lead. He's the films' trickster antagonist: he cons the Maitlands, tries to marry Lydia and has to be sent back. Fans love him, which is exactly why he should lead a side. Claude still plays the heroes.
- **Halloween Town's scary residents are villains** (Oogie Boogie, Lock, Shock and Barrel, Dr. Finkelstein, the Wolfman, the Clown, the Witch), the same way The Clawd Files put its monsters of the week on the villain side. Jack, Sally, Zero, the Mayor and Sandy Claws are heroes.
- The **Wonka children and the Frankenweenie classmates** are villains in the "troublemakers" sense (the guide allows this, as Fraggle Rock's Gorgs would be). Their fights are silly: Violet throws gum, Veruca throws walnuts. Nobody is hurt; Violet's signature is turning into a blueberry. Flagged in Open questions.

## How a universe plugs in (checked against main, ebc02be, on 2026-10-16)

**New code: `Sources/App/Universes/ClawdBurton/`**
- `BurtonRoster.swift`, in the pattern of `StevieClawdberg/ClawdbergRoster.swift`:
  - `enum BurtonHero: Int, CaseIterable` and `enum BurtonVillain: Int, CaseIterable`, append-only, grouped by film with a comment per group, `hem` last.
  - `burtonHeroPersonas` / `burtonVillainPersonas` merged from the Art files with `.reduce([.hem: hemPersona(.clawdBurton)])`.
  - `Location.burtonHome(of:)` for heroes and villains, `burtonNemeses`, the ride closure, `let burtonTheme = Theme(universe:villains:heroes:places:home:nemeses:ride:menuIcon:legend:)` with `legend: .hero(.jackSkullington)`.
  - The `static let` place keys, and `let burtonPlaces` merged from the Places files.
- `Art/BurtonHeroes1…6.swift` and `Art/BurtonVillains1…6.swift`, 8–10 personas per file.
- `Places/BurtonScenes1…N.swift`, two or three places each.
- `BurtonKit.swift`: drawing helpers shared across the Art files (stripes, stitches, the spiral), every name prefixed `burton…`.
- `BurtonIcon.swift`: the menu bar icon, 28×26, colour and mono. Spiral Hill curling up under a big moon: it reads at 26 pixels and isn't a character's face.
- `BurtonRides.swift`: the rides' drawings (phase 4), as Clawdberg keeps its own.
- `BurtonTakeANumber.swift`: the compaction effect (phase 4; see Mechanics).
- `BurtonDrills.swift`: the bespoke drills (phase 4).
- `BurtonWipes.swift`: the transitions (phase 5).

**Wiring into the existing code**, copying what `clawdberg` did. Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎.
- **`Sources/Shared/Universe.swift`:**
  - `:8–33`: the case, `key`, `title`, `villainCount` (49), `heroCount` (51).
  - `:44–52`: `agentOnly`: villains 45–48 and hero 49 (Maggott), as global ids.
  - `:58`: `claudeSide` stays false (Claude is the heroes).
  - `:61`: `rivals`: the two Victors (see Cast).
  - `:66–79`: `abductees` gets the Recently Deceased for "Take a number" (see Mechanics), with a doc comment like Clawdberg's.
- **`Sources/App/Theme.swift:47`:** `case .clawdBurton: return burtonTheme`.
- **`Sources/App/Locations.swift:74`:** `.merging(burtonPlaces) { a, _ in a }`.
- **`Sources/App/Universes/ComicTransition.swift:12, 16, 26, 36–38`:** in phase 1, add `.clawdBurton` to the `nil` cases; in phase 5, a `.burton(BurtonTrip)` case in `duration`, `draw` and `pick`, and the doc comment.
- **`Sources/App/Universes/Hem.swift:27, 87, 101, 121, 143, 180`:** HEM's persona and costume in every switch (see HEM below).
- **`Sources/App/Rides.swift`:** the new `Ride` cases and their draw dispatch (`coffinSleigh`, `walkingTub`, `sandworm`, `martianSaucer`, `glassElevator`), drawn in `BurtonRides.swift`.
- ⚠︎ **`Sources/Saver/SaverView.swift:79, 89, 214`:** the Options doc comment, the choices list (`("clawdBurton", Universe.clawdBurton.title)`), and `case "clawdBurton": tripUniverse = .clawdBurton; tripMixed = false`.
- ⚠︎ **`Sources/App/Drills.swift:54`:** add `universe != .clawdBurton` to the meditation guard: nobody in these films floats cross-legged. **`:488`:** `.merging(burtonBespokeDrills)`.
- ⚠︎ **`Sources/App/Overlay.swift:865`:** the Playground's five sample prompts (below). Lines 1113 and 1226 show how Clawdberg hooked in its set piece and its OutaTime effect: "Take a number" hooks in the same way, next to OutaTime.
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`**: decide per `if` whether Clawd Burton joins; it needs new hooks for Beetlejooce's three calls, the Mayor's head and Chessur's fade.
- **Clawd Royale** picks the cast and places up through `Universe.allCases`. Check the menu bar icon and arch-enemies when a scene is in a Clawd Burton place.
- **Tools:**
  - `Tools/Preview/main.swift:60–93`: the doc comment, `burtonHeroes`/`burtonVillains` batch lists, the `"clawdBurton"` universe lookup, and the batch loops.
  - `Tools/Transitions/main.swift:12, 122`: the usage line and the branch that renders `BurtonWipe.allCases`, plus a `burtonTitle` and `burtonShowcase` like Clawdberg's (lines 201, 262).
  - Phase 6: `Tools/RenderPromo` (`REEL=burton`), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts (Overlay.swift:865):**
- "Find out why the topiary test keeps snipping the wrong branch"
- "Write a handbook for the recently deleted files"
- "Add a lightning-rod check before the reanimate step"
- "Make the golden-ticket lookup ignore case"
- "Count the Martians in the logs and tell me which ones come in peace"

## Cast

How the engine's weapons map onto Burton's films:
- **`.none`** for the gentle heroes: Sally, Kim, Charlie, the White Queen (she's vowed never to harm a living thing). They run, point and cheer, as Elliclawd does.
- **`.saber`** for blades and bites: Edward's scissor hands, the Vorpal sword, the Headless Horseman's sword, the Sandworm's jaws, the Red Queen's flamingo mallet.
- **`.blaster` + `.thrown(colour)`** for the silly things people throw: Oogie Boogie's dice, Sandy Claws' presents, the March Hare's teacups, Violet's gum, Richie's vinyl records.
- **`.blaster` + `.beam`** for the Martians' ray guns: a green ray with a yellow core.
- **`.lightning` + `Magic`** for real magic. Every caster has its own look (table below), and `magicVariants` gives each its own drawing variant too.
- **Black and white:** Frankenweenie's characters are drawn in greys, as the film is. In Clawd Royale they're instantly from "the black-and-white one", and they can't be mixed up with the colour cast. Corpse Bride's living are drawn in grey-blues and its dead in colour, as the film does.

### Magic, one look per caster

| Caster | Family | Core / glow | What you see |
|---|---|---|---|
| Beetlejooce | `spell` | moss green `B7E35A` / `3F6B1A` | a ribbon of moss-green sparkles with the odd beetle tumbling in it |
| Jack Skullington | steady ray | pale green `D9FFC2` / `2FBF5A` | a wavering ghost-green flame, the fountain's fire from "Jack's Lament" |
| The Halloween Witch | jagged | pumpkin `FFE0B0` / `FF7A1A` | forked orange lightning off the end of her broom |
| Delorez | steady ray | white `F4F7FF` / slate `8C9BB0` | a pale wisp drawn out of the target towards her (the soul-suck, kept cartoonish) |
| Otho | `rings` | lilac `E6CCFF` / `9A5BD6` | séance rings rippling out along a faint ray |
| Lady Van Tassle | `spell` | rose `FFC2C2` / crimson `9E1B2E` | a crimson ribbon of sparks: witchcraft |
| The Western Woods Crone | `touch` | pale lime `F2F2A0` / `8F9A2A` | no stream: a sickly glowing fingertip, and a glow round whoever she points at |
| Katrina Van Tassle | `touch` | candle cream `FFF4D0` / gold `D4A645` | a warm protective charm glowing round the friend she points at |
| Grandma Florenz | `waves` | cream `FFF0E0` / pink `FF9EC8` | sound arcs pulsing from her portable record player (the yodelling record) |
| The Jabberclawky | jagged | lavender `F0D6FF` / violet `7A2BD1` | the Jabberwocky's purple lightning breath |
| Victor Frankenstien | jagged | white `FFFFFF` / grey `A8A8A8` | a black-and-white lightning bolt from his kite: the only grey lightning in the app |

The two `touch` casters (Katrina, the Crone) are a good witch and a bad one; their colours are opposite (warm gold, sour lime). The Witch's orange lightning and Victor's grey are the two jagged ones; Thorr's, Stormy's and the Electric Gremlin's are blue-white, so neither is confusable.

### Heroes (51)

**The Nightmare Before Christmas (5).** Enum first, so the skeleton's lead hero is case 0.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Jack Skullington | white skull head, tall thin black pinstripe suit, bat bow tie | ghost-green flame (steady ray) | stretches his skull into a scary face, then bows; callout "What's this?" |
| 2 | Sallee | patchwork rag doll, red yarn hair, stitched patchwork dress | none | her arm comes loose; she sews it back on |
| 3 | Zeero | white ghost dog, a glowing orange pumpkin nose | none, `.hover`, `canSit: false` | his nose lights up bright; callout "Arf!" |
| 4 | The Mayor | tall black hat with a rosette, cone head, sash | none | his head spins from the smiling face to the worried one |
| 5 | Sandy Clawz | red suit, white beard, sack | presents (`.thrown(red)`) | pats his tummy; callout "Ho ho ho!" |

**Beetlejuice and Beetlejuice Beetlejuice (8)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 6 | Lydia Deathz | spiky black fringe, black lace, an old camera round her neck | none | lifts the camera, a flash; callout "Strange and unusual." |
| 7 | Adam Maitclawd | ghost, cardigan, sensible glasses | none | pulls his face into a long-nosed scary mask, then lets it snap back |
| 8 | Barbara Maitclawd | ghost, floral dress, kind bob | none | pulls her face back into a skull-like scare |
| 9 | Delia Deathz | sharp black bob, dramatic red, huge earrings | none | strikes an arty pose beside a pointy sculpture |
| 10 | Astrid Deathz | dark hair, school blazer, scowl | none | rolls her eyes and pulls up her hood |
| 11 | Junoh | caseworker, cardigan, bun, clipboard | none | taps the Handbook; a puff of smoke curls out of her collar; callout "Read the Handbook!" |
| 12 | Wolf Jaxon | afterlife detective, slick hair, trench coat, ex-action-star swagger | pistol (`.bullet`) | flashes his badge and strikes a movie-hero pose |
| 13 | The Shrunken-Head Man | safari suit, pith helmet, a tiny shrunken head | none | his tiny head bobs and squeaks |

**Edward Scissorhands (4)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 14 | Edward Scissorclaws | wild black hair, pale face, black leather with buckles, long scissor-blade hands | scissor blades (melee) | snips a hedge into a little dinosaur topiary; callout "I'm not finished." |
| 15 | Kim Boggz | long blonde hair, pastel dress | none | dances in falling snow |
| 16 | Peg Boggz | Avon lady, lilac suit, make-up case | none | opens her case, "Avon calling!" |
| 17 | The Inventor | old gentleman, velvet smoking jacket | none | holds up a heart-shaped biscuit |

**Corpse Bride (7)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 18 | Victor Van Dawt | tall, thin, grey-blue, Victorian tailcoat | none | practises his vows, fumbling a ring; callout "With this hand…" |
| 19 | Emilee | blue skin, torn wedding dress and veil, one bony arm | none | blue butterflies swirl off her; callout "I do." |
| 20 | Victoria Everclawt | grey-lilac gown, high collar, neat hair | none | a shy curtsey |
| 21 | Scrapz | skeleton dog | bite (melee) | plays fetch with his own bone |
| 22 | Elder Gutknocked | ancient dead sage, long beard, huge book | none | thumbs through his book of rules |
| 23 | Bonejingles | one-eyed skeleton band leader, bowler hat, a trumpet | none | plays a riff and does a bony shuffle; callout "Hit it, boys!" |
| 24 | General Bonesapart | tiny skeleton, bicorne hat, a sword stuck through him | sword (melee) | salutes, pulls the sword out and waves it |

**Sleepy Hollow (4)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 25 | Ichabod Craine | black frock coat, high collar, odd magnifying spectacles | none | flips down his spectacle lenses, then faints; callout "Villainy!" |
| 26 | Katrina Van Tassle | blonde, white gown, a book of charms | protective charm (`touch`) | draws a charm in the air that glows |
| 27 | Young Masbeth | boy, cap, his father's lantern | none | holds up the lantern bravely |
| 28 | Brom Van Bruntt | big, burly, sheepskin collar | fists (melee) | flexes; puts on a pumpkin to prank |

**Mars Attacks! (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 29 | Richie Norriss | doughnut-shop uniform, mop of hair | vinyl records (`.thrown(black)`) | spins a record on one finger |
| 30 | Grandma Florenz | cardigan, big hair, a portable record player | the yodelling record (`waves`) | turns up the volume and taps along |
| 31 | President Dayle | dark suit, flag pin, side parting | none | gives a speech from a podium |
| 32 | Byron Wilyums | ex-boxer in a casino uniform | fists (melee) | shadow-boxes, then raises his gloves |
| 33 | Professor Kessclaw | pipe, tweed, Martian-loving smile | none | points his pipe at the sky; callout "A peaceful people." |

**Charlie and the Chocolate Factory (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 34 | Willy Wonky | black top hat, burgundy velvet coat, purple gloves, pageboy bob, cane | chocolate bars (`.thrown(purple)`) | twirls the cane and tips the hat; callout "Everything's eatable!" |
| 35 | Charlie Buckett | knitted jumper, scarf | none | holds up the golden ticket, which shines |
| 36 | Grampa Joe | pyjamas, cardigan, flat cap | none | hops out of bed and does a little jig |
| 37 | An Oompa-Loompah | tiny, red jumpsuit, neat hair | none | a little dance with a drum beat |
| 38 | Dr. Wilbur Wonky | dentist's coat, head mirror | toothbrushes (`.thrown(white)`) | checks a set of teeth with his little mirror |

**Alice in Wonderland (7)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 39 | Alice Kingsclaw | blonde, blue dress, later silver armour | the Vorpal sword (melee) | drinks from a tiny bottle and shrinks a moment; callout "Six impossible things." |
| 40 | Tarrant Hightop | frizzy orange hair, chalk-white face, tall patched hat with pins and ribbons | his hat (`.thrown(teal)`) | does the Futterwacken, a wild little jig; callout "Fairfarren!" |
| 41 | Chessur | grey-blue striped cat, huge grin, glowing eyes | none, `.hover` | fades away until only the grin is left, then comes back; callout "Lost, are we?" |
| 42 | Mirana the White Queen | white hair, white gown, black lips | none (she harms no living thing) | floats her hands up in a graceful pose |
| 43 | McTwisp | white rabbit, waistcoat, pocket watch | none | checks the watch and hops on the spot |
| 44 | Mally the Dormouse | tiny, red tunic, a hatpin sword | hatpin (melee) | brandishes the hatpin |
| 45 | Thackery Hare | twitchy, ragged, a teapot | teacups (`.thrown(white)`) | flings a teacup over his shoulder |

**Frankenweenie (4)**, drawn in greys

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 46 | Victor Frankenstien | small boy, black hair, sweater vest | lightning from his kite (jagged, grey) | flies a kite until lightning strikes it |
| 47 | Sparkie | bull terrier with stitches and neck bolts | bite (melee) | his bolts spark, he wags so hard his tail flies off, then it's back |
| 48 | Elsa Van Helsclaw | black bob, pale dress | none | carries her poodle's lead; a little wave |
| 49 | Mr. Rzykrusky | science teacher, long face, tie | none | holds up a frog that twitches with a zap |

**Agent-only (1):** 50 · **Maggott**, the green worm who lives in Emilee's head, on Clawd's four legs with a little worm hood; only ever an agent.

**HEM (1)**, last as always: 51.

### Villains (49)

**Beetlejuice and Beetlejuice Beetlejuice (5).** Enum first, so the skeleton's lead villain is case 0.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Beetlejooce | black-and-white striped suit, wild mossy hair, grubby green-white face | moss-green magic (`spell`) | his name bubbles up three times and he pops out of a striped ring; callout "It's showtime!" |
| 2 | The Sandwurm | huge black-and-white striped worm, a mouth inside its mouth | jaws (melee), `bulk` | rears up and its inner mouth snaps out |
| 3 | Delorez | black gown, dark hair, held together with staples | soul wisp (steady ray) | gathers her pieces and staples them back together |
| 4 | Otho | black turtleneck, red scarf, theatrical | séance rings (`rings`) | reads from the Handbook, arms raised |
| 5 | Jeremee | ghost boy, varsity sweater, a bicycle | none | leans on his bike with a too-charming smile |

**The Nightmare Before Christmas (8)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 6 | Ooogie Boogie | big burlap sack, stitched mouth, glows under UV | dice (`.thrown(white)`), `bulk` | rolls dice; a bug falls out of a seam; callout "Well, well, well…" |
| 7 | Lok | devil mask, red suit, pitchfork | pitchfork (melee) | pushes his mask up, grins |
| 8 | Shok | witch mask, purple dress, pointy hat | broom (melee) | cackles and twirls her broom |
| 9 | Barrell | skeleton mask, green, a lollipop | lollipops (`.thrown(green)`) | licks his lollipop |
| 10 | Dr. Finkelclawd | lab coat, goggles, the top of his head flips open | potion bottles (`.thrown(green)`) | flips his skull open and scratches his brain |
| 11 | The Wolfclawd | werewolf in a tattered suit | claws (melee) | howls at the moon |
| 12 | The Tear-Away Clown | clown on a unicycle | none | tears his face off to show a dark hole, then puts it back (eerie, not gory) |
| 13 | The Halloween Witch | green-faced witch, tall hat, broom | orange lightning, `.fly` | cackles round a circle on her broom |

**Edward Scissorhands (2)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 14 | Jimm | letterman jacket, blond mullet, van keys | pistol (`.bullet`) | jangles his keys and sneers |
| 15 | Joyce Monrow | big red hair, leopard-print, a phone | none | gossips into the phone, wide-eyed |

**Corpse Bride (4)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 16 | Lord Barkiss Bittern | big chin, plumed hat, red cape | sword (melee) | twirls his cape with a sly grin |
| 17 | Pastor Gallswell | huge jaw, black robes, a staff | staff (melee) | thunders a sermon, finger pointing |
| 18 | Finis Everclawt | short, stout, sour, a cane | cane (melee) | taps the cane, scowls |
| 19 | Maudeline Everclawt | tall, rigid, grey gown, pinched mouth | none | sniffs disapprovingly through a lorgnette |

**Sleepy Hollow (3)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 20 | The Headless Horseclawd | black armour and cloak, no head, teeth-like spurs | sword (melee) | throws a flaming jack-o'-lantern and catches it; his swing knocks hats off, never heads |
| 21 | Lady Van Tassle | black hair, wine-red gown | crimson witchcraft (`spell`) | stirs a little cauldron |
| 22 | The Western Woods Crone | hunched, grey, milky eyes, rags | sickly charm (`touch`) | leans on her stick and peers |

**Mars Attacks! (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 23 | The Martian Leader | big exposed brain in a glass dome, green skull face, red cape | ray gun (`.beam`) | raises a fist; callout "Ack! Ack!" |
| 24 | The Martian Ambassador | brain in a dome, white robe, a translator box | ray gun (`.beam`) | releases a dove... then zaps it into a puff of feathers; callout "We come in peace!" |
| 25 | A Martian Trooper | brain in a dome, silver spacesuit | ray gun (`.beam`) | spins the ray gun |
| 26 | The Martian Spy | tall black beehive (hiding the brain), stiff walk, chewing gum | ray gun (`.beam`) | blows a bubble and stares without blinking |
| 27 | The Martian Walker | giant robot with a Martian in a dome on top | ray (`.beam`), `armoured`, `bulk` | stomps; its dome swivels |

**Charlie and the Chocolate Factory (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 28 | Augustus Gloopp | big boy, lederhosen, chocolate smears | chocolate (`.thrown(brown)`) | stuffs in a chocolate bar |
| 29 | Veruca Saltt | posh coat, ringlets, a frown | walnuts (`.thrown(tan)`) | stamps her foot; callout "I want it now!" |
| 30 | Violet Bluregarde | blue tracksuit, gum | gum (`.thrown(blue)`) | swells up into a blueberry and back |
| 31 | Mike Teevee | grey hoodie, video-game controller | game zapper (`.energy`, white) | shrinks to a few pixels and pops back |
| 32 | Slugwurth | rival chocolatier, slicked hair, a stolen recipe | none | sneaks the recipe into his coat |

**Alice in Wonderland (5)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 33 | The Red Queen | huge round head, heart-shaped lips, red gown | flamingo mallet (melee) | swings the flamingo at a hedgehog; callout "Off with their heads!" |
| 34 | Stayne | tall Knave of Hearts, eyepatch, heart-pattern armour | sword (melee) | a slow bow, hand on the hilt |
| 35 | The Jabberclawky | dragon, long neck, bat wings | purple lightning, `bulk`, `armoured` | spreads its wings and roars |
| 36 | The Bandersnatch | white shaggy beast, spotted, huge jaws | jaws (melee), `bulk` | shakes its shaggy head |
| 37 | A Red Card Knight | armour made of playing cards, heart pattern | spear (melee), `armoured` | stands at attention, clanks |

**Frankenweenie (8)**, drawn in greys

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 38 | Edgar "E" Gorr | hunched, crooked grin, bad teeth | none | shows off his invisible goldfish (an empty bowl, a bubble) |
| 39 | Nassorr | flat-top hair, heavy brow, deep voice | none | "Ahh!" arms raised dramatically |
| 40 | Toshiakki | neat hair, competitive glare | none | fires up a little rocket bottle |
| 41 | Weird Gurl | huge round eyes, fringe, holding her cat | none | holds up Mr. Whiskers, who stares |
| 42 | Mr. Whiskerz | vampire cat with bat wings | fangs (melee), `.fly` | flaps and hisses |
| 43 | Shellee | turtle grown to a kaiju | stomp (melee), `armoured`, `bulk` | roars and stomps, the ground shaking |
| 44 | Colossuss | mummy hamster in bandages | bite (melee) | waddles with its arms out |
| 45 | The Were-Rat | rat-man in tatters | claws (melee) | sniffs the air, whiskers twitching |

**Agent-only small fry (4).** Like the MSE-6, these only ever appear as agents:
- 46 · **Bob**, one of Beetlejooce's shrunken-head workers in a suit;
- 47 · **an Oogie bug**, a beetle out of Oogie Boogie's seams;
- 48 · **a nut-sorting squirrel** from Wonka's factory;
- 49 · **a Sea-Monkey**, Frankenweenie's monstrous brine shrimp.

### HEM

As always, the last hero. His Clawd Burton costume: a crooked black top hat with a spiral band, a black-and-white striped scarf, and a big spiral lollipop he swings like a club (`.saber`). He's in the universe's colours without looking like anyone in it.

### Nemeses (24)

Each pair faces off first when both are on stage:
- Jack Skullington ↔ Ooogie Boogie
- Sallee ↔ Dr. Finkelclawd
- Sandy Clawz ↔ Lok
- Lydia Deathz ↔ Beetlejooce
- Adam Maitclawd ↔ Otho
- Barbara Maitclawd ↔ the Sandwurm
- Astrid Deathz ↔ Jeremee
- Wolf Jaxon ↔ Delorez
- Edward Scissorclaws ↔ Jimm
- Peg Boggz ↔ Joyce Monrow
- Emilee ↔ Lord Barkiss Bittern
- Victor Van Dawt ↔ Pastor Gallswell
- Ichabod Craine ↔ the Headless Horseclawd
- Katrina Van Tassle ↔ Lady Van Tassle
- President Dayle ↔ the Martian Leader
- Byron Wilyums ↔ the Martian Ambassador (the boxing match)
- Richie Norriss ↔ the Martian Walker
- Willy Wonky ↔ Slugwurth
- Charlie Buckett ↔ Veruca Saltt
- Alice Kingsclaw ↔ the Jabberclawky
- Mirana ↔ the Red Queen
- Tarrant Hightop ↔ Stayne
- Victor Frankenstien ↔ Edgar "E" Gorr
- Sparkie ↔ Mr. Whiskerz

### Rivals

**Victor Van Dawt and Victor Frankenstien** never lead two sessions back to back. Both are pale, dark-haired Burton boys called Victor; one after the other would look like the same character twice.

### Lookalikes to watch

Inside the universe:
- **The two Victors:** Van Dawt is tall and thin in a grey-blue Victorian tailcoat; Frankenstien is small, in a sweater vest, and in greys. Plus the rivals rule above.
- **Three undead dogs:** Zeero (a white floating ghost with a pumpkin nose), Scrapz (a skeleton), Sparkie (stitches and bolts, in greys). Different silhouettes and palettes.
- **Three skeletons:** Jack (tall, pinstripe suit, bat bow tie), Bonejingles (bowler hat, eyepatch, trumpet), General Bonesapart (tiny, bicorne, a sword through him).
- **Three stitched women:** Sallee (patchwork, red yarn hair), Emilee (blue, white veil), Delorez (black gown, staples).
- **Two top hats:** Willy Wonky (burgundy velvet, black hat, bob) and Tarrant Hightop (orange hair, white face, patched hat). The Mayor's hat is tall and plain with a rosette.
- **Four Martians:** told apart by robe (Ambassador), cape (Leader), spacesuit (Trooper) and the beehive (Spy).
- **Lady Van Tassle and the Crone** are sisters: Lady is upright in wine red; the Crone is hunched and grey.

Against the six existing universes (they meet in Clawd Royale):
- **Tarrant Hightop vs the Mad Milliner** (Detective Clawds): keep Tarrant's orange hair, white face and patchwork hat strong.
- **Chessur vs Cheshyre** (Detective Clawds' assassin): different names on purpose; one's a cat.
- **Beetlejooce vs the Jester** (Detective Clawds): both have green hair and a pale face. Beetlejooce's black-and-white stripes and mossy, messy hair keep him apart; no purple anywhere on him.
- **The Headless Horseclawd vs Ghost Biker** (Marvelous Clawds): no head versus a flaming skull.
- **The Martians vs the Grey and the Tall Visitor** (Clawd Files, Clawdberg): big brains in glass domes; no one else has that.
- **Ooogie Boogie vs the Trashman** (Clawd Files): a neat burlap sack against a heap of rubbish.
- **Edward vs Clawdverine:** leather, buckles and long thin blades on every finger, against three claws and yellow.
- Check Buffy's plan too when both are drawn: witches and vampires there; Lady Van Tassle and the Halloween Witch should stay distinct.

### What's tamed, and who's left out and why

- **Tamed:** Juno's smoke curls out of her collar, not her throat. Lord Barkis is "the cad who jilted Emily and ran off with her dowry". The Headless Horseman knocks hats off, never heads, and the Tree of the Dead has glowing roots, not heads. Delores's soul-suck is a pale wisp. The Martian ray doesn't strip anyone to a skeleton; it's a zap and a puff. The Red Queen's moat of heads is a moat of heart-shaped lilies. The Tear-Away Clown's face comes off to show a dark hole, nothing more.
- **Left out:** the Mars Attacks! singer who plays himself (a real person); Nathalie Lake and her dog's swapped heads, and Professor Kessler's head in a jar (body horror for a desktop toy); the Martian Girl's seduction scene (she's kept as a gum-chewing spy); Absolem (his hookah smoke rings would copy the Cigarette-Smoking Clawd's); Tweedledum and Tweedledee (two people in one sprite won't read); Bayard, Miss Argentina, Charles Deetz, Rory, Bill and Kevin Boggs, Esmeralda, Officer Allen, Taffy Dale, General Decker, Notary Hardenbrook, the Harlequin Demon, Behemoth, the Undersea Gal, Mr. Burgemeister and Persephone (too thin to carry a character, or a near-duplicate of someone kept).

## Places (22)

Each is a `Place` with a still picture, a moving layer and tall-canvas extras for the screen saver. The palettes swing wide on purpose: Halloween orange and black, Corpse Bride's grey-blue living world against its colourful dead, pastel suburbia, candy colours for Wonka, Underland's saturated greens and reds, Frankenweenie in greys.

| # | Key | Place | Still | Moving layer | Tall-canvas extras |
|---|---|---|---|---|---|
| 1 | `halloweenTown` | **Halloween Town square** (the default) | crooked houses, the green-slime fountain, the town hall, a pumpkin patch | the fountain bubbles green, jack-o'-lanterns flicker, a bat flits | Spiral Hill and the full moon high above, the gates' silhouette |
| 2 | `spiralHill` | **Spiral Hill** | the curling hill in the graveyard, a huge moon behind it | mist rolls between gravestones, Zero-like wisps float | the stars and a black cat on a far roof |
| 3 | `oogiesLair` | **Oogie Boogie's lair** | a roulette table, dice, slot machines, a UV glow | the roulette wheel spins, ultraviolet light pulses | the rope bridge and the hanging cage overhead |
| 4 | `christmasTown` | **Christmas Town** | snowy toy-town houses, a giant tree, candy-cane lamps | snow falls, windows twinkle | the northern lights and a sleigh far off |
| 5 | `maitlandHouse` | **The Maitlands' house** | the white New England house, the covered bridge below, Delia's sculptures on the lawn | wind in the trees, a curtain flaps in the attic window | the hill town on the slope behind |
| 6 | `modelWinterRiver` | **The model town in the attic** | the tabletop model of Winter River: tiny houses, a graveyard, the bridge | a spider crawls across the model; a tiny gravestone wobbles | the attic rafters and a dusty skylight |
| 7 | `afterlifeWaitingRoom` | **The Afterlife waiting room** | green walls, plastic chairs, a ticket dispenser, a "NOW SERVING" board | the number board ticks over, a strip light buzzes | a mile of corridor and filing cabinets up into the dark |
| 8 | `sandwormSaturn` | **Saturn's sand dunes** | pale yellow-ochre dunes, black rock spires, a strange ringed sky | sand ripples where something moves underneath | Saturn's rings across the whole sky |
| 9 | `pastelSuburbia` | **The pastel cul-de-sac** | candy-coloured houses, topiary animals, identical cars | sprinklers tick round, a car pulls out | the dark hill and Edward's castle above the rooftops |
| 10 | `inventorsCastle` | **The Inventor's castle** | the gothic hilltop castle hall, cogs, a cookie machine | gears turn, ice shavings drift like snow | the broken roof and the night sky through it |
| 11 | `landOfTheDead` | **The Land of the Dead** | the Ball and Socket pub, colourful skeletons, gaslight | the band's lights pulse, a skeleton head bobs | a purple-green sky with lanterns strung above |
| 12 | `everglotVillage` | **The village of the living** | grey-blue Victorian street, the Everglot mansion, a clock tower | the clock hand moves, crows flap, drizzle | rows of slate roofs and chimney smoke |
| 13 | `hollowVillage` | **Sleepy Hollow village** | the misty Dutch village, the covered bridge, the Van Tassel manor's lights | mist drifts, a lantern swings | the church spire and bare trees against a white sky |
| 14 | `treeOfTheDead` | **The Tree of the Dead** | the gnarled tree in the Western Woods, roots like claws | its roots glow red, bats leave its hollow | twisted branches up into the dark |
| 15 | `perkinsvilleKansas` | **Perkinsville, Kansas** | the doughnut shop with its giant doughnut sign, a trailer park, flat fields | the doughnut sign blinks, tumbleweed rolls | a sky of Martian saucers, far away |
| 16 | `galaxyHotel` | **The Galaxy hotel, Las Vegas** | a fictional casino tower shaped like a rocket, neon strip | neon flickers, the rocket's lights chase | the desert night and the whole lit strip |
| 17 | `martianSaucerDeck` | **Inside the Martian saucer** | glowing green consoles, brains in jars of liquid (just the Martians' own) | consoles blink, the liquid bubbles | the saucer's dome and a view of Earth |
| 18 | `chocolateRoom` | **The Chocolate Room** | the chocolate river, the waterfall, candy trees, mushrooms | the waterfall churns, the river flows | the cavern roof with candy stalactites |
| 19 | `madTeaParty` | **The mad tea party** | the long table under a dead tree by the windmill, mismatched china | steam curls from teapots, a cup rattles | Underland's strange sky and a far chessboard field |
| 20 | `salazenGrum` | **The Red Queen's castle** | heart-shaped topiaries, red stone, the throne | red banners flap, card knights patrol in the background | the castle towers and the lily moat |
| 21 | `newHollandAttic` | **Victor's attic lab, New Holland** | kites, jars, the operating table under the skylight, in greys | lightning flashes through the skylight, a kite flaps | the rooftop and a lightning-split sky |
| 22 | `windmillMiniGolf` | **The windmill mini-golf** | the mini-golf windmill on the hill, the fair below, in greys | the windmill's sails turn, torches flicker | a stormy grey sky and the town's lights |

Keys checked: none clash with the 150-odd `Location("…")` keys on main (`christmasLondon` and `mothership` exist, so these are `christmasTown` and `martianSaucerDeck`). Each is a name only this universe would use, so the six sibling plans shouldn't hit them; check again at build time with `grep -rn 'Location("' Sources/App/Universes`.

**Homes:**
- **Nightmare:** Jack, Sallee, Zeero and the Mayor in Halloween Town; Sandy Clawz in Christmas Town. Ooogie and his bugs in his lair; Lok, Shok and Barrell in the lair too; Dr. Finkelclawd, the Wolfclawd, the Clown and the Witch in Halloween Town. Spiral Hill is Jack's turf in the transitions.
- **Beetlejuice:** Lydia, Delia, Astrid, Adam and Barbara at the Maitlands' house; Junoh, Wolf Jaxon and the Shrunken-Head Man in the waiting room. Beetlejooce and Bob in the model town; the Sandwurm on Saturn; Delorez, Otho and Jeremee in the waiting room (Otho at the house; he moves in).
- **Edward Scissorhands:** Edward and the Inventor at the castle; Kim and Peg in the cul-de-sac. Jimm and Joyce in the cul-de-sac.
- **Corpse Bride:** Emilee, Scrapz, Elder Gutknocked, Bonejingles, General Bonesapart and Maggott in the Land of the Dead; Victor Van Dawt and Victoria in the village. Barkiss, Gallswell and the Everglots in the village.
- **Sleepy Hollow:** Ichabod, Katrina, Young Masbeth and Brom in the village. The Horseclawd and the Crone at the Tree of the Dead; Lady Van Tassle in the village.
- **Mars Attacks!:** Richie and Grandma Florenz in Perkinsville; Byron at the Galaxy hotel; President Dayle and Kessclaw at Perkinsville too (the White House is a real building, so it isn't a place here). The Martians on the saucer deck; the Walker in Perkinsville.
- **Charlie:** everyone in the Chocolate Room, the squirrel included; Slugwurth too (he's snooping).
- **Alice:** Alice, Tarrant, Chessur, McTwisp, Mally and Thackery at the tea party; Mirana at the tea party. The Red Queen, Stayne, the Bandersnatch and the Card Knight at Salazen Grum; the Jabberclawky at Salazen Grum.
- **Frankenweenie:** Victor, Sparkie and Mr. Rzykrusky in the attic; Elsa at the windmill. The classmates and their monsters, and the Sea-Monkeys, at the windmill.
- HEM lives in Halloween Town.

## Mechanics that make it its own universe

1. **Rides** (`BurtonRides.swift`):
   - **Jack's coffin sleigh:** a coffin on runners pulled by skeleton reindeer, Zeero's nose glowing in front. For Jack, Sallee, Zeero, the Mayor and Sandy Clawz.
   - **The walking bathtub:** Lock, Shock and Barrel's clawed tub stomping in on its feet. For Lok, Shok, Barrell and Ooogie.
   - **The Sandworm:** bursts up through the floor, the rider on its back, and dives back down. For Beetlejooce, Delorez and Jeremee (and the Maitlands leave on it, unwillingly: a fun gag, your call).
   - **The Martian saucer:** a classic silver saucer with a clear dome and a ring of flashing lights, drawn new (not the Clawd Files' saucer). For the Martians.
   - **The Great Glass Elevator:** crashes down through the top of the window and lifts off again. For Wonky, Charlie, Grampa Joe, the Oompa-Loompah and Dr. Wilbur Wonky.
   - Everyone else walks. The Headless Horseman's black horse was considered; a horse is a big new drawing for one rider, so it's left for the polish pass if there's time.
2. **Compaction: "Take a number" (recommended).** When a session led by one of **the Recently Deceased** compacts, they're called away to the Afterlife and back. The group is the Beetlejuice ghosts, all clearly dead in the films: Adam, Barbara, Junoh, Wolf Jaxon and the Shrunken-Head Man (heroes 6, 7, 10, 11, 12), and Beetlejooce, Delorez and Jeremee (villains 0, 2, 4).
   - A paper ticket pops out of a dispenser above the leader with a ridiculous number on it; they flicker out like a ghost; a "NOW SERVING" board ticks over; they flicker back, same face.
   - **Beetlejooce does it his way:** his name rises in three speech bubbles, "BEETLEJOOCE!" ×3, and he springs back up through a black-and-white striped ring. Say it three times and he's back.
   - It reuses Clawdberg's route: the list goes in `Universe.abductees`, the effect is drawn in `BurtonTakeANumber.swift` where the overlay draws OutaTime (`Overlay.swift:1226`). No new hook is needed.
   - **Alternative, "It's alive!"**: Frankenweenie's reanimated pets (Sparkie, Mr. Whiskerz, Shellee, Colossuss, the Were-Rat) are struck by lightning from Victor's kite, flash black and white, and a horror-film caption reads "IT'S ALIVE!". It's lovely but rarely seen, since four of the five are villains who seldom lead. Your pick (Open questions).
3. **Habits:**
   - **Beetlejooce, three times:** idle, his name ticks up in bubbles, one, two, three, and on the third he vanishes and pops up somewhere else on stage through a striped ring.
   - **The Mayor's two faces:** his head spins to the worried face when a session hits an error or needs approval, and back to the smile when it's going well. It ties straight into the status states.
   - **Chessur fades:** now and then he fades out until only the grin floats, then comes back.
   - **Zeero follows Jack:** when both are on stage, Zeero drifts to hover beside Jack.
   - **Oompa-Loompahs dance:** when a session on stage finishes its task, any Oompa-Loompah does a short dance (our own drum beat, never their songs).
4. **Practice drills, bespoke** (`BurtonDrills.swift`):
   - Edward clips a hedge into a topiary (a dinosaur, then a hand);
   - Jack practises scares, stretching his face at a pumpkin;
   - Victor Frankenstien flies his kite until it catches lightning;
   - Alice swings the Vorpal sword at a chess-piece dummy;
   - the Martians shoot at a Kansas billboard;
   - the Horseclawd slices pumpkins off fence posts;
   - Willy Wonky taste-tests from a tray of sweets.
   - **No meditation:** nobody in these films floats cross-legged (`Drills.swift:54`).

## Phases

Each phase builds, is checked with Preview sheets, and is shown to you before the next one.

1. **Skeleton:**
   - the universe case and all the wiring above;
   - Jack Skullington and Sallee (heroes 0 and 1) and Beetlejooce (villain 0);
   - Halloween Town square, the menu icon, HEM's costume, the saver option and Preview support;
   - plain wipes for now (`ComicTransition.pick` returns nil for it).
   
   It runs end to end in the app, the window, the screen saver and Clawd Royale.
2. **Core ensemble.** About 43 characters, the first four film groups in enum order:
   - Nightmare, Beetlejuice, Edward Scissorhands and Corpse Bride: 24 heroes and 19 villains;
   - 8 places: Halloween Town, Spiral Hill, Oogie's lair, Christmas Town, the Maitlands' house, the model town, the waiting room, and the Land of the Dead;
   - their homes and nemeses (the other places' homes fall back to the default until phase 3).
   - Fine to commit the enum cases first as stand-ins, then draw them in a second commit.
3. **The rest:** Sleepy Hollow, Mars Attacks!, Charlie, Alice, Frankenweenie, Maggott and the four agent-only villains, up to 100 characters and all 22 places, every home filled in. Ends with **the character audit**: every persona's weapon, shots, magic colours, motion, signature and callout checked against the films and this roster, and a mismatches table for you.
4. **Mechanics:** the five rides, "Take a number" (or "It's alive!"), the habits and the bespoke drills.
5. **Transitions:** the twelve `BurtonTrip`s and the spidery caption (below), wired through `ComicTransition`.
6. **Polish pass:** every weak spot noted in phases 2–5, fixed together, split by file and run in parallel with before-and-after renders for you. Always before phase 6.
7. **Docs and release (phase 6):**
   - the README's universe table and a collapsible cast-and-places section; the screen-saver paragraph; the developer notes;
   - `Tools/RenderDocs`: a `burtonLineup` desktop strip, `roster-clawd-burton.png`, `locations-clawd-burton.png` and a social preview; `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - `llms.txt`: the universe list, the folder and `Burton…` prefix, and "Take a number";
   - a `CHANGELOG.md` entry each phase;
   - the trailer, `REEL=burton` (see Promo).
   - **Needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`. Before calling a phase done, `./build.sh --release <version>` too: dense `sin`/`cos` drawing (spirals!) can hit "unable to type-check in reasonable time"; find them with `-Xfrontend -warn-long-expression-type-checking=300` and split them up.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Jack Skullington"`;
  - `build/preview fight out.png "Jack Skullington" "Ooogie Boogie"`;
  - `build/preview fight out.png "Victor Van Dawt" "Victor Frankenstien"` (side by side, to check they read apart);
  - `build/preview place out.png "Clawd Burton"`;
  - the batch sheets `burtonHeroes1…`, `burtonVillains1…`.
  
  Look at every PNG before showing you: who each character is, no lookalikes, no outline gaps, Frankenweenie's greys staying grey.
- **Transitions:** `Tools/Transitions/build.sh`, then `build/transitions build/transitions-burton halloweenTown maitlandHouse`.
- **In the app:**
  - Settings → Universe → Clawd Burton: new sessions are heroes, subagents can be villains or small fry.
  - The screen saver's Options list it.
  - Random and Clawd Royale reach it; the menu icon and arch-enemies hold in a Burton place.
- **Take a number:** `/compact` in a Claude session led by Adam or Barbara, and one led by Beetlejooce.

## Transitions (`BurtonTrip`, 12)

Each is weighted by who's on screen and where, like `ClawdbergTrip`.

**Style.** Drawn in the app's pixel art, never painted or glossy. The universe's palette: ink black and bone white (stripes everywhere), moonlit blue-violet, pumpkin orange, slime green, and a deep blood red used sparingly; each film's own palette where a trip belongs to one film (Wonka's candy colours, Frankenweenie's greys, Corpse Bride's grey-blue against colour). Spirals and black-and-white stripes are the signature shapes: they read at any size. A little grain where it helps; no fine detail that won't read.

**Finishing touch.** Every trip ends with the new place's name written in **spidery, curling hand-lettering** in a corner, with a little spiral flourish under it, the way Burton's titles look. Evoked, not copied: our own lettering, built from pixel strokes.

| # | Transition | What happens | More often with |
|---|---|---|---|
| 1 | **The Model Town Flyover** (signature opening) | The camera glides low over a hill town at dusk: rooftops, a river, the covered bridge, down a lane to a white house on a hill. A spider walks into view, enormous; pull back and it's a model on the attic table. The camera dives into the model's front door and comes out in the new place. The longest and rarest. | any time, rarely; the model town and the Maitlands' house |
| 2 | **Spiral Hill Unfurls** | A curled spiral of hill rises in silhouette against the moon, uncurls across the screen like a tongue, and rolls out the new place as it goes. | Jack, Zeero; Halloween Town, Spiral Hill |
| 3 | **The Jack-o'-Lantern** | A huge carved pumpkin swings in; its grin opens wider and wider, the candle glow inside showing the new place, until the mouth fills the screen. | Halloween Town's residents; Halloween Town, Oogie's lair |
| 4 | **Black-and-White Stripes** | Stripes slide in from both sides like Beetlejooce's suit, twist into a spinning barber-pole spiral, and unwind on the new place. | Beetlejooce, Bob; the model town |
| 5 | **The Sandworm** | The floor ripples, the striped sandworm bursts up and swallows the picture; it dives and the new place is left in its wake under settling sand. | the Sandwurm, the Maitlands; Saturn, the Maitlands' house |
| 6 | **Grey to Colour** | The old place drains to grey-blue like Corpse Bride's living world; a flurry of blue butterflies sweeps across; behind them the new place blooms into colour. | Emilee, Bonejingles, Victor Van Dawt; the Land of the Dead, the village |
| 7 | **The Horseman's Ride** | Mist rolls in; hoofbeats; the Headless Horseman gallops across, his sword sweeping a clean horizontal line. The top half of the picture slides off one way, the bottom the other, and the new place is behind them. | the Horseclawd, Ichabod; the Tree of the Dead, Sleepy Hollow |
| 8 | **Ice Dance** | Ice shavings fly up as if from Edward's blades and fall as snow, thicker and thicker, until the screen is white; it thins on the new place, with Kim's twirl in silhouette. | Edward, Kim; the castle, the cul-de-sac |
| 9 | **Saucer Swarm** | A formation of Martian saucers swoops in, zapping the picture with green rays until it breaks into pixels; they peel off and the new place is there. A tiny "ACK ACK" on the way out. | the Martians; the saucer deck, Perkinsville, the Galaxy |
| 10 | **Wonkavision** | The old picture breaks into a million tiny pixels that fly up over the screen and come down again inside an old TV set, which then zooms out to fill the screen as the new place. Made for pixel art. | Wonky, Mike Teevee; the Chocolate Room |
| 11 | **Down the Rabbit Hole** | The picture falls away; we drop down a long earthy hole past floating clocks, teacups and a piano, and land in the new place. | Alice, McTwisp, Tarrant; the tea party, Salazen Grum |
| 12 | **It's Alive!** | Lightning strikes a kite overhead; the scene flashes black and white, the new place appears in greys, and colour seeps back in (unless it's a Frankenweenie place, which stays grey). | Victor Frankenstien, Sparkie; the attic, the windmill |

**Not used, and why:** the Train to the Great Beyond (Beetlejuice already has three); Chessur's grin (better as his habit, and it'd overlap the jack-o'-lantern's grin); Oogie's roulette wheel (fine detail, and the lair is already the jack-o'-lantern's turf); the Bat-Signal and Gotham's skyline (Batman is Detective Clawds'); a cut-paper "Burton logo" title card (too close to copying a studio logo).

**Promo.** The Model Town Flyover (#1) opens the trailer, as Doctor Clawd's opens on the time vortex.

## Promo: the Clawd Burton trailer (`REEL=burton`)

Built on the Doctor Clawd and Clawdberg trailers in `Tools/RenderPromo/main.swift`, about 45–50 seconds.

- **Intro (~9 s): the flyover.** Dusk clouds part over a hill town; the camera glides across rooftops, over the river and the covered bridge, up a lane to the white house. The giant spider walks across; pull back to the attic table and the model. In the model graveyard a little striped figure pops up (Beetlejooce) and waves. **CLAWD BURTON** curls up out of the mist in spidery hand-lettering with a spiral underline, and the camera plunges through the model's door.
- **Set piece (~9.5 s): Mars Attacks Halloween Town.** Saucers drop over Halloween Town square, zapping pumpkins. The residents scream happily, as if it's a holiday. Jack stretches his scariest face; the Martians aren't scared. Then Grandma Florenz rides in on the coffin sleigh, turns up her record player: the yodel (our own notes) blasts out, and the Martians' domes pop with green goo, cartoon-style. Beetlejooce springs out of the fountain: "It's showtime!"
- **Shared shots:**
  - `hook`: as every trailer.
  - `desktop`: `brawl(ctx, .clawdBurton, …)`, with "The ghost with the most."
  - `status`: four characters, one per state; the Mayor's two faces as the funny aside ("Working… or worried?").
  - `agents`: "Every subagent gets to be a monster."
  - `window`: `windowShot(ctx, .clawdBurton, …, at: .halloweenTown)`, with "Strange and unusual."
  - `ais`: the BRING YOUR OWN AI* line-up: Jack (Claude), Willy Wonky (Desktop), Edward (Codex), Alice (Copilot), Ichabod (Qwen), Lydia (Gemini), Sparkie (pi).
  - `endcard`: Halloween Town at night, the crew lined up, the title lands with a spiral flourish, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS".
- **Music:** in the *sound* of a Burton score, never its melodies: a lopsided waltz in 3/4, wordless "la-la" choir pads, celesta and pizzicato strings, tuba on the low end, a theremin-ish wobble for the Martians. Hits on the spider's reveal, the title, the record's first note and the end card. Our own notes throughout.
- Storyboard first (`REEL=burton build/renderpromo storyboard promo`), shown to you before rendering video.

## Open questions for you

1. **The name.** Clawd Burton (recommended). Alternatives: **Tim Clawdton** (closest to the real name, but uses his first name), **Clawdburton** (one word, harder to read), **The Clawd Before Christmas** (lovely, but it promises one film and this is nine).
2. **The films.** The default is the nine above. Ready to add, or to swap in for a group:
   - **Big Fish** (+4 heroes, +3 villains): Edward Bloome (tall-tale teller, a fish on a line), Karl the Giant, Amos Callaway (the werewolf ringmaster), Sandra Bloome; villains the Witch with the glass eye (eerie, she shows how you'll die, kept vague), Don Price, Norther Winslow (the poet-turned-robber). Place: Spectre, the hidden town with shoes on the line. A daffodil-field transition would replace one of the twelve.
   - **Pee-wee's Big Adventure** (+3 heroes, +2 villains): Pee-wee Herclawd, Dottie, Large Marge (the ghost trucker; her claymation scare face as a signature); villains Francis Buxton and the bike thief. Ride: Pee-wee's bike. Place: Pee-wee's house and its breakfast machine.
   - **Miss Peregrine's Home for Peculiar Children** (+6 heroes, +3 villains): Miss Peregrine (turns into a falcon), Jake, Emma (floats, air), Olive (fire hands), Bronwyn (strong), Enoch (clay soldiers); villains Barron, a Hollowgast (invisible to most, so it'd need an outline trick), a Wight. Lots of distinct powers, and it'd push the count to about 109.
   - **Wednesday:** out by default (The Addams Family is its own franchise, only partly Burton's), but say so if you want her.
   - **Batman and Batman Returns:** out (the cast is already in Detective Clawds). **Sweeney Todd:** out (murder and cannibal pies).
3. **Beetlejuice as a villain**, and the villain side's lead. Or would you rather he were a hero-side trickster? (Then the villain lead would be Ooogie Boogie.)
4. **Compaction:** "Take a number" for the Recently Deceased (recommended, with Beetlejooce's three calls), or "It's alive!" for Frankenweenie's reanimated pets?
5. **Children as troublemaker villains:** the four Wonka kids and Frankenweenie's classmates. Keep them as villains (silly fights, nobody hurt), or move the classmates to heroes and leave only the monsters as villains?
6. **Swaps:** any character you'd rather have in or out. A swap keeps the count.
