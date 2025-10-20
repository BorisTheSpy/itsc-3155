from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    
    title = "First Citizens Checking Account"

    def __init__(self, name, curBalance, minBalance, accNum, routeNum):
        super().__init__(name, curBalance, minBalance)
        self.accNum = accNum
        self.routeNum = routeNum

    def print_customer_information(self):    
        print(self.title)
        print("Name: " + self.name)
        print("Balance: " + str(self.curBalance))
        print("Account Number: " + str(self.accNum))
        print("Route Number: " + str(self.routeNum) + "\n")
