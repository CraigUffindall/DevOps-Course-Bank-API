"""Unit tests for bank.py"""

from datetime import datetime
import pytest

from bank_api.bank import Bank


@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')

def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0

def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'

def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')

def test_add_funds_success(bank: Bank):
    # arrange
    bank.create_account('Name 1')

    # act
    bank.add_funds('Name 1', 500)

    # assert
    assert len(bank.transactions) == 1
    assert bank.transactions[0].account.name == 'Name 1'
    assert bank.transactions[0].amount == 500

def test_add_funds_with_non_existing_account(bank: Bank):
    # arrange
    bank.create_account('Name 1')

    # act/assert
    with pytest.raises(ValueError):
        bank.add_funds('Name 2', 500)

    assert len(bank.transactions) == 0

def test_add_funds_with_non_blank_account(bank: Bank):
    # arrange
    bank.create_account('Name 1')

    # act/assert
    with pytest.raises(ValueError):
        bank.add_funds('', 500)

    assert len(bank.transactions) == 0

def test_add_funds_with_0_amount(bank: Bank):
    # arrange
    bank.create_account('Name 1')

    # act/assert
    with pytest.raises(ValueError):
        bank.add_funds('Name 1', 0)

    assert len(bank.transactions) == 0

def test_add_funds_with_negative_amount(bank: Bank):
    # arrange
    bank.create_account('Name 1')

    # act/assert
    with pytest.raises(ValueError):
        bank.add_funds('Name 1', -20)

    assert len(bank.transactions) == 0

def test_create_account_with_space_characters(bank: Bank):
    # act/assert
    with pytest.raises(ValueError):
        bank.create_account('   ')