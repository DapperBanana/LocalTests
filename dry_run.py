
import math

def calculate_frustum_area(radius1, radius2, height):
    base_area1 = math.pi * radius1**2
    base_area2 = math.pi * radius2**2
    side = math.sqrt((radius1 - radius2)**2 + height**2)
    lateral_area = math.pi * (radius1 + radius2) * side
    total_area = base_area1 + base_area2 + lateral_area
    return total_area

radius1 = float(input("Enter radius of the base of frustum: "))
radius2 = float(input("Enter radius of the top of frustum: "))
height = float(input("Enter height of the frustum: "))

area = calculate_frustum_area(radius1, radius2, height)
print("The surface area of the frustum is: ", round(area, 2))
