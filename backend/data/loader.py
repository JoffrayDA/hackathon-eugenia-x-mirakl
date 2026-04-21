import json
from pathlib import Path

_BASE = Path(__file__).parent / "mock"


def _load(filename: str) -> dict | list:
    with open(_BASE / filename, encoding="utf-8") as f:
        return json.load(f)


def get_orders() -> dict:
    return {o["id"]: o for o in _load("orders.json")}


def get_customers() -> dict:
    return {c["id"]: c for c in _load("customers.json")}


def get_merchant() -> dict:
    return _load("merchant.json")


def get_carriers() -> dict:
    return _load("carrier_mock.json")


def get_scenarios() -> dict:
    return _load("scenarios.json")
