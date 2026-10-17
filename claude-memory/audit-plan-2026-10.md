---
name: audit-plan-2026-10
description: "The Oct 2026 audit plan (security, PR guard, clean-up, performance): its 4 steps and how far each got"
metadata:
  node_type: memory
  type: project
  originSessionId: be19b5c9-e9f0-4576-b0b5-ea68d1892e1a
  modified: 2026-10-16T22:01:08.751Z
---

On 2026-10-16 an audit of Clawd Clash produced a 4-step plan, worked on branch `audit` (fast-forwarded into main as each step finished). The full plan text is in the session transcript 7779a8d3 (it's not in a file).

1. **Security fixes + release 3.5.1:** DONE, released 2026-10-16. CLAWD_SHOT gating was deliberately skipped (it only saves the app's own scene).
2. **PR guard:** DONE 2026-10-17. Pieces: `scripts/pr-guard.py`, `.github/workflows/pr-guard.yml`, CODEOWNERS and CONTRIBUTING.md. GitHub rulesets were applied: main needs PR + code owner + `guard` check, with the admin bypassing. Release tags and homebrew-tap main are protected too. Fork Actions need approval for all external contributors. FilesCaption and Hem's art helpers were left in universe folders on purpose.
3. **Clean-up:** DONE 2026-10-17. Pushed to main as 5d1b851 on 2026-10-17. Also fixed: the Compact Window checkbox, which a user reported (an animated setFrame posts live-resize notifications). Left open:
   - README videos: FIXED (all 9 public, and all 7 showcase READMEs updated; see [[github-video-uploads]])
   - social preview: FIXED (7 panels, 42cf1e1); the user uploads it in GitHub Settings by hand
   - old app names (Avengers/Clawdvengers) in historical notes: the user said leave them
   - cast-size check: FIXED (now a precondition, c2f92fc)
4. **Performance:** DONE overnight 2026-10-17; pushed and released as 3.6.0 on 2026-10-17 (main 20ab1a0).
   - Done: build 9:19 -> 5:02; board view skips the hidden crew; BGRA layer images (pixel-identical); single-card redraws; opaque/ASCII pixel fast paths; refresh timer tolerance.
   - Benchmark (forced visible): list view about 4.7 -> 4.1% CPU, board view 8.1 -> 5.2%.
   - Dropped as not worth it: the frame cache (+4-11 MB for <0.5 points), the moving-layer repeat check (only 5% of frames repeat), UserDefaults/label caching (<1%), the Codex process filter (risk of missing sessions).
   - The TCC launch freeze (first GitRemote read on the main thread): FIXED in 3.6.0 (fc439f1), every read is now in the background.
   - Measuring tip: the user's screen saver hides the window at night, so use a forced-visible bench build. Builds that measure or launch must run from a path containing /build/, or they take over the hooks.

**Requested by the user on 2026-10-17: all three DONE and released in 3.6.0:**
1. **Window location-name bar:** cover the text plus a fade-out instead of the full width, and make it a little less transparent.
2. **Fights out of step:** when there are 4 or more characters (2 or more pairs), each pair's attack rhythm gets its own random phase, so the pairs don't all hit at once. The two fighters within a pair stay in step with each other.
3. **Settings like MacPacker's:**
   - a toolbar of icon tabs (General / … / About); sort the rows into sensible tabs
   - right-aligned labels beside their controls, with separators
   - an About tab with the version, links and "Check for Updates" (e.g. the GitHub releases API compared with the bundle version)

**Step 4 rules from the user:**
- Anything visible keeps at least 15 fps.
- Weigh any memory cost against gains under 1%.
- List every change that could alter the visuals, so the user can check them.
- Work on `audit` and don't push until the user has seen the results.

**Also in 3.6.0 (2026-10-17):** every supported AI listed in Settings → AIs (greyed out when not installed); About laid out like MacPacker's with "Thanks to" (`OverlayController.collaborators`, universes by `Universe.title`); Settings one level above a pinned window; character lines on a cream rounded backing; the outline check (49 characters + Necro-maintainer + the engine giving back hop/hover lift, see [[outline-frame-rule]]); the clawdify guide's Look and style section; the seven-universe promo (promo-seven merged) with a 95 MB cap on the 1080p render.
