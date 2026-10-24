---
name: show-animations-as-gifs
description: "For moving things (fights, signatures, effects) give the owner animated GIFs, not still Preview sheets; effects must read on a dark desktop"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3de462c7-ab63-403c-b587-94edbdd1f04d
  modified: 2026-10-24T09:05:59.107Z
---

When showing anything that moves (a fight effect, a signature, a magic look), give the owner animated GIFs, not still Preview sheets. Also check that dark effects and dark hands still show against the dark desktop.

**Why:** On 2026-10-24 the owner couldn't tell what Abaddon's grip did from the fight and cast sheets ("i need the actual animation instead"). In the GIFs her black hand and the black smoke were invisible on the dark background; only the lift read. The bright coil and her bare orange fist were "much better".

**How to apply:** There's no ffmpeg, so `preview fightclip` crashes before its mp4 step but leaves the PNG frames in `<out>.frames`. A scratch copy of Tools/Preview/main.swift (ffmpeg step removed, plus a `sigclip` mode for one signature) compiled with the same swiftc line as build.sh under zsh gives frames, and PIL turns them into a GIF. Put the GIFs with the review renders in ~/Desktop. Related: [[renders-outside-build]], [[superclawdtural]].
