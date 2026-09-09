"""Dhan access token loader (SECTION 4 — token consumer interface).

Reads secrets/dhan_token.json, validates schema and freshness, and returns
the access token string. Raises TokenUnavailable with a diagnostic message if
the token is missing, malformed, or expired so callers get a clear failure
rather than a silent empty string.

Called by DhanMarketAdapter at construction time. Never writes to the secrets
file — that is exclusively the responsibility of scripts/generate_dhan_token.py.
"""

import datetime
import json
from pathlib import Path
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")

REPO_ROOT = Path(__file__).resolve().parents[2]
TOKEN_FILE = REPO_ROOT / "secrets" / "dhan_token.json"

REQUIRED_FIELDS = {"access_token", "client_id", "obtained_at", "expires_at", "version"}


class TokenUnavailable(Exception):
    """Raised when the Dhan token cannot be loaded or is no longer valid."""


def load_token_record() -> dict:
    """Load and validate the raw token record from disk.

    Returns the parsed JSON dict. Raises TokenUnavailable on any problem.
    """
    if not TOKEN_FILE.exists():
        raise TokenUnavailable(
            f"Dhan token file not found: {TOKEN_FILE}\n"
            "Run:  python scripts/generate_dhan_token.py"
        )

    try:
        raw = TOKEN_FILE.read_text(encoding="utf-8")
    except PermissionError as exc:
        raise TokenUnavailable(f"Cannot read {TOKEN_FILE}: {exc}") from exc

    try:
        record = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise TokenUnavailable(f"Malformed token file {TOKEN_FILE}: {exc}") from exc

    missing = REQUIRED_FIELDS - record.keys()
    if missing:
        raise TokenUnavailable(
            f"Token file {TOKEN_FILE} is missing fields: {sorted(missing)}"
        )

    if not record.get("access_token"):
        raise TokenUnavailable(f"access_token field is empty in {TOKEN_FILE}")

    try:
        expires_at = datetime.datetime.fromisoformat(record["expires_at"])
    except (ValueError, TypeError) as exc:
        raise TokenUnavailable(
            f"Cannot parse expires_at in {TOKEN_FILE}: {exc}"
        ) from exc

    now = datetime.datetime.now(IST)
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=IST)

    if now >= expires_at:
        raise TokenUnavailable(
            f"Dhan token expired at {expires_at.isoformat()}. "
            "Run:  python scripts/generate_dhan_token.py"
        )

    return record


def get_dhan_access_token() -> str:
    """Return the current Dhan access token string.

    Raises TokenUnavailable if unavailable or expired.
    """
    return load_token_record()["access_token"]


def get_dhan_client_id() -> str:
    """Return the Dhan client ID from the persisted token record."""
    return load_token_record()["client_id"]


def token_health() -> dict:
    """Return a health summary dict — safe for logging (no secret values).

    Keys: ok (bool), message (str), expires_at (str|None), age_hours (float|None).
    """
    try:
        record = load_token_record()
        expires_at_str = record["expires_at"]
        obtained_at_str = record.get("obtained_at", "")
        now = datetime.datetime.now(IST)

        expires_at = datetime.datetime.fromisoformat(expires_at_str)
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=IST)

        ttl_hours = (expires_at - now).total_seconds() / 3600

        age_hours: float | None = None
        if obtained_at_str:
            obtained_at = datetime.datetime.fromisoformat(obtained_at_str)
            if obtained_at.tzinfo is None:
                obtained_at = obtained_at.replace(tzinfo=IST)
            age_hours = (now - obtained_at).total_seconds() / 3600

        return {
            "ok": True,
            "message": f"Token valid. TTL={ttl_hours:.1f}h",
            "expires_at": expires_at_str,
            "ttl_hours": round(ttl_hours, 2),
            "age_hours": round(age_hours, 2) if age_hours is not None else None,
        }
    except TokenUnavailable as exc:
        return {
            "ok": False,
            "message": str(exc),
            "expires_at": None,
            "ttl_hours": None,
            "age_hours": None,
        }
