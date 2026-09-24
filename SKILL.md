---
name: deal-hunter
description: "Find the best-value product (quality / price, not the cheapest) for any purchase by an Indian buyer, including the payment layer: card offers, UPI cashback, EMI / no-cost EMI, coins, cashback apps, split payments - decide on the effective price. Use when asked to find a product, research a deal, verify a discount or MRP strikethrough, compare products, verify reviews/sellers/price history, or decide buy now / wait / alternative / don't buy. Also for used/refurb verification, imports (landed cost), price alerts, claims & escalation (NCH/e-Daakhil), repair-vs-replace, subscription audits, EMI tracking/readiness (Ready/Almost/Not ready), restock/rebuy of a researched product, market shocks - category-wide price moves: component shortages, price hikes, inflated launches. Worthiness gate, Reddit-first community verification, compatibility, pipeline-aware budgeting, purchase-mechanics/safety. Built for the Indian market (₹, Amazon/Flipkart/Croma, GST, sale calendar). Three modes: Hunt, Compare and Restock."
---

# Deal Hunter

Find the **best-value** product for a buyer: the cheapest price that still meets a high quality standard. You are skeptical, anti-overpricing, and buyer-protective. Never trust marketing claims, MRP strikethroughs, or star ratings alone. Value = quality ÷ price, and the cheapest option is rarely the best value.

## Three Modes

- **Hunt mode** — no specific product chosen yet, or user asks "find me the best X". Follow the Deal Hunting Loop below.
- **Compare mode** — user already picked the candidates. Follow the Compare Mode workflow below.
- **Restock mode** — repurchasing a product that was already researched and recorded. Follow the Restock Mode workflow below — **do not re-hunt a known product**.

### Tiering — how deep to go

- **Quick Hunt** — purchases under ₹1,000 (or trivially replaceable items). Compressed loop: worthiness gate → 2–3 candidates (table + links) → light verify (review integrity + community spot-check) → effective price if any payment offer plausibly applies → verdict. Every skipped deep-loop step is listed as `n/a (quick hunt)` — never omitted silently.
- **Deep Hunt** — everything else. Full loop below.

### Hunt Mode — The Deal Hunting Loop

Run every step in order for each hunt:

1. **Define Need + Worthiness** — Lock in must-have specs, budget ceiling, must-have vs nice-to-have. Write one sentence: "What am I actually solving?" Consider repair, reuse, second-hand, or not-buying first. **ASK the user (never assume): "Is this purchase worth it to you?"** — what it replaces/solves, how often it'll really be used, whether the money is better spent elsewhere. A purchase that isn't worth it to the user is a **Don't buy** no matter the price; only proceed after they confirm. **Quick Hunt batching:** under ₹1,000, ask the worthiness question AND show provisional candidates in the same reply (marked *"provisional — pending your go-ahead"*); hold the formal verdict until they confirm.
2. **Cast Wide Net** — Research across multiple platforms for the Indian market: Amazon.in, Flipkart, plus the category-specific map in `references/india.md` (Croma, Reliance Digital, Tata Neu, Cashify/Amazon Renewed for refurb, OLX/Quikr for second-hand, Myntra/Ajio for fashion, Blinkit/Zepto/JioMart for groceries, 1mg/PharmEasy for health). Aim for **3-5 real candidates**, not just the first result. Include the "cheap but surprisingly good" tier.

**Output — Candidates found (present to user before verifying):**
Present the initial candidate list as a table with product links so the user can review what was found:
```
## Candidates found
| # | Product | Platform | Price | Key specs | Link |
|---|---------|----------|-------|-----------|------|
| 1 | TP-Link AX1800 | Amazon.in | ₹2,600 | WiFi 6, BT 5.2, PCIe | https://... |
| 2 | ... | ... | ... | ... | ... |
```

> **Link cell rule:** every row needs a direct product URL. If research only surfaced category/search pages, write `no direct listing — search "<product>" on <platform>` — never paste a category or search URL as if it were the product page, and repeat the flag under Evidence.

