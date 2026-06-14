"""Contract tests for TradingEconomicsMacroAdapter (PLAN-002 M4)."""

import json
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from src.adapters.macro import AdapterError, AdapterNotConfigured, TradingEconomicsMacroAdapter

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures" / "vendor_responses"


def _load(name: str):
    return json.loads((FIXTURES / name).read_text())


def _mock_response(payload):
    resp = MagicMock()
    resp.json.return_value = payload
    resp.raise_for_status.return_value = None
    return resp


def test_missing_credentials_raises_not_configured():
    adapter = TradingEconomicsMacroAdapter(api_key="", api_secret="")
    with pytest.raises(AdapterNotConfigured):
        adapter.fetch_indicators()


def test_fetch_indicators_maps_recorded_response():
    payload = _load("trading_economics_india_sample.json")
    adapter = TradingEconomicsMacroAdapter(api_key="k", api_secret="s")

    with patch("requests.get") as mock_get:
        mock_get.return_value = _mock_response(payload)
        indicators = adapter.fetch_indicators()

    assert indicators == {
        "GDP Growth Rate": 7.6,
        "Inflation Rate": 5.1,
        "Interest Rate": 6.5,
    }


def test_fetch_indicators_wraps_request_errors():
    import requests

    adapter = TradingEconomicsMacroAdapter(api_key="k", api_secret="s")
    with patch("requests.get", side_effect=requests.RequestException("boom")):
        with pytest.raises(AdapterError):
            adapter.fetch_indicators()


def test_fetch_indicators_rejects_unexpected_shape():
    adapter = TradingEconomicsMacroAdapter(api_key="k", api_secret="s")
    with patch("requests.get") as mock_get:
        mock_get.return_value = _mock_response({"unexpected": "shape"})
        with pytest.raises(AdapterError):
            adapter.fetch_indicators()
