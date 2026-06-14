"""Human-only audit review CLI (IMP-001 Section 6.2/6.3).

Not importable by any src/modNN_* package -- the boundary test treats this
file's use of mod10_audit.review() as the only permitted call site.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.mod10_audit import audit
from src.mod10_audit.audit import GENESIS_HASH, _compute_hash


def verify_chain() -> bool:
    prev_hash = GENESIS_HASH
    ok = True
    count = 0
    for row in audit.review():
        count += 1
        payload = json.loads(row["payload_json"])
        expected = _compute_hash(
            prev_hash, row["module"], row["capability"], row["event_type"], payload, row["recorded_at"]
        )
        if expected != row["record_hash"] or row["prev_hash"] != prev_hash:
            print(f"INTEGRITY FAILURE at audit_log.id={row['id']}")
            ok = False
        prev_hash = row["record_hash"]

    if ok:
        print(f"OK: {count} audit record(s), chain verified.")
    return ok


def list_records() -> None:
    for row in audit.review():
        print(
            f"[{row['id']}] {row['recorded_at']} cycle={row['cycle_id']} "
            f"{row['module']}.{row['capability']} {row['event_type']} {row['payload_json']}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Human-only audit review")
    parser.add_argument("--verify-chain", action="store_true")
    args = parser.parse_args()

    if args.verify_chain:
        ok = verify_chain()
        sys.exit(0 if ok else 1)
    else:
        list_records()


if __name__ == "__main__":
    main()
