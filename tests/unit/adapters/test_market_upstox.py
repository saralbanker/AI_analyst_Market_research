"""Contract tests for UpstoxMarketAdapter (PLAN-002 M4).

The HTTP layer is mocked with a recorded Upstox historical-candle response.
When real credentials are inserted, only the mocked `requests.get` boundary
changes -- the adapter code under test does not change.
"""

import json
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from src.adapters.market import AdapterError, AdapterNotConfigured, UpstoxMarketAdapter
from src.adapters.upstox_instruments import UnknownInstrument
from src.mod01_market_data.cap_data_quality import validate_bars

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures" / "vendor_responses"


def _load(name: str):
    return json.loads((FIXTURES / name).read_text())


def _mock_response(payload):
    resp = MagicMock()
    resp.json.return_value = payload
    resp.raise_for_status.return_value = None
    return resp


def test_missing_credentials_raises_not_configured():
    adapter = UpstoxMarketAdapter(api_key="", api_secret="", access_token="")
    with pytest.raises(AdapterNotConfigured):
        adapter.fetch_ohlcv("RELIANCE")


def test_unknown_symbol_raises_unknown_instrument():
    adapter = UpstoxMarketAdapter(api_key="k", api_secret="s", access_token="t")
    with pytest.raises(UnknownInstrument):
        adapter.fetch_ohlcv("UNKNOWN_SYMBOL")


def test_fetch_ohlcv_maps_recorded_response_chronologically():
    payload = _load("upstox_historical_candle_sample.json")
    adapter = UpstoxMarketAdapter(api_key="k", api_secret="s", access_token="t")

    with patch("requests.get") as mock_get:
        mock_get.return_value = _mock_response(payload)
        bars = adapter.fetch_ohlcv("RELIANCE")

    assert len(bars) == 3
    assert [b["day"] for b in bars] == [0, 1, 2]
    # Upstox returns most-recent-first; bars[0] should be the oldest candle.
    assert bars[0]["close"] == 2510.0
    assert bars[-1]["close"] == 2525.0

    validate_bars(bars, "upstox")


def test_fetch_ohlcv_wraps_request_errors():
    import requests

    adapter = UpstoxMarketAdapter(api_key="k", api_secret="s", access_token="t")
    with patch("requests.get", side_effect=requests.RequestException("boom")):
        with pytest.raises(AdapterError):
            adapter.fetch_ohlcv("RELIANCE")


def test_fetch_ohlcv_rejects_unexpected_shape():
    adapter = UpstoxMarketAdapter(api_key="k", api_secret="s", access_token="t")
    with patch("requests.get") as mock_get:
        mock_get.return_value = _mock_response({"unexpected": "shape"})
        with pytest.raises(AdapterError):
            adapter.fetch_ohlcv("RELIANCE")
