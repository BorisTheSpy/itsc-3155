
class BankAccount:
    title = "First Citizens Bank Account"

    def __init__(self, name, curBalance, minBalance):
        self.name = name
        self.curBalance = curBalance
        self.minBalance = minBalance

    def deposit(self, amount):
        self.curBalance += amount
        print(str(amount) + " deposited")
        print("New Balance: " + str(self.curBalance) + "\n")

    def withdraw(self, amount):
        if self.curBalance <= self.minBalance or (self.curBalance - amount) <= 100:
            print("You don't have enough money!")
            print("Current Balance: " + str(self.curBalance) + "\n")
        else:
            self.curBalance -= amount
            print(str(amount) + " withdrained")
            print("New Balance: " + str(self.curBalance) + "\n")

    def print_customer_information(self):
        print(self.title)
        print("Name: " + self.name)
        print("Balance: " + str(self.curBalance) + "\n")

"""
james = BankAccount("James", 5000, 100)
katie = BankAccount("Katie", 6767, 100)

james.print_customer_information()
katie.print_customer_information()
if james.curBalance > katie.curBalance:
    print("James if richer than Katie\n")
else:
    print("Katie is richer than James\n")

james.deposit(1767)
james.withdraw(6700)
"""
