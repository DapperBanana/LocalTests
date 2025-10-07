
import math

def calculate_area(a, b, c):
    # calculate semi-perimeter
    s = (a + b + c) / 2
    
    # calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Input sides of the triangle
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

# Calculate area
area = calculate_area(side1, side2, side3)

print(f"The area of the triangle is {area}")
