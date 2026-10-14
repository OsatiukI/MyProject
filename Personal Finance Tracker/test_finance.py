import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "finance_tracker",
    Path(__file__).with_name("Personal Finance Tracker.py")
)
finance_tracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(finance_tracker)


def test_calculate_income():
    transactions = [
        {"transaction_type": "income", "amount": 1000},
        {"transaction_type": "expense", "amount": 200},
        {"transaction_type": "income", "amount": 500},
    ]

    assert finance_tracker.calculate_income(transactions) == 1500