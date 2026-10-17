# Plan: a new universe, Clawd Burton (Tim Burton's films)
<!-- track: repo=HEM42/clawd-clash branch=feature-burton folder=ClawdBurton title="Clawd Burton" source="Tim Burton's films" cast=107 places=23 who=Henrik -->

## Context

Clawd Clash has six universes: Star Clawds, Marvelous Clawds, Detective Clawds, Doctor Clawd, The Clawd Files and Stevie Clawdberg. This plan adds a director universe for Tim Burton, built the way Stevie Clawdberg was: one ensemble drawn from a handful of films, grouped by film. Every character, place, move and transition has to carry the show. Nothing is added just to grow the count.

- **Name: Clawd Burton** (decided). It reads at a glance, it's a light pun on the director, and it sits next to "Stevie Clawdberg" as a pair. Like Clawdberg, its title lockup has a small **"universe"** tucked under the name (see Promo).
- **Code naming** avoids the director's name in code, as the other universes avoid theirs:
  - `case clawdBurton` with key `"clawdBurton"`.
  - Folder `Sources/App/Universes/ClawdBurton/`, file prefix `Burton…` (`BurtonRoster.swift`, `BurtonHeroes1.swift`, `burtonTheme`, `BurtonTrip`, `REEL=burton`).
  - Branch `feature-burton` (in HEM42/clawd-clash, off main `90eecab`).
  - Six other universes are being planned at the same time (Star Trek, 007, Transformers, He-Man, Game of Thrones, Buffy), so every top-level name and place key carries the `burton` prefix or a name only this universe would use.
- **Raw value: 8, provisional** (`case clawdBurton = 8`). Clawd of the Rings was merged as 6, so Clawd Slayer (planned as 6) needs another number; 8 leaves 7 free for it. To be confirmed with Rod before merging: ids are rawValue*1000 and permanent.
- **The films (decided, ten):** Beetlejuice and Beetlejuice Beetlejuice (counted as one), Edward Scissorhands, The Nightmare Before Christmas, Corpse Bride, Sleepy Hollow, Mars Attacks!, Charlie and the Chocolate Factory, Alice in Wonderland (2010), Frankenweenie (2012), and **Pee-wee's Big Adventure** (Burton's first feature), added last.
  - **Left out on purpose:** Batman and Batman Returns (Batclawd, the Jester, Cat Burglar and the Puffin already live in Detective Clawds, and they'd look like doubles in Clawd Royale); Sweeney Todd (the whole film is murder and cannibal pies; there's no desktop-toy version of it); Ed Wood and Big Eyes (real people); Dark Shadows (Barnabas's appetite is the point of him); Planet of the Apes (2001) (overlaps Gorilla Grudd's Gorilla City). Wednesday is The Addams Family, its own franchise, so it stays out. Big Fish and Miss Peregrine's Home for Peculiar Children were offered and stay out too.
- **Naming style:** light puns on the on-screen names (Jack Skullington, Edward Scissorclaws, Sandy Clawz, Violet Bluregarde, the Jabberclawky). A near-spelling where no pun fits (Ichabod Craine, Katrina Van Tassle). Actors' names are never used, and the real people who play themselves (Mars Attacks!' singer cameo) are left out.
- **Size:** **107 characters**: 54 heroes including HEM and one agent-only, 53 villains including four agent-only. Plus **23 places** and **12 transitions**.
- **Tone:** Burton is gothic but warm: his monsters are the misunderstood ones. That suits a desktop toy well. Where a film goes darker it's tamed to eerie (see "What's tamed" under Cast).

| Universe              | Heroes | Villains | Total | Places | Transitions |
|-----------------------|--------|----------|-------|--------|-------------|
| Star Clawds           |     36 |       46 |    82 |     22 | plain wipes |
| Marvelous Clawds      |    106 |       88 |   194 |     43 |           7 |
| Detective Clawds      |    111 |       97 |   208 |     43 |          15 |
| Doctor Clawd          |     56 |       42 |    98 |     20 |          10 |
| The Clawd Files       |     36 |       46 |    82 |     20 |          10 |
| Stevie Clawdberg      |     64 |       54 |   118 |     23 |          10 |
| Clawd Burton          |     54 |       53 |   107 |     23 |          12 |

(heroCount includes HEM; villainCount includes agent-only.)

**Viability: a full experience, not a limited one.** 52 heroes can lead a session and 49 villains can, well past the 20-a-side threshold. One thing to know: many Burton heroes don't fight (Sally, Kim, Charlie, the White Queen), so a lot of the hero side is `.none` or throws something silly. That's in keeping with the films, and fights stay fun because the villain side is full of monsters with claws, swords and ray guns.

**How the sides are sorted.** Heroes are the films' protagonists and their friends. Villains are the antagonists, the monsters and the troublemakers. Two calls need care:
- **Beetlejooce is a villain**, and the villain side's lead (decided). He's the films' trickster antagonist: he cons the Maitlands, tries to marry Lydia and has to be sent back. Fans love him, which is exactly why he should lead a side. Claude still plays the heroes.
- **Halloween Town's scary residents are villains** (Oogie Boogie, Lock, Shock and Barrel, Dr. Finkelstein, the Wolfman, the Clown, the Witch), the same way The Clawd Files put its monsters of the week on the villain side. Jack, Sally, Zero, the Mayor and Sandy Claws are heroes.
- The **Wonka children and Victor's Frankenweenie classmates** stay villains in the "troublemakers" sense (decided; the guide allows this, as Fraggle Rock's Gorgs would be). Their fights are silly: Violet throws gum, Augustus a candy bar, Veruca walnuts, Mike his game zapper, and each classmate fights with the lightning-charged pet they brought back (or a silly prop of their own). Nobody is hurt; Violet's signature is turning into a blueberry.
- **Pee-wee's Big Adventure** sorts simply: Pee-wee and his friends are heroes; Francis Buxton, the bike thief and the people who send Pee-wee the wrong way are villains.

## How a universe plugs in (checked against main, ebc02be, on 2026-10-16)

**New code: `Sources/App/Universes/ClawdBurton/`**
- `BurtonRoster.swift`, in the pattern of `StevieClawdberg/ClawdbergRoster.swift`:
  - `enum BurtonHero: Int, CaseIterable` and `enum BurtonVillain: Int, CaseIterable`, append-only, grouped by film with a comment per group, `hem` last.
  - `burtonHeroPersonas` / `burtonVillainPersonas` merged from the Art files with `.reduce([.hem: hemPersona(.clawdBurton)])`.
  - `Location.burtonHome(of:)` for heroes and villains, `burtonNemeses`, the ride closure, `let burtonTheme = Theme(universe:villains:heroes:places:home:nemeses:ride:menuIcon:legend:)` with `legend: .hero(.jackSkullington)`.
  - The `static let` place keys, and `let burtonPlaces` merged from the Places files.
