def fibonacci(n):
    if n <= 0:
        return "Input should be a positive."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input("Enter a positive: "))
    if n <= 0:
        print("Please enter a positive.")
    else:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
except ValueError:
    print("Invalid input. Please enter a positive.")
