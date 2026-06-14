"""Contract tests for FinnhubNewsAdapter (PLAN-002 M4).

The HTTP layer is mocked with recorded Finnhub response fixtures. When real
credentials are inserted, only the mocked `requests.get` boundary changes to
a real network call -- the adapter code under test does not change.
"""

import datetime
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from src.adapters.news import AdapterError, AdapterNotConfigured, FinnhubNewsAdapter

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures" / "vendor_responses"


def _load(name: str):
    return json.loads((FIXTURES / name).read_text())


def _mock_response(payload):
    resp = MagicMock()
    resp.json.return_value = payload
    resp.raise_for_status.return_value = None
    return resp


def test_no_api_key_raises_not_configured():
    adapter = FinnhubNewsAdapter(api_key="")
    with pytest.raises(AdapterNotConfigured):
        adapter.fetch_sentiment("RELIANCE")


def test_fetch_sentiment_maps_recorded_response():
    news_payload = _load("finnhub_company_news_sample.json")
    sentiment_payload = _load("finnhub_news_sentiment_sample.json")

    adapter = FinnhubNewsAdapter(api_key="dummy-key")

    with patch("requests.get") as mock_get:
        mock_get.side_effect = [
            _mock_response(news_payload),
            _mock_response(sentiment_payload),
        ]
        records = adapter.fetch_sentiment("RELIANCE")

    assert len(records) == 2
    for record, article in zip(records, news_payload):
        assert record["headline"] == article["headline"]
        assert record["sentiment"] == "positive"  # companyNewsScore 0.78 > 0.6
        assert record["published_at"] == datetime.datetime.fromtimestamp(article["datetime"], tz=datetime.timezone.utc).isoformat()


def test_fetch_sentiment_wraps_request_errors():
    import requests

    adapter = FinnhubNewsAdapter(api_key="dummy-key")

    with patch("requests.get", side_effect=requests.RequestException("boom")):
        with pytest.raises(AdapterError):
            adapter.fetch_sentiment("RELIANCE")


def test_fetch_sentiment_rejects_unexpected_shape():
    adapter = FinnhubNewsAdapter(api_key="dummy-key")

    with patch("requests.get") as mock_get:
        mock_get.return_value = _mock_response({"unexpected": "shape"})
        with pytest.raises(AdapterError):
            adapter.fetch_sentiment("RELIANCE")