- `Art/BurtonHeroes1…6.swift` and `Art/BurtonVillains1…6.swift`, 8–10 personas per file.
- `Places/BurtonScenes1…N.swift`, two or three places each.
- `BurtonKit.swift`: drawing helpers shared across the Art and Places files, every name prefixed `burton…`. Built in phase 1: `burtonStripes`, `burtonStitches`, `burtonSpiralDisc`, `burtonSpiralHill` and `burtonSpiralHillTop` (for things standing on the hill), `burtonTriangle`, `burtonTopHat`, `burtonLollipop`, and `burtonBeetle` (Beetlejooce drops them; the Oogie bugs can use it).
- `BurtonIcon.swift`: the menu bar icon, 28×26, colour and mono. Spiral Hill curling up under a big moon: it reads at 26 pixels and isn't a character's face.
- `BurtonRides.swift`: the rides' drawings (phase 4), as Clawdberg keeps its own.
- `BurtonTakeANumber.swift`: the compaction effect (phase 4; see Mechanics).
- `BurtonDrills.swift`: the bespoke drills (phase 4).
- `BurtonWipes.swift`: the transitions (phase 5).

**Wiring into the existing code**, copying what `clawdberg` did. Every exhaustive `switch` on `Universe` turns a missed spot into a compile error, except the ones marked ⚠︎.
- **`Sources/Shared/Universe.swift`:**
  - `:8–33`: the case, `key`, `title`, `villainCount` (53), `heroCount` (54).
  - `:44–52`: `agentOnly`: villains 49–52 (Bob, the Oogie bug, the squirrel, the Sea-Monkey) and hero 52 (Maggott), as zero-based enum indexes. As global ids that's `base + 49…52` for the villains and `base + StatusStore.heroBase + 52` for Maggott, with a comment naming all five like Clawdberg's line.
  - `:58`: `claudeSide` stays false (Claude is the heroes).
  - `:61`: `rivals`: the two Victors (see Cast).
  - `:66–79`: `abductees` gets the Recently Deceased for "Take a number" (see Mechanics), with a doc comment like Clawdberg's.
