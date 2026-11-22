# Brighton Insta Posts — RUNBOOK (read fully every run)

Owner: Kishan Patel, Brighton Solution (brightonsolution.com, Instagram @brighton.solution).
Goal: an endless stream of top-quality Instagram feed posts (singles + carousels) that win clients for websites,
mobile apps, custom software, business/management software, personal software, online stores, booking systems,
AI chatbots and automation. No upper limit. Every post better than the last.

## 0. Hard rules (never break)
- NEVER publish, queue or post anything to Instagram, Facebook or Threads. Kishan posts himself.
- Meta Community Guidelines first, always (an account was suspended once). No invented stats, results, prices,
  reviews, testimonials, clients or guarantees. No engagement bait ("like / share / tag / comment WORD to get").
  A genuine question ("Which one happens at your shop? Tell us in the comments.") is fine.
  No real brands, logos or logo-like shapes, no real people, no minors, no religion or festival names, no politics,
  no alcohol, gambling, crypto/returns, no health or medical claims, no immigration topics.
- Sample data only, visibly labelled "sample"; generic sample names ("Your Shop", "Sample Bakery").
- Posts in very simple everyday English. Grammar and spelling perfect (re-read every word on every slide).
- Never repeat a category, layout, palette or caption from the recent log (state.json).

## 1. Strategy (research, Nov 2026)
- Instagram's top ranking signals are watch time, likes per reach and SENDS per reach (DM shares). Saves are also
  weighted far above likes. Original content gets much more reach than reposts. => Design every post to be SAVED
  (useful checklist / guide / comparison) and SENT ("send this to a shop owner you know" value), not liked.
- Carousels earn the most saves and deep engagement; educational "how / what / which / mistakes / checklist" posts
  win in B2B. Captions are searchable: keyword-rich first line beats hashtag stuffing.
- So the mix is: ~35% carousels (5-7 slides), 65% singles. Every post teaches or shows one concrete useful thing for
  ONE business type, then says "we can build this for you, feel free to DM".
- Market mix (tracked in state.json): 70% India, 30% USA / Canada / global. Out of every 10 posts: 7 India, 3 abroad.
  India: go deep into micro-niches (targets.txt) and their real day-to-day problems in 2026 (UPI collections,
  udhaar/credit, stock, staff attendance, bookings, repeat customers, catalogue sharing, marketplace dependence).
  USA/Canada: home services, local shops, salons, food, professional offices; US wording (quote, booking, after hours,
  service area, ZIP/postal code); never quote prices.

## 2. Hooks and formats (rotate, never the same twice in a row)
Formats: before vs after split · spot-the-problem · one-day timeline · notebook vs software table · checklist "what
you need / what you get" · "X things an app can do" carousel · "which one do you need" guide · questions before you
build · myth vs fact · mistakes list carousel · sample app screen walkthrough · process (talk-plan-build-launch) ·
comic strip with characters · "signs you need" list · cost of doing it by hand (no numbers invented) · personal app
idea · redesign old vs new · map/route board · calendar/booking view · document mock (quote, invoice, report).
Hook first slide: name the person + their exact pain in under 10 words ("Cake orders on paper slips?").
Last slide / footer: clear soft CTA ("Want this for your shop? DM us").

## 3. Design system (variety is mandatory)
- Canvas 1080x1350 CSS px rendered at 2x → 2160x2700 (4:5). Margins >= 64 px sides; nothing within 30 px of edges.
- Every post: its own palette (never reuse a palette from the last 20), its own font pairing from installed fonts
  (Poppins, Inter, DM Sans, Montserrat, Fira Sans, Source Sans 3, Open Sans, Roboto, TeX Gyre Adventor, Archivo
  Black, Anton, Lora, Gelasio, Cardo, Crimson Text, Bitter), its own layout. Minimalist, proper type.
- Headline 54-80 px, line-height >= 1.2, text-wrap: balance; body >= 18 px. Few words, big type.
- Mockups: phone mockups LIMITED (max ~1 in 3 posts). Use browsers, tablets, laptops, documents, boards, calendars,
  cards, tables, maps, objects, illustrations. Mockup content must FIT INSIDE the device with padding — if it does
  not fit, remove items or shrink, never let it overflow or clip.
