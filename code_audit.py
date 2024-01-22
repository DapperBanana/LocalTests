
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate GCD
gcd = calculate_gcd(num1, num2)

# Print the result
print("The greatest common divisor (GCD) of", num1, "and", num2, "is", gcd)
