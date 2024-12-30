
import math

def find_square_root(num):
    if num < 0:
        return "Square root of a negative number is not possible"
    else:
        return math.sqrt(num)

num = float(input("Enter a number: "))
result = find_square_root(num)

print(f"The square root of {num} is: {result}")
