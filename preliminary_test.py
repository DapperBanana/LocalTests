
import math

def frustum_cone_area(radius1, radius2, height):
    slant_height1 = math.sqrt(radius1**2 + height**2)
    slant_height2 = math.sqrt(radius2**2 + height**2)
    
    lateral_area1 = math.pi * (radius1 + radius2) * slant_height1
    base_area1 = math.pi * radius1**2
    base_area2 = math.pi * radius2**2
    
    total_area = lateral_area1 + base_area1 + base_area2
    
    return total_area

radius1 = float(input("Enter the radius of the larger base of the frustum: "))
radius2 = float(input("Enter the radius of the smaller base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

area = frustum_cone_area(radius1, radius2, height)
print("The area of the frustum of the cone is: ", area)
