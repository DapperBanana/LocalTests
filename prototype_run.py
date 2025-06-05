
import math

def find_square_root(num):
    square_root = math.sqrt(num)
    return square_root

# Input number from user
num = float(input("Enter a number: "))

# Calculate square root
result = find_square_root(num)

# Display the result
print(f"The square root of {num} is {result}")
