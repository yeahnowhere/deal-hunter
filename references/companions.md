# Complementary Products — Reasoning Guide

> Load at verdict time. The AI uses this guide to decide whether the product being hunted needs an essential companion to function properly or achieve the user's goal.

## When to check

After the verdict is decided, before recording. Ask: **"Does this product need something else to work properly, or for the user's goal to actually be achieved?"**

If yes → surface the companion. If no → move on.

## Essential vs optional

**Essential** — the product fails or causes harm without it:
- Facewash without moisturizer → skin barrier damage
- Laptop without a bag → damage during transit
- GPU that draws 200W with a 300W PSU → system instability
- Pressure cooker without a gasket → won't seal
- Fountain pen without ink → useless

**Optional** — nice to have, but the product works fine without it:
- Headphones without a carrying case → works, less protected
- Phone case (debatable — most would say essential, but the phone functions without it)
- Laptop sleeve → protection, not function
- Extra charger → convenience, not necessity

**Rule of thumb:** if skipping the companion causes damage, failure, or defeats the purpose of the purchase → essential. If it just means less convenience → optional. When in doubt, surface it but mark as "recommended, not essential."

## How to surface

At verdict time, after the main recommendation:

```
## Complementary products
- **[Companion name]** — [one-line reason why it's essential]. Want me to find the best-value pick?
```

- One line per companion. Max 2 companions.
- Never auto-hunt. Always ask first.
- If the user already mentioned owning the companion, skip it.
- If the companion is trivially obvious and cheap (e.g. batteries included in the box), skip it.

## Category examples (learn the pattern, don't memorize)

| Product | Companion | Why essential |
|---------|-----------|---------------|
| Facewash | Moisturizer | Facewash strips natural oils; skipping it damages the skin barrier |
| Sunscreen | Moisturizer (if not in routine) | SPF alone doesn't hydrate; dry skin + sun = worse damage |
| Laptop | Laptop bag/sleeve | Transit damage risk; most laptops don't survive drops |
| Phone | Tempered glass + case | Screen repair costs 30-50% of phone price |
| GPU (high-power) | PSU check / upgrade | Insufficient PSU = crashes, data loss, fire risk |
| Blender/mixer | Spare jar + cleaning brush | Wear parts; jar cracks after ~2 years of daily use |
| Pressure cooker | Gasket + safety valve | Without gasket it won't seal; without valve it's dangerous |
| Fountain pen | Ink cartridge/bottle | Pen is useless without ink |
| Printer | Extra cartridge | First cartridge runs out fast; running out mid-print is common |
| Yoga mat | Blocks + strap | Mat alone limits most poses; blocks are foundational |
| Formal shoes | Shoe polish + conditioner | Leather cracks without care; shortens lifespan significantly |
| Air fryer | Parchment paper + accessories | Without accessories, most air fryer recipes don't work well |

## What NOT to do

- Don't surface a companion the user already owns (check if they mentioned it).
- Don't surface optional accessories as essential.
- Don't auto-hunt the companion — just flag it and ask.
- Don't surface more than 2 companions per product.
- Don't treat brand-specific bundles as companions (e.g. "buy our case too" upsell).
