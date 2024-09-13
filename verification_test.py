
import math

def is_perfect_square(num):
    # Check if the square root of the number is an integer
    sqrt = math.isqrt(num)
    return sqrt * sqrt == num

# Get user input
num = int(input("Enter a number: "))

# Check if the number is a perfect square
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
