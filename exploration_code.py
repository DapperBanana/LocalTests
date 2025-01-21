
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def find_lcm(x, y):
    gcd = find_gcd(x, y)
    return x * y // gcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", find_lcm(num1, num2))
