# Pay Smart — Financing & Payment Optimization (deep dive)

Load this file for **any financed purchase** (EMI, no-cost EMI, card offers, UPI, coins, cashback apps, split payment) or when the user asks how to pay for something they've picked. This is the engine behind **Step 5 (Pay Smart)** in the deal-hunting loop. Goal: minimize the *effective* price — what the user actually pays — by finding and stacking every legitimate discount in the payment layer. For the India-specific levers (UPI cashback, RuPay-on-UPI, coins, cashback apps, sale-season bank offers) also load `india.md`.

> [!important] Effective price, not sticker
> A price tag is not the price. The user's real cost is:
> **Effective price = list price − card discount − cashback − reward-points value + EMI processing fee + GST on waived interest**
> Decide on this number, never the sticker price.

## 1. Payment-Method Inventory (ask, don't assume)

Before researching financing, confirm what the user can actually pay with:

- Cash available (and how much they want to keep liquid — this powers split payments)
- Credit cards: which bank + network (Visa / Mastercard / RuPay / Amex) — network-specific offers differ
- Debit cards: which bank (e.g. HDFC/ICICI debit cards often get no-cost EMI)
- EMI card / line: Bajaj Finserv, Instacred, Snapmint, or bank EMI on a credit card; pay-later/BNPL apps: Simpl, LazyPay, Amazon Pay Later, Axio (ZestMoney shut down Dec 2023 — do not recommend)
- UPI (often instant cashback promotions — GPay/PhonePe/Paytm, and instant UPI discounts on marketplaces)
- RuPay credit card on UPI (the only cards that link to UPI; rewards vary — e.g. Tata Neu Infinity ~1.5%, BOBCARD Eterna ~3.75% on online+UPI; example rates churn — verify the current rate before quoting)
- Coins / reward points (Amazon Pay coins, Flipkart SuperCoins, Tata Neu coins, Myntra Insider — often worth more on their home platform)
- Cashback apps / aggregators (CashKaro, CouponDunia, GrabOn — extra % back, lands later, can expire)
- Gift cards / wallet balance / corporate discounts
- Reward points balance (can reduce effective price or pay part of the EMI)
- Exchange / buyback bonus (old device trade-in)

## 2. The Effective-Price Formula

```
Effective price = List price
                − seller/card offer (e.g. "₹3,700 off on card payment")
                − instant discount (e.g. "2% up to ₹2,000")
                − cashback (e.g. reward points, UPI cashback) valued in ₹
                − cashback-app / aggregator payout (CashKaro/CouponDunia/GrabOn) if still live
                − coin/reward redemption value (Amazon Pay / SuperCoins / Neu)
                − exchange/trade-in bonus
                + EMI processing fee (often ₹99-999 flat, sometimes %; GST at 18% applies to fees too)
                + GST on the waived interest (18% of the interest subsidy for "no-cost" EMI)
                + any hidden handling/fulfillment charge
```

If the user pays part cash + part EMI, split the math: the cash portion pays list-price-minus-offers; only the financed portion carries EMI fees.

## 3. No-Cost / Zero-Cost EMI — the reality check

"No-cost EMI" (also called "0% interest EMI" or "zero-cost EMI") means the seller/bank absorbs the interest — **but it is not free**:

- Banks charge a **processing fee** (flat or a small % of the financed amount).
- GST is charged **on the waived interest amount** (18%), which the user pays.
- Tenure is usually **capped** for true no-cost: e.g. SBI credit card 3/6 months; HDFC/ICICI debit card 3-6 months. Longer tenures fall back to regular (interest-bearing) EMI.
- Some "no-cost" offers instead show a **discount on the product** equal to the interest subsidy and charge interest on the full amount — net effect similar, but check the fine print so you don't double-count.

