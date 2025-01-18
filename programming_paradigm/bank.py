# Demonstration of public, protected and private properties.
class Bank:
    def __init__(self, balance):
        self.bank_name = "Br&Fr Investments."
        self.__bank_balance = balance

    def depost(self, amount):
        self.__bank_balance += amount

    def display_balance(self):
        print(self.__bank_balance)


opio = Bank(100)
print(opio.bank_name)
opio.depost(20)
opio.display_balance()
print(opio._Bank__bank_balance)
