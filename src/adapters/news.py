"""News/sentiment adapter interface + implementations (EXT-001 WP01).

`NewsAdapter.fetch_sentiment(symbol)` returns a list of supplementary,
advisory-only sentiment records (CAP-08, VAL05-04/FORB-03/DEP-04 --
structurally incapable of reaching CAP-12/13/15/16 numeric computation).
Record shape: `{"headline": str, "sentiment": str, "published_at": str}`.
"""

import datetime
from typing import Protocol


class AdapterNotConfigured(Exception):
    """Raised by a real-vendor adapter when required credentials are absent."""


class AdapterError(Exception):
    """Raised when a real-vendor adapter's HTTP call fails or returns an
    unexpected shape. Callers should treat this like an empty result, not a
    crash -- news/sentiment is advisory-only (CAP-08)."""


class NewsAdapter(Protocol):
    def fetch_sentiment(self, symbol: str) -> list[dict]:
        ...


class StubNewsAdapter:
    """Always-available stub: no news source configured (Phase 2 default)."""

    def fetch_sentiment(self, symbol: str) -> list[dict]:
        return []


def _score_to_label(score: float) -> str:
    if score > 0.6:
        return "positive"
    if score < 0.4:
        return "negative"
    return "neutral"


class FinnhubNewsAdapter:
    """Finnhub news/sentiment adapter.

    Requires FINNHUB_API_KEY. Combines two Finnhub endpoints because Finnhub
    does not provide per-headline sentiment on the free tier:
      - `/company-news` for the last 7 days of headlines
      - `/news-sentiment` for an aggregate `companyNewsScore` (0..1), mapped
        to a "positive"/"neutral"/"negative" label applied to every headline
        in the window (CAP-08 record shape requires a per-record label, and
        this is the closest available proxy).
    """

    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(self, api_key: str):
        self._api_key = api_key

    def fetch_sentiment(self, symbol: str) -> list[dict]:
        if not self._api_key:
            raise AdapterNotConfigured("Finnhub API key not configured")

        import requests

        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)

        try:
            news_resp = requests.get(
                f"{self.BASE_URL}/company-news",
                params={
                    "symbol": symbol,
                    "from": week_ago.isoformat(),
                    "to": today.isoformat(),
                    "token": self._api_key,
                },
                timeout=10,
            )
            news_resp.raise_for_status()
            articles = news_resp.json()

            sentiment_resp = requests.get(
                f"{self.BASE_URL}/news-sentiment",
                params={"symbol": symbol, "token": self._api_key},
                timeout=10,
            )
            sentiment_resp.raise_for_status()
            sentiment_data = sentiment_resp.json()
        except requests.RequestException as exc:
            raise AdapterError(f"Finnhub request failed: {exc}") from exc

        if not isinstance(articles, list):
            raise AdapterError(f"Finnhub company-news returned unexpected shape: {articles!r}")

        score = sentiment_data.get("companyNewsScore", 0.5) if isinstance(sentiment_data, dict) else 0.5
        label = _score_to_label(score)

        records = []
        for article in articles:
            try:
                published_at = datetime.datetime.fromtimestamp(article["datetime"], tz=datetime.timezone.utc).isoformat()
                records.append({
                    "headline": article["headline"],
                    "sentiment": label,
                    "published_at": published_at,
                })
            except (KeyError, TypeError, ValueError):
                continue

        return records
