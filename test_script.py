
import math

def area_of_triangle(side1, side2, side3):
    # calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2
    
    # calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    
    return area

# input sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# calculate and print the area of the triangle
triangle_area = area_of_triangle(side1, side2, side3)
print(f"The area of the triangle is: {triangle_area}")
