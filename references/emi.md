# EMI Tracking & Purchase Readiness

Load this file for **any financed purchase** (EMI / no-cost EMI / split payment) or **any new purchase while EMIs are active** — it is the engine behind the **EMI-readiness check** (JOB 9) and Step 5's affordability layer. It turns a scattered EMI record into one readable ledger, then answers the question the user actually cares about: *"am I ready for this purchase, given what I already owe?"*

> [!important] The core question
> Before any financed purchase — or any purchase while EMIs are active — compute:
> **committed (Σ monthly EMI on active EMIs) + new purchase's monthly cost vs the user's monthly EMI ceiling**
> and give a verdict: **Ready / Almost (get ready) / Not ready**. Never recommend financing without running this.

## 1. Where the EMI data lives

Two layers — read the **ledger**, link to the **detail**:

- **Ledger (read this):** the user's active-EMI registry (e.g. an `EMI Tracker` note) — one flat row per active EMI + a summary block. This is what you load on every purchase.
- **Detail (link, don't copy):** the user's per-device record (e.g. their devices note → EMI Schedule) holds the fine-grained installment tables (disbursement, per-instalment principal, due dates). Each ledger row links to its schedule.

If no ledger exists, ask the user for their active EMIs (product, financier, principal, monthly EMI, tenure left, due date) and offer to create one — store it at the config-driven route from `environment.md` (the vault `Trackers/emi_file` via MCP or this machine's `vault_paths`, else the workspace), not in the skill's files; if no write access, output a copy-paste block.

## 2. Ledger schema

`Date | Product | Financier | Principal | Monthly EMI | Tenure | Started | Remaining (mo) | Paid | Remaining obligation | Interest | Due date | Early-closure penalty | Status | → Schedule`

- **Monthly EMI** — exact figure from the statement when available; estimate = principal ÷ tenure until then (flag as estimate)
- **Remaining obligation** — principal still owed (Σ of unpaid instalments); this is **committed future spend**
- **Interest** — e.g. `0% (no-cost)`, `15% p.a.`; also note processing/convenience fees
- **Early-closure penalty** — fetch the actual figure from the financier's statement/loan agreement before ever recommending closure; never estimate it
- **Status** — `active` / `closed` / `early-closed` (canonical EMI words in `recall.md`); keep closed rows as history
- Summary block (top of ledger): **monthly EMI ceiling**, **total monthly committed**, **remaining obligation**, **last updated**

The user-defined **monthly EMI ceiling** is the budget line — store it in the ledger once, reuse it on every check.

## 3. The readiness check (the verdict)

```
committed    = Σ monthly EMI of active ledger rows
remaining    = Σ remaining obligation of active ledger rows
ceiling      = user's monthly EMI budget (from the ledger; if unset, ask once)
headroom     = ceiling − committed
new monthly  = the new purchase's monthly EMI (or one-time cost if cash)
```

Then the verdict:

| Condition | Verdict | What to tell the user |
|---|---|---|
| `committed + new monthly ≤ ceiling` (comfortably, ≥ ~10% headroom) | **Ready** | Buy can be financed; shortest tenure that fits. |
| `committed + new monthly ≤ ceiling` but tight (< ~10% headroom), or only fits via a longer tenure / bigger down payment | **Almost — get ready** | Name exactly what frees room: wait 1–2 months for a current EMI to close (headroom grows), take a shorter/longer tenure that fits the ceiling, raise the down payment, or close a high-interest EMI first if the closure penalty < the interest saved. |
| `committed + new monthly > ceiling` | **Not ready** | Defer/skip unless a cash payoff opens room, or drop the target price so the monthly fits. Show the shortfall. |

Always show the numbers: **ceiling, committed, new, headroom** — the verdict without the math is useless.

Worked example: committed ₹2,500/mo, ceiling ₹5,000/mo → headroom ₹2,500/mo. A new ₹1,700/mo EMI → ₹4,200 ≤ ₹5,000 → **Ready** (with ~16% headroom). A new ₹3,000/mo EMI → ₹5,500 > ₹5,000 → **Not ready** (shortfall ₹500/mo; or wait until the ₹2,500 EMI closes → fully ready).

## 4. Pipeline integration

An active EMI's **remaining obligation** is committed future spend, not "already bought":

```
Pipeline total = ₹ out (spent)
               + ₹ queued (waiting/noted-Buy, see tracker.md)
               + ₹ active-EMI remaining obligation
               + ₹ new
```

Surface this on any new purchase (JOB 7) before deciding. Informational — never silently block.

## 5. EMI hygiene rules

- **Keep 0% / no-cost EMIs** (they cost only the processing fee + GST on waived interest) — don't early-close them.
- **Consider closing high-interest EMIs early** only when the closure penalty < the interest remaining to be saved.
- **Re-verify no-cost claims** — processing fee + GST on the waived interest are real costs (see `finance.md` §3).
- **Monthly ritual:** when statements arrive, update monthly EMI / remaining months / due dates, mark closed EMIs, and fill pending breakups (a ledger with stale numbers produces wrong readiness verdicts).
- **Keep the auto-debit funded** — a missed NACH/bank debit means bounce fees plus a credit-bureau hit; confirm the mandate account has balance before each due date.
- **Credit-bureau reality** — every EMI/pay-later line is bureau-reported (CIBIL etc.); clean repayment builds the score, while misses and over-extension hurt future loan eligibility. Mention this when the readiness verdict is Almost/Not ready.

## 6. Output

For any financed purchase (or any purchase while EMIs are active):

```
## EMI readiness
- Ceiling (monthly): ₹X | Committed: ₹Y/mo | New: ₹Z/mo | Headroom: ₹(X−Y) → after new: ₹(X−Y−Z)
- Verdict: Ready / Almost (get ready) / Not ready
- What to do: [exactly one concrete action]
- Remaining obligation ₹E counted in the pipeline total (JOB 7)
```

## 7. Boundaries

- The skill inventories and recommends — it does not sanction loans, run credit checks, or move money; EMI eligibility is the bank's call.
- Monthly EMI figures come from the user's statements; estimates are flagged and must be confirmed.
- The ceiling is user-defined — never invent one; ask and store it in the ledger.

## 8. Related

- `finance.md` — effective-price formula, no-cost-EMI reality check, affordability depth (§6)
- `tracker.md` — the pipeline-aware budget rule (queued + EMI remaining = future spend)
- `recall.md` — canonical EMI status words (`active` / `closed` / `early-closed`) + how to answer later "any EMI running?" questions
- `subscriptions.md` — the recurring-spend audit (EMIs are the recurring-spend cousin)
