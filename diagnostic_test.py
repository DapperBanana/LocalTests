
import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

# Input the three sides of the triangle
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

# Calculate the area of the triangle
area = calculate_area(side_a, side_b, side_c)
print("The area of the triangle is:", area)
