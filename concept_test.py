
import math

def check_perfect_square(num):
    if num < 0:
        return False
    
    sqrt_num = math.isqrt(num)
    
    return sqrt_num * sqrt_num == num

num = int(input("Enter a number: "))
if check_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
