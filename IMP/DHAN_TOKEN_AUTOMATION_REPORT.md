# DHAN_TOKEN_AUTOMATION_REPORT

**Task:** DHAN_TOKEN_AUTOMATION_AND_OPERATIONAL_READINESS
**Date:** 2026-06-21
**Mode:** Implementation + verification. No architectural modification.
**Authority basis (inherited, unmodified):** SDM_V2.3 ▸ VAL05 ▸ SADR_V2.1 ▸ ARCHITECTURE_FOUNDATION_V1 ▸ ADR-000..007 ▸ IMP-001 ▸ VER-001 ▸ EXT-001 ▸ EXT-002 ▸ VER-002 ▸ VER-003
**Blocking predecessor:** VER-003 ruling — CAP-02 requires ≥2 independent market-data vendors; current system self-compares Upstox. Dhan is the selected second vendor.

---

## SECTION 1 — Architecture Design

### Folder Structure

```
AI_analyst_Market_research/
│
├── secrets/                          # chmod 700 — runtime only, gitignored
│   ├── .gitkeep                      # directory marker (committed, empty)
│   └── dhan_token.json               # daily token — NEVER committed
│
├── logs/                             # chmod 700 — runtime only, gitignored
│   ├── .gitkeep                      # directory marker
│   └── token_refresh.log            # append-only operational log
│
├── scripts/
│   └── generate_dhan_token.py       # token acquisition + persistence script
│
├── src/
│   ├── security/                    # NEW — token consumer interface
│   │   ├── __init__.py
│   │   └── token_loader.py          # read-only, raises TokenUnavailable on problems
│   └── adapters/
│       ├── dhan_instruments.py      # NEW — symbol → Dhan securityId registry
│       ├── market.py                # EXTENDED — DhanMarketAdapter added
│       └── factory.py               # EXTENDED — variant="b" routes to Dhan
│
├── tools/
│   └── check_dhan_token.py          # health diagnostics
│
└── systemd/
    ├── dhan-token-refresh.service    # oneshot service
    ├── dhan-token-refresh.timer      # fires 06:00 IST daily
    └── install.sh                    # one-time user-level timer installation
```

### Ownership

| Concern | Owner |
|---|---|
| Token acquisition | `scripts/generate_dhan_token.py` (sole writer) |
| Token persistence | `secrets/dhan_token.json` (atomically replaced daily) |
| Token reading | `src/security/token_loader.py` (read-only, no write authority) |
| Adapter construction | `src/adapters/factory.py` (calls token_loader at construction time) |
| Market data fetching | `src/adapters/market.DhanMarketAdapter` (sole Dhan HTTP caller) |
| Scheduling | `systemd/dhan-token-refresh.timer` + `.service` |
| Diagnostics | `tools/check_dhan_token.py` |

**No module (mod01..mod11) imports src/security directly** — token access flows through the adapter layer only, which is already outside the boundary-scan perimeter.

---

## SECTION 2 — Python Automation (scripts/generate_dhan_token.py)

**Implemented at:** `scripts/generate_dhan_token.py`

Responsibilities:
- Reads `DHAN_CLIENT_ID` and `DHAN_CLIENT_SECRET` from `src/.env` / environment.
- POSTs to Dhan token endpoint (`DHAN_TOKEN_URL`, default `https://api.dhan.co/v2/token`).
- Accepts `accessToken` or `access_token` response field (handles both casing variants).
- Validates the token is non-empty.
- Computes `expires_at` as next midnight IST (tokens expire at midnight IST).
- Writes atomically via tempfile → chmod 600 → rename.
- Logs every outcome to `logs/token_refresh.log` (no token values in logs, only masked prefix).

Exit codes: 0=success, 1=credentials absent, 2=API error, 3=persistence error.

---

## SECTION 3 — Secret Persistence (secrets/dhan_token.json)

**Schema:**
```json
{
  "access_token": "<bearer-token>",
  "client_id": "<dhan-client-id>",
  "obtained_at": "2026-06-21T06:00:47+05:30",
  "expires_at": "2026-06-22T00:00:00+05:30",
  "version": 1
}
```

