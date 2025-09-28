
def add(num, num1): #simple function for adding two numbers
    return num + num1

def multiply(num, num1): #simple function for multiplying two numbers
    return num * num1

def subtract(num, num1): #simple function for subtracting two numbers
    return num - num1

def divide(num, num1): #simple function for dividing two numbers
    return num / num1

def main():
    operation = input("Choose an operation: \n\tAdd/Subtract/Multiply/Divide (a/s/m/d): ")
    while (operation != "a" and operation != "s" and operation != "m" and operation != "d"): 
        #while loop ensures good input

        print("Invalid Input!\n")
        operation = input("Choose an operation: \n\tAdd/Subtract/Multiply/Divide (a/s/m/d): ")
    
    num = float(input("Enter the first number: "))
    num1 = float(input("Enter the second number: "))

    #Choosing the correct function to use depending on users input
    if operation == "a":
        print(add(num, num1))
    elif operation == "s":
        print(subtract(num, num1))
    elif operation == "m":
        print(multiply (num, num1))
    elif operation == "d":
        print(divide(num, num1))

if __name__ == '__main__':
    main()
