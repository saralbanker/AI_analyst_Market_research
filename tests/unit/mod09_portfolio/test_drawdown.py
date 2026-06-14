"""Drawdown tracking tests (PLAN-002 M2 / F-B).

Uses a temporary system.db / audit.db (monkeypatched paths) so paper-trading
writes never touch the real project databases.
"""

import pytest

from src.persistence import db
from src.mod09_portfolio import cap_paper_trading as pt
from src.mod09_portfolio import get_state as get_portfolio_state
from src.mod06_governance import detectors


@pytest.fixture
def isolated_db(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "SYSTEM_DB_PATH", tmp_path / "system.db")
    monkeypatch.setattr(db, "AUDIT_DB_PATH", tmp_path / "audit.db")
    db.init()


def test_opening_position_does_not_change_drawdown_at_par(isolated_db):
    pt.open_position("RELIANCE", quantity=10, price=100.0)

    state = get_portfolio_state()
    # capital(5000-1000) + book value(1000) == 5000 == peak -> 0 drawdown
    assert state.drawdown_pct == 0.0


def test_closing_at_loss_increases_drawdown(isolated_db):
    pt.open_position("RELIANCE", quantity=10, price=100.0)
    pt.close_position("RELIANCE", price=50.0)  # realized loss of 500

    state = get_portfolio_state()
    assert state.capital == pytest.approx(4500.0)
    # equity dropped from peak 5000 to 4500 -> 10% drawdown
    assert state.drawdown_pct == pytest.approx(0.10)


def test_drawdown_breach_triggers_conditional_suspension(isolated_db):
    pt.open_position("RELIANCE", quantity=100, price=10.0)  # cost=1000, capital->4000
    pt.close_position("RELIANCE", price=2.5)  # proceeds=250, realized loss=750

    state = get_portfolio_state()
    # equity = 4000 + 250 = 4250 vs peak 5000 -> drawdown = 15%
    assert state.drawdown_pct == pytest.approx(0.15)

    result = detectors.run_drawdown_detector()
    assert result["transition"] == "ENTERED_CONDITIONAL_SUSPENSION"

    halts = detectors.run_drawdown_detector()
    assert halts["state3_status"] == "active"
