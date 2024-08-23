
import math

def is_perfect_square(num):
    if num < 0:
        return False
    
    root = math.isqrt(num)
    return root * root == num

num = int(input("Enter a number to check if it is a perfect square: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
