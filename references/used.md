# Used & Refurb Verification Playbook

Load this file for **any used/refurb candidate** (used GPU/RAM/phone/laptop, "renewed", second-hand marketplaces). Used is a **separate tier** — the price is lower because the risk is higher, so it needs its own verification, not the new-product checklist.

> [!important] Used ≠ new
> A used part has no platform-grade warranty, no return policy (usually), and a prior owner. The deal only exists if the **on-spot test** passes and the **warranty reality** is known before payment. If the seller refuses to let you test, the answer is no.

## 1. Where the Indian used market lives

- **TechEnclave buy-sell** — serious hardware forum; check user join-date, heat score, and deal threads before wiring money
- **r/IndianGaming bazaar/market threads** — search `market` / `bazaar`; private sellers, cash-on-delivery preferred
- **Gamer's Loot** — established gaming-hardware reseller; still verify the specific listing
- **ZedUpgrade** — Apple/Mac refurb specialist; confirm grading + warranty terms
- **Flipkart/Amazon "renewed", Cashify refurb & official refurb stores** — platform-backed (7-day return) = safer than private sales, but warranty is usually the **refurbisher's**, not the brand's
- **Olx / Facebook Marketplace** — highest scam surface; meet in person, test on the spot, never prepay

## 2. On-spot test plan (per category)

### GPU
- Visual: card looks original (no re-sticker, no BIOS-flashed PCB), no obvious reball/repair marks
- Bench: run a benchmark (e.g. FurMark/Unigine) for 15–30 min — stability + temps; VRAM test for artifacting
- Check the serial against the brand's warranty portal (if warranty is claimed as "remaining")
- Mining history is the killer — cards that ran 24/7 mining die early (see signals below)

### RAM
- MemTest86 for at least a full pass; run at the rated speed/XMP profile (RAM sold with a dead XMP bin is a common used-India trap)
- Check the label/serial for warranty transfer eligibility

### Phone
- IMEI blacklist check — **CEIR (ceir.gov.in)** for the government stolen/blocked registry + the brand's own portal (stolen/blocked devices are unsellable)
- Battery health % and whether the battery is replaceable + cost
- Test: earpiece, mics, speakers, camera, charging, SIM slots, Wi-Fi/BT, screen for burn-in
- Hidden-config check: paid diagnostic apps (e.g. Hidden Test) for the real state

### Laptop
- Boot + battery report (`powercfg /batteryreport` on Windows), check wear %
- Test keyboard, trackpad, ports, hinge, webcam, display dead pixels
- Verify the serial/warranty on the brand portal (many "warranty till 2027" claims are false)

### Console
- Test controllers on-site — stick drift is the #1 used-console fault
- Check account-ban status (online/multiplayer bans can bind the machine, not the seller); test HDMI output and the disc drive with an actual disc

### Watch / wearable
- Battery health + whether the battery is serviceable; pair to a phone on the spot (activation locks and region locks surface immediately)
- Screen burn-in, strap/lug cracks, sensor function

### Monitor / TV
- Full-screen dead-pixel + backlight-bleed test (solid white/red/green/blue slides); panel uniformity at low brightness
- Confirm ports carry the resolution/refresh you need (HDMI version matters)

### Audio (TWS / headphones)
- Battery degradation is the killer — test full-charge duration if possible; check charging-case contacts for corrosion
- Left-right balance, driver rattle at low volume

## 3. Red flags (walk away signals)

- **Mining card signals** — "used only for gaming, never mined" + dustless-to-perfection card, multiple identical GPUs from one seller, no original box
- **Stolen-device signals** — no invoice, no box, pressured "urgent, no questions", IMEI blacklisted, price absurdly below market
- **Seller patterns** — brand-new account, one listing, advance-payment-only, refuses on-spot testing, "no returns, as-is" + wants payment before you inspect
- **Remote-deal red flags** — refuses a live video call showing the device working, "courier will deliver, pay first", stock photos instead of real shots

**Inter-city/shipped deals:** transact only with long-term, verifiably established members (join date, heat score, post history), demand the live video proof **before** paying, and prefer COD where the platform supports it.
- **Warranty-transfer lies** — seller claims remaining warranty but the brand's portal shows it's non-transferable or expired; read owner reports, not the marketing line

## 4. Warranty-transfer reality

- Indian brands often treat warranties as **non-transferable** (or transfer only with the original invoice + brand approval) — verify on the brand's own portal with the serial
- "Renewed/refurb" warranty is the **refurbisher's**, typically 3–6 months, and often excludes batteries/accidental damage
- Private sales: no-return is the norm, so the **test before payment** IS the warranty

## 5. Pricing the risk

- A used item should cost meaningfully less than "new at next sale effective price" — if it doesn't, the new item wins (you get a full warranty + returns for ~10–15% more)
- Compare used price against the **effective price** of new (see `finance.md`), not the inflated MRP
- Factor in the test cost and any replacement parts (battery, PSU, cooler)

## 6. Related

- `community.md` — section 3b: used marketplaces; used-specific community signals
- `india.md` — scam safety for the Indian market
- `finance.md` — effective-price math for the new-vs-used comparison
- `tracker.md` — record the used candidate with its on-spot test result
