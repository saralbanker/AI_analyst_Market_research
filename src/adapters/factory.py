"""Adapter factories (EXT-001 WP01).

Reads credentials via `src.config` and returns the configured real-vendor
adapter if credentials are present, otherwise the always-available stub --
so callers never need to branch on configuration state themselves.

Selection is by config-presence only: required environment variables are
checked, and the matching adapter is constructed without calling any of its
methods. This keeps adapter selection free of network calls -- once a real
adapter's `fetch_*` body makes live HTTP requests, construction-time
selection must not trigger one.

CAP-02 vendor assignments (two independent sources, SDM-02 Rule 2):
  variant="a"  primary   → Upstox (UpstoxMarketAdapter or FixtureMarketAdapter)
  variant="b"  secondary → Dhan   (DhanMarketAdapter    or FixtureMarketAdapter)
"""

import os

from src.adapters.market import (
    DhanMarketAdapter,
    FixtureMarketAdapter,
    MarketAdapter,
    UpstoxMarketAdapter,
)
from src.adapters.news import FinnhubNewsAdapter, NewsAdapter, StubNewsAdapter
from src.adapters.macro import MacroAdapter, StubMacroAdapter, TradingEconomicsMacroAdapter


def get_market_adapter(variant: str = "a") -> MarketAdapter:
    if variant == "b":
        return _get_dhan_adapter()
    return _get_upstox_adapter(variant=variant)


def _get_upstox_adapter(variant: str = "a") -> MarketAdapter:
    api_key = os.environ.get("UPSTOX_API_KEY", "")
    api_secret = os.environ.get("UPSTOX_API_SECRET", "")
    access_token = os.environ.get("UPSTOX_ACCESS_TOKEN", "")
    if api_key and api_secret and access_token:
        return UpstoxMarketAdapter(api_key=api_key, api_secret=api_secret, access_token=access_token)
    return FixtureMarketAdapter(variant=variant)


def _extract_client_id_from_jwt(token: str) -> str:
    """Decode JWT payload (no signature verification) to find Dhan client ID."""
    import base64
    import json as _json
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return ""
        padded = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = _json.loads(base64.urlsafe_b64decode(padded))
        for field in ("clientId", "dhanClientId", "sub", "userId", "client_id", "id"):
            val = payload.get(field)
            if val:
                return str(val)
    except Exception:
        pass
    return ""


def _get_dhan_adapter() -> MarketAdapter:
    api_key = os.environ.get("DHAN_API_KEY", "")
    client_id = os.environ.get("DHAN_CLIENT_ID", "")

    # Path 1: DHAN_API_KEY is the live access token (client_id from env or JWT).
    if api_key:
        resolved_id = client_id or _extract_client_id_from_jwt(api_key)
        if resolved_id:
            return DhanMarketAdapter(client_id=resolved_id, access_token=api_key)

    # Path 2: secrets file written by scripts/generate_dhan_token.py.
    if client_id:
        try:
            from src.security.token_loader import get_dhan_access_token, TokenUnavailable
            access_token = get_dhan_access_token()
            return DhanMarketAdapter(client_id=client_id, access_token=access_token)
        except TokenUnavailable:
            pass

    # F-4 fix: fall back to Upstox so cross_verify() sees equal bar counts.
    # This restores the A-1 condition (Upstox-vs-Upstox) until Dhan is configured.
    return _get_upstox_adapter(variant="a")


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
