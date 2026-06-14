"""Macro data adapter interface + implementations (EXT-001 WP01).

`MacroAdapter.fetch_indicators()` returns a dict of macro indicators (e.g.
GDP growth, inflation, interest rates) for use as supplementary context by
MOD-02 (CAP-05/CAP-06). Not yet consumed by any module -- available for
wiring once Trading Economics credentials are inserted.
"""

from typing import Protocol


class AdapterNotConfigured(Exception):
    """Raised by a real-vendor adapter when required credentials are absent."""


class AdapterError(Exception):
    """Raised when a real-vendor adapter's HTTP call fails or returns an
    unexpected shape."""


class MacroAdapter(Protocol):
    def fetch_indicators(self) -> dict:
        ...


class StubMacroAdapter:
    """Always-available stub: no macro source configured (Phase 2 default)."""

    def fetch_indicators(self) -> dict:
        return {}


class TradingEconomicsMacroAdapter:
    """Trading Economics macro indicator adapter.

    Requires TRADING_ECONOMICS_API_KEY and TRADING_ECONOMICS_SECRET, combined
    as the API's `key:secret` auth token. Fetches India's indicator list and
    maps it to `{category: latest_value}`.
    """

    BASE_URL = "https://api.tradingeconomics.com"
    COUNTRY = "india"

    def __init__(self, api_key: str, api_secret: str):
        self._api_key = api_key
        self._api_secret = api_secret

    def fetch_indicators(self) -> dict:
        if not (self._api_key and self._api_secret):
            raise AdapterNotConfigured("Trading Economics credentials not configured")

        import requests

        try:
            response = requests.get(
                f"{self.BASE_URL}/country/{self.COUNTRY}",
                params={"c": f"{self._api_key}:{self._api_secret}", "f": "json"},
                timeout=10,
            )
            response.raise_for_status()
            payload = response.json()
        except requests.RequestException as exc:
            raise AdapterError(f"Trading Economics request failed: {exc}") from exc

        if not isinstance(payload, list):
            raise AdapterError(f"Trading Economics country endpoint returned unexpected shape: {payload!r}")

        indicators = {}
        for entry in payload:
            try:
                indicators[entry["Category"]] = entry["LatestValue"]
            except (KeyError, TypeError):
                continue

        return indicators
