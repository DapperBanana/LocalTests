
import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

area = calculate_area(a, b, c)
print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area}")