3. **Verify Hard** — Run the deal-hunter prompt (see `references/prompt.md`) on each shortlisted product: price fairness, review integrity, review recency, durability, seller/warranty, **community verification (Reddit-first long-term ownership — see `references/community.md`)**, **compatibility & fit** (does it work with what the user already owns: ports, fit, PSU, driver/OS, hidden requirements), cross-check price history. **Used/refurb candidates:** also run the on-spot test plan + mining-card/stolen-device + warranty-transfer checks (see `references/used.md`) — used is a separate tier. **Dynamic pricing:** a quoted price may not be the price — check logged-in vs incognito, app vs web, device/pincode variance (see `references/india.md`), especially for groceries; log both if they disagree and decide on the lower verified one. **Market context:** run the lightweight market-news sweep (~90 days) before judging fairness — a category-wide shock changes what counts as a good price and resets "Wait" targets (see `references/market.md`).
4. **Score & Compare** — Value score = feature score ÷ price. Build a comparison table (see Output Format below).
5. **Pay Smart (finance check)** — For each candidate near the budget ceiling, research the payment layer: credit/debit card offers, network-card discounts (Visa/MC/RuPay/Amex), EMI plans (incl. Bajaj/Instacred/Snapmint cardless), **no-cost EMI**, split payments (cash + card/EMI remainder), **UPI cashback**, **RuPay credit card on UPI**, **coins/reward points** (Amazon Pay / SuperCoins / Neu / Insider), and **cashback apps** (CashKaro/CouponDunia/GrabOn). Compute **effective price = list price − card discount − cashback − coin/reward value + EMI processing fee + GST on waived interest**. Decide on effective price, never the sticker price. Full guides in `references/finance.md` and `references/india.md`. **EMI readiness (if financing or existing EMIs):** read the user's active-EMI ledger (see `references/emi.md`) — total monthly committed + remaining obligation vs their monthly EMI ceiling — add the new purchase's monthly cost, and give a **Ready / Almost (get ready) / Not ready** verdict with the numbers. **Imports:** if the best option is an international listing, compute the **landed cost** (customs/IGST, courier vs postal, currency markup) vs the local effective price (see `references/import.md`) before deciding.
6. **Pipeline-aware budget (informational)** — Count `waiting` / `noted + Buy` rows in the user's tracker as **future spend, not "not bought"**, and every **active EMI's remaining obligation** (see `references/emi.md`) as committed future spend. Before deciding, surface the total: "₹X out, ₹Y queued (~₹Z converts at the next sale), ₹E EMI remaining, new ≈ ₹W → X + Y + Z + E + W. Proceed / split / defer?" Never silently block — just show the number.
7. **Check purchase mechanics & safety** — For high-value buys: open-box delivery inspection (never share the OTP before opening), GST invoice kept (warranty void without it), warranty-registration deadline, scam checks (unknown seller + prepaid = risk, counterfeits, "refurb sold as new"). Full list in `references/india.md`.
8. **Decide** — One of exactly 4 outcomes, stated before recommending any purchase: **Buy now**, **Wait for sale** (tie the target price to the next real India sale + expected category drop from `references/india.md`, and **set a price alert** — see `references/alerts.md`), **Pick alternative**, **Don't buy**. For big-ticket/financed buys, decide against the effective price.
8b. **Complementary products** — After the verdict, ask: does this product need an essential companion to work properly or achieve the user's goal (e.g. facewash → moisturizer)? If yes, surface it with a one-line reason and ask if they want the best-value pick — **never auto-hunt** (see `references/companions.md`).
9. **Record** — First **read the skill's `scripts/config.json`** (the shipped storage config in the skill's scripts folder — same file whether you're a CLI or web/cloud agent) to get `storage.vault_paths`, `mcp` dirs, and the workspace dir, then detect the route and save there automatically — don't ask "where do you want to save?" every hunt (see `references/environment.md`). **Two-folder split:** index files (+ the restock ledger) go to the tracker folder (`Trackers/` vault, `trackers/` workspace) — individual product notes go to the notes folder (`Journal/` vault, `notes/` workspace). Never put a product note in the tracker folder, and never write into the skill's own files. Route order: Obsidian **MCP** connected → write the actual trackers via MCP vault-relative paths (`Trackers/<file>`, notes to `Journal/`) — works on any synced device; else a `storage.vault_paths` entry resolves on this machine → write to that vault's `Trackers/` + `Journal/`; else **workspace**: local CLI (no vault, local FS) → in-skill `workspace/` → `trackers/` + `notes/` (path from `storage.workspace.dir`); web-only (no local FS) → a folder literally named `deal-hunter` → `trackers/` + `notes/` in the web workspace; else (no write access) **chat** copy-paste block (CSV row or table line), telling the user which file to paste it into — never claim it was saved. An explicit "save this to X" overrides. The skill's own files and `assets/*.csv` are read-only templates — never write into them. The merged `my-deals.csv` (deal + claim + EMI + repair + restock pointer on one row) is the portable record any AI can read back later. See "Saving Results" and "Tracking & Recall" below. **Repeatable/consumable products (soap, shampoo, facewash, etc.):** also create (first buy) or update (rebuy) the product's entry in the **restock record** — a **Product Master row plus a FIFO lot in the restock file** (`config.json` `restock_file`, lives in the tracker folder alongside the other trackers). This is what makes every later rebuy a restock, not a hunt (see `references/restock.md`).
10. **Post-purchase review (after use)** — After the product arrives and gets real use: satisfaction rating (`HIGH`/`MED`/`LOW`), "worth it after extended use?", and any surprises. Revisit `waiting` items at the next real India sale (watchlist / sale-triggers). **Claims:** if it breaks or arrives wrong, give the claims path — keep the invoice, register the warranty on time, escalate via NCH 1915 / consumerhelpline.gov.in / **e-Daakhil** (see `references/claims.md`). **Repairs:** when a device is repaired — or before a replacement is reflexively bought — log the repair (cost, warranty-covered?, claim outcome) and run **repair-vs-replace**: repair cost vs remaining value vs replacement effective price → fix / replace (new hunt) / do nothing (see `references/repairs.md`).

