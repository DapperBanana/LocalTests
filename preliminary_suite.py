
import math

def find_square_root(num):
    if num < 0:
        return "Square root of negative numbers is not real."
    else:
        return math.sqrt(num)

# Taking input from the user
num = float(input("Enter a number: "))

# Calculating square root
result = find_square_root(num)

print(f"The square root of {num} is: {result}")