**Atomic replacement protocol:**
1. Write to `secrets/.dhan_token_tmp_<random>` (same filesystem as final path).
2. `chmod 600` the temp file.
3. `os.rename(tmp, final)` — atomic on Linux (POSIX rename guarantee, single filesystem).
4. On any failure, unlink the temp file.

File and directory permissions:
- `secrets/` — `700` (owner read/write/execute only)
- `secrets/dhan_token.json` — `600` (owner read/write only)

`.gitignore` protects both `secrets/dhan_token.json` and `secrets/.dhan_token_tmp_*`.

---

## SECTION 4 — Token Loader (src/security/token_loader.py)

**Implemented at:** `src/security/token_loader.py`

Public interface:
```python
load_token_record() -> dict      # full record, raises TokenUnavailable on any problem
get_dhan_access_token() -> str   # raw token string
get_dhan_client_id() -> str      # client_id from record
token_health() -> dict           # safe for logging (no secret values)
```

`TokenUnavailable` is raised (with a diagnostic message) when:
- Token file does not exist.
- File cannot be read (permissions error).
- JSON is malformed.
- Required fields are absent.
- `access_token` is empty.
- `expires_at` is in the past.

The loader never writes. It is purely a read path.

---

## SECTION 5 — Linux Automation

### systemd vs cron (selection rationale)

| Criterion | systemd timer | cron |
|---|---|---|
| Survives missed fires after reboot | **Yes** (`Persistent=true`) | No (missed fire is gone) |
| Built-in retry on failure | **Yes** (`Restart=on-failure`) | No (requires external wrapper) |
| Structured logging | **Yes** (`journalctl -u`) | Redirected to file only |
| Dependency on daemon | systemd (always present on Arch) | crond (optional, may not be installed) |
| Precision | Second-level | Minute-level |
| Privilege separation | **Yes** (`User=`, capability drops) | Depends on crontab owner |

**Decision: systemd timer.** On Arch Linux, systemd is init and is always present. cron is optional. `Persistent=true` guarantees token refresh even after a reboot that missed the fire window — this is critical for a market data system that must have fresh tokens before 09:15 IST NSE open.

### Timer schedule

- `OnCalendar=*-*-* 00:30:00 UTC` = 06:00:00 IST daily.
- Fires 3h 15m before NSE open, giving time for retry on outage.
- `RandomizedDelaySec=5min` prevents exact-second burst.
- `Persistent=true` catches up after reboot.

### Installation (user-level, no root required)

```bash
# 1. Set credentials in src/.env first
echo "DHAN_CLIENT_ID=your-id" >> src/.env
echo "DHAN_CLIENT_SECRET=your-secret" >> src/.env

# 2. Run the installer once
bash systemd/install.sh

# 3. Verify
python tools/check_dhan_token.py
systemctl --user list-timers dhan-token-refresh.timer
```

The installer:
- Copies `.service` and `.timer` to `~/.config/systemd/user/`.
- Runs `daemon-reload`.
- Enables and starts the timer.
- Runs a one-off token refresh immediately.

To view logs: `journalctl --user -u dhan-token-refresh`

---

## SECTION 6 — Observability (logs/token_refresh.log)

**Log file:** `logs/token_refresh.log` (chmod 600, created by the script on first run)

**Format:** `<ISO-timestamp> <LEVEL> <message>`

**Events logged:**
- `INFO  dhan_token_refresh: starting`
- `INFO  Acquiring token for client_id=<id> via <url>`
- `INFO  Token written: client_id=<id> token=<first8>...<last4> expires_at=<iso> path=<path>`
- `ERROR DHAN_CLIENT_ID is not set` (exit 1)
- `ERROR Token acquisition failed: <detail>` (exit 2)
- `ERROR Failed to write <path>: <detail>` (exit 3)

Token values are never written to the log. Only a masked form (`first8...last4`) appears on success.

systemd also captures stdout/stderr per run; view with:
```bash
journalctl --user -u dhan-token-refresh --since "today"
```

---

## SECTION 7 — Health Checks (tools/check_dhan_token.py)

**Implemented at:** `tools/check_dhan_token.py`

