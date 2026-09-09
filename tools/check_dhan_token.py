#!/usr/bin/env python3
"""Dhan token health check (SECTION 7 — health diagnostics).

Run:
    python tools/check_dhan_token.py           # human-readable
    python tools/check_dhan_token.py --json    # machine-readable JSON

Checks:
  1. Token file exists at secrets/dhan_token.json.
  2. File has correct permissions (600).
  3. JSON is well-formed with required fields.
  4. access_token is non-empty.
  5. Token has not expired (expires_at is in the future).
  6. Token age (time since obtained_at) is reported.

Exit codes:
  0 — token is present, valid, and not expired
  1 — token is missing, malformed, or expired (action required)
"""

import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.security.token_loader import token_health, TOKEN_FILE


def _file_permissions_ok() -> tuple[bool, str]:
    """Return (ok, message) for file permission check."""
    if not TOKEN_FILE.exists():
        return False, f"File does not exist: {TOKEN_FILE}"
    mode = TOKEN_FILE.stat().st_mode & 0o777
    if mode != 0o600:
        return False, f"Permissions are {oct(mode)} — should be 600. Fix: chmod 600 {TOKEN_FILE}"
    return True, f"Permissions OK (600): {TOKEN_FILE}"


def main() -> int:
    as_json = "--json" in sys.argv

    perm_ok, perm_msg = _file_permissions_ok()
    health = token_health()

    result = {
        "token_file": str(TOKEN_FILE),
        "permissions_ok": perm_ok,
        "permissions_msg": perm_msg,
        "token_ok": health["ok"],
        "token_msg": health["message"],
        "expires_at": health["expires_at"],
        "ttl_hours": health["ttl_hours"],
        "age_hours": health["age_hours"],
        "overall_ok": perm_ok and health["ok"],
    }

    if as_json:
        print(json.dumps(result, indent=2))
        return 0 if result["overall_ok"] else 1

    # Human-readable output.
    status = "OK" if result["overall_ok"] else "FAIL"
    print(f"[{status}] Dhan token health check")
    print(f"  file:         {result['token_file']}")
    print(f"  permissions:  {'OK' if perm_ok else 'FAIL'} — {perm_msg}")
    print(f"  token:        {'OK' if health['ok'] else 'FAIL'} — {health['message']}")
    if health["expires_at"]:
        print(f"  expires_at:   {health['expires_at']}")
    if health["ttl_hours"] is not None:
        print(f"  ttl_hours:    {health['ttl_hours']:.1f}h remaining")
    if health["age_hours"] is not None:
        print(f"  age_hours:    {health['age_hours']:.1f}h since last refresh")

    if not result["overall_ok"]:
        print()
        print("ACTION REQUIRED: run  python scripts/generate_dhan_token.py")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
