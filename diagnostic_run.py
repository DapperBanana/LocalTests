
def calculate_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return calculate_gcd(num2, num1 % num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = calculate_gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd}")
