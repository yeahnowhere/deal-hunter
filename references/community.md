# Deal Hunter Community — Community Verification (Reddit-first)

Load this file for **every shortlisted product** before a verdict. Platform reviews are curated and gamed — communities are not. This is how you find out what a product is *really* like after weeks/months of real use, before spending money.

> [!abstract] The core rule
> **Store reviews tell you the launch story. Communities tell you the ownership story.** If a product has glowing ratings but a wall of "it broke after 3 months" posts, it is not a deal at any price. Verify in communities *before* the verdict, not after.

## Where to look (in priority order)

### 1. Reddit (primary)
Search the subreddit that matches the category, then filter for **long-term ownership** posts and old threads (sort by new, check 6+ month-old posts).

| Category | Subreddits |
|----------|------------|
| General purchases | r/BuyItForLife, r/Frugal_Ind |
| Beauty & skincare | r/IndianBeautyDeals, r/IndianSkincareAddicts (ingredient-science culture) |
| PCs & parts | r/IndianGaming, r/BuildAPCIndia, r/IndiaTech (~780K members), r/IndianDeals |
| Used PC parts | r/IndianGaming (bazaar/market threads), TechEnclave buy-sell, Gamer's Loot, ZedUpgrade |
| Phones & gadgets | r/GadgetsIndia, r/IndiaTech, r/Android, r/IndianDeals |
| Audio | r/headphones, r/audiophile, r/IndianGaming (peripheral threads) |
| Appliances / home | Reddit coverage is thin — use r/BuyItForLife (global), ValuePickr consumer-durables threads, Local Circles |
| Automotive | Team-BHP ownership & grievance boards (India's most rigorous vehicle forum) |
| Fashion / thrift | r/IndiaThriftStore; otherwise thin — lean on marketplace Q&A + MouthShut |
| Watches / accessories | r/watches (global); brand-specific owner threads via Google `site:` search |
| Cameras | r/AskPhotography, r/india (tech megathreads) |

Search patterns that find the truth:
- Google `site:reddit.com "<product>"` — far more reliable than Reddit's native search; start here
- `"<product>" review` — recency + depth filter
- `"<product>" after <N> months` / `"<product>" still working` — durability signal
- `"<product>" vs "<competitor>"` — head-to-head from real owners
- `"<product>" refund` / `"<product>" broken` / `"<product>" doa` — failure signals
- Hinglish variants catch what English misses: `"<product>" kaisa hai`, `kharab ho gaya`, `paisa vasool`
- On the subreddit: `sort=new` on the search, then read the 6–18-month-old threads too

### 2. X (Twitter) & YouTube
- Search `"<product>" long-term` / `"<product>" review honest` — reviewers who buy their own units
- YouTube: look for **6-month/long-term review** videos, not just launch-day first impressions; check comment sections for owners reporting failures
- Red flag: all reviewers got the unit free from the same PR drop = launch-hype echo chamber

### 2b. Marketplace Q&A sections (when external coverage is thin)
Amazon/Flipkart question sections are full of real-owner answers ("battery backup?", "after-sales service?"). Sort by recent; read buyer answers honestly, seller answers skeptically.

### 3. Indian tech forums & communities
- **TechEnclave** — the serious Indian hardware forum; search model names, owner threads, market-price threads
- **XDA Forums** — phones, custom ROM, hardware quirks
- **erodov** — older Indian gadget forum, good for legacy product durability reports
- **ValuePickr forums** — investor-run corporate forensics; members track when brands cut material/durability corners to protect margins (advanced signal — read for trend, not product reviews)
- **Indicarr / WhatsApp / Telegram deal groups** — deal alerts, not quality verdicts (use for price, not quality)

### 3b. Used & second-hand marketplaces
Used purchases skip platform protections — so community verification is *more* important, not less. Where the Indian used market actually lives:
- **TechEnclave buy-sell** — the serious hardware forum; check user join-date, heat score, and deal threads before wiring money
- **r/IndianGaming bazaar/market threads** — search `market` / `bazaar`; private sellers, cash-on-delivery preferred
- **Gamer's Loot** — established gaming hardware reseller; still verify the specific listing
- **ZedUpgrade** — Apple/Mac refurb specialist; confirm the grading and warranty terms
- **Flipkart/Amazon "renewed" & official refurb** — platform-backed (7-day return), safer than private sales, but the warranty is usually the refurbisher's, not the brand's

Private-sale rules: advance payment to an unknown seller = scam signal; **no-return is the norm** for private sales, so price in the risk and test before final payment. Full on-spot testing + warranty-transfer reality in `references/used.md`.

### 4. Complaint portals (last resort, high signal)
- **consumerhelpline.gov.in / National Consumer Helpline (NCH)** — registered complaints per brand/model
- **MouthShut.com** — India's oldest long-form review portal; durability + after-sales service records across goods and telecom
- **ConsumerComplaints.in** — public ledger of e-commerce fraud/service failures; corporate escalation teams monitor it for PR damage
- **Consumer Voice / Local Circles** — category-level complaint reports
- **X @ brand handle** — "my X broke after Y months, no support" threads cluster here

## What you're looking for

- **Long-term ownership experiences** — someone who's used it for weeks/months, not a first-day reviewer
- **Recurring failure modes** — the *same* problem in multiple threads ("battery swelled", "card reader died", "band snapped")
- **Service-center reality** — how the brand's warranty actually behaves (does support respond? do they replace?)
- **Honest verdicts on hype** — "bought it because of reviews, would not rebuy"

## Paid-plant & astroturf detection

- **All-positive, launch-day accounts** — accounts created near launch, only posting hype
- **Coordinated phrasing** — several "reviews" using the same unusual phrases
- **Contradiction between store reviews and community** — 4.5★ on Amazon but "avoid this brand" consensus on Reddit = store reviews are gamed
- **Incentivized reviews** — refund-for-review, extra-warranty-for-review programs (Amazon "invite" review batches, "supplemented review" badge groups)
- **Giveaway/PR-drop echo chambers** — everyone reviewing the *same* unit from the same PR batch

When detected: **zero-out the store-review weight** for that listing, mark the review-integrity gate ⚠️, and note the pattern in Evidence. Never average manipulated reviews into the verdict.

## Weighting the evidence

| Signal | Trust |
|--------|-------|
| ≥2–3 independent long-term ownership posts (≤24 months old) | **High** — decide on this |
| One detailed teardown/service story | Medium-High |
| Single "broke after a month" post | Medium — check for more |
| Launch-day hype / all-positive burst | Low — ignore for verdicts |
| Store reviews alone | Low — verify elsewhere |

**Sample-size floor:** a single independent thread caps at Medium-High — never decide High on one post.
**Age cap:** ownership posts older than ~24 months describe an older production batch (QC changes over years) — treat old praise as weak-positive and note the batch-era caveat.

## Zero-coverage protocol (when communities are silent)

Budget brands and niche categories often have NO Reddit/forum presence. Silence is a finding, not a failure — never quietly substitute platforms or skip the check. Ladder:
1. Google `site:reddit.com "<product>"` + the category subreddits above
2. Indian forums (TechEnclave, MouthShut, ConsumerComplaints.in)
3. Marketplace Q&A + critical-review mining (sort recent, read 1–3★)
4. Still nothing → the verdict carries **`community: no coverage`** in the gates summary and the Community gate reads ⚠️ (unverified by community). Say it plainly: "no independent owner reports found — store reviews only."

## Used & second-hand specifics (what to dig for)

When the candidate is used/refurb, add these community signals on top of the normal ones:
- **Mining-card history** — "used for gaming only", GPU sag/card aesthetics, and owner threads on the specific model's used-market red flags; mining cards run hot 24/7 and fail early
- **Warranty-transfer reality** — will the brand honor a transferred warranty, or is it non-transferable/voided? Read owner reports, not the marketing line
- **Battery / degradation** — for phones/laptops: reported battery health, replaceability, and price of the replacement battery
- **IMEI / serial checks** — for phones: IMEI blacklist (stolen/blocked), check on brand portals; never buy prepaid-to-unknown for a device
- **Refurb-grading honesty** — "renewed" grading (e.g. Mint/Good/Fair) in Indian listings often means cosmetic damage; check the refund window and whether the warranty is the refurbisher's
- **Seller patterns** — brand-new accounts, one listing, "urgent, no questions" tone = red flags; established marketplaces/heat are the only soft safety net

## Recording it

- Verdict vocabulary (one word, one meaning): **clean** (verified OK) / **mixed** (conflicting signals — say which) / **red-flag** (recurring failures) / **no coverage** (silent communities)
- Feed the finding into the gates-summary line: `Community: ✅ / ⚠️ / ❌ / n/a`
- For the tracker row, cite **which community and what it said** (e.g. `TechEnclave: 2 owner threads, 1 cracked after 8 mo`)
- The user's own Reddit research/drafts live under the `type/reddit-draft` tag — reuse those threads as evidence when relevant
- Link the strongest thread as the clipping if saving to the vault

## Related

- `prompt.md` — JOB 2.6 (community verification) is part of every analysis
- `india.md` — platform map + scam safety for the Indian market
- `tracker.md` — where the community verdict gets recorded
