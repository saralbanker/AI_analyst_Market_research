#!/usr/bin/env python3
"""Dhan daily access-token generator (SECTION 2 — token acquisition script).

Run:
    python scripts/generate_dhan_token.py

Responsibilities:
  1. Load DHAN_CLIENT_ID and DHAN_CLIENT_SECRET from src/.env or environment.
  2. POST to Dhan's token endpoint to obtain a fresh access_token.
  3. Validate the response (non-empty token, well-formed JSON).
  4. Atomically write to secrets/dhan_token.json (temp → chmod 600 → rename).
  5. Log every outcome (success and failure) to logs/token_refresh.log.

Invoked daily by systemd/dhan-token-refresh.timer at 06:00 IST (before NSE
opens at 09:15 IST). Also run manually after first credential setup.

Exit codes:
  0 — token written successfully
  1 — configuration error (credentials absent)
  2 — API error (Dhan endpoint unreachable or rejected credentials)
  3 — persistence error (cannot write secrets/dhan_token.json)

Dhan token endpoint (configure via DHAN_TOKEN_URL env var if the default
changes):

    POST https://api.dhan.co/v2/token
    Content-Type: application/json
    { "clientId": "<DHAN_CLIENT_ID>", "clientSecret": "<DHAN_CLIENT_SECRET>" }

    Expected response:
    {
      "accessToken": "<token>",
      "dhanClientId": "<client_id>",
      "tokenType": "Bearer"
    }

Verify the exact endpoint and field names against your Dhan API welcome email
or https://api.dhan.co/v2/docs after KYC approval.
"""

import datetime
import json
import logging
import os
import sys
import tempfile
from pathlib import Path
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = REPO_ROOT / "logs" / "token_refresh.log"
TOKEN_FILE = REPO_ROOT / "secrets" / "dhan_token.json"
ENV_FILE = REPO_ROOT / "src" / ".env"

IST = ZoneInfo("Asia/Kolkata")
DEFAULT_TOKEN_URL = "https://api.dhan.co/v2/token"


# ---------------------------------------------------------------------------
# Logging — dual output: log file (always) + stderr (failures only).
# Never print token values.
# ---------------------------------------------------------------------------

def _setup_logging() -> logging.Logger:
    LOG_FILE.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    LOG_FILE.touch(mode=0o600, exist_ok=True)

    fmt = "%(asctime)s %(levelname)s %(message)s"
    datefmt = "%Y-%m-%dT%H:%M:%S%z"

    logger = logging.getLogger("dhan_token_refresh")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    logger.addHandler(fh)

    return logger


# ---------------------------------------------------------------------------
# Config loading (mirrors src/config._parse_env_file without importing src)
# ---------------------------------------------------------------------------

def _load_env() -> None:
    """Merge src/.env into os.environ (never overrides real env vars)."""
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


# ---------------------------------------------------------------------------
# Expiry calculation — Dhan tokens expire at midnight IST
# ---------------------------------------------------------------------------

