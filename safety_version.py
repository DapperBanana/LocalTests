
import math

def square_root(num):
    return math.sqrt(num)

# Taking input from user
num = float(input("Enter a number: "))

if num < 0:
    print("Square root is not defined for negative numbers")
else:
    result = square_root(num)
    print(f"The square root of {num} is {result}")
