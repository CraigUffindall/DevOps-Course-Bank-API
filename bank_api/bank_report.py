from bank_api.bank import Bank

class BankReport:
    def __init__(self, bank: Bank):
        self.bank = bank

    def get_balance(self, name: str) -> int:
        balance = 0

        for trans in self.bank.transactions:
            if trans.account.name == name:
                balance = balance + trans.amount

        return balance