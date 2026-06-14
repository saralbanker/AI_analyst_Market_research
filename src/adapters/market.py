"""Market data adapter interface + implementations (EXT-001 WP01).

`MarketAdapter.fetch_ohlcv(symbol)` returns the same bar shape as
`mod01_market_data.fixtures`: a list of
`{"day": int, "open": float, "high": float, "low": float, "close": float,
"volume": int}` dicts (validated by `cap_data_quality.validate_bars`).
"""

import datetime
from typing import Protocol


class AdapterNotConfigured(Exception):
    """Raised by a real-vendor adapter when required credentials are absent."""


class AdapterError(Exception):
    """Raised when a real-vendor adapter's HTTP call fails or returns an
    unexpected shape."""


class MarketAdapter(Protocol):
    def fetch_ohlcv(self, symbol: str) -> list[dict]:
        ...


class FixtureMarketAdapter:
    """Always-available stub backed by the Phase 2 vertical-slice fixture."""

    def __init__(self, variant: str = "a"):
        self._variant = variant

    def fetch_ohlcv(self, symbol: str) -> list[dict]:
        from src.mod01_market_data import fixtures

        if self._variant == "a":
            return fixtures.vendor_a_bars()
        return fixtures.vendor_b_bars()


class UpstoxMarketAdapter:
    """Upstox historical-candle market data adapter.

    Requires UPSTOX_API_KEY, UPSTOX_API_SECRET, UPSTOX_ACCESS_TOKEN. Fetches
    daily candles for the last 90 days via Upstox's v2 historical-candle
    endpoint and maps them to the fixture bar shape. Candles come back from
    Upstox most-recent-first; they are re-indexed 0..n-1 in chronological
    order so `day` has no gaps (required by cap_data_quality.validate_bars).
    """

    BASE_URL = "https://api.upstox.com/v2"

    def __init__(self, api_key: str, api_secret: str, access_token: str):
        self._api_key = api_key
        self._api_secret = api_secret
        self._access_token = access_token

    def fetch_ohlcv(self, symbol: str) -> list[dict]:
        if not (self._api_key and self._api_secret and self._access_token):
            raise AdapterNotConfigured("Upstox credentials not configured")

        import requests

        from src.adapters.upstox_instruments import instrument_key_for

        instrument_key = instrument_key_for(symbol)

        to_date = datetime.date.today()
        from_date = to_date - datetime.timedelta(days=90)

        url = (
            f"{self.BASE_URL}/historical-candle/{instrument_key}/day/"
            f"{to_date.isoformat()}/{from_date.isoformat()}"
        )

        try:
            response = requests.get(
                url,
                headers={"Authorization": f"Bearer {self._access_token}", "Accept": "application/json"},
                timeout=10,
            )
            response.raise_for_status()
            payload = response.json()
        except requests.RequestException as exc:
            raise AdapterError(f"Upstox request failed: {exc}") from exc

        try:
            candles = payload["data"]["candles"]
        except (KeyError, TypeError) as exc:
            raise AdapterError(f"Upstox historical-candle returned unexpected shape: {payload!r}") from exc

        # Upstox returns most-recent-first; reverse to chronological order.
        candles = sorted(candles, key=lambda c: c[0])

        bars = []
        for day_index, candle in enumerate(candles):
            try:
                _, open_, high, low, close, volume = candle[:6]
                bars.append({
                    "day": day_index,
                    "open": float(open_),
                    "high": float(high),
                    "low": float(low),
                    "close": float(close),
                    "volume": int(volume),
                })
            except (ValueError, TypeError) as exc:
                raise AdapterError(f"Upstox candle malformed: {candle!r}") from exc

        return bars
