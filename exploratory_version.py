
import math

# Function to calculate the area of a triangle given its three sides
def calculate_area(a, b, c):
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2
    # Calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Input the three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Calculate the area of the triangle
area = calculate_area(side1, side2, side3)
print("The area of the triangle is: {:.2f}".format(area))
