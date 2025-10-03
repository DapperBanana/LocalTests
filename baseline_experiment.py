
import math

def calculate_area(side1, side2, side3):
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

area = calculate_area(side1, side2, side3)
print("The area of the triangle is: ", round(area, 2))
