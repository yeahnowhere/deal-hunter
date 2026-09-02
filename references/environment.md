# Agent Environment & Storage

Load this file at the start of any session, before answering "where should I save?" or recording a hunt result. It replaces the old *"always ask where to save, default is chat output"* rule with an **environment-aware** model: detect where you're running, read the one-time config, and save to the right place automatically.

**Why:** an Obsidian user may reach the same vault from multiple devices, and the vault's absolute filesystem path can differ per device. A config with one hardcoded path breaks everywhere else. The fix: **prefer MCP** (vault-relative paths, identical on any device) and keep **per-machine** paths only for direct local access.

## Step 0 — Resolve the config (run the script, don't read prose)

Run **`scripts/resolve-config.py`** — it returns the config file path (or exits non-zero if none exists). **The script output is authoritative**; this doc is human documentation only. Lookup it performs:

1. `~/.agents/deal-hunter/config.json` — the canonical per-user home (survives any launch directory).
2. `$PWD/deal-hunter.config.json` — convenience copy, if present.

If nothing resolves, ask once to create the config — either run `scripts/resolve-config.py --init`, or copy `scripts/config.example.json` to `~/.agents/deal-hunter/config.json` — then it's deterministic forever.

## The environment probe (run in this order, don't ask the user)

1. **Obsidian MCP connected?** (e.g. an `*_mcp` server with `read_note`/`create_note`/`append_note`/`list_folder` tools taking vault-relative paths) → **MCP route**. Auto-selected — no config needed. Works on any synced device.
2. **No MCP, but a `storage.vault_paths` entry resolves on THIS machine?** → **PC/local route**.
3. **Can write to a working directory (web/workspace or non-Obsidian CLI)?** → **Workspace route**.
4. **Cannot write files at all?** → **Chat route** (copy-paste block).

State the detected route briefly to the user (one line), then store there. Only ask to create the config when genuinely ambiguous, and only once.

## The three storage routes

| # | Route | That's you if… | Store at |
|---|-------|----------------|----------|
| 1 | **MCP** | an Obsidian MCP server is connected (same vault, any device) | vault-relative: `Trackers/<file>` → `Journal/<product>.md` |
| 2 | **PC/local** | you have direct filesystem access to the vault on this machine, no MCP | `<vault_paths[this machine]>/Trackers/` + `Journal/` |
| 3 | **Workspace** | web/workspace user, or non-Obsidian CLI user | `.agents/deal-hunter/workspace/` |
| 4 | **Chat** | no file write access at all | copy-paste row (see `recall.md`) |

Routes 1 and 2 reach the **same actual tracker files** — one source of truth across devices.

## Vault targets (vault-relative, same everywhere)

- **Trackers** → `<vault>/Trackers/`
  - `Deal Tracker.md`, `EMI Tracker.md`, `Claim Tracker.md`, `Repair Tracker.md`
  - `my-deals.csv` (consolidated merged record — deal + claim + EMI + repair, one row per purchase)
- **Individual hunt notes** → `<vault>/Journal/<product>.md` (`notes_dir = Journal`; Digital Clippings are not required)

## Workspace layout (Route 3)

```
.agents/deal-hunter/workspace/
  Deal Tracker.md
  EMI Tracker.md
  Claim Tracker.md
  Repair Tracker.md
  my-deals.csv
  _notes/<product>.md
```

**Path resolution:** use the user-home default (`C:\Users\<you>\.agents\deal-hunter\workspace`) unless `storage.workspace.dir` or a web workspace sets it explicitly.

## Config schema — `deal-hunter.config.json`

One-time user config under the user's data home (user data — never a skill file, never deployed in the skill zip). Schema (paths are per-machine examples — replace `<you>`):

```json
{
  "storage": {
    "prefer_mcp": true,
    "fallback": "pc",
    "vault_paths": {
      "pc":     "C:\\Users\\<you>\\Obsidian\\Vault"
    },
    "mcp": {
      "tracker_dir": "Trackers",
      "notes_dir":   "Journal"
    },
    "workspace": {
      "dir": "C:\\Users\\<you>\\.agents\\deal-hunter\\workspace"
    }
  },
  "tracker_file": "Deal Tracker.md",
  "emi_file":     "EMI Tracker.md",
  "claim_file":   "Claim Tracker.md",
  "repair_file":  "Repair Tracker.md",
  "csv_file":     "my-deals.csv"
}
```

| Field | Meaning |
|-------|---------|
| `storage.prefer_mcp` | Auto-use MCP whenever an Obsidian MCP is connected (default `true`). |
| `storage.fallback` | Route when no MCP: `pc` (use `vault_paths`) or `workspace`. |
| `storage.vault_paths` | **Per-machine** absolute paths. Use whichever key resolves on the current machine (e.g. `pc`, a device name you choose). |
| `storage.mcp.tracker_dir` | Vault-relative folder for trackers (default `Trackers`). |
| `storage.mcp.notes_dir` | Vault-relative folder for individual notes (default `Journal`). |
| `storage.workspace.dir` | Workspace/portable record location. |
| `tracker_file`/`emi_file`/`claim_file`/`repair_file` | Canonical tracker filenames (schema in `tracker.md`). |
| `csv_file` | Consolidated merged record filename (`my-deals.csv`). |

## Rules

- **Prefer MCP when connected** — it's device-independent and the user's stated preference. Config-gating MCP off is never needed unless the user says so.
- **Config is optional for MCP users** — the vault-relative `tracker_dir`/`notes_dir` have defaults (`Trackers`, `Journal`).
- **Config is never shipped with the skill** — it's user data in their working directory.
- **An explicit user instruction ("save this to X") always overrides the config.**
- **The skill's `assets/*.csv` are read-only templates** the user copies once into their chosen storage — never write targets.
- **On first run with no config:** state the detected route; if ambiguous, ask once to create the config, then it's deterministic. Never re-ask every hunt.

## Pairings

- `tracker.md` — row schema + pipeline (what a tracker row holds).
- `recall.md` — read-back source order (MCP `Trackers/` → `vault_paths` `Trackers/` → workspace → attached CSV → chat) and the copy-paste fallback.
