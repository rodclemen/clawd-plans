---
name: planned-universes-batch
description: "Seven more universes planned 2026-10-16 (Buffy first, then Star Trek, 007, Transformers, He-Man, GoT, Tim Burton); plan files in ~/.claude/plans/"
metadata:
  node_type: memory
  type: project
  originSessionId: 0cb5d9d2-8731-4fff-92c1-e3b26663eafb
  modified: 2026-10-16T08:41:50.132Z
---

On 2026-10-16 the user asked for plans for seven more universes, each in its own file in `~/.claude/plans/`:
- **Buffy** (top priority, raw value 6, `case slayer`, branch `buffy`): `buffy.md`. Named **Clawd Slayer**; all open questions settled 2026-10-16 (Angel in, Spike/Faith heroes, Harmony/Illyria villains, Angstel, no swaps): ready for phase 1. Firefly (as a rare cameo pack inside Buffy) was discussed and declined by the user on 2026-10-16: not for now.
- Star Trek `clawd-trek.md` (`clawdTrek`, prefix Trek), 007 `clawd-james-clawd.md` (`spy`, prefix Spy), Transformers = Clawdformers `clawdformers.md` (`clawdformers`, prefix Bots), He-Man = Clawds of the Universe `clawds-of-the-universe.md` (`eternia`), Game of Thrones `game-of-clawds.md` (`thrones`), Tim Burton `clawd-burton.md` (`clawdBurton`).

The others' raw values are "next free when the build starts". As of 2026-10-16 all seven have their open questions settled (a "Decisions" section at the end of each): all are ready for phase 1.

**Why:** the user wants a pipeline of universes after [[clawd-files-universe]] and [[stevie-clawdberg-universe]].

**How to apply:** when the user says start one, resolve its open questions first, then follow clawdify_guide.md step 7.

**Plans repo:** on 2026-10-16 the user asked for a private repo just for the plans: rodclemen/clawd-plans (local clone `~/Documents/- CODE -/clawd-plans`), holding the seven plans plus clawd-files.md and doctor-clawd.md. Keep it in sync whenever a plan in `~/.claude/plans/` changes (copy, commit, push; no Claude attribution).

**Clawd Slayer started 2026-10-16:** branch `buffy` (off main) in clawd-clash; the plan was moved to `in-progress/buffy.md` in clawd-plans and copied to `CLAWD-SLAYER-PLAN.md` at the clawd-clash repo root (working copy for the build; delete before merging, like the Clawd Files handoff). clawd-plans folders: top level = free to pick up, `in-progress/` = someone's building it, `done/` = built.
