
import math

def find_square_root(number):
    if number < 0:
        return "Square root is not defined for negative numbers"
    else:
        return math.sqrt(number)

# Input number from user
number = float(input("Enter a number: "))

# Find square root
result = find_square_root(number)

# Print the result
print(f"The square root of {number} is {result}")
