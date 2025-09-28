
def add(num, num1):
    return num + num1

def multiply(num, num1):
    return num * num1

def subtract(num, num1):
    return num - num1

def divide(num, num1):
    return num / num1

def combine(num, num1):
    return float(str(num) + str(num1))

def main():
    operation = input("Choose an operation: \n\tAdd/Subtract/Multiply/Divide (a/s/m/d): ")
    num = float(input("Enter the first number: "))
    num1 = float(input("Enter the second number: "))
    if operation == "a" and operation != "s" and operation != "m" and operation != "d":
        print(num + num1)
    elif operation == "s" and operation != "a" and operation != "m" and operation != "d":
        print(num - num1)
    elif operation == "m" and operation != "s" and operation != "a" and operation != "d":
        print(num * num1)
    elif operation == "d" and operation != "s" and operation != "m" and operation != "a":
        print(num / num1)

if __name__ == '__main__':
    main()
