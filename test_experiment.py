
import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Get input from user for the three sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate and print the area of the triangle
area = calculate_area(a, b, c)
print(f"The area of the triangle with sides {a}, {b}, {c} is: {area}")