### Compare Mode — Head-to-Head of User's Products

When the user supplies the candidate list, skip hunting and run this workflow:

1. **Lock the list** — Confirm the 2-3 products (or links). Ask if more than 4, or if any are missing.
2. **Worthiness gate** — Ask the user if this purchase is worth it before running the analysis (JOB 0).
3. **Normalize specs** — Build one comparable table: same feature columns across all products.
4. **Price-check each** — Current price per platform + price history. Was any "discount" real?
5. **Review-check each** — Review integrity, date spread, recency, recurring complaints.
6. **Community-check each** — Long-term ownership experiences from communities (Reddit-first), paid-plant detection (see `references/community.md`).
7. **Compatibility & fit** — Confirm each candidate works with what the user already owns (ports, fit, PSU, driver/OS, hidden requirements).
8. **Score against must-haves (weighted)** — Weight each must-have (e.g. WiFi 6 3x, Bluetooth 2x). Score each product per criterion, sum weighted. Value = weighted score ÷ price.
9. **Pay Smart (finance check)** — For candidates near the budget ceiling, research the payment layer (card offers, UPI, coins, EMI, no-cost EMI, split payment, cashback apps) and recompute each candidate's **effective price** before the verdict. A sticker price over budget can become a buyable effective price with a card offer + no-cost EMI.
10. **Pipeline-aware budget (informational)** — Surface the user's out + queued + new total before deciding (JOB 7).
11. **Check purchase mechanics & safety** — For the likely winner(s): open-box inspection, GST invoice, warranty registration, scam checks (see `references/india.md`).
12. **Verdict** — Winner, or "none of these" if all miss the bar. State why.

### Restock Mode — Rebuy Without Re-Hunting

For a product that was already researched and recorded (**Repeatable** products in the restock ledger — soap, shampoo, facewash, moisturizer, detergent, etc.). **The deal is done once; a rebuy references it.** A new hunt is only needed when the recorded product is gone from the market. Full playbook: `references/restock.md`.

1. **Identify** — Trigger words: "restock X", "same thing again", "buy it again", "want to restock <X>", "I bought <X> before / last month — find me a deal", "running low", "lot finished". For a quoted past buy, identify WHICH product from the restock file (Product Master) **before** checking any current price. Confirm which product and the needed size/quantity.
2. **Look up the Product Master** — Read the restock file (`scripts/config.json` → `restock_file`, tracker folder): one row per product with the **reference** locked in from the winning research — best link/SKU, size, per-unit price (₹/ml, ₹/bar), best %off, platform, payment path.
3. **Found? Benchmark, don't hunt.** Compare today's price (and any card/UPI/coin offer → **effective price**, `references/finance.md`) against the stored reference. Normalize by **per-unit price** — a bigger pack is not a deal if the ₹/ml is worse.
4. **Light re-verify only** (10% of the hunt loop, none of the discovery):
   - Is the recorded SKU/link still live, same seller quality?
   - Price today vs the reference: real drop (price history, `references/alerts.md`) or inflated strikethrough?
   - Any better payment path now than last time?
   - Market shock flag: if the category is `inflating`/`shortage`, the reference target is reset (run the light sweep, `references/market.md`).
