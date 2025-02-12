
import math

def is_perfect_square(num):
    square_root = math.isqrt(num)
    return square_root * square_root == num

num = int(input("Enter a number to check if it is a perfect square: "))

if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
