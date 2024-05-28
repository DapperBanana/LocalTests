
import math

def frustum_area(radius1, radius2, height):
    # Calculate the slant height of the frustum
    slant_height = math.sqrt((radius1 - radius2)**2 + height**2)
    
    # Calculate the lateral surface area of the frustum
    lateral_area = math.pi * (radius1 + radius2) * slant_height
    
    # Calculate the base areas of the top and bottom circles
    base_area1 = math.pi * radius1**2
    base_area2 = math.pi * radius2**2
    
    # Calculate the total surface area of the frustum
    total_area = lateral_area + base_area1 + base_area2
    
    return total_area

radius1 = float(input("Enter the radius of the top circle of the frustum: "))
radius2 = float(input("Enter the radius of the bottom circle of the frustum: "))
height = float(input("Enter the height of the frustum: "))

area = frustum_area(radius1, radius2, height)
print("The area of the frustum of the cone is:", area)
