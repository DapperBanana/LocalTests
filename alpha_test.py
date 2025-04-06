
import math

def is_perfect_square(num):
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