```bash
python tools/check_dhan_token.py         # human-readable
python tools/check_dhan_token.py --json  # machine-readable JSON
```

Checks:
1. Token file exists at `secrets/dhan_token.json`.
2. File permissions are exactly `600`.
3. JSON is well-formed.
4. All required fields present (`access_token`, `client_id`, `obtained_at`, `expires_at`, `version`).
5. `access_token` is non-empty.
6. Token has not expired (`expires_at` is in the future relative to current IST).
7. Reports TTL in hours and age since last refresh.

Exit code: 0=healthy, 1=action required.

Example healthy output:
```
[OK] Dhan token health check
  file:         /path/to/secrets/dhan_token.json
  permissions:  OK — Permissions OK (600)
  token:        OK — Token valid. TTL=17.3h
  expires_at:   2026-06-22T00:00:00+05:30
  ttl_hours:    17.3h remaining
  age_hours:    6.7h since last refresh
```

---

## SECTION 8 — Failure Recovery

| Failure mode | Behaviour |
|---|---|
| **API outage at 06:00 IST** | systemd retries twice (60s apart) per `StartLimitBurst=3`. If all fail, existing token (from yesterday) remains. Token valid until midnight IST — window for manual retry before market open. `journalctl` shows failure. |
| **Invalid/rejected credentials** | Script exits 2, logs error. Existing token untouched. Health check reports expired after midnight. |
| **Token expired, no file** | Factory falls back to `FixtureMarketAdapter` — advisory cycle continues in stub mode, no crash. `TokenUnavailable` is caught in `_get_dhan_adapter()`. |
| **Malformed token file** | `token_loader.load_token_record()` raises `TokenUnavailable`. Factory falls back to fixture. Health check reports FAIL. |
| **Machine rebooted, missed fire** | `Persistent=true` causes the timer to fire once on boot, refreshing the token immediately. |
| **Write permission denied** | Script exits 3, logs error. Existing token untouched (atomic write protects consistency). |
| **CAP-02 with only one live vendor** | `cross_verify(bars_a, bars_b)` compares Upstox vs fixture — will likely fail or pass vacuously. Same degradation as today (A-1 condition from EXT-002). CAP-02 still guards the gate. |

---

## SECTION 9 — Security Review

| Item | Status |
|---|---|
| `secrets/dhan_token.json` never committed | **CONFIRMED** — gitignored: `secrets/dhan_token.json` |
| Temp files never committed | **CONFIRMED** — gitignored: `secrets/.dhan_token_tmp_*` |
| `src/.env` never committed | **CONFIRMED** — pre-existing gitignore entry |
| Token value never printed to stdout | **CONFIRMED** — script prints only masked form to log |
| Token value never printed to log | **CONFIRMED** — log only shows `first8...last4` masked form |
| Least privilege: service runs as user | **CONFIRMED** — `User=virus` in `.service`, not root |
| Capability drops in service | **CONFIRMED** — `CapabilityBoundingSet=`, `NoNewPrivileges=true`, `PrivateTmp=true`, `ProtectSystem=strict` |
| `ReadWritePaths` scoped to minimum | **CONFIRMED** — only `secrets/` and `logs/` writable from the service |
| `DHAN_CLIENT_SECRET` protected | **CONFIRMED** — never leaves `src/.env` or environment; not written to any file other than `.env` |
| `DHAN_CLIENT_ID` in `config.py` as OPTIONAL_KEY | **CONFIRMED** — diagnostics prints `set`/`EMPTY`, never the value |
| Architecture boundaries unchanged | **CONFIRMED** — `tests/architecture` 6/6 passed; `src/security` is outside module scan |
| No broker execution path introduced | **CONFIRMED** — `DhanMarketAdapter` is read-only market data; no order routing |

---

## SECTION 10 — Verification

### Test suite

```
pytest                    → 51 passed (was 48; +3 new Dhan factory tests)
pytest tests/architecture → 6/6 passed (unchanged; boundary enforcement intact)
```

