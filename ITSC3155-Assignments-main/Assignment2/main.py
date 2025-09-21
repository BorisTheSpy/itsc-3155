import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")
    while choice != "off":
        if choice == "small" and sandwich_maker_instance.check_resources(recipes["small"]["ingredients"]):
            if(cashier_instance.transaction_result(cashier_instance.process_coins(), recipes["small"]["cost"])):
                sandwich_maker_instance.make_sandwich("small", recipes["small"]["ingredients"])
        elif choice == "medium" and sandwich_maker_instance.check_resources(recipes["medium"]["ingredients"]):
            if(cashier_instance.transaction_result(cashier_instance.process_coins(), recipes["medium"]["cost"])):
                sandwich_maker_instance.make_sandwich("medium", recipes["medium"]["ingredients"])
        elif choice == "large" and sandwich_maker_instance.check_resources(recipes["large"]["ingredients"]):
            if(cashier_instance.transaction_result(cashier_instance.process_coins(), recipes["large"]["cost"])):
                sandwich_maker_instance.make_sandwich("large", recipes["large"]["ingredients"])
        elif choice == "off":
            break
        elif choice == "report":
            print("Bread: " + str(resources["bread"]) + " slice(s)\n"
                    "Ham: " + str(resources["ham"]) + " slice(s)\n"
                  "Cheese: " + str(resources["cheese"]) + " pound(s)\n")

        choice = input("What would you like? (small/ medium/ large/ off/ report): ") 

if __name__=="__main__":
    main()
