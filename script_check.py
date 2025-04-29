
import math

def square_root(num):
    return math.sqrt(num)

num = float(input("Enter a number: "))
if num < 0:
    print("Invalid input. Please enter a positive number.")
else:
    result = square_root(num)
    print(f"The square root of {num} is {result}")
