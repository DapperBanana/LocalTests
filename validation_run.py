
import math

def calculate_square_root(num):
    if num < 0:
        return "Invalid input. Please enter a non-negative number."
    else:
        return math.sqrt(num)

# Main program
number = float(input("Enter a number to calculate its square root: "))
result = calculate_square_root(number)

print(f"The square root of {number} is {result}")
