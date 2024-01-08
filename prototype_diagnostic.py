
import math

def frustum_area(r, R, h):
    A = math.pi * (R**2 + R*r + r**2)
    return A

# Taking input from the user
r = float(input("Enter the radius of the top face: "))
R = float(input("Enter the radius of the bottom face: "))
h = float(input("Enter the height of the frustum: "))

# Calculating the area
area = frustum_area(r, R, h)

print("The area of the frustum of a cone is:", area)
