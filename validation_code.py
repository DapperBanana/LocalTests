
import math

def find_square_root(num):
    return math.sqrt(num)

try:
    num = float(input("Enter a number to find its square root: "))
    if num < 0:
        print("Square root is not defined for negative numbers.")
    else:
        result = find_square_root(num)
        print(f"The square root of {num} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
