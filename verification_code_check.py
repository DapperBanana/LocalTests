
import math

def calculate_area(a, b, c):
    # Calculate semiperimeter
    s = (a + b + c) / 2

    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

# Get user input for the three sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate and display the area of the triangle
area = calculate_area(a, b, c)
print(f"The area of the triangle is: {area}")
