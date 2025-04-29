
import math

num = float(input("Enter a number: "))

if num < 0:
    print("Please enter a positive number.")
else:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")
