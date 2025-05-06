
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking input from user
num = int(input("Enter a number: "))

# Checking if the number is negative
if num < 0:
    print("Factorial of a negative number is not defined.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
