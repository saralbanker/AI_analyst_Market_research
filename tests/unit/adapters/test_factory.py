"""Adapter factory selection tests (PLAN-002 M1).

Selection must be by config-presence only -- no construction-time calls to
any adapter method (which would become a live network call once `fetch_*`
bodies are implemented).
"""

import json
import datetime

import pytest

from src.adapters import factory
from src.adapters.market import DhanMarketAdapter, FixtureMarketAdapter, UpstoxMarketAdapter
from src.adapters.news import FinnhubNewsAdapter, StubNewsAdapter
from src.adapters.macro import StubMacroAdapter, TradingEconomicsMacroAdapter
from src.security.token_loader import TOKEN_FILE

UPSTOX_VARS = ("UPSTOX_API_KEY", "UPSTOX_API_SECRET", "UPSTOX_ACCESS_TOKEN")
TE_VARS = ("TRADING_ECONOMICS_API_KEY", "TRADING_ECONOMICS_SECRET")


def _clear(monkeypatch, *keys):
    for key in keys:
        monkeypatch.delenv(key, raising=False)


def test_market_adapter_defaults_to_fixture(monkeypatch):
    _clear(monkeypatch, *UPSTOX_VARS)
    assert isinstance(factory.get_market_adapter(), FixtureMarketAdapter)


def test_market_adapter_partial_credentials_still_fixture(monkeypatch):
    _clear(monkeypatch, *UPSTOX_VARS)
    monkeypatch.setenv("UPSTOX_API_KEY", "key")
    monkeypatch.setenv("UPSTOX_API_SECRET", "secret")
    assert isinstance(factory.get_market_adapter(), FixtureMarketAdapter)


def test_market_adapter_full_credentials_selects_upstox(monkeypatch):
    monkeypatch.setenv("UPSTOX_API_KEY", "key")
    monkeypatch.setenv("UPSTOX_API_SECRET", "secret")
    monkeypatch.setenv("UPSTOX_ACCESS_TOKEN", "token")

    adapter = factory.get_market_adapter()

    assert isinstance(adapter, UpstoxMarketAdapter)


def test_news_adapter_defaults_to_stub(monkeypatch):
    monkeypatch.delenv("FINNHUB_API_KEY", raising=False)
    assert isinstance(factory.get_news_adapter(), StubNewsAdapter)


def test_news_adapter_with_key_selects_finnhub(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "key")
    assert isinstance(factory.get_news_adapter(), FinnhubNewsAdapter)


def test_macro_adapter_defaults_to_stub(monkeypatch):
    _clear(monkeypatch, *TE_VARS)
    assert isinstance(factory.get_macro_adapter(), StubMacroAdapter)


def test_macro_adapter_with_credentials_selects_trading_economics(monkeypatch):
    monkeypatch.setenv("TRADING_ECONOMICS_API_KEY", "key")
    monkeypatch.setenv("TRADING_ECONOMICS_SECRET", "secret")
    assert isinstance(factory.get_macro_adapter(), TradingEconomicsMacroAdapter)


def test_market_adapter_variant_b_defaults_to_fixture_no_credentials(monkeypatch):
    monkeypatch.delenv("DHAN_CLIENT_ID", raising=False)
    monkeypatch.delenv("DHAN_API_KEY", raising=False)
    _clear(monkeypatch, *UPSTOX_VARS)
    adapter = factory.get_market_adapter(variant="b")
    assert isinstance(adapter, FixtureMarketAdapter)


def test_market_adapter_variant_b_falls_back_when_token_missing(
    monkeypatch, tmp_path
):
    monkeypatch.setenv("DHAN_CLIENT_ID", "test-client")
    monkeypatch.delenv("DHAN_API_KEY", raising=False)
    _clear(monkeypatch, *UPSTOX_VARS)
    # Patch TOKEN_FILE to a nonexistent path so TokenUnavailable is raised.
    monkeypatch.setattr("src.security.token_loader.TOKEN_FILE", tmp_path / "no_token.json")
    adapter = factory.get_market_adapter(variant="b")
    # Falls back through Upstox path to fixture (no Upstox creds either).
    assert isinstance(adapter, FixtureMarketAdapter)


def test_market_adapter_variant_b_selects_dhan_via_api_key(monkeypatch):
    """DHAN_API_KEY + DHAN_CLIENT_ID env vars → DhanMarketAdapter (no secrets file)."""
    monkeypatch.setenv("DHAN_API_KEY", "live-access-token")
    monkeypatch.setenv("DHAN_CLIENT_ID", "test-client-direct")
    adapter = factory.get_market_adapter(variant="b")
    assert isinstance(adapter, DhanMarketAdapter)


def test_market_adapter_variant_b_selects_dhan_when_configured(monkeypatch, tmp_path):
    monkeypatch.setenv("DHAN_CLIENT_ID", "test-client")
    # Write a valid (non-expired) token file at the patched path.
    from zoneinfo import ZoneInfo
    IST = ZoneInfo("Asia/Kolkata")
    record = {
        "access_token": "test-token-abc",
        "client_id": "test-client",
        "obtained_at": datetime.datetime.now(IST).isoformat(),
        "expires_at": (datetime.datetime.now(IST) + datetime.timedelta(hours=12)).isoformat(),
        "version": 1,
    }
    token_path = tmp_path / "dhan_token.json"
    token_path.write_text(json.dumps(record))
    monkeypatch.setattr("src.security.token_loader.TOKEN_FILE", token_path)
    adapter = factory.get_market_adapter(variant="b")
    assert isinstance(adapter, DhanMarketAdapter)


def test_factory_never_calls_adapter_methods(monkeypatch):
    """Construction-time selection must not invoke fetch_* (would be a live call)."""
    monkeypatch.setenv("UPSTOX_API_KEY", "key")
    monkeypatch.setenv("UPSTOX_API_SECRET", "secret")
    monkeypatch.setenv("UPSTOX_ACCESS_TOKEN", "token")
    monkeypatch.setenv("FINNHUB_API_KEY", "key")
    monkeypatch.setenv("TRADING_ECONOMICS_API_KEY", "key")
    monkeypatch.setenv("TRADING_ECONOMICS_SECRET", "secret")

    def _boom(*args, **kwargs):
        raise AssertionError("adapter method called during factory selection")

    monkeypatch.setattr(UpstoxMarketAdapter, "fetch_ohlcv", _boom)
    monkeypatch.setattr(FinnhubNewsAdapter, "fetch_sentiment", _boom)
    monkeypatch.setattr(TradingEconomicsMacroAdapter, "fetch_indicators", _boom)

    factory.get_market_adapter()
    factory.get_news_adapter()
    factory.get_macro_adapter()