- **`Sources/App/Theme.swift:47`:** `case .clawdBurton: return burtonTheme`.
- **`Sources/App/Locations.swift:74`:** `.merging(burtonPlaces) { a, _ in a }`.
- **`Sources/App/Universes/ComicTransition.swift:12, 16, 26, 36–38`:** in phase 1, add `.clawdBurton` to the `nil` cases; in phase 5, a `.burton(BurtonTrip)` case in `duration`, `draw` and `pick`, and the doc comment.
- **`Sources/App/Universes/Hem.swift:27, 87, 101, 121, 143, 180`:** HEM's persona and costume in every switch (see HEM below).
- **`Sources/App/Rides.swift`:** the new `Ride` cases and their draw dispatch (`coffinSleigh`, `walkingTub`, `sandworm`, `martianSaucer`, `glassElevator`, `herclawdBike`), drawn in `BurtonRides.swift`.
- **`Sources/Saver/SaverView.swift`:** nothing to add any more. Since Clawd of the Rings was merged (`f281192`), the Options list `Universe.offered`.
- **`Universe.isReleased`** is false for Clawd Burton until phase 6 (`self != .clawdBurton`): Settings, Random, Clawd Royale and the screen saver leave it out while it's being built; the tools still see it. Flip it in phase 6.
- ⚠︎ **`Sources/App/Drills.swift:54`:** add `universe != .clawdBurton` to the meditation guard: nobody in these films floats cross-legged. **`:488`:** `.merging(burtonBespokeDrills)`.
- ⚠︎ **`Sources/App/Overlay.swift:865`:** the Playground's five sample prompts (below). Lines 1113 and 1226 show how Clawdberg hooked in its set piece and its OutaTime effect: "Take a number" hooks in the same way, next to OutaTime.
- ⚠︎ **`Sources/App/Pose.swift`** (`classic`) and **`Habits.swift`**: decide per `if` whether Clawd Burton joins; it needs new hooks for Beetlejooce's three calls, the Mayor's head and Chessur's fade.
- **Clawd Royale** picks the cast and places up through `Universe.offered` (so only once it's released). Check the menu bar icon and arch-enemies when a scene is in a Clawd Burton place.
- **Engine, added in phase 1 for Jack's scare:** `Magic.pulse` (`Persona.swift`), drawn in `Pose.swift`, with `screamPeriod` in `Fights.swift`: waves sent out as a scream, a burst of three thick slow arcs every 1.6 seconds, then a pause. Off by default; nobody else uses it. It's its own commit, apart from the Burton ones.
- **Tools:**
  - `Tools/Preview/main.swift:60–93`: the doc comment, `burtonHeroes`/`burtonVillains` batch lists, the `"clawdBurton"` universe lookup, and the batch loops.
  - `Tools/Transitions/main.swift:12, 122`: the usage line and the branch that renders `BurtonWipe.allCases`, plus a `burtonTitle` and `burtonShowcase` like Clawdberg's (`clawdbergTitle` at lines 199–225, the showcase at 262). `burtonTitle` is the lockup described under Promo: CLAWD over BURTON with a small "universe" under the right end of BURTON.
  - `Tools/RenderPromo`: its four exhaustive per-universe switches (window-mode cast, brawl cast, the "pick your universe" caption, `pickVerse`) need a Burton line to compile; phase 1 put in stand-ins (Jack, Sallee and Beetlejooce in Halloween Town, "Coming soon: Clawd Burton.", a "BOO!" panel in violet), to be redone with the trailer.
  - Phase 6: `Tools/RenderPromo` (`REEL=burton`, with its own `burtonTitle` like `clawdbergTitle` at lines 3411–3435), `Tools/RenderDocs`, `Tools/MakeSocial`, `Tools/RenderShowcase`.

**Playground prompts (Overlay.swift:865):**
- "Find out why the topiary test keeps snipping the wrong branch"
- "Write a handbook for the recently deleted files"
- "Add a lightning-rod check before the reanimate step"
- "Make the golden-ticket lookup ignore case"
- "Count the Martians in the logs and tell me which ones come in peace"

## Cast

How the engine's weapons map onto Burton's films:
- **`.none`** for the gentle heroes: Sally, Kim, Charlie, the White Queen (she's vowed never to harm a living thing). They run, point and cheer, as Elliclawd does.
- **`.saber`** for blades and bites: Edward's scissor hands, the Vorpal sword, the Headless Horseman's sword, the Sandworm's jaws, the Red Queen's flamingo mallet, and Beetlejooce's snake arm (a poltergeist changes shape; he doesn't cast spells).
- **`.blaster` + `.thrown(colour)`** for the silly things people throw: Oogie Boogie's dice, Sandy Claws' presents, the March Hare's teacups, Violet's gum, Richie's vinyl records.
- **`.blaster` + `.beam`** for the Martians' ray guns: a green ray with a yellow core.
- **`.lightning` + `Magic`** for real magic. Every caster has its own look (table below), and `magicVariants` gives each its own drawing variant too.
- **Black and white:** Frankenweenie's characters are drawn in greys, as the film is. In Clawd Royale they're instantly from "the black-and-white one", and they can't be mixed up with the colour cast. Corpse Bride's living are drawn in grey-blues and its dead in colour, as the film does.

### Magic, one look per caster

| Caster | Family | Core / glow | What you see |
|---|---|---|---|
| Jack Skullington | `waves` + `pulse` | bone `FFF0D8` / pumpkin `FF8A2A` | the scare: he pulls his scary face, hands clawing, and the fright goes out of his gaping mouth in slow throbbing bursts of arcs, his mouth gaping wider with each |
| The Halloween Witch | jagged | pumpkin `FFE0B0` / `FF7A1A` | forked orange lightning off the end of her broom |
| Delorez | steady ray | white `F4F7FF` / slate `8C9BB0` | a pale wisp drawn out of the target towards her (the soul-suck, kept cartoonish) |
| Otho | `rings` | lilac `E6CCFF` / `9A5BD6` | séance rings rippling out along a faint ray |
| Lady Van Tassle | `spell` | rose `FFC2C2` / crimson `9E1B2E` | a crimson ribbon of sparks: witchcraft |
| The Western Woods Crone | `touch` | pale lime `F2F2A0` / `8F9A2A` | no stream: a sickly glowing fingertip, and a glow round whoever she points at |
| Katrina Van Tassle | `touch` | candle cream `FFF4D0` / gold `D4A645` | a warm protective charm glowing round the friend she points at |
| Grandma Florenz | `waves` | cream `FFF0E0` / pink `FF9EC8` | sound arcs pulsing from her portable record player (the yodelling record) |
| The Jabberclawky | jagged | lavender `F0D6FF` / violet `7A2BD1` | the Jabberwocky's purple lightning breath |
| Victor Frankenstien | jagged | white `FFFFFF` / grey `A8A8A8` | a black-and-white lightning bolt from his kite: the only grey lightning in the app |

The two `touch` casters (Katrina, the Crone) are a good witch and a bad one; their colours are opposite (warm gold, sour lime). The Witch's orange lightning and Victor's grey are the two jagged ones; Thorr's, Stormy's and the Electric Gremlin's are blue-white, so neither is confusable. Jack's scare is pumpkin orange too, but arcs in bursts, not forks; it's orange because the other `waves` casters (Bansheen, the Barrow-write) are green, and it's the only pulsing one.

### Heroes (54)

**The Nightmare Before Christmas (5).** Enum first, so the skeleton's lead hero is case 0.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Jack Skullington | egg-shaped bone-white skull on a thin neck (big black eye sockets, two nose slits, a stitched grin curling up), the spiky bat-wing collar, black pinstripe suit narrower than Clawd, heart-shaped white shirt front, bat bow tie, ragged tails, long arms, bony fingers | the scare (`waves` + `pulse`) | his scary face (skull stretching tall, mouth gaping with teeth, angry eyes, both hands clawing beside it), then a deep bow; callout "What's this?" |
| 2 | Sallee | the rag doll: tall pale-blue face on a stitched neck, big eyes with lashes, dark lips, stitched seams from the mouth, long red yarn hair past her waist, patchwork dress (mustard, teal, lilac, black, pink), long stitched arms and legs | none | her whole arm drops off onto the floor; she picks it up, sews it back with needle and red thread, and wiggles it |
| 3 | Zeero | a small white ghost dog floating on a wispy tail instead of hind legs, floppy ears hanging down, a collar with a bow tie, a glowing pumpkin nose | none, `.hover`, `canSit: false` | his nose blazes like a jack-o'-lantern and he loops once round in the air; callout "Arf!" |
| 4 | The Mayor | a cone of a head, pointed at the top and widest at his collar, the hat perched on the point (a little brim, a tall thin crooked stovepipe); a fat grey tailcoat flaring out like a bell, short pinstriped legs, a white collar with a black spider bow tie, a red rosette; his megaphone. Two faces: happy (tan, spiral eyes, a big toothy grin) and worried (pale, droopy eyes, a zigzag frown) | none, `bulk` | his head spins from one face to the other and back; he wears the worried face while his session waits for you |
| 5 | Sandy Clawz | round red fur-trimmed coat, belt and gold buckle, black boots, big white beard, the hat's tip drooping behind, his sack over his shoulder | presents (`.thrown(red)`), `bulk` | pats his bouncing tummy; callout "Ho ho ho!" |

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

**Pee-wee's Big Adventure (3)**, appended last of the film groups

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 50 | Pee-wee Herclawd | slicked-back hair, rosy cheeks, a too-small grey suit, red bow tie, white shoes | joke-shop novelties from the magic shop (`.thrown(red)`) | kicks off his shoes and does his big-shoe dance on the spot; callout "I know you are, but what am I?" |
| 51 | Dottie | short tousled hair, bike-shop overalls, a spanner in the pocket | none | rings a bike bell and gives a hopeful little wave; callout "Drive-in, Saturday?" |
| 52 | Large Marge | the ghost trucker: big hair, trucker's shirt, a sweet grin, a faint glow round her edges | none | her face stretches into the claymation scare (eyes pop out on stalks, jaw drops), then snaps back to the sweet grin; callout "Tell 'em Large Marge sent ya!" |

Large Marge is the universe's best jump scare, kept eerie-fun: big rubbery clay eyes and a stretched jaw, nothing gory, and her crash story isn't told.

**Agent-only (1):** 53 · **Maggott**, the green worm who lives in Emilee's head, on Clawd's four legs with a little worm hood; only ever an agent.

**HEM (1)**, last as always: 54.

### Villains (53)

**Beetlejuice and Beetlejuice Beetlejuice (5).** Enum first, so the skeleton's lead villain is case 0.

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 1 | Beetlejooce | bursting bright-lime mane round a tall pale mouldy face, dark sunken eyes, huge sharp yellow grin; black-and-white striped suit with white shirt and black tie, black boots | snake arm (melee, `bulk`): his arm turns into a black-and-white banded snake that slithers out and snaps, jaws open, tongue out | his name bubbles up three times and he drops into a striped ring, hands on its rim, and springs back out; a beetle drops out of his sleeve now and then; callout "It's showtime!" |
| 2 | The Sandwurm | huge black-and-white striped worm, a mouth inside its mouth | jaws (melee), `bulk` | rears up and its inner mouth snaps out |
| 3 | Delorez | black gown, dark hair, held together with staples | soul wisp (steady ray) | gathers her pieces and staples them back together |
| 4 | Otho | black turtleneck, red scarf, theatrical | séance rings (`rings`) | reads from the Handbook, arms raised |
| 5 | Jeremee | ghost boy, varsity sweater, a bicycle | none | leans on his bike with a too-charming smile |

**The Nightmare Before Christmas (8)**

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 6 | Ooogie Boogie | the biggest sprite in the universe: a huge pale burlap sack, its tied top flopping over, stitched seams, slanted hollow eyes, a wide stitched grin, stubby arms, four stumpy feet; bugs in green, purple, orange, blue and yellow keep falling out of his seams and scuttling off (`burtonBeetle`) | dice (`.thrown(white)`), `bulk`, can't sit | shakes the dice and rolls them along the floor, then laughs as a seam bulges and a bug pops out; callout "Well, well, well…" |
| 7 | Lok | a small kid in a red suit with a pointy tail, a red devil mask with horns and yellow eyes | pitchfork (melee) | pushes his mask up and grins a wicked grin |
| 8 | Shok | a small kid in a purple dress, a pale witch mask under a tall crooked black hat | broom (melee) | pushes her mask up, cackling, and twirls her broom |
| 9 | Barrell | a small round kid in green, a bone-white skull mask, a mop of dark hair | lollipops (`.thrown(green)`) | pushes his mask up and licks his lollipop |
| 10 | Dr. Finkelclawd | in his wheelchair (it stands in for his legs): white lab coat, round black goggles, a flat beak of a mouth, the top of his head a lid on a hinge | potion bottles (`.thrown(green)`), can't sit | flips the lid of his skull open and scratches his brain |
| 11 | The Wolfclawd | a werewolf in a tattered brown suit, grey-brown fur, pointed ears, a snout, yellow eyes | claws (melee), `bulk` | throws his head back and howls at the moon |
| 12 | The Tear-Away Clown | a pale clown riding a unicycle on the spot (it stands in for his legs), a dark purple shirt with orange pom-poms, red tufts of hair, a little hat | none, can't sit | tears his face off, leaving a dark hole, holds it out, then claps it back on |
| 13 | The Halloween Witch | a green face with a hooked nose and pointed chin, a tall crooked hat with a buckle, a black dress, her broom (she rides it when she flies) | orange forked lightning, `.fly` | loops round in the air on her broom, cackling; callout "Hee hee hee!" |

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
| 28 | Augustus Gloopp | big boy, lederhosen, chocolate smears | a candy bar (`.thrown(brown)`) | stuffs in a chocolate bar |
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
| 38 | Edgar "E" Gorr | hunched, crooked grin, bad teeth | his lightning-charged invisible goldfish, a crackling blob of water (`.thrown(white)`) | shows off his invisible goldfish (an empty bowl, a bubble) |
| 39 | Nassorr | flat-top hair, heavy brow, deep voice | a sparking hamster ball, Colossuss's old one (`.thrown(grey)`) | "Ahh!" arms raised dramatically |
| 40 | Toshiakki | neat hair, competitive glare | bottle rockets (`.thrown(silver)`) | fires up a little rocket bottle |
| 41 | Weird Gurl | huge round eyes, fringe, holding her cat | static-charged fur-balls off Mr. Whiskerz (`.thrown(grey)`) | holds up Mr. Whiskerz, who stares |
| 42 | Mr. Whiskerz | vampire cat with bat wings | fangs (melee), `.fly` | flaps and hisses |
| 43 | Shellee | turtle grown to a kaiju | stomp (melee), `armoured`, `bulk` | roars and stomps, the ground shaking |
| 44 | Colossuss | mummy hamster in bandages | bite (melee) | waddles with its arms out |
| 45 | The Were-Rat | rat-man in tatters | claws (melee) | sniffs the air, whiskers twitching |

All four Wonka children and all four classmates fight with something silly (gum, a candy bar, walnuts, a game zapper, a charged pet or its leftovers). Nobody is hurt; a hit is a splat, a fizz or a puff of fur.

**Pee-wee's Big Adventure (4)**, appended last of the film groups

| # | Name | Look | Weapon | Signature |
|---|---|---|---|---|
| 46 | Francis Buxtun | big spoilt rich boy, curly hair, a striped bathrobe, a toy boat | rubber bath toys (`.thrown(yellow)`) | lolls in a bubble bath with his toy boat, smug, then sinks out of sight |
| 47 | The Bike Thief | a shadowy figure, hat pulled low, collar up, bolt cutters | bolt cutters (melee) | tiptoes, snips a chain, and sneaks off with a cartoon "tee-hee" |
| 48 | Madam Rubee | phoney fortune-teller, turban, beads, a crystal ball | none | waves her hands over the crystal ball, which glows; callout "The basement of the Alamo!" |
| 49 | Andee | Simone's enormous, short-tempered boyfriend, crew cut, plaid shirt | fists (melee), `bulk` | cracks his knuckles and stomps after someone |

Madam Rubee and Andee earn their places: Rubee sends Pee-wee off on the wrong trail (and her turban and crystal ball read at once), and Andee's chase through the dinosaur park is one of the film's big set pieces.

**Agent-only small fry (4).** Like the MSE-6, these only ever appear as agents:
- 50 · **Bob**, one of Beetlejooce's shrunken-head workers in a suit;
- 51 · **an Oogie bug**, a beetle out of Oogie Boogie's seams;
- 52 · **a nut-sorting squirrel** from Wonka's factory;
- 53 · **a Sea-Monkey**, Frankenweenie's monstrous brine shrimp.

(The tables number from 1; the enum indexes are one lower, so the agent-only villains are indexes 49–52 and Maggott is hero index 52.)

### HEM

As always, the last hero. His Clawd Burton costume: a crooked black top hat with a spiral band, a black-and-white striped scarf, and a big spiral lollipop he swings like a club (`.saber`). He's in the universe's colours without looking like anyone in it.

### Nemeses (25)

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
- Pee-wee Herclawd ↔ Francis Buxtun

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
- **Two spoilt boys:** Francis Buxtun (bathrobe, toy boat) and Augustus Gloopp (lederhosen, chocolate smears).
- **Three fortune-tellers and witches:** Madam Rubee (turban and beads, no hat, a crystal ball), the Halloween Witch (green face, tall hat) and the Crone (hunched, grey).
- **Two big faces:** Large Marge's scare and Jack's stretched skull. Marge's is clay-brown and bug-eyed; Jack's is bone white.

Against the six existing universes (they meet in Clawd Royale):
- **Tarrant Hightop vs the Mad Milliner** (Detective Clawds): keep Tarrant's orange hair, white face and patchwork hat strong.
- **Chessur vs Cheshyre** (Detective Clawds' assassin): different names on purpose; one's a cat.
- **Beetlejooce vs the Jester** (Detective Clawds): both have green hair and a pale face. Beetlejooce's black-and-white stripes and his bursting spiky mane keep him apart; no purple anywhere on him (his reference cartoons have purple eye rings and ties; his stay dark grey and black).
- **The Headless Horseclawd vs Ghost Biker** (Marvelous Clawds): no head versus a flaming skull.
- **The Martians vs the Grey and the Tall Visitor** (Clawd Files, Clawdberg): big brains in glass domes; no one else has that.
- **Ooogie Boogie vs the Trashman** (Clawd Files): a neat burlap sack against a heap of rubbish.
- **Edward vs Clawdverine:** leather, buckles and long thin blades on every finger, against three claws and yellow.
- **Pee-wee's bike vs E.T.'s moon bike** (Clawdberg, `moonBike`): a big red-and-white cruiser with chrome and a horn, against a small BMX with a basket and a blanket.
- Check Buffy's plan too when both are drawn: witches and vampires there; Lady Van Tassle and the Halloween Witch should stay distinct.

### What's tamed, and who's left out and why

- **Tamed:** Juno's smoke curls out of her collar, not her throat. Lord Barkis is "the cad who jilted Emily and ran off with her dowry". The Headless Horseman knocks hats off, never heads, and the Tree of the Dead has glowing roots, not heads. Delores's soul-suck is a pale wisp. The Martian ray doesn't strip anyone to a skeleton; it's a zap and a puff. The Red Queen's moat of heads is a moat of heart-shaped lilies. The Tear-Away Clown's face comes off to show a dark hole, nothing more. Large Marge's scare is rubbery clay eyes and a stretched jaw; the story of her crash isn't told.
- **Left out:** the Mars Attacks! singer who plays himself (a real person); Nathalie Lake and her dog's swapped heads, and Professor Kessler's head in a jar (body horror for a desktop toy); the Martian Girl's seduction scene (she's kept as a gum-chewing spy); Absolem (his hookah smoke rings would copy the Cigarette-Smoking Clawd's); Tweedledum and Tweedledee (two people in one sprite won't read); Bayard, Miss Argentina, Charles Deetz, Rory, Bill and Kevin Boggs, Esmeralda, Officer Allen, Taffy Dale, General Decker, Notary Hardenbrook, the Harlequin Demon, Behemoth, the Undersea Gal, Mr. Burgemeister, Persephone, and from Pee-wee's Big Adventure Simone, Mickey the escaped convict, Mario the magic-shop owner and the biker gang (too thin to carry a character, or a near-duplicate of someone kept).

## Places (23)

Each is a `Place` with a still picture, a moving layer and tall-canvas extras for the screen saver. The palettes swing wide on purpose: Halloween orange and black, Corpse Bride's grey-blue living world against its colourful dead, pastel suburbia, candy colours for Wonka, Underland's saturated greens and reds, Frankenweenie in greys, and Pee-wee's toy-box primaries.

| # | Key | Place | Still | Moving layer | Tall-canvas extras |
|---|---|---|---|---|---|
| 1 | `halloweenTown` | **Halloween Town square** (the default) | in purples, under an orange-yellow moon: two rows of crooked houses that bend and bulge with witch-hat roofs curled at the tip, about half pulling jack-o'-lantern faces with their windows; the town hall with a gable, a spider-web rose window, orange-and-black bunting, two curled turrets and a bent spire with a bat vane; the green-slime fountain; pumpkins on the cobbles and on a ridge behind the town | the fountain spouts and bubbles, the carved pumpkins flicker, the rose window glows, a bat flits | Spiral Hill curling in front of a huge moon, a graveyard all over it (graves on both slopes and down its sides, a crooked fence, pumpkins), and the town gates on a far ridge |
| 2 | `spiralHill` | **Spiral Hill** | a near-black sky and a huge yellow moon with the hill's curl in front of it, graves up its slope; tombstones, crosses and an obelisk across the yard, red berry bushes, a crooked iron fence, a stone gargoyle | mist drifts low between the graves; ghost wisps rise and fade | the hill on a far ridge, a middle distance of graves, the yard graves and gargoyle large in front |
| 3 | `oogiesLair` | **Oogie Boogie's lair** | his casino under ultraviolet light: a giant roulette wheel on the back wall with a glowing rim, neon-green arches, a stack of giant dice, a slot machine framed in bulbs, playing cards on the walls, a chequered floor glowing at its edge | the wheel spins, the reels flicker (skull, bug, die), the bulbs chase, the UV light throbs, bugs scuttle across the floor | the rope bridge sagging across and a cage hanging from it |
| 4 | `christmasTown` | **Christmas Town** | candy-coloured toy houses (the odd tower) with snowy roofs and warm windows, a giant tree with a gold star, candy-cane lamp posts, a snowy street | snow falls, the tree's lights twinkle | snowy hills with a far row of little houses, the northern lights rippling, a sleigh crossing far off |
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
| 23 | `breakfastMachineHouse` | **Pee-wee's house and the breakfast machine** | a toy-crammed kitchen in bright primaries, the long Rube Goldberg breakfast machine along the counter, the red-and-white bike by the door | the machine runs its loop: a dinosaur toy tips, a little ball rolls, the toaster pops, a flipped pancake lands on the plate (big, clear moves only) | the sunny yard and Francis's mansion next door over the fence |

Keys checked: none clash with the 150-odd `Location("…")` keys on main (`christmasLondon` and `mothership` exist, so these are `christmasTown` and `martianSaucerDeck`; nothing on main mentions breakfast, bikes or Pee-wee, so `breakfastMachineHouse` is free). Each is a name only this universe would use, so the six sibling plans shouldn't hit them; check again at build time with `grep -rn 'Location("' Sources/App/Universes`.

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
- **Pee-wee's Big Adventure:** everyone at Pee-wee's house: Pee-wee and Dottie; Large Marge (her truck stop isn't a place, so she haunts the house's porch light); Francis (next door), the Bike Thief, Madam Rubee and Andee (they've followed the bike there).
- HEM lives in Halloween Town.

## Mechanics that make it its own universe

1. **Rides** (`BurtonRides.swift`):
   - **Jack's coffin sleigh:** a coffin on runners pulled by skeleton reindeer, Zeero's nose glowing in front. For Jack, Sallee, Zeero, the Mayor and Sandy Clawz.
   - **The walking bathtub:** Lock, Shock and Barrel's clawed tub stomping in on its feet. For Lok, Shok, Barrell and Ooogie.
   - **The Sandworm:** bursts up through the floor, the rider on its back, and dives back down. For Beetlejooce, Delorez and Jeremee (and the Maitlands leave on it, unwillingly: a fun gag, your call).
   - **The Martian saucer:** a classic silver saucer with a clear dome and a ring of flashing lights, drawn new (not the Clawd Files' saucer). For the Martians.
   - **The Great Glass Elevator:** crashes down through the top of the window and lifts off again. For Wonky, Charlie, Grampa Joe, the Oompa-Loompah and Dr. Wilbur Wonky.
   - **Pee-wee's bike:** the big red-and-white cruiser with chrome, a horn and a headlamp, pedalled in fast with a skid stop. For Pee-wee, Dottie and Francis; the Bike Thief rides it too, furtively (it's stolen, after all). Large Marge doesn't ride: she fades in out of the dark. Drawn new, not E.T.'s `moonBike`.
   - Everyone else walks. The Headless Horseman's black horse was considered; a horse is a big new drawing for one rider, so it's left for the polish pass if there's time.
2. **Compaction: "Take a number" (decided).** When a session led by one of **the Recently Deceased** compacts, they're called away to the Afterlife and back. The group is the Beetlejuice ghosts, all clearly dead in the films: Adam, Barbara, Junoh, Wolf Jaxon and the Shrunken-Head Man (heroes 6, 7, 10, 11, 12), and Beetlejooce, Delorez and Jeremee (villains 0, 2, 4).
   - A paper ticket pops out of a dispenser above the leader with a ridiculous number on it; they flicker out like a ghost; a "NOW SERVING" board ticks over; they flicker back, same face.
   - **Beetlejooce does it his way:** his name rises in three speech bubbles, "BEETLEJOOCE!" ×3, and he springs back up through a black-and-white striped ring. Say it three times and he's back.
   - It reuses Clawdberg's route: the list goes in `Universe.abductees`, the effect is drawn in `BurtonTakeANumber.swift` where the overlay draws OutaTime (`Overlay.swift:1226`). No new hook is needed.
   - The ids, zero-based: heroes 6, 7, 10, 11, 12 and villains 0, 2, 4 (unchanged by the Pee-wee additions, which are appended). Large Marge is a ghost too, but she isn't one of the Recently Deceased, so she stays out of the list.
   - "It's alive!" (Frankenweenie's reanimated pets) was the alternative; it lives on as transition #12 instead.
3. **Habits:**
   - **Beetlejooce, three times:** idle, his name ticks up in bubbles, one, two, three, and on the third he vanishes and pops up somewhere else on stage through a striped ring.
   - **The Mayor's two faces:** his head spins to the worried face when a session hits an error or needs approval, and back to the smile when it's going well. It ties straight into the status states. (Built early, in phase 2: his drawing shows the worried face whenever his session is waiting for you.)
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

1. **Skeleton** (**done**, 2026-10-16, branch `feature-burton` in HEM42/clawd-clash, on upstream main `f281192`):
   - the universe case and all the wiring above;
   - Jack Skullington and Sallee (heroes 0 and 1) and Beetlejooce (villain 0);
   - Halloween Town square, the menu icon, HEM's costume, the saver option and Preview support;
   - plain wipes for now (`ComicTransition.pick` returns nil for it).
   
   It runs end to end in the app, the window, the screen saver and Clawd Royale. The whole roster (107) is registered up front with homes and nemeses, so ids never move; the others are stand-ins. Jack, Sallee, Beetlejooce and Halloween Town were each redrawn from reference pictures before moving on (see Decisions during phase 1).
2. **Core ensemble** (in progress: **Nightmare done**, its 11 characters and 3 places, 2026-10-17). About 43 characters, the first four film groups in enum order, each group's design directions agreed with you before it's drawn:
   - Nightmare, Beetlejuice, Edward Scissorhands and Corpse Bride: 24 heroes and 19 villains;
   - 8 places: Halloween Town, Spiral Hill, Oogie's lair, Christmas Town, the Maitlands' house, the model town, the waiting room, and the Land of the Dead;
   - their homes and nemeses (the other places' homes fall back to the default until phase 3).
   - Fine to commit the enum cases first as stand-ins, then draw them in a second commit.
3. **The rest:** Sleepy Hollow, Mars Attacks!, Charlie, Alice, Frankenweenie, Pee-wee's Big Adventure, Maggott and the four agent-only villains: 29 heroes and 34 villains, up to 107 characters and all 23 places, every home filled in. (Big enough to split into 3a, the first three films, and 3b, the last three plus the agent-only, if that's easier to review.) Ends with **the character audit**: every persona's weapon, shots, magic colours, motion, signature and callout checked against the films and this roster, and a mismatches table for you.
4. **Mechanics:** the six rides, "Take a number", the habits and the bespoke drills.
5. **Transitions:** the twelve `BurtonTrip`s and the spidery caption (below), wired through `ComicTransition`.
6. **Polish pass:** every weak spot noted in phases 2–5, fixed together, split by file and run in parallel with before-and-after renders for you. Always before phase 6.
7. **Docs and release (phase 6):**
   - the README's universe table and a collapsible cast-and-places section; the screen-saver paragraph; the developer notes;
   - `Tools/RenderDocs`: a `burtonLineup` desktop strip, `roster-clawd-burton.png`, `locations-clawd-burton.png` and a social preview; `Tools/MakeSocial`, `Tools/RenderShowcase`;
   - `llms.txt`: the universe list, the folder and `Burton…` prefix, and "Take a number";
   - the `CHANGELOG.md` entry, written once, here at the end: CHANGELOG.md is the file upstream changes most, so an entry per phase would make every rebase conflict;
   - the trailer, `REEL=burton` (see Promo), with the `burtonTitle` lockup (CLAWD over BURTON, a small "universe" under BURTON's right end) on the intro, the end card, the transitions showcase and the social preview.
   - **Needs your OK first, since it's public:** a showcase repo, a cask in `release.sh` (`write_cask`, the `others` list), releasing, pushing, a PR.

Ids are append-only, so the enum order is the order characters are added, and phases never renumber.

## Verification

- **Build:** `./build.sh`. The cast-size assert in `Overlay.swift` catches a wrong `heroCount` or `villainCount`. Before calling a phase done, `./build.sh --release <version>` too: dense `sin`/`cos` drawing (spirals!) can hit "unable to type-check in reasonable time"; find them with `-Xfrontend -warn-long-expression-type-checking=300` and split them up.
- **Characters:** `Tools/Preview/build.sh`, then:
  - `build/preview cast out.png "Jack Skullington"`;
  - `build/preview fight out.png "Jack Skullington" "Ooogie Boogie"`;
  - `SCALE=6 SECONDS=8 build/preview fightclip out.mp4 jackSkullington beetlejooce` for a moving fight, an mp4 (a melee opponent, like `indianaBones`, shows Beetlejooce's snake striking; against magic he only blocks);
  - `build/preview fight out.png "Victor Van Dawt" "Victor Frankenstien"` (side by side, to check they read apart);
  - `build/preview fight out.png "Pee-wee Herclawd" "Francis Buxtun"`;
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
| 1 | **The Model Town Flyover** (signature opening) | The camera glides low over a hill town at dusk: rooftops, a river, the covered bridge, down a lane to a white house on a hill. A spider walks into view, enormous; pull back and it's a model on the attic table. The camera dives into the model's front door and comes out in the new place. The longest and rarest. | any time, rarely; the model town, the Maitlands' house, Pee-wee's house |
| 2 | **Spiral Hill Unfurls** | A curled spiral of hill rises in silhouette against the moon, uncurls across the screen like a tongue, and rolls out the new place as it goes. | Jack, Zeero; Halloween Town, Spiral Hill |
| 3 | **The Jack-o'-Lantern** | A huge carved pumpkin swings in; its grin opens wider and wider, the candle glow inside showing the new place, until the mouth fills the screen. | Halloween Town's residents, Large Marge (the other big scary face); Halloween Town, Oogie's lair |
| 4 | **Black-and-White Stripes** | Stripes slide in from both sides like Beetlejooce's suit, twist into a spinning barber-pole spiral, and unwind on the new place. | Beetlejooce, Bob; the model town |
| 5 | **The Sandworm** | The floor ripples, the striped sandworm bursts up and swallows the picture; it dives and the new place is left in its wake under settling sand. | the Sandwurm, the Maitlands; Saturn, the Maitlands' house |
| 6 | **Grey to Colour** | The old place drains to grey-blue like Corpse Bride's living world; a flurry of blue butterflies sweeps across; behind them the new place blooms into colour. | Emilee, Bonejingles, Victor Van Dawt; the Land of the Dead, the village |
| 7 | **The Horseman's Ride** | Mist rolls in; hoofbeats; the Headless Horseman gallops across, his sword sweeping a clean horizontal line. The top half of the picture slides off one way, the bottom the other, and the new place is behind them. | the Horseclawd, Ichabod; the Tree of the Dead, Sleepy Hollow |
| 8 | **Ice Dance** | Ice shavings fly up as if from Edward's blades and fall as snow, thicker and thicker, until the screen is white; it thins on the new place, with Kim's twirl in silhouette. | Edward, Kim; the castle, the cul-de-sac |
| 9 | **Saucer Swarm** | A formation of Martian saucers swoops in, zapping the picture with green rays until it breaks into pixels; they peel off and the new place is there. A tiny "ACK ACK" on the way out. | the Martians; the saucer deck, Perkinsville, the Galaxy |
| 10 | **Wonkavision** | The old picture breaks into a million tiny pixels that fly up over the screen and come down again inside an old TV set, which then zooms out to fill the screen as the new place. Made for pixel art. | Wonky, Mike Teevee; the Chocolate Room |
| 11 | **Down the Rabbit Hole** | The picture falls away; we drop down a long earthy hole past floating clocks, teacups and a piano, and land in the new place. | Alice, McTwisp, Tarrant; the tea party, Salazen Grum |
| 12 | **It's Alive!** | Lightning strikes a kite overhead; the scene flashes black and white, the new place appears in greys, and colour seeps back in (unless it's a Frankenweenie place, which stays grey). | Victor Frankenstien, Sparkie; the attic, the windmill |

**Not used, and why:** the Train to the Great Beyond (Beetlejuice already has three); Chessur's grin (better as his habit, and it'd overlap the jack-o'-lantern's grin); Oogie's roulette wheel (fine detail, and the lair is already the jack-o'-lantern's turf); the Bat-Signal and Gotham's skyline (Batman is Detective Clawds'); a cut-paper "Burton logo" title card (too close to copying a studio logo); Pee-wee's breakfast machine as a chain-reaction wipe (lovely, but fine detail for one place, and it's already that place's moving layer), so no 13th transition. The Pee-wee cast instead nudges two existing ones: Large Marge owns a share of the Jack-o'-Lantern, and Pee-wee's house counts as turf for the Model Town Flyover (another small-town house the camera can dive into).

**Promo.** The Model Town Flyover (#1) opens the trailer, as Doctor Clawd's opens on the time vortex.

## Promo: the Clawd Burton trailer (`REEL=burton`)

Built on the Doctor Clawd and Clawdberg trailers in `Tools/RenderPromo/main.swift`, about 45–50 seconds.

- **Intro (~9 s): the flyover.** Dusk clouds part over a hill town; the camera glides across rooftops, over the river and the covered bridge, up a lane to the white house. The giant spider walks across; pull back to the attic table and the model. In the model graveyard a little striped figure pops up (Beetlejooce) and waves. The **Clawd Burton title lockup** (below) curls up out of the mist, and the camera plunges through the model's door.
- **Set piece (~9.5 s): Mars Attacks Halloween Town.** Saucers drop over Halloween Town square, zapping pumpkins. The residents scream happily, as if it's a holiday. Jack stretches his scariest face; the Martians aren't scared. Then Grandma Florenz rides in on the coffin sleigh, turns up her record player: the yodel (our own notes) blasts out, and the Martians' domes pop with green goo, cartoon-style. Beetlejooce springs out of the fountain: "It's showtime!"
- **Shared shots:**
  - `hook`: as every trailer.
  - `desktop`: `brawl(ctx, .clawdBurton, …)`, with "The ghost with the most."
  - `status`: four characters, one per state; the Mayor's two faces as the funny aside ("Working… or worried?").
  - `agents`: "Every subagent gets to be a monster."
  - `window`: `windowShot(ctx, .clawdBurton, …, at: .halloweenTown)`, with "Strange and unusual."
  - `ais`: the BRING YOUR OWN AI* line-up: Jack (Claude), Willy Wonky (Desktop), Edward (Codex), Alice (Copilot), Ichabod (Qwen), Lydia (Gemini), Sparkie (pi).
  - `endcard`: Halloween Town at night, the crew lined up, the title lockup lands with its spiral flourish, "Have fun. Keep track.", "One of many universes in Clawd Clash · free for macOS".
- **The title lockup, `burtonTitle`.** Like `clawdbergTitle` (`Tools/Transitions/main.swift:199–225`, `Tools/RenderPromo/main.swift:3411–3435`), one function per tool, used for the trailer intro, the end card, the transitions showcase and the social preview.
  - **Two lines, CLAWD over BURTON**, not one: spindly lettering needs height to read, and a single long line would shrink it to hairlines. CLAWD sits smaller on top, BURTON big below, as STEVIE sits over CLAWDBERG.
  - **The lettering is Burton-style but our own:** tall, thin, slightly wobbly pixel strokes, letters leaning a touch off true, curled spiral ends on the C, the W's points and the N's tail, and BURTON's O drawn as a full moon. It's built from pixel strokes, not a system font (Clawdberg uses Avenir Next; nothing installed looks spidery), so it shares one small pixel alphabet with the transitions' place-name caption, kept in `BurtonKit.swift`.
  - **A small "universe"** in the same spidery hand, lower case, tucked under the right end of BURTON, just as Clawdberg's sits under CLAWDBERG. BURTON's underline curls off its left end into a spiral (Spiral Hill's shape), leaving room for "universe" at the right.
  - **The Burton palette:** bone white letters `F2EEE3` with an ink-black outline and a moonlit blue-violet glow `6B5BD6` (where Clawdberg glows blue round gold); "universe" in bone white with a softer glow. A fleck of pumpkin orange only in the moon-O's shading.
  - `alpha` fades it and `scale` grows it, exactly as `clawdbergTitle` does.
- **Music:** in the *sound* of a Burton score, never its melodies: a lopsided waltz in 3/4, wordless "la-la" choir pads, celesta and pizzicato strings, tuba on the low end, a theremin-ish wobble for the Martians. Hits on the spider's reveal, the title, the record's first note and the end card. Our own notes throughout.
- Storyboard first (`REEL=burton build/renderpromo storyboard promo`), shown to you before rendering video.

## Decisions (2026-10-16)

1. **Name: Clawd Burton.** Like Stevie Clawdberg, its title lockup has a small "universe" tucked under the name: CLAWD over BURTON in spidery pixel lettering, bone white with a moonlit violet glow, "universe" under the right end of BURTON (`burtonTitle`, see Promo; used on the trailer intro, end card, transitions showcase and social preview).
2. **Films: the nine plus Pee-wee's Big Adventure**, appended last. Big Fish and Miss Peregrine stay out; Wednesday, the Batman films and Sweeney Todd stay out. Pee-wee brings heroes Pee-wee Herclawd, Dottie and Large Marge (table rows 50–52), villains Francis Buxtun, the Bike Thief, Madam Rubee and Andee (rows 46–49; Madam Rubee and Andee added because they truly carry the film), a sixth ride (Pee-wee's bike, `herclawdBike`), a 23rd place (`breakfastMachineHouse`), the nemesis pair Pee-wee ↔ Francis, and a share in two existing transitions (no 13th). The agent-only ids move to villains 49–52 and hero 52 (Maggott), zero-based.
3. **Beetlejooce is a villain** and leads the villain side.
4. **Compaction: "Take a number"** for the Recently Deceased, with Beetlejooce's three calls.
5. **Children stay troublemaker villains:** the four Wonka kids and Victor's Frankenweenie classmates, each with something silly to fight with (gum, a candy bar, walnuts, a game zapper, a charged pet or its leftovers).
6. **Swaps:** none.

New totals: 54 heroes (HEM and Maggott included), 53 villains (four agent-only), 107 characters, 23 places, 12 transitions.

## Decisions during phase 1 (2026-10-16, Henrik, with Rod's note on the scare)

1. **Raw value 8**, provisional (see Context), and **unreleased** (`isReleased` false) until phase 6.
2. **Jack fights by scaring**, not with a green flame: on screen, scaring is what he does. `waves` + the new `pulse`: slow throbbing bursts (Rod asked for slower and pulsing), bone-white arcs with a pumpkin glow, his scary face gaping in time. Redrawn from reference pictures: egg skull, thin neck, bat-wing collar (three broad filled spikes a side; thin lines turned into fishbones under the app's outline), heart-shaped shirt front, slimmer suit.
3. **Beetlejooce fights with a snake arm**, not `spell` sparkles: a poltergeist changes shape. `.saber`, with `bulk` so duel partners stand clear of it; the swing stays in front of him. Redrawn from reference pictures (three alternatives, the cartoon one chosen, eyes darkened): bursting lime mane, pale mouldy face, dark sunken eyes, huge sharp grin, white shirt and black tie. No purple (the Jester). Beetles drop out of his sleeve.
4. **Sallee is the rag doll** from the references: tall pale-blue stitched face, long red yarn hair, patchwork dress, long stitched arms; her signature shows the whole arm falling off and being sewn back.
5. **Halloween Town** redrawn from three alternatives (faces, graveyard, pumpkin patch): the faces one chosen, with the graveyard over the whole of Spiral Hill and a town hall with more character.
6. **No CHANGELOG entry per phase;** one at the end (phase 6).

**Weak spots so far** (for the polish pass): HEM's striped scarf hides behind his beard; Sallee's arms are faint at rest and her needle is tiny; Jack's tailcoat tails blur into his back legs; Beetlejooce's shirt V and tie read a little as an "M"; the menu icon's mono version has a notch where the hill's foot meets the moon.

## Decisions during phase 2 (2026-10-17, Henrik)

1. **Before each film group is drawn, its design directions are listed for you to steer.** References help, but stay with the Clawd look: blocky, four short legs, no fine detail; take silhouettes and iconic pieces from the references, not the originals' exact design.
2. **The Mayor** was drawn from photos: his cone head points up (narrow at the top, widest at his collar), the hat on the point with a tall thin crooked stovepipe, a grey bell of a coat. "Cone head" alone didn't say which way the point goes; say so in future rows.
3. **Ooogie Boogie** is the biggest sprite, with bugs of every colour falling out of him (`burtonBeetle`, coloured).
4. **The trick-or-treaters** are small kids with masks on sticks; in their signatures the mask goes up.
5. **Dr. Finkelclawd's wheelchair and the Tear-Away Clown's unicycle stand in for their legs:** the one exception to "always on Clawd's four legs", as The Clawd Files' fishbowl is, because that's what makes them recognisable.
6. **Burton draws its own boots** (`burtonBoots`) instead of borrowing another universe's helpers.

**Weak spots from phase 2:** the Wolfclawd's snout is short (he reads a little like a big cat); Finkelclawd is boxy; Spiral Hill's gargoyle reads more like a hooded statue; the middle of Christmas Town's sky on the screen saver is still mostly snow.

Phase 1 is done; phase 2 is under way (Nightmare done; Beetlejuice next).
