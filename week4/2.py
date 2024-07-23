def add(a,b):
    return a+b
def subtract(a,b):
    if b > a:
        return b-a
    else:
        return a-b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        print("Division by zero not possible ")
    else:
        return a/b

try:
    num1 = int(input("Enter the first number: "))
except:
    print("Enter an integer")
    num1 = int(input("Enter the first number: "))

try:
    num2 = int(input("Enter the second number: "))
except:
    print("Enter an integer")
    num2 = int(input("Enter the second number: "))



while True:
    try:
        operation = int(input("""
        Enter your Choice of the operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. division
        """))
    except:
        operation = int(input("""
        Enter your Choice of the:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. division
        """))
    if operation == 1:
        print(f"the sum of {num1} and {num2} is ", add(num1, num2))
        break
    elif operation == 2:
        print(f"the difference between {num1} and {num2} is ", subtract(num1, num2))
        break
    elif operation == 3:
        print(f"the product of {num1} and {num2} is ", multiply(num1, num2))
        break
    elif operation == 4:
        print(f"the result of {num1} divided by {num2} is ", divide(num1, num2))
        break
    else:
        print("Enter a valid operation")
