# Examples

> All examples are **illustrative** — sample figures for demonstration, not the author's actual purchases.

## Example 1: Buy now (flagship win)

- Input: "I need WiFi + Bluetooth for my desktop. Budget ~₹3,000."
- Steps:
  1. Define need: must-have = WiFi 6 + BT, direct-fit PCIe (no adapter)
  2. Net: TP-Link AX1800 card (~₹2,600), a T4E-class card (~₹1,900, no BT), a WE3000-class card (~₹3,500), an mPCIe adapter (~₹2,000, reuses old b/g/n card)
  3. Verify: the AX1800 card shows 4.4★/2.7K ratings, is a best-seller, MRP ~₹5,600 → 53% real vs historical pricing
  4. Score: the AX1800 card wins on features-per-rupee
- Output: **Buy now — the AX1800 card.** WiFi 6 + BT 5.2 + card included, direct-fit PCIe x1, only ~₹600 more than a low-value adapter. Logged to tracker as "bought".

## Example 2: Wait for sale

- Input: "Is ₹4,999 a good price for [headphones]?"
- Steps: Verify finds historical low of ₹3,499 reached 3x in past year; current price is typical, not low.
- Output: **Wait for sale.** Target price ₹3,799. Track it; no purchase now.

## Example 3: Don't buy

- Input: "Should I buy [gadget] for ₹6,145?"
- Steps: Verify finds equivalent spec (₹1,899) and ₹6,145 is a niche adapter with no warranty; need can be met cheaper or not at all.
- Output: **Don't buy.** The need is inflated or met better elsewhere. Log the decision.

## Example 4: Compare mode (user's own list)

- Input: "Compare these 3 headphones — Sennheiser HD 450BT ₹6,999, Sony WH-CH520 ₹4,499, JBL Tune 510BT ₹2,999. Which should I get? Must-have: long battery + Bluetooth 5."
- Steps:
  1. Lock list: 3 products confirmed
  2. Normalize specs: battery hours, BT version, ANC, weight, driver
  3. Price-check each: CH520's ₹4,499 is ~30% above its typical ₹3,500
  4. Review-check each: JBL review dates clustered (flag); Sony/Sennheiser spread out
  5. Weighted score: battery 3x, BT 2x → Sony CH520 (with price caveat) vs JBL
- Output: **Pick alternative — JBL Tune 510BT** if budget is king; **Sony CH520** if battery matters most (wait for ~₹3,500). State both and why, per must-have weights. Then ask where to save.

## Example 5: Pay Smart flips a verdict (financing layer)

- Input: "Cashify Google Pixel 8a vs Pixel 8, which should I buy? Budget under ₹30,000. Must-haves: battery, long-term updates, compact, camera. It'll be a second phone for travel."
- Sticker-price analysis (Compare mode, steps 1-5):
  - Pixel 8a ₹23,699 (₹23,099 w/ Gold) — **OUT OF STOCK** (Notify Me), updates ~2031, reviewers call camera "average"
  - Pixel 8 ₹30,799 (₹30,199 w/ Gold) — **IN STOCK**, better camera + wireless charging, updates ~2030, 4.8★/43 (95% positive)
  - Sticker verdict would be: 8a better value/rupee but unavailable → "wait for restock"
- Pay Smart (step 6) changes the answer:
  - Card-offer badges on the Pixel 8 page: **₹3,700 / ₹4,000 off on card payment** (RewardEagle confirms Cashify coupons, Aug 2026)
  - **No-cost EMI**: SBI credit card 3/6 mo; HDFC/ICICI debit card 3-6 mo; cardless EMI via Snapmint/Instacred; EMI from ₹1,757/mo
  - **Split payment**: ₹10k cash + card/EMI for the remainder
  - Effective price ≈ ₹30,799 − ₹600 (Gold) − ₹3,700 (card offer) ≈ **₹26,499-27,099** — **under the ₹30k ceiling**
- Output: **Buy now — Pixel 8** (at effective price ~₹27k with card offer + no-cost EMI). Sticker price alone said "wait"; the payment layer made it affordable today. Then ask where to save.

## Example 6: EMI readiness flips a verdict

- Input: "Am I ready to buy [phone] at ₹72,999 on 6-mo EMI (~₹12,167/mo)? My active [phone] EMI is ₹3,500/mo."
- Steps: read the EMI ledger → committed ₹3,500/mo, ceiling ₹6,000/mo → headroom ₹2,500/mo. New monthly ≈ ₹12,167/mo → committed + new ≈ ₹15,667/mo, way over the ceiling.
- Output: **Not ready.** New EMI busts the ₹6,000/mo ceiling ~2.6x. Options: wait until the current EMI closes (~6 months → full ₹6,000 headroom), pick a cheaper model whose EMI fits the ceiling, or raise the down payment. Numbers shown: ceiling ₹6,000, committed ₹3,500, new ₹12,167, shortfall ₹9,667. Then ask where to save.
