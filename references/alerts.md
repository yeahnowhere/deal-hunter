# Price Alerts & Watchlist Re-check

Load this file for **every "Wait" verdict** and for the monthly Watchlist re-check. A "wait" without an alert is a leak — the sale passes silently and the waiting item either converts at full price or gets forgotten.

> [!important] A wait without an alert is a leak
> Every "wait" verdict must end with an alert set (or offered) and a named sale trigger. Otherwise the target price is aspirational, not actionable.

## 1. Alert tools (India-friendly)

| Tool | What it tracks | Notes |
|------|---------------|-------|
| **Keepa** | Amazon.in price history + price-drop alerts | Extension + site; the most reliable for Amazon; alert via browser + email |
| **pricehistory.in** | Flipkart (and other) price history | Less reliable than Keepa; cross-check with the sale calendar |
| **BuyHatke / PriceBefore** | Amazon.in + Flipkart price history & alerts | Second signal — cross-check against Keepa and the sale calendar |
| **camelcamelcamel** | Amazon-only, simpler | Fine as a second signal |
| **Telegram/Discord deal channels** | Daily deals / category drops | Alerts, not price-history; use for finding, not verifying |
| **Manual price-history page** | Marketplace product page | Check the Keepa/camel chart before buying to confirm the current price is actually a low |

## 2. The alert-setting checklist

1. Set the alert at the **target price** from the verdict (not the current price)
2. Add the **named sale trigger**: next real India sale (Great Indian Festival / Big Billion Days / Flipkart sale calendar from `india.md`) + expected category drop
3. Tell the user where the alert lives and what it will do (browser extension notification, email, Telegram)
4. If the platform has no alert: set a calendar/reminder for the sale start date instead
5. When an alert fires, **re-verify the listing before buying** — trackers follow the buy-box price, and Indian sellers switch constantly (the seller/variant at alert time may differ from what you shortlisted)

## 3. Monthly Watchlist re-check routine

The Watchlist (see `tracker.md`) is not a graveyard. On a monthly cadence (user-triggered, or agent-scheduled where the deployment supports it) — and always before each big sale:

- Re-run the **current price vs target price** for every `waiting` row
- Re-run the **market sweep** (`market.md` §1) for categories tagged `inflating`/`shortage` — a stale environment tag produces wrong convert/stale decisions (a "missed target" may mean the market moved, not that the item is stale)
- **Convert** items that hit target (decision → Buy; status → `buying`, then `bought` on delivery)
- **Downgrade/stale** items that keep missing target: re-verify the product is still worth wanting (a stale wait may no longer be a good value vs newer alternatives — re-run JOB 0 worthiness)
- **Kill** items the user no longer wants — a cleaned watchlist makes the next hunt honest
- Feed the re-check output into the pipeline budget (JOB 7): "₹Y queued, ~₹Z converts this month"

## 4. Rules

- An alert at the *current* price is noise — alerts only earn their place at the target price
- Set targets off the CURRENT environment, not the all-time low: under an `inflating`/`shortage` classification (`market.md`), a pre-shock historical low is a dead target — alert at the post-shock floor × the category's usual sale drop instead
- Never re-affirm a "wait" without a sale trigger; if the next real sale is months away, say so and set the reminder
- Cross-check the alert tool's history before trusting a "drop" — a fake-low (inflated MRP strikethrough) is not a real drop (see `india.md` dynamic/surveillance pricing)

## 5. Related

- `india.md` — the real India sale calendar + dynamic-pricing checks
- `tracker.md` — the Watchlist statuses and the monthly re-check fields
- `claims.md` — price-protection windows for items bought at full price that then drop
