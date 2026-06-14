"""Upstox instrument key lookup (EXT-001 WP01 / PLAN-002 M4).

Upstox's historical candle API addresses instruments by `instrument_key`
(exchange + ISIN), not bare ticker symbols. This maps the symbols used by
the Phase 2 universe (`mod01_market_data.fixtures`) to their NSE equity
instrument keys.
"""

SYMBOL_TO_INSTRUMENT_KEY = {
    "RELIANCE": "NSE_EQ|INE002A01018",
}


class UnknownInstrument(Exception):
    """Raised when a symbol has no known Upstox instrument key."""


def instrument_key_for(symbol: str) -> str:
    try:
        return SYMBOL_TO_INSTRUMENT_KEY[symbol]
    except KeyError:
        raise UnknownInstrument(f"no Upstox instrument_key mapped for symbol {symbol!r}") from None
