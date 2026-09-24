# Deal Tracker (price-history database)

Load this file when recording a hunt result or when the user asks "what's a fair price for X?" — the tracker is a personal record of real prices so future hunts never trust MRP strikethroughs.

> [!important] Destination is environment-driven
> This is the **suggested default format**, not a hardcoded save location. Storage is **config-driven and environment-aware** (see `environment.md`): the AI reads the skill's `scripts/config.json`, then writes to the `Trackers/` index at `<vault>/Trackers/` (via Obsidian **MCP** when connected — vault-relative, works on any device — or the machine's per-device `vault_paths` path), or to the **workspace** record (in-skill `workspace/` → `trackers/` + `notes/`) for non-vault/web users. The skill's `assets/*.csv` are read-only templates, never write targets.

> [!warning] Two-folder split
> `Trackers/` (or workspace `trackers/`) holds **only** the index files. Every **individual product note** goes to `Journal/` (or workspace `notes/`) — never into the tracker folder. The `→ Note` cell links to that note wherever it lives.

## Schema

`Date | Product | Specs | Platform | Price | Effective price | Payment | MRP | %off | Value score | Decision | Status | Satisfaction | Alert/Claim | Link | → Note`

- **Price** — sticker/list price at research time
- **Effective price** — actual cost after card offers, cashback, and EMI fees (see `finance.md`); leave blank for straight-cash buys
- **Payment** — pay path that gave the effective price (e.g. "cash", "card ₹3,700 off", "₹10k cash + 6-mo no-cost EMI", "Bajaj EMI", "UPI cashback ₹500", "SuperCoins 2000 + card 5%", "CashKaro 3% cashback")
- **%off** — effective price vs MRP (not sticker vs MRP)
- **Satisfaction** — `HIGH`/`MED`/`LOW` + "worth it after extended use?" verdict, appended after real use
- **Alert/Claim** — price alert set (Keepa/pricehistory.in + target + sale trigger) for `waiting` rows; warranty-registration date + claim status for `bought` rows (see `alerts.md` / `claims.md`)
- **→ Note** — optional link to the note/clipping where the detail lives (the user's own deal note, per-device note, etc.). Keep the full research there; the tracker row only references it.

## Status Flow

`noted` → `waiting` → `buying` → `bought` → `skipped` / `cancelled`

- **noted** — product researched, pending decision
- **waiting** — decision = Wait for sale; target price + sale trigger noted
- **buying** — order placed, not yet delivered
- **bought** — purchase made and delivered
- **skipped** — rejected *before* purchase (bad value / alternative won / don't-buy)
- **cancelled** — order placed, then cancelled (check the refund landed)

(Canonical vocabulary shared with `recall.md` — one word, one meaning across all files.)

**Recall normalization:** when a later *"status of X?"* question is answered from the record, normalize these words to the canonical vocabulary in `recall.md` (`noted` / `waiting` / `buying` / `bought` / `skipped` / `cancelled`); answer with product, date, effective price, status, where it's recorded, and next action. The merged `assets/my-deals.csv` (deal + claim + EMI + repair + a restock pointer on one row) is the everything-in-one portable schema for users who keep a single file.

After a bought product gets real use, append a **satisfaction rating** (`HIGH`/`MED`/`LOW`) and the **"worth it after extended use?"** verdict to the row — it calibrates future value scores. If it breaks or arrives wrong, log the **claim status** on the row (warranty filed / NCH / e-Daakhil) so the escalation isn't forgotten (see `claims.md`). If a device gets **repaired**, log the repair (cost, warranty-covered?, claim outcome) and run **repair-vs-replace** before replacing it (see `repairs.md`) — a repair history is the durability truth behind the next value score.

> [!warning] Pipeline-aware budget rule
> **`waiting` / `noted + Buy` rows are future spend, not "not bought"** — and so is the **remaining obligation on active EMIs** (see `emi.md`). When any new purchase is considered, total = ₹ out (spent) + ₹ queued (waiting/noted-Buy) + ₹ active-EMI remaining + ₹ new. Surface the total before deciding — "₹X out, ₹Y queued (~₹Z converts at the next sale), ₹E EMI remaining, new ≈ ₹W → X + Y + Z + E + W. Proceed / split / defer?" This layer sits on top of per-project budgets.

## Watchlist (waiting for a sale trigger)

Items queued for a real India sale (see `india.md` sale calendar) with their target price. Revisit at the trigger — bought if hit, downgraded/dropped if it never drops and isn't essential.

> Illustrative example — replace with the user's actual watchlist.

| Item | Current | Target | Sale trigger | Notes |
|------|---------|--------|--------------|-------|
| 16GB DDR5 kit (used) | ₹7,500–8,500 | ~₹7,000 | Great Indian Festival / Big Billion Days (~Sep–Oct) | example only — adapt to the user's build |
| 27" 1440p IPS monitor | ₹15,000–18,000 | ~₹14,000 | Diwali sale | example only — verify fit and ports first |
| Robot vacuum (mid-range) | ₹12,000–15,000 | ~₹10,500 | Great Indian Festival (~Sep–Oct) | example only — check parts availability |

## Decisions

Exactly 4, matching the verdict step:

- **Buy** — price near historical low, product verified
- **Wait** — track it, note the target price
- **Alternative** — a better-value candidate won
- **Skip** — need wasn't real, or price inflated

## Example Rows

> Fictional rows — they show the schema, not anyone's real purchases.

```
2026-06-02 | Noise Buds N1 TWS | 13mm drivers, 42h battery | Amazon.in | 1499 | 1199 | UPI cashback ₹300 | 3990 | 70% | High | Buy | bought | - | warr-reg 2026-06-05 | https://... | notes/tws-hunt.md
2026-06-02 | Xiaomi 33W GaN charger | PD 33W, 2-port | Amazon.in | 999 | 899 | card 5% off | 1999 | 55% | Med | Wait | waiting | - | Keepa @ ₹850 + GIF | https://... | notes/charger-hunt.md
2026-05-18 | Samsung Galaxy A55 (refurb) | 120Hz AMOLED, long updates | Cashify | 24999 | 21999 | ₹5k cash + 6-mo no-cost EMI | 42999 | 49% | High | Buy | buying | - | OBD delivery booked | https://... | notes/phone-hunt.md
2026-05-18 | OnePlus Nord CE4 (refurb) | 120Hz, 50MP | Flipkart | 18999 | 17499 | SuperCoins 1500 + card 5% | 25999 | 33% | Med | Alternative | skipped | - | - | - | notes/phone-hunt.md
2026-04-09 | pTron Bassbuds neckband | 10mm drivers, 30h | Flipkart | 699 | 549 | UPI cashback ₹150 | 1999 | 73% | Low | Skip | skipped | - | - | - | -
```

## Outcome Note Pattern

After a hunt, record a short note like:

> **Noise Buds N1 ₹1,499 → ₹1,199 effective.** ₹300 UPI cashback via a payment-app promo; sale-season price vs ₹3,990 MRP. Kept GST invoice for warranty. See `india.md`.

> **Samsung Galaxy A55 ₹24,999 → ~₹22k effective.** ₹500 card offer + ₹500 platform cashback + 6-mo no-cost EMI (₹5k cash + EMI remainder). Sticker price busted the ₹22k budget; the payment layer made it buyable. See `finance.md`.

> **TP-Link AX1800 card ~₹2,600 won.** WiFi 6 + Bluetooth 5.2 + card included, direct-fit PCIe x1, 4.4★/2.7K ratings, best-seller. Cost only ~₹600 more than the adapter alone but delivered far higher standard.

## Rules

- Append one row per product researched, newest at top
- Re-researching a product = a **new row cross-linked to the prior row** (history preserved); never overwrite an old row
- Link each row to the note/clipping where the detail lives (→ Note); the tracker indexes, it never duplicates the research
- Write to the config-driven destination (vault `Trackers/` via MCP or this machine's `vault_paths`, else the workspace `workspace/` (`trackers/` + `notes/`)) per `environment.md` — ask to create the one-time config only when needed; an explicit "save this to X" overrides
- Write the decision **before** the purchase, not after
- For financed purchases, record the **effective price** and the pay path, not just the sticker price
- If a "Wait" verdict is tied to a sale, note the sale name + expected date in the Status/Decision, and record the **price alert** set (target price + tool) in the Alert/Claim column
- For `bought` rows, log the **warranty-registration date** in the Alert/Claim column so the deadline isn't missed
- After real use, append the **satisfaction rating** (`HIGH`/`MED`/`LOW`) + "worth it after extended use?" verdict
- When the user mentions using a bought product, **ask for the missing satisfaction rating** and append it — don't wait to be told twice
- For devices that broke or got repaired, log the repair (cost, warranty-covered?, claim outcome) and run repair-vs-replace before replacing (see `claims.md` / `repairs.md`)
- Before any new spend, surface the pipeline total: ₹ out + ₹ queued + ₹ active-EMI remaining + ₹ new (informational — never block silently)
- Active EMIs live in the EMI ledger (`emi.md`); their remaining obligation counts in every pipeline total
- Over time the tracker tells you the true fair price for any category
- Record & Recall playbook: `recall.md` (canonical status words, the merged `assets/my-deals.csv` schema, and web copy-paste rows for agents that can't write files)
