
import math

def isPerfectSquare(num):
    sqrt = math.isqrt(num)
    return sqrt ** 2 == num

num = int(input("Enter a number: "))
if isPerfectSquare(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
