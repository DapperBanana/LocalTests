
import math

def frustum_area(radius1, radius2, height):
    side = math.sqrt((radius1 - radius2)**2 + height**2)
    area = math.pi * (radius1 + radius2) * side + math.pi * radius1**2 + math.pi * radius2**2
    return area

radius1 = float(input("Enter the radius of the top of the frustum: "))
radius2 = float(input("Enter the radius of the base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

frustum_area = frustum_area(radius1, radius2, height)
print("The area of the frustum of the cone is:", frustum_area)
