---
name: superclawdtural
description: "Superclawdtural (Supernatural parody): released in 4.1.0 on 2026-10-25, number 10, key hunters, prefix Hunt; showcase rodclemen/superclawdtural"
metadata:
  node_type: memory
  type: project
  originSessionId: 3de462c7-ab63-403c-b587-94edbdd1f04d
  modified: 2026-10-23T16:07:50.134Z
---

The Supernatural universe is **Superclawdtural**, spelled with "clawd" (the user corrected "Superclawtural" on 2026-10-17). A code key like `hunters` is fine.

**Started 2026-10-23:** number 10 (reserved on `main` in 7b71584, not pushed yet), branch `superclawdtural`, folder `Sources/App/Universes/Superclawdtural/`, prefix `Hunt`, key `hunters`, reel `hunters`. Made with `Tools/new-universe.sh`. Plan: clawd-plans `in-progress/superclawdtural.md` (updated 2026-10-23 to the folder flow). Release will be 4.1.0 (version rule changed 2026-10-25).

**Names (2026-10-23):** every pun gets its "d": Dean and Sam Winclawdster, Clawdstiel, Clawdley (Crowley; owner OK'd despite The Clawd Files' Tad O'Clawdley), Bobby Clawdsinger, Balthaclawds, Garth Fitzclawd IV, Charlie Clawdbury, Rowena MacClawd.

**Released 2026-10-25 in 4.1.0** (merge 777b49c, tag v4.1.0, notarized, cask updated). Showcase repo rodclemen/superclawdtural is public. The trailer is at user-attachments cdd105eb-1056-415e-b5bc-9cce6e1ae66a, in both READMEs. The owner still has to upload the showcase's social preview by hand (Settings → General). Lessons:
- Stress-test places and trips over many sizes: a `lo..<hi` range with lo > hi crashed four of them.
- Adding a universe can push the main promo's vortex title past its shot. The waves now close up to fit (535a0ed).

**Why:** the user explicitly asked that the build follow clawdify_guide.md; the folder flow means nothing outside the folder changes except NUMBERS.

**How to apply:** fixes after the release are PRs that touch only its folder. During the build it went one phase at a time, show Preview sheets before the next; check.sh Superclawdtural every phase; changelog/README text goes in the hand-off, not CHANGELOG.md. One engine request: Clawdstiel appearing behind the nearest hero (phase 4, built on main as its own commit, or dropped). Related: [[clawd-not-claw]], [[version-rule]], [[stranger-clawds]].