def _expires_at_midnight_ist() -> datetime.datetime:
    """Return the next midnight IST as a timezone-aware datetime."""
    now_ist = datetime.datetime.now(IST)
    # Roll forward to the start of the next calendar day in IST.
    tomorrow = (now_ist + datetime.timedelta(days=1)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    return tomorrow


# ---------------------------------------------------------------------------
# Atomic write — temp file → chmod 600 → rename (atomic on same filesystem)
# ---------------------------------------------------------------------------

def _atomic_write_token(record: dict) -> None:
    """Persist token record to TOKEN_FILE atomically."""
    TOKEN_FILE.parent.mkdir(mode=0o700, parents=True, exist_ok=True)

    content = json.dumps(record, indent=2, ensure_ascii=False) + "\n"

    tmp_fd, tmp_path_str = tempfile.mkstemp(
        dir=TOKEN_FILE.parent, prefix=".dhan_token_tmp_"
    )
    tmp_path = Path(tmp_path_str)
    try:
        os.write(tmp_fd, content.encode("utf-8"))
        os.close(tmp_fd)
        tmp_path.chmod(0o600)
        tmp_path.rename(TOKEN_FILE)  # atomic on Linux (same filesystem)
    except Exception:
        try:
            tmp_path.unlink(missing_ok=True)
        except OSError:
            pass
        raise


# ---------------------------------------------------------------------------
# Token acquisition
# ---------------------------------------------------------------------------

def _acquire_token(client_id: str, client_secret: str, token_url: str) -> str:
    """Call Dhan token endpoint and return the raw access_token string.

    Raises RuntimeError with a diagnostic message on any failure.
    """
    try:
        import requests
    except ImportError as exc:
        raise RuntimeError(
            "requests library not available. Install with: pip install requests"
        ) from exc

    payload = {
        "clientId": client_id,
        "clientSecret": client_secret,
    }

    try:
        resp = requests.post(
            token_url,
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            timeout=15,
        )
        resp.raise_for_status()
    except requests.HTTPError as exc:
        raise RuntimeError(
            f"Dhan token endpoint returned HTTP {exc.response.status_code}: "
            f"{exc.response.text[:200]}"
        ) from exc
    except requests.ConnectionError as exc:
        raise RuntimeError(f"Cannot reach Dhan API ({token_url}): {exc}") from exc
    except requests.Timeout:
        raise RuntimeError(f"Dhan API timed out after 15s ({token_url})")
    except requests.RequestException as exc:
        raise RuntimeError(f"Dhan API request failed: {exc}") from exc

    try:
        body = resp.json()
    except ValueError as exc:
        raise RuntimeError(
            f"Dhan token response is not valid JSON: {resp.text[:200]}"
        ) from exc

    # Dhan may use "accessToken" or "access_token" — handle both.
    token = body.get("accessToken") or body.get("access_token") or ""
    if not token:
        raise RuntimeError(
            f"Dhan token response missing accessToken field. "
            f"Keys present: {list(body.keys())}"
        )

    return token


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main() -> int:
    _load_env()
    log = _setup_logging()

    log.info("dhan_token_refresh: starting")

    client_id = os.environ.get("DHAN_CLIENT_ID", "").strip()
    client_secret = os.environ.get("DHAN_CLIENT_SECRET", "").strip()
    token_url = os.environ.get("DHAN_TOKEN_URL", DEFAULT_TOKEN_URL).strip()

    if not client_id:
        log.error("DHAN_CLIENT_ID is not set. Add it to src/.env.")
        print("ERROR: DHAN_CLIENT_ID is not set. Add it to src/.env.", file=sys.stderr)
        return 1

    if not client_secret:
        log.error("DHAN_CLIENT_SECRET is not set. Add it to src/.env.")
        print("ERROR: DHAN_CLIENT_SECRET is not set. Add it to src/.env.", file=sys.stderr)
        return 1

    log.info("Acquiring token for client_id=%s via %s", client_id, token_url)

    try:
        access_token = _acquire_token(client_id, client_secret, token_url)
    except RuntimeError as exc:
        log.error("Token acquisition failed: %s", exc)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    expires_at = _expires_at_midnight_ist()
    obtained_at = datetime.datetime.now(IST)

    record = {
        "access_token": access_token,
        "client_id": client_id,
        "obtained_at": obtained_at.isoformat(),
        "expires_at": expires_at.isoformat(),
        "version": 1,
    }

    try:
        _atomic_write_token(record)
    except Exception as exc:
        log.error("Failed to write %s: %s", TOKEN_FILE, exc)
        print(f"ERROR: Failed to write token file: {exc}", file=sys.stderr)
        return 3

    masked = f"{access_token[:8]}...{access_token[-4:]}" if len(access_token) > 12 else "***"
    log.info(
        "Token written: client_id=%s token=%s expires_at=%s path=%s",
        client_id,
        masked,
        expires_at.isoformat(),
        TOKEN_FILE,
    )
    print(
        f"OK: Dhan token refreshed. "
        f"client_id={client_id} expires_at={expires_at.isoformat()} "
        f"path={TOKEN_FILE}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
