class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self._account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.amount = amount
        balance = self.amount + self._account_balance
        self.initial_balance = balance
        return f"{self.initial_balance}"

    def withdraw(self, amount):
        self.amount = amount
        if self._account_balance > self.amount:
            balance = self._account_balance - self.amount
            self.initial_balance = balance
            return f"{self.initial_balance}"
        else:
            return f"Insufficient balance"

    def display_balance(self):

        return f"Current balance is:${self.initial_balance}"


if __name__ == "__main__":

    account = BankAccount(100)
    print(account.deposit(100))
    print(account.withdraw(60))
    print(account.display_balance())
