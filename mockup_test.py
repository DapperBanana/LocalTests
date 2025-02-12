
import math

def find_square_root(num):
    if num < 0:
        return "Square root is not real"
    else:
        return math.sqrt(num)

# Taking input from the user
num = float(input("Enter a number: "))

# Calling the function to find square root
result = find_square_root(num)

# Displaying the result
print(f"The square root of {num} is {result}")
