# Record & Recall — the tracker half

Tracking only pays off if the record can be **read back later**. This playbook covers both halves:
**Record** writes one row per purchase; **Recall** answers later *"status of X?"* questions **from that row — without re-researching the product**. It is the other half of `tracker.md` (schema + pipeline) and is referenced by `claims.md`, `emi.md`, and `repairs.md` for their shared status words.

## Why this exists

- A deal's worth isn't proven until it's used, and its claim/EMI/repair lifecycle runs for months after the verdict.
- Web/cloud agents **can't write skill files** and often can't write any file; chat history resets between chats.
- So the **portable truth is the user's own merged `my-deals.csv`** (one row per purchase: deal + claim + EMI + repair) plus the AI platform's memory. The skill's `assets/*.csv` are **read-only templates** the user copies once.

## Record — one row per purchase

1. Save to the config-driven route (MCP / PC vault path / workspace / chat) per `environment.md` — don't re-ask "where to save?" every hunt (see SKILL.md "Saving Results").
2. **Vault/local agents:** append a row to the user's tracker note (`tracker.md` schema) or their own `my-deals.csv`. One row per purchase; link the note where detail lives.
3. **Web/cloud agents (can't write files):** output the row as a **copy-paste block** (a CSV row or a markdown table line) and tell the user which file to paste it into. **Never claim it was saved.**
4. **Merged schema (everything in one file):** `assets/my-deals.csv` — deal + claim + EMI + repair columns on one row, so recall has the full lifecycle without cross-filing. Per-domain alternatives (same data, split): `assets/deal-tracker.csv`, `assets/emi-tracker.csv`, `assets/repairs.csv`.
5. The skill's own files are never write targets.

## Recall — answer from the record

**Triggers:** *"what's the status of X?"*, *"where is my claim?"*, *"any EMI running?"*, *"what did I pay for Y?"* → this is a **recall job: read the record, don't re-research**.

1. **Source, in order:**
   1. The vault tracker/note (local users).
   2. The AI platform's memory — same project/thread (web users; the platform remembers its own past answers). If the record may have changed since, ask before trusting a stale answer.
   3. The user's attached `my-deals.csv` — any fresh chat where they attach the file.
2. **Answer always shows:** product, date, effective price, **current status**, **where it's recorded** (file/row/note), and **next action** (e.g. *"claim open — if the brand ignores >7 days, escalate to NCH 1915"*; *"EMI active, 4 of 12 paid, due date the 5th"*). Include the **satisfaction rating** when one is recorded.
3. **Standard status words** (one word, one meaning — see table below). If the record uses a different word, normalize it to the canonical one.
4. **Not tracked yet?** Say *"not found — record it now?"* and emit the row to add. Never make the user dig through their own notes.

## Status vocabulary (canonical)

| Domain | Status | Meaning / typical next action |
|---|---|---|
| Deal | `noted` | Researched, decision pending. Next: worthiness verdict |
| Deal | `waiting` | Queued — counts as **future spend** in the pipeline (see `tracker.md`). Next: sale trigger + price alert |
| Deal | `buying` | In-flight (ordered, not delivered). Next: delivery/installation check |
| Deal | `bought` | Purchased. Next: post-purchase review (satisfaction, claims path if broken) |
| Deal | `skipped` | Rejected *before* purchase (bad value / alternative won / don't-buy). Done |
| Deal | `cancelled` | Order placed, then cancelled. Done — confirm the refund landed |
| Claim | `open` | Filed, in progress. Next: chase at brand's promised SLA; escalate >7-14 days |
| Claim | `approved` | Approved. Next: confirm refund/replacement timeline |
| Claim | `rejected` | Denied. Next: escalation path (brand → NCH 1915 → e-Daakhil, see `claims.md`) |
| Claim | `refund-issued` | Money back confirmed. Done |
| Claim | `escalated` | Moved up the escalation chain. Next: track consumer-forum case |
| EMI | `active` | Still paying. Next: monthly due date, remaining obligation |
| EMI | `closed` | Fully paid. Done |
| EMI | `early-closed` | Closed early (foreclosure/penalty noted). Done |
| Repair | `done` | Repaired, paid, resolved. Next: satisfaction/duration note |
| Repair | `warranty` | Repaired under warranty (covered). Next: keep invoice for the rest of warranty |
| Repair | `oow` | Out of warranty (paid OOP). Next: repair-vs-replace verdict (see `repairs.md`) |

## Export

Export **any format on request**: the whole record as `my-deals.csv`, a markdown table, or a note — whatever the user wants. If the user's record may have changed since it was recorded, ask before exporting a stale copy.