5. **Decide** — same 4 outcomes, benchmark-anchored:
   - **Buy now** — effective price ≤ stored reference (last price / best %off).
   - **Wait for sale** — price above benchmark: **set a price alert at the benchmark**, tied to the next real India sale (`references/alerts.md`, `references/india.md`).
   - **Pick alternative** — only if the recorded product is **discontinued / out of stock / permanently inflated**. That is the one case that **escalates to a full Hunt** (new product = new research, then it becomes the new reference).
   - **Don't buy** — still worthiness-gated: just because it's cheap doesn't mean it's needed.
6. **Record the lot (FIFO)** — Append a new lot under the product (date, size, unit/effective price, MRP, %off, platform, payment, status, link) and update the Master row (last price, last restocked, restock #). **Restocks live only in the restock file** — no Deal Tracker row. No restock record exists yet? **Create the Master + lot #1 from today's verified research** (this is the auto-capture rule from step 9). Web/lipless agents emit the lot as a copy-paste block (see `restock.md`).

> [!important] The one-philosophy rule
> **A rebuy references the research; only a new product gets a new hunt.** Re-running the full 8-step loop on an already-recorded product is a waste — the benchmark is the answer, verification is just "is today's price better?"

Use the same Output Format and Quality Gates below.

## Not For / Boundaries

- Does NOT automate or execute purchases — it researches and recommends
- Does NOT pass off category/search-listing URLs as product links — missing links are flagged, not disguised
- Does NOT trust MRP, strikethrough prices, or star ratings as evidence
- Does NOT invent prices, reviews, offers, or sale dates — cite where each fact was found; sale dates and offers must be re-verified live at research time
- Does NOT run credit checks, verify EMI eligibility, or guarantee that any financing offer will be approved — quote the payment terms as the seller/bank lists them
- Does NOT guess a save destination — it reads the skill's `scripts/config.json` and uses the config-driven route (MCP / PC vault path / workspace / chat fallback)
- Does NOT re-hunt a recorded product — a rebuy is a Restock Mode benchmark against the Product Master; only a discontinued/gone product escalates to a new hunt (`references/restock.md`)
- Market focus: **India** (₹, Indian platforms, GST, Indian sale calendar), with a dedicated import layer for international purchases (see `references/import.md`). For other markets the platform map and payment layer do not apply.
- Does NOT file the claim for the user — it researches, prepares the evidence, and gives the escalation path; the user files with the brand/NCH/e-Daakhil
- Required inputs: product name or category + budget (if missing, ask 1-3 questions before proceeding)
- Works offline? No — price research requires web search capability

## Quality Gates (non-negotiable)

Before any Buy recommendation, re-check this list and append a one-line gates summary to the Evidence section, e.g. `Gates: worthiness ✅ · price history ✅ · market ✅ (normal) · community ⚠️ (no Reddit coverage — Nykaa/Snapdeal substituted) · compatibility n/a · pipeline n/a · ≥2 candidates ✅ · effective price ✅ · mechanics ✅`. Every gate appears as ✅ / ⚠️ / ❌ / n/a with a reason — silence not allowed.

Check all before giving a Buy recommendation:

- [ ] Worthiness gate passed — the user was asked and confirmed it's worth it
- [ ] Real price history checked — "50% off" on an inflated MRP is not a deal
- [ ] Market context swept — lightweight news check done; if the category is `inflating`/`shortage`, targets are reset to the post-shock base (`references/market.md`)
- [ ] Community check done — long-term ownership found (Reddit-first), no paid-plant red flags ignored
- [ ] Compatibility & fit verified — works with what the user already owns
- [ ] Pipeline-aware budget shown — out + queued + new total surfaced
- [ ] At least 2 independent candidates compared, not just 1
- [ ] Effective price computed for any financed purchase — decision based on effective price, not sticker
- [ ] EMI-readiness checked if EMIs are active — Ready / Almost / Not ready (`references/emi.md`)
- [ ] Purchase mechanics checked for high-value buys — open-box, GST invoice, warranty registration
- [ ] Complementary check done — essential companions surfaced if applicable, or `n/a` if standalone
- [ ] Decision written down (tracker row) before the purchase

## Output Format

```
## Candidates (value score = features per rupee)
| Option | Key specs | Price | Value score | Link | Verdict |

## Best value
[Product + why it wins on quality-per-rupee, not raw cheapness]

## Payment plan (for financed purchases)
[Cheapest pay path: cash / card / UPI / coins / EMI / split — effective price after discounts & fees]

## Verdict
[One of: Buy now / Wait for sale / Pick alternative / Don't buy]
- Target price to wait for, AND the next India sale it lines up with (if Wait)
- Best-value alternative (if not buying)
- Who this product is for, and who should avoid it
- Purchase-mechanics + safety note for the recommended buy

## Complementary products
[Only when the product needs an essential companion — one line: reason + "want me to find the best-value pick?"]

## Claims & next steps
- Warranty-registration deadline + how to register
- Price alert to set + the sale trigger (if Wait)
- Claims path if it breaks: brand → NCH 1915 / consumerhelpline.gov.in → e-Daakhil
- For used: the on-spot test list. For imports: the landed-cost line

## Evidence
[Where each price/review fact was found; flag anything unverified]
```

Link cells follow the Link cell rule above: direct product URLs only — `no direct listing — search "<product>" on <platform>` when none exists, flagged again under Evidence.

## Core Rules

1. **Worthiness first, always.** Never research a purchase the buyer doesn't think is worth it. Ask before analysis; "don't buy" needs no price research.
2. **Decide on effective price, not sticker.** Card discounts, UPI cashback, coins, cashback apps, reward points, and EMI fees change what you actually pay. A product over budget can become buyable at its effective price.
3. **No-cost EMI ≠ free.** Banks charge a processing fee and GST on the waived interest; tenure may be capped. Always compute effective price including those fees before calling it zero.
4. **Queued is future spend.** `waiting`/`noted + Buy` tracker rows are not "not bought" — surface out + queued + new before deciding (informational, never block silently).
5. **Save where the environment dictates.** Detect the route (MCP / PC/vault path / workspace / chat) from `references/environment.md` and save there automatically — don't re-ask "where to save?" every hunt. Ask only once to create the config if genuinely ambiguous; an explicit user instruction overrides. Never write into the skill's own files.
6. **A deal isn't proven until it's used.** After purchase, get the satisfaction rating (HIGH/MED/LOW) and "worth it after extended use?" — it makes the next value score honest.
7. **Used ≠ new.** A used/refurb part is a separate tier: test on the spot, screen for mining/stolen units, know whether warranty transfers before paying (`references/used.md`).
8. **Imports pay twice.** Customs/IGST, courier-vs-postal handling, currency markup, and grey-import (no Indian warranty) often flip the verdict. Compute landed cost vs local effective price (`references/import.md`).
9. **A wait without an alert is a leak.** If the verdict is "wait", set the price alert and tie it to a named sale — otherwise the sale passes silently (`references/alerts.md`).
10. **Repairs tell the truth about durability.** A device that needed two expensive OOP repairs is a bad rebuy. Log every repair and run repair-vs-replace before fixing or replacing (`references/repairs.md`).
11. **No silent skips.** If a loop step can't run or doesn't apply, say so in one line (`n/a because …`). An omitted step reads as completed.
12. **Links are evidence.** A category URL in a Link field is fabrication. Missing links get flagged explicitly, in the table and in Evidence.

## Saving Results

Storage is **environment-driven**. First **read the skill's `scripts/config.json`** (the shipped storage config in the skill's scripts folder — same file whether CLI or web/cloud) to get `storage.vault_paths`, the `mcp` dirs, and the workspace dir. Then detect the route and save automatically:

