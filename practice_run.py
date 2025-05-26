
import math

def frustum_area(radius1, radius2, height):
    area = math.pi * (radius1 + radius2) * (radius1**2 + radius2**2 + height**2)
    return area

radius1 = float(input("Enter the radius of the top base of the frustum: "))
radius2 = float(input("Enter the radius of the bottom base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

frustum_area = frustum_area(radius1, radius2, height)
print("The area of the frustum of the cone is:", frustum_area)
