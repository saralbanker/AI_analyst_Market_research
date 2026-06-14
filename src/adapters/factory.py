"""Adapter factories (EXT-001 WP01).

Reads credentials via `src.config` and returns the configured real-vendor
adapter if credentials are present, otherwise the always-available stub --
so callers never need to branch on configuration state themselves.

Selection is by config-presence only: required environment variables are
checked, and the matching adapter is constructed without calling any of its
methods. This keeps adapter selection free of network calls -- once a real
adapter's `fetch_*` body makes live HTTP requests, construction-time
selection must not trigger one.
"""

import os

from src.adapters.market import FixtureMarketAdapter, MarketAdapter, UpstoxMarketAdapter
from src.adapters.news import FinnhubNewsAdapter, NewsAdapter, StubNewsAdapter
from src.adapters.macro import MacroAdapter, StubMacroAdapter, TradingEconomicsMacroAdapter


def get_market_adapter(variant: str = "a") -> MarketAdapter:
    api_key = os.environ.get("UPSTOX_API_KEY", "")
    api_secret = os.environ.get("UPSTOX_API_SECRET", "")
    access_token = os.environ.get("UPSTOX_ACCESS_TOKEN", "")
    if api_key and api_secret and access_token:
        return UpstoxMarketAdapter(api_key=api_key, api_secret=api_secret, access_token=access_token)
    return FixtureMarketAdapter(variant=variant)


def get_news_adapter() -> NewsAdapter:
    api_key = os.environ.get("FINNHUB_API_KEY", "")
    if api_key:
        return FinnhubNewsAdapter(api_key=api_key)
    return StubNewsAdapter()


def get_macro_adapter() -> MacroAdapter:
    api_key = os.environ.get("TRADING_ECONOMICS_API_KEY", "")
    api_secret = os.environ.get("TRADING_ECONOMICS_SECRET", "")
    if api_key and api_secret:
        return TradingEconomicsMacroAdapter(api_key=api_key, api_secret=api_secret)
    return StubMacroAdapter()
