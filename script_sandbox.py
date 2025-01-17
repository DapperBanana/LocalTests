
import math

def isPerfectSquare(num):
    if num < 0:
        return False
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num

num = int(input("Enter a number: "))
if isPerfectSquare(num):
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")
