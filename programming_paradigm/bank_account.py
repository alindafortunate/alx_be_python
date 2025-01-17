class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self._account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit should be positive.")

    def withdraw(self, amount: float):

        if amount > self._account_balance:
            print("Insufficient funds.")
            return False
        self._account_balance -= amount
        # return True
        return f"Withdrew:${amount}"

    def display_balance(self):

        print(f"Current Balance: ${self._account_balance:.2f}")


# account = BankAccount(250)
# account.display_balance()
