"""Adapter factory selection tests (PLAN-002 M1).

Selection must be by config-presence only -- no construction-time calls to
any adapter method (which would become a live network call once `fetch_*`
bodies are implemented).
"""

from src.adapters import factory
from src.adapters.market import FixtureMarketAdapter, UpstoxMarketAdapter
from src.adapters.news import FinnhubNewsAdapter, StubNewsAdapter
from src.adapters.macro import StubMacroAdapter, TradingEconomicsMacroAdapter

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
