import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "finance_tracker",
    Path(__file__).with_name("Personal Finance Tracker.py")
)

finance_tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(finance_tracker)


def test_calculate_income():
    original_transactions = finance_tracker.transactions

    finance_tracker.transactions = [
        {"transaction_type": "income", "amount": 1000},
        {"transaction_type": "expense", "amount": 200},
        {"transaction_type": "income", "amount": 500},
    ]

    try:
        assert finance_tracker.calculate_income() == 1500
    finally:
        finance_tracker.transactions = original_transactions


def test_calculate_balance():
    original_transactions = finance_tracker.transactions

    finance_tracker.transactions = [
        {"transaction_type": "income", "amount": 1000},
        {"transaction_type": "expense", "amount": 200},
        {"transaction_type": "income", "amount": 500},
    ]

    try:
        assert finance_tracker.calculate_balance() == 1300
    finally:
        finance_tracker.transactions = original_transactions


def test_calculate_expenses():
    original_transactions = finance_tracker.transactions

    finance_tracker.transactions = [
        {"transaction_type": "income", "amount": 1000},
        {"transaction_type": "expense", "amount": 200},
        {"transaction_type": "income", "amount": 500},
        {"transaction_type": "expense", "amount": 100},
    ]

    try:
        assert finance_tracker.calculate_expenses() == 300
    finally:
        finance_tracker.transactions = original_transactions


def test_calculate_expenses_by_category():
    original_transactions = finance_tracker.transactions

    finance_tracker.transactions = [
        {
            "transaction_type": "expense",
            "amount": 50,
            "category": "Food",
            "description": "Lunch",
        },
        {
            "transaction_type": "expense",
            "amount": 30,
            "category": "Food",
            "description": "Dinner",
        },
        {
            "transaction_type": "expense",
            "amount": 20,
            "category": "Transport",
            "description": "Bus",
        },
        {
            "transaction_type": "income",
            "amount": 100,
            "category": "Salary",
            "description": "Monthly salary",
        },
    ]

    try:
        assert finance_tracker.calculate_expenses_by_category("Food") == 80
    finally:
        finance_tracker.transactions = original_transactions


def test_validate_transaction():
    valid_transaction = {
        "transaction_type": "expense",
        "amount": 50,
        "category": "Food",
        "description": "Lunch",
    }

    assert finance_tracker.validate_transaction(valid_transaction) is True


def test_validate_transaction_rejects_invalid_amount():
    invalid_transaction = {
        "transaction_type": "expense",
        "amount": -50,
        "category": "Food",
        "description": "Lunch",
    }

    assert finance_tracker.validate_transaction(invalid_transaction) is False


def test_validate_transaction_rejects_empty_category():
    transaction = {
        "transaction_type": "expense",
        "amount": 50,
        "category": "   ",
        "description": "Lunch",
    }

    assert finance_tracker.validate_transaction(transaction) is False


def test_validate_transaction_rejects_invalid_type():
    transaction = {
        "transaction_type": "transfer",
        "amount": 50,
        "category": "Food",
        "description": "Lunch",
    }

    assert finance_tracker.validate_transaction(transaction) is False


def test_validate_transaction_rejects_nan():
    transaction = {
        "transaction_type": "expense",
        "amount": float("nan"),
        "category": "Food",
        "description": "Lunch",
    }

    assert finance_tracker.validate_transaction(transaction) is False


def test_load_transactions_valid_file(tmp_path, monkeypatch):
    import json

    transaction = {
        "transaction_type": "income",
        "amount": 1000,
        "category": "Salary",
        "description": "Monthly salary",
    }

    file_path = tmp_path / "transactions.json"
    file_path.write_text(
        json.dumps([transaction]),
        encoding="utf-8",
    )

    monkeypatch.chdir(tmp_path)

    loaded_transactions, data_loaded = finance_tracker.load_transactions()

    assert data_loaded is True
    assert loaded_transactions == [transaction]


def test_load_transactions_corrupted_file(tmp_path, monkeypatch):
    file_path = tmp_path / "transactions.json"
    file_path.write_text("{invalid json", encoding="utf-8")

    monkeypatch.chdir(tmp_path)

    loaded_transactions, data_loaded = finance_tracker.load_transactions()

    assert loaded_transactions == []
    assert data_loaded is False


def test_load_transactions_invalid_transaction(tmp_path, monkeypatch):
    import json

    transaction = {
        "transaction_type": "expense",
        "amount": -50,
        "category": "Food",
        "description": "Lunch",
    }

    file_path = tmp_path / "transactions.json"
    file_path.write_text(json.dumps([transaction]), encoding="utf-8")

    monkeypatch.chdir(tmp_path)

    loaded_transactions, data_loaded = finance_tracker.load_transactions()

    assert loaded_transactions == []
    assert data_loaded is False


def test_load_transactions_missing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    loaded_transactions, data_loaded = finance_tracker.load_transactions()

    assert loaded_transactions == []
    assert data_loaded is True