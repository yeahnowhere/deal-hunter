# Restock & Rebuy — the rehunt-free loop

Load this file for any **restock / rebuy** of a product that was already researched and recorded — "restock X", "same thing again", "want to restock <X>", **"I bought <X> before"**, **"bought this last month — find me a deal"**. It is the third mode of the deal-hunter skill (SKILL.md → Restock Mode).

## The one philosophy

> **A deal is verified research done once. The tracker records it. A rebuy of the *same* product references that research instead of running a new hunt.**

Hunt Mode is expensive on purpose (it verifies worthiness, reviews, communities, compatibility, market). That work should be owned once per product, not per bottle. The restock record is the souvenir of a done deal — the same link, size, per-unit price, platform and payment path you already proved, reused for the next buy.

**The rule:** *A rebuy references the research; only a new product gets a new hunt.* The only thing a restock verifies is "is today's price better than my benchmark?" — everything else is already known.

## The record — Product Master + FIFO lots

Two tables, one file per user. This mirrors the live working example (`Trackers/Household & Restock Tracker.md` in the author's vault) — same shape, portable everywhere.

### 1. Product Master — one row per product

| Column | Meaning |
|---|---|
| Product | Exact name (brand + variant). One entry per product, ever. |
| Latest size | The size bought most recently (e.g. `125g x6`, `200ml`). |
| MRP | Stored so future strikethroughs can be cross-checked against the real MRP. |
| Last price | Most recent actual/effective price paid. |
| First bought | Date of the first purchase (lot #0/#1). |
| Last restocked | Date of the most recent lot. |
| Restock # | Running rebuy count (`#1`, `#2`, …). Marker that this product is in the restock loop. |
| Link | The canonical product link from the winning research. |

### 2. Restock Ledger (FIFO) — one lot per buy, layered under the product

| Column | Meaning |
|---|---|
| Lot | `0` (first buy) then `1`, `2`, … per rebuy. |
| Date | Purchase/order date. |
| Size | Exact size/SKU of this lot. |
| Unit price | **Per-unit price** (`₹/ml`, `₹/bar`, `₹/kg`) — the honest comparator across pack sizes. |
| Total | Amount paid (or effective price if a card/UPI/coin offer applied). |
| MRP | Stored MRP at buy time. |
| %off | Real discount vs stored MRP (and whether the strikethrough was genuine). |
| Platform | Where it was bought (Amazon, Amazon Fresh, Flipkart, Zepto, …). |
| Payment | Payment path used (UPI, credit card, Amazon Pay, …). |
| Status | Canonical lot status: `ordered` / `in use` / `finished <date>`. |
| Link | This lot's product link (same as Master unless the SKU changed). |

**FIFO rule:** consume the **lowest-numbered lot first**. When a lot runs out, set its Status to `finished 2026-xx-xx` — that is the restock trigger: it ran out, so a rebuy is due.

## First buy → auto-capture (step 9 of the Hunt loop)

The first time a **repeatable/consumable** product is bought (soap, shampoo, facewash, moisturizer, detergent, refills, consumables), the hunt's step 9 also creates the Product Master row + lot `#1` (or `#0`) from today's **verified** research. This is automatic — no need to ask. It is the whole point: *AI research it, then stock it* — so the next time, no hunt.

Which products qualify? Anything the user will **buy again in kind**. If unsure whether a product is repeatable, ask once ("will you need this again?"). A one-off device is a Deal Tracker row only; a consumable is a Deal Tracker row **and** a restock Master entry.

## Restock loop (triggered by "restock X", "same thing again", "want to restock <X>", "I bought <X> before — find me a deal", a `finished` lot, or low stock)

1. **Read the record FIRST — never price-hunt before the lookup.** Identify the product + needed size against the Product Master in the restock file (blur-tolerant: "the soap" = the recorded Santoor bar, not a new hunt for "soap"). When the user quotes a past buy ("bought this last month, want to restock it"), the **Household & Restock Tracker/restock file is where you find WHICH product and ITS benchmark — look it up before checking any current price.** Only if the product is not recorded does this become a hunt (then the first buy auto-captures it — see below).
2. **Read the benchmark from the Master** — canonical link/SKU, size, per-unit price, best %off, platform, payment path.
3. **Price-check today, benchmark-anchored:**
   - Same SKU live? Same seller quality level?
   - Current price vs the reference. Is today's "discount" a **real** drop (price history via `alerts.md` tools — Keepa/camel on the same ASIN) or an inflated strikethrough?
   - Re-run **Pay Smart** lightly: does a card offer / UPI cashback / coins / coupon make the **effective price** cross below the reference? (full guide `finance.md`)
   - **Market context:** one lightweight check — if the category is `inflating`/`shortage` (`market.md`), the reference is reset to the post-shock floor; a "pre-shock low" is no longer the target.
4. **Verdict** (same 4 outcomes, benchmark-anchored):
   - **Buy now** — effective price ≤ stored reference (last price or best %off). Also check purchase mechanics lightly for the lot (`india.md`: open-box, invoice) only if it's a high-value restock — routine groceries skip this as `n/a`.
   - **Wait for sale** — price is above benchmark: **set a price alert at the benchmark price** and tie it to the next real India sale. A restock wait without an alert is a leak — the reference exists precisely so the alert target is known.
   - **Pick alternative** — **only** when the recorded product is **discontinued / out of stock / permanently inflated**. This is the single case that **escalates to a full Hunt** for a replacement. The replacement, once verified, becomes the new Master entry (keep the old variant as a historical row or note it replaced).
   - **Don't buy** — still worthiness-gated: "it's on offer" ≠ "it's needed". A restock of something over-stocked is a skip.
5. **Record the lot (FIFO)** — append the new lot under the product; bump the Master (last price, last restocked, restock #). **Restocks live only in the restock file** — no Deal Tracker row, and never a new hunt note. Web/lipless agents emit the lot as a copy-paste block (CSV row from `assets/restock.csv` or a table row) and say which file/table to paste it into — never claim it was saved.

## Size changes — always compare per-unit

A bigger pack at a higher total is not a deal if the per-unit price is worse. Normalize every comparison to **₹ per ml / bar / kg**:

```
per-unit = total ÷ quantity (in a single consistent unit)
```

The Master's "Latest size" and each lot's "Unit price" exist for exactly this. If the brand shrink-flates (same ₹/ml stealthily, smaller pack — `market.md`), flag it and re-benchmark per unit.

## When a restock ISN'T a restock

- Product discontinued / OOS / permanently upgraded away → **full Hunt** for a replacement.
- User wants a **different** product of the same category (new soap brand) → **full Hunt** — the old entry stays as history.
- Bundles/packs that change the SKU (buying 3 bars when the Master is 1) → record as its own lot with its own per-unit math.
- If the record shows a bad-satisfaction product (`LOW` post-purchase, or repeated repairs/claims on the same consumable brand) → **let the record veto the rebuy**: a new Hunt is justified to find a better product. A rebuy doesn't rubber-stamp a known-bad buy.

## Alerts for restocks

- The reference IS the target price. Set alerts at the benchmark, not the current price (`alerts.md` §4).
- On a `Wait for sale` restock, set it and name the next real India sale (Great Indian Festival / Big Billion Days / Flipkart sale calendar in `india.md`).
- Two tools if the platform supports it: a price-drop alert on the exact ASIN (Keepa) + a calendar reminder for the sale date so a "no alert tool" platform still converts.

## Where the record lives

Config-driven, same routes as `environment.md` — the restock file is a **tracker-folder ledger** (Product Master + FIFO lots), sitting alongside the Deal/EMI/Claim/Repair trackers. It is the one data-bearing file kept in the tracker folder; every *product note* still goes to the notes folder:

- **Vault (MCP or PC path):** `<tracker_dir>/<restock_file>` — e.g. `Trackers/Household & Restock Tracker.md`.
- **Workspace (local/web):** `trackers/<restock_file>` under the workspace root (fixed `deal-hunter` folder for web-only).
- **No write access:** chat copy-paste block.
- Filename comes from `scripts/config.json` → `restock_file`. Never invent a location — read the config (`environment.md`).

## Portable copy — assets/restock.csv

For web/CLI users without a vault note, `assets/restock.csv` is the read-only **template**: Master fields + this lot's fields on one row per lot, so a flat file recreates both tables (`recall.md` can answer "any restock due?" from it). Copy it once into your storage; never write into the skill's `assets/`.

## Minimum working example

```
# Stock
## Master List
| Product | Latest size | MRP | Last price | First bought | Last restocked | Restock # | Link |
| Plum Green Tea Pore Cleansing Face Wash | 150ml (₹1.92/ml) | ₹360 | ₹288 | 2026-08-15 | 2026-09-24 | #1 | https://www.amazon.in/dp/B0D46SLJKR |

## Restock Ledger (FIFO)
### Plum Green Tea Pore Cleansing Face Wash
| Lot | Date | Size | Unit price | Total | MRP | %off | Platform | Payment | Status | Link |
| 0 | 2026-08-15 | 100ml | ₹2.25/ml | ₹225.40 | ₹275 | 18% | Amazon | Credit card | finished 2026-09-20 | https://.../B0C629LWVS |
| 1 | 2026-09-24 | 150ml | ₹1.92/ml | ₹288 | ₹360 | 20% | Amazon | Amazon Pay | in use | https://.../B0D46SLJKR |
```

Rebuy of lot #1 = benchmark ₹1.92/ml → rebuy when a 150ml at ≤ ₹288 (or any size whose ₹/ml ≤ 1.92) is live.

## Related

- `environment.md` — where the restock file lives (config + routes)
- `tracker.md` / `recall.md` — the deal side of the record; restock recall (lot statuses, "any restock due?" answers from the Master)
- `alerts.md` — benchmark-anchored restock alerts
- `market.md` — shrinkflation / category-shock re-benchmarking
- `finance.md` — effective-price math reused for the benchmark comparison
- `india.md` — sale calendar for restock waits; purchase mechanics for high-value lots