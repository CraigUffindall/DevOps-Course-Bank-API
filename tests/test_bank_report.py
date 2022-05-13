"""Unit tests for bank_report.py"""

import pytest

from bank_api.bank_report import BankReport
from bank_api.bank import Bank

@pytest.fixture
def bank_report() -> BankReport:
    bank = Bank()

    bank.create_account('Account1')
    bank.add_funds('Account1', 100)
    bank.add_funds('Account1', 200)

    bank.create_account('Account2')
    bank.add_funds('Account2', 1000)

    return BankReport(bank)

def test_get_balance_zero(bank_report: BankReport):
    # act
    balance = bank_report.get_balance('demo')
    
    # assert
    assert balance == 0

def test_get_balance_over_zero(bank_report: BankReport):
    # act
    balance = bank_report.get_balance('Account1')
    
    # assert
    assert balance == 300