Worked example: a refurb phone at ₹30,000. ₹3,700 off on card payment → ₹26,300. Split ₹10k cash + ₹16,300 financed on 6-mo no-cost EMI → EMI ≈ ₹2,720/mo. Even adding a ₹199 processing fee + GST on the waived interest (~₹300-400), effective price ≈ **₹26.7k** — under a ₹30k ceiling that the sticker price busted.

## 4. Split Payments (the cash + card/EMI model)

Split payment = pay part with cash and the rest by card or EMI. Useful when:

- The user wants to keep liquidity (e.g. ₹10k cash + ₹20k card)
- Only part of the amount qualifies for a card offer (offer caps)
- The card limit won't cover the full price but covers the remainder

Check each platform's split limits and whether the card offer still applies to the financed portion.

## 5. Offer-Stacking Rules (in the right order)

Discounts stack in a specific order — always verify against the actual page:

1. **Platform/coupon offer** first (e.g. product coupon, brand discount)
2. Then **payment-method offer** (e.g. "₹3,700 off on card payment", "2% instant discount")
3. Then **cashback / reward points** credited after the purchase
4. **Exchange/trade-in bonus** as a separate line (often a floor-price guarantee on the old device)

Rules: cashback is not a price cut (it arrives later and may expire); never assume two offers combine unless the page says so; re-check the **order of application** because it changes the final number.

## 6. Affordability Check

Financing turns a price into a monthly outflow. Before recommending EMI:

- **Read the EMI ledger first** (see `emi.md`) — committed monthly EMI + remaining obligation vs the user's monthly EMI ceiling. The new EMI must fit the remaining headroom, not just the income ratio.
- **EMI-readiness verdict** — committed + new monthly vs the user's monthly EMI ceiling (see `emi.md`): Ready / Almost / Not ready, with the numbers shown.
- EMI amount vs monthly income — is the outflow comfortable?
- **Credit-bureau impact** — pay-later/BNPL and EMI lines are reported to CIBIL and other bureaus; even a no-cost EMI adds a bureau-reported line. N active lines or a missed payment can affect future loan eligibility — say so in the readiness verdict.
- Total interest over the chosen tenure (use 3/6/12-mo figures)
- Down payment (zero-down vs a lump sum — a bigger down payment shrinks processing fee + GST)
- Opportunity cost: would the cash be better kept for something else?

Recommend the shortest tenure that fits their budget — shorter tenure = less interest/fees.

## 7. Where Offers Are Found

- Product page payment section (EMI options, card badges, coupon strip, UPI cashback banners) — always cite what you see
- Seller's offers page (e.g. Cashify has platform-specific card/debit offers)
- Bank/network sites for no-cost-EMI schedules (SBI, HDFC, ICICI) and sale-season bank offers (SBI/ICICI ~10% instant on Flipkart/Amazon during Big Billion Days / Great Indian Festival)
- Coupon aggregators (CashKaro, CouponDunia, GrabOn — verify the offer is still live before quoting it)
- UPI app offer pages (GPay/PhonePe/Paytm cashback promos)
- Cite each offer's source; flag anything unverified as unverified.

## 8. Price Protection (post-purchase price drops)

A deal isn't over at checkout. If the price drops right after you buy:

- **Platform refund/price-match** — Amazon.in and Flipkart have limited price-protection windows (often 7 days) for price drops on the same listing; check the order page for a "price dropped" notification. Not guaranteed — always check the order/support page.
- **No-cost-EMI rebooking** — if the financed price drops within the return window, you may be able to cancel + rebuy at the new price instead of chasing a refund.
- **Return-and-rebuy math** — only if the drop exceeds the return/restocking friction: return shipping, time, and any price-protection credit. Compute before acting.
- **Card price-protection benefit** — some premium cards offer purchase/price protection (refund the difference if an item's price drops within N days). Cite the card's terms; don't assume.

## 9. Boundaries

- This skill **researches and recommends** — it does not apply for a loan, run credit checks, or guarantee approval.
- EMI eligibility depends on the bank's checks; the skill only quotes the terms as listed.
- Prices/offers change daily — always re-verify before purchasing.
