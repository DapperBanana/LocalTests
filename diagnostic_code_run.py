
import math

def frustum_area(radius1, radius2, height):
    base1_area = math.pi * (radius1 ** 2)
    base2_area = math.pi * (radius2 ** 2)
    slant_height = math.sqrt((radius1 - radius2) ** 2 + height ** 2)
    
    lateral_surface_area = math.pi * (radius1 + radius2) * slant_height
    
    total_area = base1_area + base2_area + lateral_surface_area
    
    return total_area

# Taking input from the user
radius1 = float(input("Enter the radius of the top base of the frustum: "))
radius2 = float(input("Enter the radius of the bottom base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

area = frustum_area(radius1, radius2, height)
print(f"The area of the frustum of the cone is: {area}")