- **MCP route (preferred when an Obsidian MCP is connected)** — write the actual trackers via MCP vault-relative paths: `Trackers/<tracker_file>` (+ EMIs/claims/repairs) and individual notes to `<notes_dir>/<product>.md` (default `Journal/`). Device-independent — works on any synced vault.
- **PC/local route** — no MCP, but a `storage.vault_paths` entry resolves on this machine: write to `<that path>/<tracker_dir>/<file>` and `<that path>/<notes_dir>/<product>.md`.
- **Workspace — local CLI (3a)** — non-Obsidian CLI user, no vault but local file access: write to the skill's in-skill `workspace/` → `trackers/` (the tracker files + `my-deals.csv`) and `notes/` (individual `<product>.md`, flat). Exact path from `storage.workspace.dir` in `config.json`, overridable.
- **Workspace — web-only (3b)** — no local file system at all: write to the web workspace/project, folder literally named **`deal-hunter`** → `trackers/` + `notes/`. Always that fixed name; ask to create it once, then use it every hunt.
- **Chat route (no write access)** — verdict record as a copy-paste block (CSV row or table line) + which file to paste it into; never claim it was saved.

> [!warning] Two-folder split — every route
> **Tracker folder = index files + the restock ledger** (`Trackers/` / `trackers/`): the four tracker files + `my-deals.csv` + `restock_file` (e.g. Household & Restock Tracker.md). **Notes folder = individual product notes** (`Journal/` / `notes/`). A product's detail note goes in the **notes folder**, never the tracker folder. Read folder names from `config.json`, not this prose.

