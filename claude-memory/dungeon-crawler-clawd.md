---
name: dungeon-crawler-clawd
description: "Dungeon Crawler Clawd (number 12, branch dungeon-crawler-clawd): phases 1-6 done 2026-11-05, owner's review next; art picks; status in the plan"
metadata:
  node_type: memory
  type: project
  originSessionId: eac62097-5ca7-4c97-8a37-6ca7b2bd9735
  modified: 2026-10-30T13:56:41.492Z
---

Dungeon Crawler Clawd, universe 12, on branch `dungeon-crawler-clawd` (pushed to origin 2026-10-30, 763144c). Plan and handoff: clawd-plans `in-progress/dungeon-crawler-clawd.md` ("Handoff" section at the end). Phases 1 to 6 done by 2026-11-05 (polish pass 6d12f11; the Hydra's engine commit is on main as 711cee2); next is the owner's review in clawd-plans `review/dungeon-crawler-clawd/Polish/Needs your call/`, then phase 7 docs. The plan's latest Status section wins.

Owner's art decisions:
- Donut: mostly brown fur with a ginger saddle, tail the same brown as her body, cream ruff and muzzle. The first busy tortie was rejected as "a jumble of gfx".
- Mongo: blue-grey hide (more blue than green), pink only as plumage. All-pink was rejected.
- Prepotente stands on his own; no Bianca under him.

**Why:** the owner steers art by picking from a few takes; give versions when a look is uncertain.
**How to apply:** for new looks, keep few big clean shapes and colours exactly as described; offer takes A-D when asked. Related: [[clawd-four-legs]], [[show-review-images-plainly]].

Lessons from the polish pass (2026-11-05): ten helpers at once pushed the Mac's load to 50-70 and took about two hours; four or five is kinder. Give each helper its own scratch subfolder in the brief, because they share one scratchpad and overwrote each other's scripts. Don't brief `git reset --hard`: a permission check blocks it; say `git merge --ff-only <commit>`. After merging, look for private copies of art that another helper redrew (the Recap's mantis).
