---
name: version-rule
description: "Universe bumps the middle number (4.1.0), everything else the last; first stays at 4; scripts/next-version.sh computes it"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3de462c7-ab63-403c-b587-94edbdd1f04d
  modified: 2026-10-24T22:10:50.935Z
---

From Superclawdtural on (decided 2026-10-25): a new universe newly `shipped` in NUMBERS raises the middle number (4.0.x -> 4.1.0 -> 4.2.0), everything else, features included, the last one (4.1.1). The first number stays at 4 and moves only by hand, for a new generation of the app. Superclawdtural ships as 4.1.0. Committed on main as ed0c418 (script, guide, llms.txt, CHANGELOG).

**Why:** the user felt the numbers were climbing too fast and too high under the 2026-10-23 rule (universe = first number, Stranger Clawds 4.0.0), which would have hit ~13.0.0 with the planned universes. Before that they had 3.N.0 per universe; they still want a universe to be visible in the number.

**How to apply:** don't pick versions by hand; `./release.sh` with no version uses `scripts/next-version.sh`. Never propose a rule that moves the first number per universe again. Related: [[audit-plan-2026-10]].
