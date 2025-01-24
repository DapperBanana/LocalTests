
import math

def calculate_area_of_triangle(side1, side2, side3):
    # calculate the semi-perimeter of the triangle
    s = (side1 + side2 + side3) / 2
    
    # calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    
    return area

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

area = calculate_area_of_triangle(side1, side2, side3)

print("The area of the triangle is: ", area)
