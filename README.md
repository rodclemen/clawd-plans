# Clawd plans

Plans for [Clawd Clash](https://github.com/rodclemen/clawd-clash) universes, written with [`clawdify_guide.md`](clawdify_guide.md) (a copy of the one in the clawd-clash repo, as of 3.7.0). Plans only, no code.

Folders: plans at the top level are free to pick up; `in-progress/` is being built by someone (don't start it); `done/` is built and released.

The Status column fills itself in. Every few hours [`scripts/status.py`](scripts/status.py) looks at clawd-clash (and the forks) on GitHub and works out how far each universe has got: its phase, how many of its characters and places are drawn, and the release it shipped in. It can only see pushed branches. Each plan says where its build lives in a hidden `<!-- track: … -->` line under its title; a new plan needs one too.

| Plan | Universe | Status |
|---|---|---|
| [clawd-trek.md](clawd-trek.md) | Clawd Trek (Star Trek) | plan ready, no branch pushed yet |
| [clawd-james-clawd.md](clawd-james-clawd.md) | James Clawd (007) | plan ready, no branch pushed yet |
| [clawdformers.md](clawdformers.md) | Clawdformers (Transformers) | plan ready, no branch pushed yet |
| [clawds-of-the-universe.md](clawds-of-the-universe.md) | Clawds of the Universe (He-Man and She-Ra) | plan ready, no branch pushed yet |
| [game-of-clawds.md](game-of-clawds.md) | Game of Clawds (Game of Thrones) | plan ready, no branch pushed yet |
| [supernatural.md](supernatural.md) | Superclawdtural (Supernatural) | plan ready, no branch pushed yet |
| [battlestar.md](battlestar.md) | Battleclawd Galactica (Battlestar Galactica 2004 and Caprica) | plan ready, no branch pushed yet |
| [stranger-things.md](stranger-things.md) | Stranger Clawds (Stranger Things, all five seasons) | plan ready, no branch pushed yet |
| [harry-potter.md](harry-potter.md) | Harry Clawder (Harry Potter, the seven books and eight films) | plan ready, no branch pushed yet |
| [dungeon-crawler-carl.md](dungeon-crawler-carl.md) | Dungeon Clawd Carl (Dungeon Crawler Carl, all eight books) | plan ready, no branch pushed yet |
| [in-progress/clawd-burton.md](in-progress/clawd-burton.md) | Clawd Burton (Tim Burton's films) | **in progress**, nothing pushed yet (Henrik, branch `feature-burton` in HEM42/clawd-clash) |
| [done/clawd-slayer.md](done/clawd-slayer.md) | Clawd Slayer (Buffy the Vampire Slayer) | released in 3.7.0 |
| [done/clawd-files.md](done/clawd-files.md) | The Clawd Files (The X-Files) | released in 3.3.0 |
| [done/doctor-clawd.md](done/doctor-clawd.md) | Doctor Clawd (Doctor Who) | released in 3.1.0 |
| [done/stevie-clawdberg.md](done/stevie-clawdberg.md) | Stevie Clawdberg (Spielberg's films) | released in 3.4.0 |
| (no plan here) | Clawd of the Rings (The Lord of the Rings) | built by Henrik (PR #3), in Clawd Clash since 3.5.0 |

## Engine plans

| Plan | What | Status |
|---|---|---|
| [universe-modules.md](universe-modules.md) | Universes as self-contained modules: one folder each, a template that never ships, a checker, and a checkbox per universe in Settings | planned, no branch pushed yet |
