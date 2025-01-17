class BankAccount:
    def __init__(self, account_balance: float, initial_balance=0):
        self._account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit should be positive.")

    def withdraw(self, amount: float):

        if amount < self._account_balance:
            self._account_balance -= amount

        else:

            return f'"Insufficient funds"'

    def display_balance(self):

        print(f"Current Balance:${self._account_balance}")
