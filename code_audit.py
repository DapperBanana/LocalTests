
import math

def is_perfect_square(num):
    # Check if the square root of the number is an integer
    sqrt_num = math.sqrt(num)
    if sqrt_num.is_integer():
        return True
    else:
        return False

# Test cases
num1 = 16
num2 = 25
num3 = 10

print(f"{num1} is a perfect square: {is_perfect_square(num1)}")
print(f"{num2} is a perfect square: {is_perfect_square(num2)}")
print(f"{num3} is a perfect square: {is_perfect_square(num3)}")
