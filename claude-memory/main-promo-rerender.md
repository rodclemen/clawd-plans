---
name: main-promo-rerender
description: "Main Clawd Clash promo + Clawd Royale teaser need a re-render, held until the LOTR universe is in"
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
