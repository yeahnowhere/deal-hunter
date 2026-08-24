# Market Context & News Layer (shock detection)

Load this file on **every hunt** — the sweep is one lightweight search; deep-dive only when shock signals appear. Historical price baselines lie during structural market shocks: when a category-wide event moves prices (component shortage, currency swing, duty change), yesterday's "good price" no longer exists, and "wait for the sale" can be advice to wait for a floor that's already gone.

> [!important] A price is only fair or unfair relative to its market
> The same ₹89,999 phone can be overpriced in a normal market and the honest new normal after a component-cost shock. Judge the listing against its **current environment**, not just its own history.

## 1. The lightweight sweep (every hunt)

One or two searches before trusting any price verdict:

- Search: `<category or key component> price increase OR shortage OR price hike`, filtered to roughly the last 90 days
- Memory-sensitive categories (RAM, SSDs, phones, laptops, GPUs, consoles, handhelds): add a DRAM/NAND check ("DRAM price trend", "memory shortage") — memory cycles move every downstream device
- Big-ticket brand launches: check "<brand> <product> launch price vs predecessor" — launch-inflation gets announced and cited once, then the listing page never mentions it again

If nothing surfaces and the price history looks seasonally normal, classify `normal` and move on. Don't manufacture drama out of one slow news week.

## 2. Shock signals (any two → deep dive)

| Signal | What it looks like |
|---|---|
| All brands rising together | Every candidate up 10–30%+ across 1–2 quarters — macro, not a bad listing |
| Step-change in price history | Chart jumps and stays elevated instead of the usual dip-and-recover around sales |
| Spec shrinkflation | Same/near price but less than the predecessor: less RAM/storage, slower chip, dropped features |
| Vendor hike announcements | Brands publicly blame input costs (memory, silicon, logistics) for price increases |
| Stockouts + scalping | Models vanish at MRP while resellers charge above it — availability risk, not just price risk |

## 3. Classify the environment

| Environment | Tag | Price-verdict implication |
|---|---|---|
| Normal | `normal` | Standard rules — typical/historical price stays the baseline |
| Softening | `softening` | Waiting has the edge; set targets below current with a named sale trigger |
| Inflating | `inflating` | Historical lows are dead targets — reset expectations to the post-shock base (see §4) |
| Shortage | `shortage` | Price AND availability risk — delay can cost more, or lose the item entirely |

## 4. How a shock flips verdict logic

- **Reset "Wait" targets.** A sale discount applies off the NEW base: target = post-shock floor × the category's usual sale drop — not the pre-shock historical low.
- **"Buy now before the next hike" is legitimate** when the trend is still rising — cite the trend evidence; never manufacture urgency without it.
- **Category inflation ≠ fake discount.** Don't flag an MRP strikethrough as a scam when the whole category reset upward — but DO still flag a listing priced above its own category's new base.
- **Penalize shrinkflation in value scoring.** A successor at +₹10k with *less* RAM scores worse per rupee than its predecessor did — say so explicitly in the verdict.
- **Availability risk counts.** Under shortage, waiting can mean paying more later or not finding the model at all — weigh delay cost into every Wait verdict.
- **Financing angle:** deferring a needed buy in an inflating category usually raises its effective price; in a softening one, patience pays.

## 5. Sourcing discipline

- Cite source + date for every market claim (news URL, analyst note, brand statement). No citation = don't claim it.
- News older than ~90 days is a weak signal — recheck whether the condition still holds before acting on it.
- Re-verify live at research time, same as sale dates and offers. Never extrapolate a trend line yourself.
- Strong sources: Counterpoint / TrendForce / IDC / Gartner notes, brand statements, established tech press. Forum panic ≠ market data.

## 6. Record it

- Tag the tracker row's environment (`normal` / `softening` / `inflating` / `shortage`) with the source link, so the next re-check starts from evidence instead of scratch
- Gates summary carries `Market ✅ (normal)` / `⚠️ (inflating — targets reset)` / `n/a`

## 7. Related

- `india.md` — sale calendar + dynamic pricing (§9): the other reasons a quoted price isn't the price
- `alerts.md` — target-setting under each environment
- `tracker.md` — where the environment tag lives
