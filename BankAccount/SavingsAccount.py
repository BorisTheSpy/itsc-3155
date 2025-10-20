from BankAccount import BankAccount

class SavingsAccount(BankAccount):

    title = "First Citizens Savings Account"
    interest = .05

    def __init__(self, name, curBalance, minBalance, accNum, routeNum):
        super().__init__(name, curBalance, minBalance)
        self.accNum = accNum
        self.routeNum = routeNum

    def earn_interest(self):
        print(self.name + " Earned Interest!")
        self.curBalance = self.curBalance * self.interest + self.curBalance

    def print_customer_information(self):
        print(self.title)
        print("Name: " + self.name)
        print("Balance: " + str(self.curBalance))
        print("Account Number: " + str(self.accNum))
        print("Route Number: " + str(self.routeNum) + "\n")