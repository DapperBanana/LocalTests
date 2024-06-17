
import math

def calculate_area(a, b, c):
    # calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2
    # calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# get the lengths of the sides of the triangle from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# calculate the area of the triangle
area = calculate_area(a, b, c)

print(f"The area of the triangle with sides {a}, {b}, and {c} is {area}.")
