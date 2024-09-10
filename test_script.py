
import math

def find_square_root(num):
    return math.sqrt(num)

# Input number from user
num = float(input("Enter a number to find its square root: "))

# Check if the number is positive
if num >= 0:
    result = find_square_root(num)
    print(f"The square root of {num} is {result}")
else:
    print("Please enter a positive number.")
