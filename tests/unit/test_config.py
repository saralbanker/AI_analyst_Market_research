import pytest

from src import config


REQUIRED_TRUE_FALSE = {
    "APP_ENV": "development",
    "AUDIT_CHAIN_ENABLED": "true",
    "GOVERNANCE_ENABLED": "true",
    "PAPER_TRADING_ENABLED": "true",
    "AUTO_EXECUTION_ENABLED": "false",
    "BROKER_EXECUTION_ENABLED": "false",
}


@pytest.fixture
def clean_env(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "ENV_FILE", tmp_path / "does_not_exist.env")
    for key in config.ALL_KEYS:
        monkeypatch.delenv(key, raising=False)


def test_missing_required_key_raises_config_error(clean_env, monkeypatch):
    for key, value in REQUIRED_TRUE_FALSE.items():
        if key != "APP_ENV":
            monkeypatch.setenv(key, value)
    # APP_ENV deliberately left unset

    with pytest.raises(config.ConfigError, match="APP_ENV"):
        config.load_config()


def test_invalid_boolean_raises_config_error(clean_env, monkeypatch):
    for key, value in REQUIRED_TRUE_FALSE.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("AUDIT_CHAIN_ENABLED", "not-a-bool")

    with pytest.raises(config.ConfigError, match="AUDIT_CHAIN_ENABLED"):
        config.load_config()


def test_empty_optional_vendor_keys_are_fine(clean_env, monkeypatch):
    for key, value in REQUIRED_TRUE_FALSE.items():
        monkeypatch.setenv(key, value)
    # All OPTIONAL_KEYS (vendor credentials) left unset/empty.

    merged = config.load_config()

    for key in config.OPTIONAL_KEYS:
        assert merged.get(key, "") == ""


def test_diagnostics_does_not_print_secret_values(clean_env, monkeypatch):
    for key, value in REQUIRED_TRUE_FALSE.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("FINNHUB_API_KEY", "super-secret-value")

    merged = config.load_config()
    output = config.diagnostics(merged)

    assert "super-secret-value" not in output
    assert "FINNHUB_API_KEY=set" in output
