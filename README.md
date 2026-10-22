# Clawd plans

Plans for [Clawd Clash](https://github.com/rodclemen/clawd-clash) universes, written with [`clawdify_guide.md`](clawdify_guide.md) (a copy of the one in the clawd-clash repo, as of 3.7.0). Plans only, no code.

Folders: plans at the top level are free to pick up; `in-progress/` is being built by someone (don't start it); `done/` is built and released.

The status below fills itself in. Every few hours [`scripts/status.py`](scripts/status.py) looks at clawd-clash (and the forks) on GitHub and works out how far each universe has got: its phase, how many of the plan's characters and places are drawn, and the release it shipped in. It can only see pushed branches. Each plan says where its build lives in a hidden `<!-- track: … -->` line under its title; a new plan needs one too. The detail overhaul reads `main` and `universe-modules` together; a refresh commit can name what it covered in a footer like `Detail: villains, Area 51` (groups are heroes, villains and places).

<!-- track: kind=overhaul repo=rodclemen/clawd-clash branch=universe-modules since=v3.7.0 finished=all title="Detail overhaul" source="Every released universe redrawn to the detail bar the Star Clawds refresh set. Done: what was below the bar was redrawn, the rest was audited and left as it was." -->
<!-- track: repo=rodclemen/clawd-clash folder=ClawdOfTheRings title="Clawd of the Rings" url="https://github.com/rodclemen/clawd-clash/pull/3" source="The Lord of the Rings, built without a plan here (PR #3)" cast=76 places=22 who=Henrik -->

<!-- status:start -->
🚧 **2** being built · ✅ **5** released · 📝 **9** ready to pick up

### 🚧 Being built

| Universe | Progress | Where it's at |
|---|---|---|
| **[Stranger Clawds](in-progress/stranger-clawds.md)**<br><sub>Stranger Things, all five seasons</sub> | `█████████░` 92% | **Phase 6 of 6**, docs and trailer<br><sub>44/44 characters · 16/16 places · `stranger-clawds`, last commit 22 Oct</sub> |
| **[Clawd Burton](in-progress/clawd-burton.md)**<br><sub>Tim Burton's films</sub> | `████████░░` 80% | **Phase 5 of 6**, transitions<br><sub>107/107 characters · 23/23 places · Henrik · `feature-burton` in HEM42/clawd-clash, last commit 21 Oct</sub> |

### 🎨 Detail overhaul

Every released universe redrawn to the detail bar the Star Clawds refresh set. Done: what was below the bar was redrawn, the rest was audited and left as it was.

**Overall** ✅ finished `██████████` 100% · 934/934 characters · 213/213 places<br><sub>`main` since 3.7.0, last commit 19 Oct</sub>

| Universe | Characters | Places |
|---|---|---|
| **Star Clawds** ✅ | `██████████` 100%<br><sub>81/81</sub> | `██████████` 100%<br><sub>22/22</sub> |
| **Marvelous Clawds** ✅ | `██████████` 100%<br><sub>193/193</sub> | `██████████` 100%<br><sub>43/43</sub> |
| **Detective Clawds** ✅ | `██████████` 100%<br><sub>207/207</sub> | `██████████` 100%<br><sub>43/43</sub> |
| **Doctor Clawd** ✅ | `██████████` 100%<br><sub>97/97</sub> | `██████████` 100%<br><sub>20/20</sub> |
| **The Clawd Files** ✅ | `██████████` 100%<br><sub>81/81</sub> | `██████████` 100%<br><sub>20/20</sub> |
| **Stevie Clawdberg** ✅ | `██████████` 100%<br><sub>117/117</sub> | `██████████` 100%<br><sub>23/23</sub> |
| **Clawd of the Rings** ✅ | `██████████` 100%<br><sub>75/75</sub> | `██████████` 100%<br><sub>22/22</sub> |
| **Clawd Slayer** ✅ | `██████████` 100%<br><sub>83/83</sub> | `██████████` 100%<br><sub>20/20</sub> |

### 📝 Ready to pick up

| Universe | Size |
|---|---|
| **[Battleclawd Galactica](battleclawd-galactica.md)**<br><sub>Battlestar Galactica 2004 and Caprica</sub> | 51 characters · 17 places |
| **[James Clawd](clawd-james-clawd.md)**<br><sub>007</sub> | 96 characters · 21 places |
| **[Clawd Trek](clawd-trek.md)**<br><sub>Star Trek</sub> | 100 characters · 21 places |
| **[Clawdformers](clawdformers.md)**<br><sub>Transformers</sub> | 112 characters · 23 places |
| **[Clawds of the Universe](clawds-of-the-universe.md)**<br><sub>He-Man and She-Ra</sub> | 85 characters · 21 places |
| **[Dungeon Crawler Clawd](dungeon-crawler-clawd.md)**<br><sub>Dungeon Crawler Carl, all eight books</sub> | 95 characters · 20 places |
| **[Game of Clawds](game-of-clawds.md)**<br><sub>Game of Thrones</sub> | 99 characters · 20 places |
| **[Harry Clawder](harry-clawder.md)**<br><sub>Harry Potter, the seven books and eight films</sub> | 85 characters · 22 places |
| **[Superclawdtural](superclawdtural.md)**<br><sub>Supernatural</sub> | 80 characters · 20 places |

### ✅ Released

| Universe | Released in | Size |
|---|---|---|
| **[Clawd Slayer](done/clawd-slayer.md)**<br><sub>Buffy the Vampire Slayer</sub> | **3.7.0** | 84 characters · 20 places |
| **[Clawd of the Rings](https://github.com/rodclemen/clawd-clash/pull/3)**<br><sub>The Lord of the Rings, built without a plan here (PR #3)</sub> | **3.5.0**<br><sub>by Henrik</sub> | 76 characters · 22 places |
| **[Stevie Clawdberg](done/stevie-clawdberg.md)**<br><sub>Spielberg's films</sub> | **3.4.0** | 118 characters · 23 places |
| **[The Clawd Files](done/clawd-files.md)**<br><sub>The X-Files</sub> | **3.3.0** | 82 characters · 20 places |
| **[Doctor Clawd](done/doctor-clawd.md)**<br><sub>Doctor Who</sub> | **3.1.0** | 98 characters · 20 places |

### ⚙️ Engine plans

| Plan | Status |
|---|---|
| **[Universes as modules](done/universe-modules.md)**<br><sub>One folder each, a template that never ships, a checker, and a checkbox per universe in Settings</sub> | ✅ shipped in **3.7.1** |
<!-- status:end -->
