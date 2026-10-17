---
name: main-promo-rerender
description: "Main Clawd Clash promo re-rendered with all seven universes (3.6.0); the Royale teaser video may still need one"
metadata:
  node_type: memory
  type: project
  originSessionId: 9ce77e11-3709-4313-8504-ef04b37376e2
  modified: 2026-10-16T10:17:32.078Z
---

As of 2026-10-16 the main promo (`REEL=promo`, `promo/clawd-clash-promo.mp4`, the README's top video) and the Clawd Royale teaser (`REEL=royale`) are out of date:
- they don't show The Clawd Files or Stevie Clawdberg;
- they count universes ("One app. Three universes. Pick yours.", "ALL THREE UNIVERSES. ONE SCENE.") against the rule in `clawdify_guide.md` (never say how many);
- the rendered main promo predates the BRING YOUR OWN AI* shot (commit efe4f8e), so the video still shows the old AI line-up (no pi, "Claude plays the heroes"); the code is already fixed.

**Why:** the user decided to wait for the Lord of the Rings universe so it's re-rendered only once (2026-10-16).

**How to apply:** when the LOTR universe is done, bring this up: add the new universes to both reels, reword the counts, re-render (1080p + 720p), and ask the user to upload the new 720p. Related: [[stevie-clawdberg-universe]].

**Update 2026-10-17:** the main promo is done. It was rebuilt on branch `promo-seven` (now merged into main) to show all seven universes as comic-book pages and to grow with the universe list, re-rendered at 1080p (85.8 MB, under GitHub's 100 MB limit thanks to a bitrate cap) and 720p, and uploaded; the README plays it, released with 3.6.0. The Royale teaser's code handles any number of universes, but its video wasn't re-rendered then: check `promo/` before assuming it's current.
