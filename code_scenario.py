
import math

def is_perfect_square(number):
    if number < 0:
        return False
    
    sqrt = math.isqrt(number)
    return sqrt * sqrt == number

number = int(input("Enter a number: "))
if is_perfect_square(number):
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")
