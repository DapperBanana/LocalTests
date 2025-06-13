
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")
