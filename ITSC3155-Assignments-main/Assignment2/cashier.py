class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        ldollar = input("How many large dollars?: ")
        hdollar = input("How many half dollars?: ")
        quarters = input("How many quarters?: ")
        nickles = input("How many nickles?: ")
        return float(ldollar) + float(hdollar) * .5 + float(quarters) * .25 + float(nickles) * .05

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            print(f"Here is ${coins - float(cost):.2f} in change.")
            return True