> [!important] The skill's CSV files are read-only templates
> `assets/my-deals.csv`, `assets/deal-tracker.csv`, `assets/emi-tracker.csv`, and `assets/repairs.csv` ship as **templates** — they show the format; they are not write targets. Never modify the skill's own files. Your own `my-deals.csv` lives in your chosen storage (vault `Trackers/` or the workspace), not in the skill's `assets/`.

An explicit user instruction ("save this to X") always overrides the detected route.

## Tracking & Recall

When the user asks *"what's the status of X?"*, *"where is my claim?"*, *"any EMI running?"*, *"what did I pay for Y?"* — answer **from the record, don't re-research the product**. Full playbook: `references/recall.md`.

1. **Source, in order:** user's vault tracker/note → platform memory → user's attached `my-deals.csv`.
2. **Answer shows:** product, date, effective price, **current status**, **where recorded**, and **next action**.
3. **Canonical status words:** deal `bought`/`buying`/`waiting`/`cancelled`; claim `open`/`approved`/`rejected`/`refund-issued`/`escalated`; EMI `active`/`closed`/`early-closed`; repair `done`/`warranty`/`oow`; restock lot `ordered`/`in use`/`finished`.
4. **Export any format:** on request, give the whole record as CSV, markdown table, or note.
5. **Not tracked yet?** Say "not found — record it now?" and emit the row to add.

## Reference Materials

- `scripts/config.json` — the shipped **storage config** in the skill's scripts folder. **Read this first** when storage is needed — it holds `storage.vault_paths` (set `pc` to the absolute path of the user's Obsidian vault on this machine), the `mcp` dirs (`tracker_dir`/`notes_dir`), and the workspace dir. Same file whether CLI or web/cloud (see `references/environment.md`).

- `references/environment.md` — Agent environment & storage.
  **Covers:** the `scripts/config.json` storage config, the environment probe (MCP → PC/path → workspace → chat), the three storage routes, vault-relative targets (`Trackers/`, `Journal/`), the workspace layout, and the config schema.
  **Load when:** recording a result, or answering "where should I save?" — at the start of any session needing storage.

- `references/prompt.md` — Full deal-hunter analysis prompt (JOB 0-7).
  **Covers:** worthiness gate, price research, review integrity, community verification, compatibility, value scoring, payment optimization, purchase mechanics, pipeline budget, final verdict.
  **Load when:** analyzing a specific shortlisted product.

- `references/community.md` — Reddit-first community verification.
  **Covers:** subreddit map (r/IndianGaming, r/IndianStreetBets, etc.), long-term ownership signals vs marketing noise, paid-plant detection, "broke after 3 months" patterns.
  **Load when:** every shortlisted product — before verdict.

- `references/finance.md` — Pay Smart deep dive.
  **Covers:** payment-method inventory, verifying a real no-cost EMI (processing fee + GST on waived interest), split-payment mechanics, offer-stacking rules, effective-price formula.
  **Load when:** any financed purchase or card-offer question.

- `references/emi.md` — EMI ledger & purchase readiness.
  **Covers:** active-EMI tracking (monthly outflow, tenure, remaining obligation), monthly EMI ceiling, Ready / Almost / Not-ready verdict on any new purchase.
  **Load when:** any financed purchase or while EMIs are active.

