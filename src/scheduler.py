"""Continuous / cycle-independent process (IMP-001 Section 5.4).

Runs MOD-06 detectors (CAP-19, CAP-23, CAP-24, CAP-27, CAP-31) on a fixed
interval, independent of cycle activation (INV-14) -- never paused by any
halt state (GOV-01). Also realizes:
  - Mode 1 (scheduled activation): triggers an on-demand cycle every
    `--cycle-every` detector passes.
  - Mode 3 (event-driven activation): when a detector reports a state
    transition, calls MOD-11 activate(mode="event_driven", ...) and runs a
    cycle in-process (the bounded MOD-06 -> MOD-11 signal, ADR-007 Section
    8.1) -- a direct function call carrying only (event_type, cycle_trigger).
"""

import argparse
import signal
import sys
import time

from src import config
from src.persistence import db
from src.mod06_governance import run_detectors
from src.main import run_cycle

_shutdown = False


def _handle_signal(signum, frame):
    global _shutdown
    _shutdown = True


def _has_transition(detector_result: dict) -> bool:
    return any(
        section.get("transition") is not None
        for section in detector_result.values()
        if isinstance(section, dict)
    )


def loop(interval_seconds: float, cycle_every: int, once: bool = False) -> None:
    signal.signal(signal.SIGTERM, _handle_signal)
    signal.signal(signal.SIGINT, _handle_signal)

    cfg = config.load_config()
    print(config.diagnostics(cfg))

    db.init()

    pass_count = 0
    while not _shutdown:
        pass_count += 1
        result = run_detectors(cycle_id=None)
        print(f"[scheduler] pass {pass_count}: {result}")

        if _has_transition(result):
            print("[scheduler] governance transition detected -> event-driven cycle (Mode 3)")
            run_cycle(mode="event_driven", trigger="governance_signal")

        if cycle_every > 0 and pass_count % cycle_every == 0:
            print("[scheduler] scheduled cycle (Mode 1)")
            run_cycle(mode="scheduled", trigger="schedule")

        if once:
            break

        time.sleep(interval_seconds)

    print("[scheduler] shutdown complete")


def main() -> None:
    parser = argparse.ArgumentParser(description="Continuous governance detector loop")
    parser.add_argument("--interval", type=float, default=5.0, help="seconds between detector passes")
    parser.add_argument("--cycle-every", type=int, default=0, help="run a scheduled cycle every N passes (0 = never)")
    parser.add_argument("--once", action="store_true", help="run a single pass and exit")
    args = parser.parse_args()

    loop(interval_seconds=args.interval, cycle_every=args.cycle_every, once=args.once)


if __name__ == "__main__":
    main()
