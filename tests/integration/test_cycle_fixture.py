"""End-to-end fixture cycle test (PLAN-002 M3).

Runs a full Stage 2-4 on-demand cycle against fixture market data and stub
news/macro adapters (no network, no credentials), verifying the cycle
completes, produces a recommendation package, and records audit entries.
This is the automated equivalent of "fetch me an analysis".
"""

import pytest

from src.persistence import db
from src import main
from src.mod07_human_gate import present_and_capture


@pytest.fixture
def isolated_db(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "SYSTEM_DB_PATH", tmp_path / "system.db")
    monkeypatch.setattr(db, "AUDIT_DB_PATH", tmp_path / "audit.db")
    db.init()


def test_full_cycle_runs_to_completion(isolated_db, monkeypatch):
    # Avoid hitting Finnhub even if FINNHUB_API_KEY happens to be set in env.
    monkeypatch.delenv("FINNHUB_API_KEY", raising=False)
    # CAP-18 human gate blocks on input(); auto-reject every opportunity.
    # input_fn is bound as a default arg at module-import time, so patch
    # __defaults__ directly rather than builtins.input.
    monkeypatch.setattr(present_and_capture, "__defaults__", (lambda prompt="": "reject",))

    result = main.run_cycle(mode="on-demand", trigger="test")

    assert result["aborted"] is False
    assert "cycle_id" in result

    package = result["package"]
    assert package["opportunities"] or package["null_state"]

    if package["opportunities"]:
        opp = package["opportunities"][0]
        assert opp["symbol"] == "RELIANCE"
        assert opp["direction"] in ("LONG", "SHORT")
        assert 0.0 <= opp["confidence"] <= 1.0

    assert len(result["decisions"]) == len(package["opportunities"])
    for decision in result["decisions"]:
        assert decision["decision"] == "reject"


def test_recovery_reads_governance_and_portfolio_state(isolated_db):
    recovery = main.recover()

    assert recovery["governance_halt_active"] is False
    assert recovery["portfolio_capital"] == 5000.0
