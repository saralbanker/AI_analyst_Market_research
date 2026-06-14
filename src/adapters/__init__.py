"""External data adapters (EXT-001 WP01).

This package is a shared, non-constitutional utility layer (not a `modNN_*`
package -- it owns no capability, no table-group, and is exempt from the
boundary-enforcement Allowed Edge Table in
`tests/architecture/test_boundaries.py`, which only walks `modNN_*`
packages). `modNN_*` packages may import from `adapters` freely, the same
way they import `persistence` or `mod10_audit`.

Each adapter kind (market/news/macro) defines a small `Protocol` interface
plus a fixture-backed stub implementation (always available, no credentials)
and a real-vendor skeleton (Upstox/Finnhub/Trading Economics) that reads its
credentials from `src.config` and raises `AdapterNotConfigured` until those
credentials are present. No live network calls are made anywhere in this
package.
"""

from src.adapters.factory import get_market_adapter, get_news_adapter, get_macro_adapter

__all__ = ["get_market_adapter", "get_news_adapter", "get_macro_adapter"]
