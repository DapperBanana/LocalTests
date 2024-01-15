
import math

def calculate_octagon_area(s):
    area = 2 * (1 + math.sqrt(2)) * s**2
    return area

# Reading the length of the side
s = float(input("Enter the length of the side of the octagon: "))

# Calculating the area
area = calculate_octagon_area(s)

# Displaying the result
print("The area of the octagon is:", area)
