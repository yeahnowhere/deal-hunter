# deal-hunter

**AI skill for smart buying in India.** Find the best-value product (not just the cheapest), verify the deal is real, find the cheapest way to pay, and keep the whole thing tracked - from first hunt to the warranty claim two years later.

Works with any AI agent that supports skills (Agent Skills-compatible tools).

---

## What it does

| Area | What you get |
|---|---|
| **Hunt / compare / deal-check** | 3-5 real candidates across Amazon.in, Flipkart, and category platforms, scored **value = features ÷ price** |
| **Worthiness gate** | Asks *"is this purchase worth it to you?"* before any research - the answer can be **Don't buy**, no matter the price |
| **Deal verification** | Real price history vs inflated MRP, review-integrity checks (bursts = manipulation), community long-term-ownership checks (Reddit-first) |
| **Market shock awareness** | Lightweight news sweep per hunt — category-wide shocks (RAM/memory shortages, component-cost hikes, launch inflation) reset targets instead of false "fake discount" flags |
| **Pay Smart** | Effective price after card offers, UPI cashback, coins, cashback apps, EMI / no-cost EMI (with its hidden fees), split payment - **you decide on what you actually pay** |
| **EMI readiness** | Committed monthly EMI + new EMI vs your ceiling → **Ready / Almost / Not ready**, with the numbers |
| **Used / refurb** | On-spot test plan, mining-card & stolen-device signals, warranty-transfer reality |
| **Imports** | Landed cost (customs/IGST, courier vs postal) vs buying local - imports are a separate tier |
| **Price alerts** | Keepa / pricehistory.in / deal bots, tied to the next real India sale |
| **Claims & warranty** | Invoice kept, warranty-registration deadlines, escalation: brand → NCH 1915 → consumerhelpline.gov.in → e-Daakhil |
| **Repair tracking** | Every repair logged; **repair-vs-replace** (fix / replace / do nothing) before spending |
| **Subscription audit** | Recurring-spend inventory with worthiness per subscription |
| **Record & recall** | One row per purchase (deal + claim + EMI + repair), then *"what's the status of X?"* is answered **from the record**, not by re-researching |

## What it does NOT do

- **Does not buy anything** - it researches and recommends
- **Does not trust MRP, strikethroughs, or star ratings** as evidence - everything is cited or flagged unverified
- **Does not invent prices, reviews, offers, or sale dates** - sale dates/offers are re-verified live at research time
- **Does not file claims, run credit checks, or guarantee financing/warranty approval** - it prepares the evidence and gives the escalation path
- **Never writes into its own files** - `assets/*.csv` are read-only templates; web/cloud agents hand you a copy-paste row instead

## How it works

```
hunt → verify hard → score & compare → pay smart (effective price)
  → pipeline budget (out + queued + EMI + new) → verdict
  → record (tracker row / my-deals.csv / copy-paste row)
  → recall (later "status of X?" answered from the record)
```

Verdicts are exactly one of: **Buy now / Wait for sale / Pick alternative / Don't buy** - with a target price, the next real India sale, the best alternative, and a purchase-mechanics + safety note for the recommended buy.

## Install

The skill is a folder with a `SKILL.md` — copy it into your agent's skills directory (or upload the zip):

```bash
git clone https://github.com/johnsstalk/deal-hunter.git
cp -r deal-hunter /path/to/your-agent/skills/
```

Or download the latest `.skill` zip from **Releases** and upload it through your agent's interface.

> Install only from trusted sources, and audit the bundled files before use.

## Quick start

```
find me the best <product> under ₹<budget>, must-have: <spec>
is this a good deal? <URL>
compare these: <A> <B> <C> - which should I get?
am I ready for <product> ~₹<price> on EMI? (my ceiling is ₹X/month)
help me claim warranty on <product> - what's the escalation path?
what's the status of <product>? / where is my claim?
```

## Data & privacy

- **Nothing leaves your machine.** The skill researches the open web; all *your* records stay in your own tracker note or your own `my-deals.csv`.
- **`my-deals.csv`** is the portable record - a single merged file (deal + claim + EMI + repair, one row per purchase) that any AI can read back on a later session.
- On platforms where the agent can't write files, it gives you a **copy-paste row** to drop into your file.
- The skill's own files are **read-only templates** - never write targets.

## Project layout

```
deal-hunter/
├── SKILL.md          # the skill - frontmatter tells the agent when to use it
├── references/       # playbooks the agent loads on demand
├── assets/           # read-only CSV templates (my-deals, deal-tracker, emi, repairs)
├── README.md         # this file - repo-facing only, not part of the skill
└── .github/          # CI (validate + release)
```

## Reference playbooks

| File | Load when… |
|---|---|
| `prompt.md` | analyzing a specific shortlisted product (JOB 0-10 copy-paste prompt) |
| `india.md` | any India-market buy - platform map, sale calendar, scams |
| `community.md` | verifying long-term ownership (Reddit-first, paid-plant detection) |
| `finance.md` | any financed purchase - effective price, no-cost EMI reality, offer-stacking |
| `emi.md` | any financed purchase or while EMIs are active - readiness verdict |
| `repairs.md` | a device breaks or needs a repair - repair-vs-replace |
| `claims.md` | a product breaks or arrives wrong - warranty → NCH → e-Daakhil |
| `used.md` | used/refurb candidates - on-spot testing, mining/stolen signals |
| `import.md` | international listings - landed-cost math vs local |
| `alerts.md` | every Wait verdict - price alert + sale trigger |
| `market.md` | every hunt (lightweight) - market-shock detection: shortages, category-wide price resets, shrinkflation |
| `subscriptions.md` | subscription/recurring-spend questions |
| `tracker.md` | recording a hunt result - schema, pipeline rule, watchlist |
| `recall.md` | any "status of X / where is my claim?" - read the record, don't re-research |
| `examples.md` | seeing the pipeline in action - 8 worked examples (Buy now, Wait, Don't buy, Compare, Pay Smart flip, EMI flip, Quick Hunt, Market-shock flip) |

## Development

- **Docs-first:** draft behavior changes in the project docs, mirror them into `SKILL.md`/`references/`, then deploy.
- **Validate:** `sync-dealhunter.ps1 -CheckSync` verifies deployed = master = git HEAD; CI runs the same frontmatter, reference-integrity, and leak checks on every push.
- The `.skill` zip is built on release tags; the repo stays free of build artifacts.

## License

All rights reserved. This repository is public for viewing only; no license grants permission to copy, modify, or redistribute the contents.
