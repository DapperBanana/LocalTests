
import math

def is_perfect_square(num):
    # Check if the square root of the number is an integer
    if math.sqrt(num).is_integer():
        return True
    else:
        return False

# Test the function
num = 16
if is_perfect_square(num):
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")
