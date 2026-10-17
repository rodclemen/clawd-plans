---
name: outline-frame-rule
description: Characters' white outline is cut wherever solid art reaches the 72x52 frame edge; check with build/preview edges
metadata:
  type: project
---

The app outlines only fully opaque pixels inside each character's 72x52 canvas, so art on or past the edge loses its outline there, and half-opaque edge pixels make it dotted. Fixed for every character in 3.6.0 (2026-10-17), and the rule is now in clawdify_guide.md's "Look and style" section.

**How to apply:** after drawing or changing any character, run `build/preview edges out.txt "<Universe title>"` (80 moments of each state, 40 of each habit/signature). Everything it lists must be on purpose: shots, thrown things, exits, things from the sky. The user approves such art fixes one by one from before/after pictures. Related: [[audit-plan-2026-10]].
