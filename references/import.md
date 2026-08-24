# Imports & Global Purchases (import-vs-local)

Load this file for **any international listing** the user is considering — Amazon US/UK/DE, eBay, brand-direct overseas sites, "imported" listings on Indian marketplaces. The sticker price abroad is not the price; the **landed cost** is, and it's often higher than the local effective price once customs and warranty reality are added.

> [!warning] AliExpress is still banned in India
> AliExpress has been blocked in India since 2020, and the government clarified in Aug 2025 that no unblocking order exists. Treat any AliExpress purchase as a legality/policy risk *plus* the usual grey-import risks (no warranty, no returns path) — steer to Indian-marketplace equivalents or other import channels instead.

> [!important] Imports pay twice
> **Landed cost = foreign price + shipping + customs duty + IGST + handling/courier fees (+ currency-markup)**. A ₹3,000 saving on the sticker can vanish in customs + a grey-import (no Indian warranty) — compute the landed cost vs the local effective price before the verdict.

## 1. Landed-cost math

```
Landed cost = foreign price (converted to ₹)
            + international shipping
            + customs duty (varies by category — the duty is on the assessable value, not the paid price)
            + IGST
            + courier handling/clearance fees (courier lines charge more than postal)
            + currency-conversion markup (forex fees on the payment method)
```

- **Assessable value** is the base — customs duty % + IGST apply on top of it; aggregator quotes differ from the self-import reality
- **Courier vs postal**: couriers (FedEx/DHL/UPS) are faster but charge clearance/handling fees and bill customs directly; postal (India Post + trackable services) is slower but often cheaper
- **TCS/LRS** — foreign spends above the LRS free limit attract Tax Collected at Source (currently 5% above ₹7L/year for most categories); relevant for big-ticket imports and subscriptions billed abroad
- The de-minimis relief applies to the **postal/gift channel** (goods up to ₹5,000 imported by post as gifts are duty-exempt in theory) — commercial courier imports don't get the same treatment, and courier handling fees can still make small parcels not worth it; verify the current threshold before assuming

## 2. Grey-import warranty reality (the part that flips verdicts)

- **Grey imports** (parallel imports, "international version", no Indian warranty) — the brand's Indian service center can refuse service; warranty is either none or "seller-side" only
- Even when the brand honors global warranty, Indian centers may reject products not sold through the Indian channel (common with electronics, phones, laptops)
- Battery-replacement, hinge, and other service costs land on the user — factor them in
- **BIS-restricted categories** (electronics, toys, etc.) — mandatory Indian BIS registration; non-compliant imports can be blocked at customs or unsupported locally; check the category before buying
- **Crowdfunded imports (Kickstarter/Indiegogo)** — no consumer-protection net: delivery can slip by years or never arrive, and a failed campaign leaves a chargeback as the only recourse; treat as speculation, not shopping

## 3. When imports actually win

- Brand not available in India (or the Indian variant is a downgrade)
- Local price inflated far beyond the landed cost (some niche gear, specific audio brands, prosumer hardware)
- The user accepts the grey-import risk (no warranty, no local support) because the savings are large and the failure likelihood is low
- Items exempt/lightly taxed (books, some clothing under limits) where the duty is negligible

## 4. Rules before recommending an import

- Always show **landed cost vs local effective price** (local effective price from `finance.md` — discount + card + cashback applied), never sticker vs sticker
- Flag **BIS-restricted** categories and the **grey-import warranty** in the verdict
- Add the realistic **lead time** (courier vs postal) and return-friction: returning a failed import usually costs more than the product
- Payment method matters — international fees and the card's forex markup change the final ₹; cite the card's forex rate if known

## 5. Boundaries

- Customs rates/thresholds change; always verify current duty % for the specific category and the current ₹ threshold
- The skill computes and compares — it cannot guarantee clearance, final duty, or delivery

## 6. Related

- `finance.md` — effective-price math for the local comparison
- `claims.md` — what happens if an import breaks (often no Indian warranty path)
- `india.md` — platform map; BIS-scam safety notes for the Indian market
