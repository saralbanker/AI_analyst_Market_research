"""Dhan security ID registry (parallel to upstox_instruments.py).

Dhan identifies instruments by numeric security IDs, not by NSE ticker
symbols. This mapping must be populated from Dhan's instruments CSV (available
after KYC approval at https://api.dhan.co/v2/instruments).

Security IDs below are indicative values confirmed against Dhan's NSE_EQ
instrument list. Verify against the current instruments CSV before
paper-trading activation.
"""

from src.adapters.market import AdapterNotConfigured

# Dhan NSE_EQ security IDs. Key = NSE symbol (upper). Value = Dhan securityId.
SYMBOL_TO_SECURITY_ID: dict[str, str] = {
    "RELIANCE": "2885",  # NSE_EQ confirmed from Dhan instruments CSV (SEM_SMST_SECURITY_ID)
    # Extend when PLAN-003 multi-symbol universe is authorized.
}


def security_id_for(symbol: str) -> str:
    """Return the Dhan securityId for an NSE symbol.

    Raises AdapterNotConfigured when the symbol has no registered mapping.
    """
    sid = SYMBOL_TO_SECURITY_ID.get(symbol.upper())
    if not sid:
        raise AdapterNotConfigured(
            f"Dhan security ID not registered for symbol '{symbol}'. "
            "Add it to src/adapters/dhan_instruments.py."
        )
    return sid
