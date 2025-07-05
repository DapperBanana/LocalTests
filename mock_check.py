
import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The roots are real and different.")
        print(f"Root1 = {root1}, Root2 = {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print("The roots are real and equal.")
        print(f"Root = {root}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print("The roots are complex and different.")
        print(f"Root1 = {real_part} + {imaginary_part}i, Root2 = {real_part} - {imaginary_part}i")

# Input coefficients of the quadratic equation
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

find_roots(a, b, c)
