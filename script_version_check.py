
import math

def frustum_area(radius1, radius2, height):
    base_area1 = math.pi * (radius1 ** 2)
    base_area2 = math.pi * (radius2 ** 2)
    side_length = math.sqrt((radius1 - radius2) ** 2 + height ** 2)
    
    lateral_surface_area = math.pi * (radius1 + radius2) * side_length
    total_surface_area = base_area1 + base_area2 + lateral_surface_area
    
    return total_surface_area

radius1 = float(input("Enter the radius of the larger base of the frustum: "))
radius2 = float(input("Enter the radius of the smaller base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

area = frustum_area(radius1, radius2, height)
print("The area of the frustum of the cone is:", area)
