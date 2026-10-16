---
name: release-setup
description: "Clawd Clash release prerequisites on this Mac: notary profile, Developer ID cert, team ID, public repos, brew trust step"
metadata:
  node_type: memory
  type: project
  originSessionId: d926bf6a-6c29-4d4f-969c-daebd2276adf
  modified: 2026-10-14T10:03:54.448Z
---

Releasing Clawd Clash (`./release.sh <version>`) works on this Mac as of 2026-10-14 (3.0.0 published, notarized):
- notarytool keychain profile `clawd-clash` (Apple ID rodclemen@gmail.com, Team ID `2S5TWMXL9G`; the `H77YK3C36K` in the Apple Development cert name is NOT the team ID).
- "Developer ID Application: Rod Clemen (2S5TWMXL9G)" is in the keychain.
- The optimized universal build can hit Swift "unable to type-check in reasonable time" on dense sin/cos drawing expressions; find them with `-Xfrontend -warn-long-expression-type-checking=300` and split them.
- All repos are public (clawd-clash, star-clawds, marvelous-clawds, detective-clawds, homebrew-tap). The tap has `cask_renames.json` mapping the old cask names (clawd-wars etc.) to the universe names.
- Newer Homebrew requires `brew trust rodclemen/tap` before installing; install docs include it.

**Why:** these took a session to sort out; the release was blocked until the cert existed and the repo was public.

**How to apply:** before a release, check `security find-identity -v -p codesigning` and `xcrun notarytool history --keychain-profile clawd-clash`. Related: [[changelog-policy]].