New tests added in `tests/unit/adapters/test_factory.py`:
- `test_market_adapter_variant_b_defaults_to_fixture_no_client_id` — no DHAN_CLIENT_ID → FixtureMarketAdapter
- `test_market_adapter_variant_b_falls_back_to_fixture_when_token_missing` — token file absent → FixtureMarketAdapter
- `test_market_adapter_variant_b_selects_dhan_when_configured` — valid token + DHAN_CLIENT_ID → DhanMarketAdapter

### File verification (runtime artefacts not committed)

```bash
# Confirm secrets/dhan_token.json is gitignored
git check-ignore -v secrets/dhan_token.json
# → .gitignore:23:secrets/dhan_token.json    secrets/dhan_token.json

# Confirm secrets/ and logs/ directories are tracked (via .gitkeep)
git ls-files secrets/ logs/
# → logs/.gitkeep
# → secrets/.gitkeep

# Confirm no token in src/.env committed
git check-ignore -v src/.env
# → .gitignore:16:src/.env    src/.env
```

### Token refresh simulation (run once Dhan KYC + credentials are available)

```bash
# Step 1: Set credentials
echo "DHAN_CLIENT_ID=your-id" >> src/.env
echo "DHAN_CLIENT_SECRET=your-secret" >> src/.env

# Step 2: Run refresh
python scripts/generate_dhan_token.py
# Expected: OK: Dhan token refreshed. client_id=... expires_at=... path=secrets/dhan_token.json

# Step 3: Health check
python tools/check_dhan_token.py
# Expected: [OK] Dhan token health check ...

# Step 4: Verify file permissions
stat secrets/dhan_token.json
# Expected: File: secrets/dhan_token.json   Mode: 0600

# Step 5: Verify adapter selection
python -c "
from src.adapters import factory
adapter = factory.get_market_adapter(variant='b')
print(type(adapter).__name__)
# Expected: DhanMarketAdapter
"

# Step 6: Install timer
bash systemd/install.sh
systemctl --user list-timers dhan-token-refresh.timer
```

### Reboot persistence verification

```bash
# Simulate reboot by stopping the timer, waiting past fire time, then re-enabling.
systemctl --user stop dhan-token-refresh.timer
# ... wait past 06:00 IST ...
systemctl --user start dhan-token-refresh.timer
# Persistent=true causes immediate catch-up fire.
journalctl --user -u dhan-token-refresh --since "today"
# Expected: token refresh log entry within seconds of start.
```

---

## Constitutional compliance

| Constraint | Met? |
|---|---|
| No SDM/SADR/ADR modification | YES |
| No capability boundary change | YES |
| No audit chain modification | YES |
| No broker execution capability | YES |
| Architecture frozen | YES |
| `tests/architecture` still 6/6 | YES |
| No secrets committed | YES |
| No external DB dependency (Redis/Postgres/Supabase) | YES — plain JSON file, stdlib only |
| Token lifecycle invisible after setup | YES — systemd handles rotation automatically |
| Credential insertion only | YES — set `DHAN_CLIENT_ID`/`DHAN_CLIENT_SECRET` in `.env`, no code change |

---

## Known verification boundaries (require Dhan KYC completion)

| Item | Status | Resolution |
|---|---|---|
| Exact Dhan token endpoint | `https://api.dhan.co/v2/token` (configurable via `DHAN_TOKEN_URL` env var) | Verify from Dhan API welcome email after KYC |
| Dhan response field casing (`accessToken` vs `access_token`) | Both handled in `generate_dhan_token.py` | Verify once against real response |
| RELIANCE Dhan security ID | `"1333"` in `dhan_instruments.py` | Verify from Dhan instruments CSV after KYC |
| True 24h vs midnight-IST expiry | Computed as next midnight IST | Adjust `_expires_at_midnight_ist()` if needed |
| Dhan historical candle response shape | `open[], high[], low[], close[], volume[]` arrays | Verify against actual API response |

All unknowns are bounded to a single file each (`generate_dhan_token.py` endpoint/field, `dhan_instruments.py` security ID, `market.py` response mapping). No architectural change is needed to accommodate them.

---

*DHAN_TOKEN_AUTOMATION_REPORT — implementation complete. Awaiting Dhan KYC completion to validate live token acquisition and adapter smoke test.*
