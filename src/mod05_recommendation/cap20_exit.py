"""CAP-20: Exit Suggestion (MOD-05).

Minimal real rule: if the portfolio holds an open position in a symbol
that is not among the currently validated LONG signals, suggest exit.
"""


def compute_exit_suggestions(positions: dict, validated_signals: list) -> list[dict]:
    validated_symbols_long = {
        s.symbol for s in validated_signals if s.direction == "LONG"
    }

    suggestions = []
    for symbol, position in positions.items():
        if symbol not in validated_symbols_long:
            suggestions.append({"symbol": symbol, "action": "EXIT", "reason": "signal no longer valid"})

    return suggestions
