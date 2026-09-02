# Repair Tracking & Repair-vs-Replace

Load this file when a user's device **breaks, needs a repair, or arrives broken** — or when a device's repair history would change a buying decision ("this brand's screen died on me twice — don't rebuy"). It turns scattered repair facts into one readable ledger, then answers the question the user actually cares about: *"fix it, replace it, or do nothing?"*

> [!important] The core question
> When a device breaks, don't just fix it on reflex. Run **repair-vs-replace**:
> **repair cost vs the device's remaining value vs a replacement's effective price — plus "does the repaired device still meet the need?"**
> A repair is only worth it if it restores the need for less than the alternative — and every repair is logged, warranty-covered or not, because repair history is durability truth.

## 1. Where the repair data lives (two record layers)

The skill works for vault users and non-vault users alike — same schema, two ships:

- **Vault users (rich, linked):** a rollup ledger (e.g. a `Repair Tracker` note) — one flat row per repair + a summary block (total OOP spend, open claims). The per-device detail tables (e.g. the user's devices note → Repairs) hold the fine-grained record; each ledger row links to its device row.
- **Everyone (portable, zero-setup):** the skill's CSV template `assets/repairs.csv` (read-only template — the user copies it to keep their own record). The user's actual repair record lives at the config-driven route from `environment.md` (vault `Trackers/repair_file` via MCP or this machine's `vault_paths`, else the workspace `.agents/deal-hunter/workspace/`); with no write access, output the repair row as a copy-paste block. This is the record for users without Obsidian.

If no ledger exists, ask the user for the repair facts (date, device, issue, cost, warranty-covered?, claim status) and offer to create one — store it at the config-driven route from `environment.md`, never in the skill's files (no write access → copy-paste block).

## 2. Ledger schema

`Date | Device | Issue | Cause | Cost | Warranty-covered? | Claim status | Paid by | Outcome | → Device link`

- **Cause** — `drop` / `defect` / `wear` / `user` (what actually caused it — drives whether a claim was ever realistic)
- **Warranty-covered?** — `Yes` / `No` / `Partial` / `N/A` (e.g. self-sourced part)
- **Claim status** — `none` / `open` / `approved` / `rejected` / `refund-issued` / `escalated` (the canonical claim words from `recall.md`; `none` = no claim was ever filed)
- **Paid by** — `OOP` / `warranty` / `insurance`
- **Outcome** — one line: what happened after the repair (healthy / still broken / escalated / replaced)
- **Repair status (canonical, for recall answers)** — `done` / `warranty` (covered fix) / `oow` (out of warranty, paid OOP); maps from Paid by + Outcome. See `recall.md`.
- Summary block (top of ledger): **total OOP repair spend**, **open warranty claims**, **last updated**

## 3. How repairs feed the loop

- **Post-purchase review (satisfaction):** a device that broke and needed an OOP repair changes the "worth it after extended use?" verdict — the value score must include what it cost to keep working (`tracker.md`).
- **Claims path (`claims.md`):** a broken device is the moment to use the warranty. Log the claim outcome: a **successful claim** proves the warranty was part of the deal; a **denied claim** (fair or not) becomes an OOP repair — record it as such.
- **Value-score calibration:** repair history is the strongest durability signal for the *next* buy of the same brand/category. Two expensive OOP repairs on brand X's screen = don't rebuy brand X, no matter the deal.
- **Pipeline:** an OOP repair is money already out. When a repair-vs-replace says "replace", that replacement is a **new hunt** — it enters the pipeline total (out + queued + EMI remaining + new) like any purchase.

## 4. Repair-vs-replace (the verdict)

The worthiness gate applied to fixing. When a device breaks:

```
repair cost          = the quote/estimate (OOP; a warranty-covered repair is ~₹0 and wins by default)
remaining value      = what the device sells for used in working order (or is worth to the user)
replacement cost     = effective price of the best replacement (run a hunt — don't guess)
need                 = does the repaired device still meet the original need? (specs/condition/age)
```

**Get a real quote first.** ASC quotes run high — for out-of-warranty devices, price a reputable third-party repair shop as the comparison point before recommending replacement. Trade-off to state plainly: third-party repair can void any remaining warranty, so it's only the right call when the warranty is already gone or the saving dwarfs the remaining coverage.

| Condition | Verdict | What to tell the user |
|---|---|---|
| Warranty covers the fix | **Repair now (free)** | Use the claim first — the warranty is part of the deal (`claims.md`). Log the repair with Paid by = warranty. |
| `repair cost ≤ ~50% of replacement cost` AND the repaired device still meets the need | **Repair** | Fix it; the money saved vs replacing funds the next upgrade instead. Log it OOP. |
| `repair cost > ~50% of replacement cost`, or repair is recurring (same fault 2+ times), or the device no longer meets the need | **Replace** | It's a new hunt — worthiness gate first, then the full deal-hunter loop. Log the failed repair as the reason. |
| Repair cost high AND replacement isn't affordable/needed | **Do nothing / defer** | Keep it, don't spend ₹5,000 on a ₹2,000-value device. Log the decision. |

Always show the numbers: **repair cost, remaining value, replacement effective price**. A repair that costs more than the device is worth is usually a "no" — unless the device genuinely can't be replaced for a sane price.

Worked example: a refurb phone (bought ~₹30k, ~1.5 yrs old, used resale ~₹18k) needs a ₹6,000 display. Replacement refurb ≈ ₹28k effective. 50% of replacement ≈ ₹14k → ₹6,000 repair is ≤ 50% → **Repair** (and the ₹6,000 is far less than a new EMI). A ₹2,500 battery on a ₹3,000 used phone that no longer gets updates → **do nothing** unless the phone still does the job.

## 5. Pipeline integration

A repair is either zero-cost (warranty) or an OOP outflow. When repair-vs-replace says **replace**, the replacement joins the pipeline total:

```
Pipeline total = ₹ out (spent, incl. OOP repairs)
               + ₹ queued (waiting/noted-Buy, see tracker.md)
               + ₹ active-EMI remaining (see emi.md)
               + ₹ new replacement
```

Surface this on any replacement purchase (JOB 7) before deciding. Informational — never silently block.

## 6. Repair hygiene rules

- **Log every repair, warranty-covered or not** — a claim that succeeds is evidence the warranty was worth it; a denied one is evidence about the brand.
- **Record at the moment it happens** — a stale ledger produces wrong repair-vs-replace calls and wrong value scores.
- **Cause matters** — a `drop` denial is fair; a `defect` denial is a real signal. Record the cause honestly.
- **Ask before writing** — chat, ledger note, CSV, or the user's file. Never assume a destination.
- **Repair history feeds the next buy** — before recommending any brand that the user has repaired before, check the ledger.

## 7. Output

For any broken/repaired device:

```
## Repair log
- Device | Issue | Cost | Warranty-covered? | Claim status | Paid by | Outcome
- Total OOP repair spend: ₹X | Open claims: N

## Repair-vs-replace
- Repair: ₹R | Remaining value: ₹V | Replacement (effective): ₹P | Still meets need? yes/no
- Verdict: Repair (free/paid) / Replace (new hunt) / Do nothing
- What to do: [one concrete action]
```

## 8. Boundaries

- The skill prepares the evidence and gives the verdict — it does not book repairs, file claims, or guarantee any repair outcome.
- Repair cost must come from a real quote/invoice, not a guess — flag estimates as estimates.
- Warranty terms vary by brand and listing — always verify the specific product's terms before promising a covered fix.

## 9. Related

- `claims.md` — the claims path (warranty → NCH → e-Daakhil) and where claim outcomes get logged
- `recall.md` — canonical repair status words (`done` / `warranty` / `oow`) + how to answer later "what's the repair status?" questions
- `tracker.md` — post-purchase review / satisfaction; pipeline-aware budget rule
- `emi.md` — why a replacement might mean a new EMI (repair-vs-replace matters most then)
- `finance.md` — effective-price math for the replacement side
