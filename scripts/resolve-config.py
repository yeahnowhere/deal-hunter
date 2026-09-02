#!/usr/bin/env python3
"""Resolve (or create) the deal-hunter config file path.

Deterministic lookup, run by the AI at the start of any session that needs
storage.

Usage:
  resolve-config.py          # print resolved config path (exit 0)
  resolve-config.py --init   # create a default config if none exists, then print path
                             # (--init never overwrites an existing config)

On success prints the config path to stdout, exit 0. On failure prints a short
message to stderr and exits 1.

Lookup order (first hit wins):
  1. Canonical home (per-user data dir, survives any launch directory):
        ~/.agents/deal-hunter/config.json
     On Windows: C:\\Users\\<you>\\.agents\\deal-hunter\\config.json
  2. CWD convenience copy:
        ./deal-hunter.config.json

The config is user data; it is never a skill file, never committed/deployed.
A fill-in template ships with this script at scripts/config.example.json.
"""

import json
import os
import sys
from pathlib import Path


DEFAULT_TEMPLATE = {
    "storage": {
        "prefer_mcp": True,
        "fallback": "pc",
        "vault_paths": {
            "pc": "C:\\Users\\<you>\\Obsidian\\Vault"
        },
        "mcp": {"tracker_dir": "Trackers", "notes_dir": "Journal"},
        "workspace": {"dir": str(Path.home() / ".agents" / "deal-hunter" / "workspace")},
    },
    "tracker_file": "Deal Tracker.md",
    "emi_file": "EMI Tracker.md",
    "claim_file": "Claim Tracker.md",
    "repair_file": "Repair Tracker.md",
    "csv_file": "my-deals.csv",
}


def canonical_home() -> Path:
    """The per-user data home. Honors DEAL_HUNTER_HOME override, else ~/.agents/deal-hunter."""
    override = os.environ.get("DEAL_HUNTER_HOME")
    if override:
        return Path(override)
    return Path.home() / ".agents" / "deal-hunter"


def lookup() -> Path | None:
    home_cfg = canonical_home() / "config.json"
    if home_cfg.is_file():
        return home_cfg

    cwd_cfg = Path.cwd() / "deal-hunter.config.json"
    if cwd_cfg.is_file():
        return cwd_cfg

    return None


def validate(path: Path) -> str | None:
    """Return an error string if the config is malformed, else None."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return f"config exists but is not valid JSON: {path} ({exc})"
    if not isinstance(data, dict) or "storage" not in data:
        return f"config missing required 'storage' section: {path}"
    return None


def init() -> Path:
    """Create a default config at the canonical home if none exists. Never overwrites."""
    target = canonical_home() / "config.json"
    if not target.is_file():
        canonical_home().mkdir(parents=True, exist_ok=True)
        with open(target, "w", encoding="utf-8") as fh:
            json.dump(DEFAULT_TEMPLATE, fh, indent=2)
            fh.write("\n")
    return target


def main(argv: list[str]) -> int:
    path = lookup()

    if "--init" in argv:
        target = init()
        err = validate(target)
        if err:
            print(err, file=sys.stderr)
            return 1
        existing = path is not None
        created = " (created)" if not existing else " (already exists, left unchanged)"
        print(f"{target}{created}")
        return 0

    if path is None:
        home = canonical_home()
        print(
            "no deal-hunter config found. "
            f"create one with `resolve-config.py --init` or at {home / 'config.json'} "
            "(template: scripts/config.example.json).",
            file=sys.stderr,
        )
        return 1

    err = validate(path)
    if err:
        print(err, file=sys.stderr)
        return 1

    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
