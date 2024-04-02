
import math

def is_perfect_square(num):
    square_root = math.sqrt(num)
    return square_root.is_integer()

# Get input from user
num = int(input("Enter a number: "))

if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
