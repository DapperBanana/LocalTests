
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def find_lcm(num1, num2):
    lcm = (num1 * num2) // gcd(num1, num2)
    return lcm

# Example usage:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM of", num1, "and", num2, "is", find_lcm(num1, num2))
