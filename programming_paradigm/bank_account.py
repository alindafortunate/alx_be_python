class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self._account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):

        self._account_balance += amount

    def withdraw(self, amount):

        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):

        print(f"Current Balance: ${self._account_balance:.2f}")
