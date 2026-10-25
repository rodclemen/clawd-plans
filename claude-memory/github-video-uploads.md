---
name: github-video-uploads
description: README videos (github.com/user-attachments) only go public once the issue/comment is submitted; 720p mode only shrinks the 1080p already rendered
metadata:
  node_type: memory
  type: reference
  originSessionId: be19b5c9-e9f0-4576-b0b5-ea68d1892e1a
  modified: 2026-10-25T08:15:30.798Z
---

README videos are `https://github.com/user-attachments/assets/<uuid>` links, made by dragging an mp4 into an issue or comment box on github.com. There's no API for it.

- **What makes an upload public:** the issue or comment it was dropped into must be **submitted**, and the repo must be public. A link in a pushed README doesn't do it, and neither does an unsubmitted draft. Uploads made while a repo was private stay 404 for signed-out visitors.
- **The working routine (2026-10-17):**
  1. Drag the files into a new clawd-clash issue.
  2. Submit the issue, then close it (issue #4 holds the README videos).
  3. Paste the links into the README.
  4. Check each link signed out with `curl -s -o /dev/null -w '%{http_code}'`: 302 means public, 404 means private.
- **For a new universe's video:** drag it into a new comment on closed issue #4 and post it. Posting is what makes it public, and comments on a closed issue are posted too. Confirmed with the Stranger Clawds trailer on 2026-10-23 (signed-out check gave 302).
- **Links work in any repo's README:** the same link can serve both clawd-clash and a universe's showcase repo.
- **Video size:** uploads must be under 10 MB.
  - `REEL=<reel> build/renderpromo 720p promo` writes `promo/720p/<Name>.mp4`. Run it after `REEL=<reel> build/renderpromo video promo`.
  - `720p` only shrinks the 1080p mp4 already in `promo/`; it renders nothing. After a code change, or a `git checkout` of the tracked promo mp4, it silently gives you the old cut. On 2026-10-25 two "fixed" 720p cuts sent to the owner were really the old promo.
  - The `avconvert` presets come out too large.
- **Before uploading, check the render date:** a video rendered before a promo change carries the old text. On 2026-10-17, five trailers predated the BRING YOUR OWN AI line-up (efe4f8e) and had to be re-rendered.

See [[audit-plan-2026-10]].
