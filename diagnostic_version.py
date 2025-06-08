
import math

def frustum_area(radius1, radius2, height):
    # Calculate the slant height of the frustum
    slant_height = math.sqrt((radius1 - radius2)**2 + height**2)
    
    # Calculate the lateral surface area of the frustum
    lateral_area = math.pi * (radius1 + radius2) * slant_height
    
    # Calculate the base areas of the two cones
    base_area1 = math.pi * radius1**2
    base_area2 = math.pi * radius2**2
    
    # Calculate the total surface area of the frustum
    total_area = lateral_area + base_area1 + base_area2
    
    return total_area

# Input values for radius1, radius2, and height of the frustum
radius1 = float(input("Enter the radius of the larger base: "))
radius2 = float(input("Enter the radius of the smaller base: "))
height = float(input("Enter the height of the frustum: "))

# Calculate the area of the frustum
area = frustum_area(radius1, radius2, height)

print("The area of the frustum of the cone is: ", area)
