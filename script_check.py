
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input from user
num = int(input("Enter a number to calculate its factorial: "))

# Calculate and display factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
