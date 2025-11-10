
import math

def frustum_area(radius1, radius2, height):
    if radius1 < 0 or radius2 < 0 or height < 0:
        return "Invalid input! Radius and height must be positive."
    
    slant_height1 = math.sqrt((radius1**2) + (height**2))
    slant_height2 = math.sqrt((radius2**2) + (height**2))
    
    lateral_area1 = math.pi * (radius1 + radius2) * slant_height1
    lateral_area2 = math.pi * (radius2 + radius1) * slant_height2
    base_area1 = math.pi * (radius1**2)
    base_area2 = math.pi * (radius2**2)
    
    total_area = lateral_area1 + lateral_area2 + base_area1 + base_area2
    return total_area

radius1 = float(input("Enter the radius of the larger base of the frustum: "))
radius2 = float(input("Enter the radius of the smaller base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

result = frustum_area(radius1, radius2, height)
print(f"The total surface area of the frustum is: {result:.2f} square units.")
