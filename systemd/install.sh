#!/usr/bin/env bash
# Install Dhan token refresh systemd timer (run once after initial setup).
#
# Usage:
#   cd /mnt/data/rj/AI_analyst_Market_research
#   bash systemd/install.sh
#
# What this does:
#   1. Copies .service and .timer to ~/.config/systemd/user/ (user-level units).
#   2. Reloads the systemd daemon.
#   3. Enables and starts the timer.
#   4. Runs a one-off token refresh immediately.
#   5. Shows timer status.
#
# Requires:
#   - DHAN_CLIENT_ID and DHAN_CLIENT_SECRET must be set in src/.env first.
#   - requests must be installed: pip install --user requests

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SYSTEMD_USER_DIR="$HOME/.config/systemd/user"
SERVICE_NAME="dhan-token-refresh"

echo "[install] repo root: $REPO_ROOT"
echo "[install] installing to: $SYSTEMD_USER_DIR"

mkdir -p "$SYSTEMD_USER_DIR"

# Expand the WorkingDirectory placeholder in the service file before copying.
sed "s|/mnt/data/rj/AI_analyst_Market_research|$REPO_ROOT|g" \
    "$REPO_ROOT/systemd/${SERVICE_NAME}.service" \
    > "$SYSTEMD_USER_DIR/${SERVICE_NAME}.service"

cp "$REPO_ROOT/systemd/${SERVICE_NAME}.timer" \
   "$SYSTEMD_USER_DIR/${SERVICE_NAME}.timer"

echo "[install] reloading systemd user daemon"
systemctl --user daemon-reload

echo "[install] enabling timer"
systemctl --user enable "${SERVICE_NAME}.timer"

echo "[install] starting timer"
systemctl --user start "${SERVICE_NAME}.timer"

echo "[install] running one-off token refresh now"
python3 "$REPO_ROOT/scripts/generate_dhan_token.py"

echo ""
echo "[install] timer status:"
systemctl --user status "${SERVICE_NAME}.timer" --no-pager || true

echo ""
echo "[install] next scheduled fires:"
systemctl --user list-timers "${SERVICE_NAME}.timer" --no-pager || true

echo ""
echo "[install] done. To check token health: python tools/check_dhan_token.py"
echo "[install] To view logs:                 journalctl --user -u ${SERVICE_NAME}"
