
import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("Equal Roots. Root:", root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print("Complex Roots. Root 1:", real_part, "+", imaginary_part, "i")
        print("Complex Roots. Root 2:", real_part, "-", imaginary_part, "i")

a = float(input("Enter coefficient of x^2: "))
b = float(input("Enter coefficient of x: "))
c = float(input("Enter constant term: "))

find_roots(a, b, c)
