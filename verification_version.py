
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n by factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Test the function
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
