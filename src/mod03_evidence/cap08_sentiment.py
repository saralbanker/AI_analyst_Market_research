"""CAP-08: News/Sentiment Signal Intake (supplementary, advisory-only, MOD-03).

VAL05-04/FORB-03/DEP-04: this output is structurally incapable of reaching
CAP-12/13/15/16 computation -- it is returned only for MOD-07's distinct
advisory section. Backed by `src.adapters.get_news_adapter()`, which falls
back to a stub (empty list) until Finnhub credentials are configured.
"""

from src.adapters import get_news_adapter
from src.adapters.news import AdapterError


def fetch_sentiment(symbol: str) -> list[dict]:
    try:
        return get_news_adapter().fetch_sentiment(symbol)
    except AdapterError:
        return []
