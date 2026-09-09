"""Runtime secret management — token loading only.

This package is outside the MODULES boundary-scan (only mod01..mod11 are
scanned). It provides a thin, read-only interface over the persisted token
file written by scripts/generate_dhan_token.py.

No module in mod01..mod11 should import this package directly. Adapters
(src/adapters/) consume it when constructing vendor clients.
"""
