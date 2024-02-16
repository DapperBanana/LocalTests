
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the GCD
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)
