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

        if self._account_balance > amount:
            self._account_balance -= amount

            return f"Withdrew:${amount}"
        elif self._account_balance < amount:
            print("Insufficient funds.")
            

    def display_balance(self):

        print(f"Current Balance:${self._account_balance}")