- Characters (Open Peeps, MIT) only when they add meaning; prefer bust poses (Device, Paper, Coffee, PointingUp,
  Explaining, ArmsCrossed); no "Geek" pose (logo-like icon), no religious headwear.
- Real Brighton logo (tools/postkit/logo.svg via page()), dim brightonsolution.com watermark (page() adds both).
- Carousel slides: "n / total" in the top bar, "Swipe" CTA on all but the last slide.

## 4. Build (tools/postkit)
- Setup once per container: `cd tools/postkit && npm i` (react, react-dom, react-peeps). Python: playwright, Pillow.
  Chrome at /usr/bin/google-chrome.
- Write a batch file `batches/bNNN.py` (see examples/batch0_a.py, batch0_b.py for the style and helpers:
  page(), phone(), browser(), peep(), ic()). Keys: `pNNNN_slug` or `pNNNN_slug_s1..s7` for carousels.
- Render: `python3 batches/bNNN.py` → work/out/*.png and prints ISSUES.

## 5. QA gate (a post may only be saved to GitHub / Drive after ALL pass)
1. Automated: render() runs check_text.js + check_gfx.js. ISSUES must be "none" for that post. check_gfx flags any
   element escaping its card / mockup / box, or touching the canvas edge. Use class "free" ONLY for deliberate
   decoration (e.g. truck wheels) — never to silence a real overflow.
2. Visual: open a contact sheet of the batch AND a 1:1 crop of each post's headline and densest mockup. Look for:
   text touching or overlapping, graphics outside mockups, clipped buttons at the bottom of phones, empty dead
   areas, misaligned rows, tiny unreadable text, orphan words, colour clashes. Fix and re-render until clean.
3. Copy check: read every word: grammar, spelling, simple English, labels match the business, "sample" present.
4. Policy check (section 0) on image text, caption and alt text.
5. Self-score 1-10 on: stops the scroll, save-worthy, send-worthy, clarity in 2 seconds, design finish, originality
   vs log. Any score < 8 → improve and re-check. Write the scores into the post meta.

## 6. Save (only passed posts)
- Convert to JPG quality 94 (4:4:4) → `posts/NNNN_<FORMAT>_<MARKET>_<Category>/` with files `1.jpg` (single) or
  `1.jpg..7.jpg` (carousel) and `post.md` (format SINGLE or CAROUSEL n slides, market, category, caption, alt text per
  image, scores). Commit + push in groups of ~5 posts.
- Google Drive folder "Brighton Insta Posts" (id in state.json): for each post one text file
  `NNNN · FORMAT · Market · Category.txt` with: format line ("SINGLE post: upload 1 image" / "CAROUSEL: upload all N
  images in order"), GitHub links to every image (https://github.com/Kishan3864/Insta-Posts/blob/main/posts/...),
  caption, alt text per image. Several create_file calls per message. Refresh an index sheet
  ("Brighton Insta Posts index") about every 25 posts (create new from index.csv, trash the old, store id).

## 7. Captions
English. First line = keyword-rich (business type + what we build). Length varies at random (short / medium / long).
Then a fresh DM CTA. Then 1-5 lines of a single "." (random, never the same count as the previous post). Then 3-5
relevant hashtags for this market + category (never the same set twice; India tags for India, US/Canada tags for
abroad). Alt text for every image: describe layout, key text and mockups plainly.

## 8. Self-improvement (every run)
- Before building, read LEARNINGS.md and the last 20 entries of state.json log. After each batch, append 2-4 concrete
  lessons to LEARNINGS.md (what looked weak, what fixed it, new idea to try). Apply them next batch.
- Every batch must try at least one new layout idea or visual technique not used before.

## 9. Run loop
- Lock: state.json lock_until_utc. Future → another run is active, exit quietly. Past/null → take it, set +50 min,
  extend as you deliver. On stop: lock null, last_run set.
- Loop: pick next targets (respect 7:3 mix) → write batch of 5 posts → render → QA gate → save → Drive → update
  state.json (posts_done, used_categories, palettes, fonts, formats, hashtags, log) → commit + push → next batch.
  Keep going as long as the run allows. Never idle.
- Notify Kishan (PushNotification, short Hinglish) at every 100 posts, or if push / Drive fails. Otherwise silent.
