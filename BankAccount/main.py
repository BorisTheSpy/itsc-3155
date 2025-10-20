import BankAccount
from CheckingAccount import CheckingAccount 
from SavingsAccount import SavingsAccount

katie_SA = SavingsAccount("Katie", 1000000, 500, 6767, 6769)
katie_CA = CheckingAccount("Katie", 500000.01, 100, 6768, 6770)
katie_CA.print_customer_information()
katie_SA.print_customer_information()
katie_SA.earn_interest()
katie_SA.print_customer_information()
