"""Environment/configuration validation (EXT-001 WP02).

Composition-root concern only: called from `main.py` / `scheduler.py` before
`persistence.db.init()`. Introduces no architecture, no modules, no
capabilities -- pure startup diagnostics so missing/invalid configuration is
caught with an actionable message instead of failing deep inside a module.

Reads `src/.env` (if present) into `os.environ` (without overriding values
already set in the real environment), then validates presence/shape of the
variables declared there. Credential values (Upstox/Finnhub/Trading
Economics) are allowed to be empty -- those adapters operate in stub mode
until credentials are inserted (EXT-001 PRIMARY_OBJECTIVE: "credential
insertion only").
"""

import os
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent / ".env"

# Variables that must be *declared* (key present) but may be empty --
# typically vendor credentials, populated when paper trading goes live.
OPTIONAL_KEYS = {
    "DATABASE_URL",
    "UPSTOX_API_KEY",
    "UPSTOX_API_SECRET",
    "UPSTOX_REDIRECT_URI",
    "UPSTOX_ACCESS_TOKEN",
    "FINNHUB_API_KEY",
    "TRADING_ECONOMICS_API_KEY",
    "TRADING_ECONOMICS_SECRET",
    "ALPHA_VANTAGE_API_KEY",
    "TWELVE_DATA_API_KEY",
    # Dhan — CAP-02 independent second market-data vendor.
    # DHAN_API_KEY: paste the live access token directly (client_id extracted from JWT).
    # DHAN_CLIENT_ID + DHAN_CLIENT_SECRET: used by scripts/generate_dhan_token.py
    # for automated daily token rotation via systemd/dhan-token-refresh.timer.
    "DHAN_API_KEY",
    "DHAN_CLIENT_ID",
    "DHAN_CLIENT_SECRET",
}

# Variables that must be present AND non-empty.
REQUIRED_KEYS = {
    "APP_ENV",
    "AUDIT_CHAIN_ENABLED",
    "GOVERNANCE_ENABLED",
    "PAPER_TRADING_ENABLED",
    "AUTO_EXECUTION_ENABLED",
    "BROKER_EXECUTION_ENABLED",
}

# Variables whose value must parse as a boolean ("true"/"false", any case).
BOOLEAN_KEYS = {
    "AUDIT_CHAIN_ENABLED",
    "GOVERNANCE_ENABLED",
    "PAPER_TRADING_ENABLED",
    "AUTO_EXECUTION_ENABLED",
    "BROKER_EXECUTION_ENABLED",
}

ALL_KEYS = REQUIRED_KEYS | OPTIONAL_KEYS


class ConfigError(Exception):
    """Raised when startup configuration is missing or invalid."""


def _parse_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip()
    return values


def _to_bool(value: str) -> bool:
    if value.lower() in ("true", "1", "yes"):
        return True
    if value.lower() in ("false", "0", "no"):
        return False
    raise ValueError(f"not a boolean: {value!r}")


def load_config() -> dict[str, str]:
    """Load `.env` into `os.environ` (without overriding real env vars),
    validate it, and return the merged configuration as a dict.

    Raises ConfigError, with one message per problem, if startup should be
    blocked.
    """
    file_values = _parse_env_file(ENV_FILE)
    for key, value in file_values.items():
        os.environ.setdefault(key, value)

    merged = {key: os.environ.get(key, file_values.get(key, "")) for key in ALL_KEYS}
    # Any additional vars declared only in the real environment are preserved too.
    for key in file_values:
        merged.setdefault(key, os.environ.get(key, ""))

    errors: list[str] = []

    for key in REQUIRED_KEYS:
        if key not in merged or merged[key] == "":
            errors.append(f"missing required environment variable: {key}")

    for key in BOOLEAN_KEYS:
        value = merged.get(key, "")
        if value == "":
            continue
        try:
            _to_bool(value)
        except ValueError:
            errors.append(f"environment variable {key} must be true/false, got {value!r}")

    if errors:
        raise ConfigError(
            "Startup configuration invalid:\n  - " + "\n  - ".join(errors)
            + f"\n\nCheck {ENV_FILE}"
        )

    return merged


def diagnostics(config: dict[str, str]) -> str:
    """Human-readable startup diagnostics summary (no secret values printed)."""
    lines = ["[config] startup diagnostics:"]
    for key in sorted(REQUIRED_KEYS):
        lines.append(f"  {key}={config.get(key, '')}")
    for key in sorted(OPTIONAL_KEYS):
        present = "set" if config.get(key) else "EMPTY (stub mode)"
        lines.append(f"  {key}={present}")
    return "\n".join(lines)
