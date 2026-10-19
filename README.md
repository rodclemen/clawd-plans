# Clawd plans

Plans for [Clawd Clash](https://github.com/rodclemen/clawd-clash) universes, written with [`clawdify_guide.md`](clawdify_guide.md) (a copy of the one in the clawd-clash repo, as of 3.7.0). Plans only, no code.

Folders: plans at the top level are free to pick up; `in-progress/` is being built by someone (don't start it); `done/` is built and released.

The status below fills itself in. Every few hours [`scripts/status.py`](scripts/status.py) looks at clawd-clash (and the forks) on GitHub and works out how far each universe has got: its phase, how many of the plan's characters and places are drawn, and the release it shipped in. It can only see pushed branches. Each plan says where its build lives in a hidden `<!-- track: … -->` line under its title; a new plan needs one too.

<!-- track: kind=overhaul repo=rodclemen/clawd-clash branch=universe-modules title="Detail overhaul" source="Every released universe redrawn to the detail bar the Star Clawds refresh set. Counted from the `detail` line in each universe's `universe.conf`." -->
<!-- track: repo=rodclemen/clawd-clash folder=ClawdOfTheRings title="Clawd of the Rings" source="The Lord of the Rings, no plan here (PR #3)" cast=76 places=22 who=Henrik -->

<!-- status:start -->
🚧 **1** being built · ✅ **5** released · 📝 **10** ready to pick up

### 🚧 Being built

| Universe | Progress | Where it's at |
|---|---|---|
| **[Clawd Burton](in-progress/clawd-burton.md)**<br><sub>Tim Burton's films</sub> | `░░░░░░░░░░` 0% | **In progress**<br><sub>Henrik · `feature-burton` in HEM42/clawd-clash, nothing pushed yet</sub> |

### 🎨 Detail overhaul

Every released universe redrawn to the detail bar the Star Clawds refresh set. Counted from the `detail` line in each universe's `universe.conf`.

**Overall** `█░░░░░░░░░` 7% · 81/934 characters · 4/213 places<br><sub>`universe-modules`, last commit 19 Oct</sub>

| Universe | Characters | Places |
|---|---|---|
| **Star Clawds** | `██████████` 100%<br><sub>81/81</sub> | `██░░░░░░░░` 18%<br><sub>4/22</sub> |
| **Marvelous Clawds** | `░░░░░░░░░░` 0%<br><sub>0/193</sub> | `░░░░░░░░░░` 0%<br><sub>0/43</sub> |
| **Detective Clawds** | `░░░░░░░░░░` 0%<br><sub>0/207</sub> | `░░░░░░░░░░` 0%<br><sub>0/43</sub> |
| **Doctor Clawd** | `░░░░░░░░░░` 0%<br><sub>0/97</sub> | `░░░░░░░░░░` 0%<br><sub>0/20</sub> |
| **The Clawd Files** | `░░░░░░░░░░` 0%<br><sub>0/81</sub> | `░░░░░░░░░░` 0%<br><sub>0/20</sub> |
| **Stevie Clawdberg** | `░░░░░░░░░░` 0%<br><sub>0/117</sub> | `░░░░░░░░░░` 0%<br><sub>0/23</sub> |
| **Clawd of the Rings** | `░░░░░░░░░░` 0%<br><sub>0/75</sub> | `░░░░░░░░░░` 0%<br><sub>0/22</sub> |
| **Clawd Slayer** | `░░░░░░░░░░` 0%<br><sub>0/83</sub> | `░░░░░░░░░░` 0%<br><sub>0/20</sub> |

### 📝 Ready to pick up

| Universe | Size |
|---|---|
| **[Battleclawd Galactica](battlestar.md)**<br><sub>Battlestar Galactica 2004 and Caprica</sub> | 51 characters · 17 places |
| **[James Clawd](clawd-james-clawd.md)**<br><sub>007</sub> | 96 characters · 21 places |
| **[Clawd Trek](clawd-trek.md)**<br><sub>Star Trek</sub> | 100 characters · 21 places |
| **[Clawdformers](clawdformers.md)**<br><sub>Transformers</sub> | 112 characters · 23 places |
| **[Clawds of the Universe](clawds-of-the-universe.md)**<br><sub>He-Man and She-Ra</sub> | 85 characters · 21 places |
| **[Dungeon Clawd Carl](dungeon-crawler-carl.md)**<br><sub>Dungeon Crawler Carl, all eight books</sub> | 95 characters · 20 places |
| **[Game of Clawds](game-of-clawds.md)**<br><sub>Game of Thrones</sub> | 99 characters · 20 places |
| **[Harry Clawder](harry-potter.md)**<br><sub>Harry Potter, the seven books and eight films</sub> | 85 characters · 22 places |
| **[Stranger Clawds](stranger-things.md)**<br><sub>Stranger Things, all five seasons</sub> | 45 characters · 16 places |
| **[Superclawdtural](supernatural.md)**<br><sub>Supernatural</sub> | 80 characters · 20 places |

### ✅ Released

| Universe | Released in | Size |
|---|---|---|
| **[Clawd Slayer](done/clawd-slayer.md)**<br><sub>Buffy the Vampire Slayer</sub> | **3.7.0** | 84 characters · 20 places |
| **Clawd of the Rings**<br><sub>The Lord of the Rings, no plan here (PR #3)</sub> | **3.5.0**<br><sub>by Henrik</sub> | 76 characters · 22 places |
| **[Stevie Clawdberg](done/stevie-clawdberg.md)**<br><sub>Spielberg's films</sub> | **3.4.0** | 118 characters · 23 places |
| **[The Clawd Files](done/clawd-files.md)**<br><sub>The X-Files</sub> | **3.3.0** | 82 characters · 20 places |
| **[Doctor Clawd](done/doctor-clawd.md)**<br><sub>Doctor Who</sub> | **3.1.0** | 98 characters · 20 places |

### ⚙️ Engine plans

| Plan | Status |
|---|---|
| **[Universes as modules](universe-modules.md)**<br><sub>One folder each, a template that never ships, a checker, and a checkbox per universe in Settings</sub> | 🚧 **in progress**<br><sub>`universe-modules`, 26 commits ahead of `main`, last commit 19 Oct</sub> |
<!-- status:end -->
