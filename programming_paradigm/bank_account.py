class BankAccount:
    def __init__(self, account_balance: float, initial_balance=0):
        self._account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount: float):

        self._account_balance += amount

        return f"{self._account_balance}"

    def withdraw(self, amount: float):

        if self._account_balance > amount:
            self._account_balance -= amount

            return f"{self._account_balance}"
        else:
            return f"Insufficient balance"

    def display_balance(self):

        return f"Current Balance:${self._account_balance}"














# if __name__ == "__main__":

#     account = BankAccount(100)
#     print(account.deposit(100))
#     print(account.withdraw(60))
#     print(account.display_balance())
