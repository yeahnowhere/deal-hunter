# Subscriptions & Recurring-Spend Audit

Load this file for **subscription/recurring-spend questions** — streaming, Prime/Quick-commerce membership, app subscriptions, SaaS, gyms, ISP/cable, cloud storage, EMI review, insurance. Recurring spend is the biggest silent leak in an Indian budget: nobody re-verifies a subscription after the free trial ends.

> [!important] Subscriptions renew themselves
> A subscription is a monthly hunt on the same money. Inventory it, test each one's worthiness, and prefer annual/shared/student plans. The audit is a recurring job, not a one-time cleanup.

## 1. Inventory (get the list first)

Ask for / pull together every recurring item — don't assume a subset:

- OTT/streaming (Netflix, Prime Video, Hotstar/Disney+, YouTube Premium, music apps)
- Memberships (Amazon Prime, Flipkart Plus, quick-commerce plans, Zomato/Swiggy One)
- App/subscription tiers (iCloud, Google One, software, VPNs)
- Utilities/bills (ISP, phone recharges, cloud storage)
- Physical (gym, subscriptions boxes, insurance)
- **EMIs** — the recurring-spend cousin; review tenure, interest, and early-payment penalties

## 2. Per-subscription worthiness test (apply JOB 0 to each)

For each line, ask:
1. **Did you use it last month?** (log out of "I might use it")
2. **Is the price still right?** — what it costs now vs when you joined (trail pricing, price hikes)
3. **Is there a cheaper equivalent?** — shared family plans, annual-vs-monthly, student discounts, Jio/Airtel bundle offsets, cashback on recharge; for software/SaaS, research alternatives on **AlternativeTo** and check G2/Capterra for free-tier or cheaper competitors before concluding "no cheaper equivalent"
4. **Would you notice it gone in 7 days?** — if no, it's a candidate for churn

## 3. Annual vs monthly + GST math

- **Annual vs monthly**: compare ₹/month effectively — annual is usually ~2 months free, but only if the user actually keeps it a year
- **GST**: subscriptions carry 18% GST (and 5% for some plan types) — the "₹99/mo" headline is ₹116.82 after GST; compare on the GST-inclusive number
- **Renewal lock-ins**: some annual plans auto-renew and charge the full year at once — flag the auto-renew so it can't silently renew at full price
- **Bundles**: one platform's family plan split 4 ways can replace three separate accounts (and some Indian bank cards give free OTT as an add-on — check the card's rewards page)

## 4. EMI audit (the recurring-spend cousin)

Use the active-EMI ledger and readiness check (see `emi.md`) — the ledger (e.g. an `EMI Tracker` note) holds one row per active EMI plus the user's monthly EMI ceiling:

- List active EMIs from the ledger: principal remaining, monthly outflow, tenure left, interest rate, early-closure penalty
- Recommend: keep 0% / no-cost EMIs, consider closing high-interest ones with early payoff if the penalty < the interest saved
- Run the readiness check on any new purchase: committed + new monthly vs the monthly ceiling → Ready / Almost / Not ready (see `emi.md`)
- Feed the total monthly EMI **and remaining obligation** into the pipeline budget (see `tracker.md` and `emi.md`) — EMIs are committed future spend, not "already bought"

## 5. Output

- A table: each subscription | ₹/mo (GST-inclusive) | used last month? | keep / downgrade / churn / switch
- **Total monthly committed** vs value delivered — the headline number
- Top 3 concrete savings with amounts (switch to annual, kill unused, split a family plan)
- Renewal dates + auto-renew flags so nothing renews silently
- **Free trials in flight** — any trial with an end date gets its own line: trial ends on X, cancel-before date, and what it converts to if not cancelled

**Where cancellations actually happen:** UPI Autopay / NACH mandates are managed in the **bank app** (mandates/UPI Autopay section) or the merchant's account page — the skill points the user there; it cannot cancel anything itself.

## 6. Boundaries

- The skill inventories and recommends — it does not cancel subscriptions, block cards, or move money
- Prices and plan structures change; verify current prices before acting on a recommendation

## 7. Related

- `tracker.md` — where the audit output and EMI rows land
- `finance.md` — card add-on benefits (free OTT as a card perk) and effective-price thinking
- `alerts.md` — renewal-date reminders so annual auto-renews don't slip by