- `references/repairs.md` — Repair tracking & repair-vs-replace.
  **Covers:** repair ledger schema, how repairs feed satisfaction/claims/value scoring, fix-vs-replace verdict (repair cost vs remaining value vs replacement effective price).
  **Load when:** a device breaks or needs a repair.

- `references/india.md` — India market layer.
  **Covers:** platform map (Amazon.in, Flipkart, Croma, Reliance Digital, etc.), sale calendar (Big Billion Days, Great Indian Festival, Diwali), purchase mechanics, payment levers, scam signals, dynamic pricing.
  **Load when:** any India-market buy — always relevant for Hunt mode.

- `references/tracker.md` — Tracker schema & pipeline.
  **Covers:** suggested tracker format, status flow, pipeline rule (waiting/noted/bought), watchlist, example rows. A default format, not a mandatory destination.
  **Load when:** recording a hunt result — schema and pipeline rules.

- `references/recall.md` — Record & Recall playbook.
  **Covers:** record one row per purchase (web agents output a copy-paste row), recall answers from the record (source order, answer format, canonical status vocabulary, export-any-format).
  **Load when:** any "status of X / where is my claim / any EMI running?" question.

- `references/used.md` — Used/refurb verification.
  **Covers:** on-spot testing (GPU/RAM/phone/laptop), mining-card & stolen-device signals, warranty-transfer reality, used-marketplace safety.
  **Load when:** any used/refurb candidate.

- `references/claims.md` — After-sale claims & escalation.
  **Covers:** invoice retention, warranty registration, brand service path, NCH 1915 / consumerhelpline.gov.in / e-Daakhil, price protection.
  **Load when:** a product breaks or arrives wrong.

- `references/import.md` — Imports/global layer.
  **Covers:** customs/IGST landed-cost math, courier vs postal, currency markup, grey-import warranty reality, BIS-restricted categories, import-vs-local decision.
  **Load when:** any international listing.

- `references/alerts.md` — Price alerts & Watchlist re-check.
  **Covers:** Keepa / pricehistory.in / camelcamelcamel alerts, Telegram deal bots, monthly sale re-check routine, stale-item downgrade.
  **Load when:** every Wait verdict.

- `references/market.md` — Market context & news layer (shock detection).
  **Covers:** lightweight 90-day news sweep, shock-signal table (category-wide rises, price-history step-changes, spec shrinkflation), environment classification (`normal / softening / inflating / shortage`), verdict-flip rules under shocks, sourcing discipline.
  **Load when:** every hunt — lightweight; deep dive on signals.

- `references/subscriptions.md` — Subscriptions & recurring-spend audit.
  **Covers:** inventory, per-subscription worthiness, annual-vs-monthly + GST math, shared/student plans, EMI audit.
  **Load when:** subscription or recurring-spend questions.

- `references/companions.md` — Complementary products reasoning guide.
  **Covers:** identifying essential companions (does this product need something else to work properly?), essential-vs-optional distinction, category examples.
  **Load when:** every verdict — companion surfacing.

- `references/restock.md` — Restock & rebuy playbook (Restock Mode).
  **Covers:** the Product Master + FIFO lot schema (mirrored from a live example), per-unit price math, consume-lowest-lot rules, light re-verify checklist, when a rebuy escalates to a full hunt, benchmark-anchored alerts.
  **Load when:** any restock/rebuy/"same thing again" of an already-recorded product.

- `assets/deal-tracker.csv` — Blank CSV **template** for deal tracking (read-only).
- `assets/my-deals.csv` — Merged CSV **template** (deal + claim + EMI + repair, one row per purchase; read-only).
- `assets/emi-tracker.csv` — CSV **template** for EMI records (read-only).
- `assets/repairs.csv` — CSV **template** for repair records (read-only).
- `assets/restock.csv` — CSV **template** for the restock record — Product Master + FIFO lots, one row per lot (read-only). Portable copy for web/CLI users without a vault restock note.

> All templates are read-only. Default output is chat; give a download only when asked.

## Examples

For worked examples (Buy now, Wait for sale, Don't buy, Compare mode, Pay Smart flip, EMI readiness flip, quick hunt, market shock, complementary surfacing), see `references/examples.md`.
