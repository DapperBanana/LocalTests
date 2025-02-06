
import math

def frustum_area(radius1, radius2, height):
    # Calculate the slant height
    slant_height = math.sqrt((radius1 - radius2)**2 + height**2)
    
    # Calculate the lateral surface area of the frustum
    lateral_area = math.pi * (radius1 + radius2) * slant_height
    
    # Calculate the base area of the frustum
    base_area = math.pi * (radius1**2 - radius2**2)
    
    # Calculate the total surface area of the frustum
    total_area = lateral_area + base_area
    
    return total_area

# Input values
radius1 = float(input("Enter the radius of the top base of the frustum: "))
radius2 = float(input("Enter the radius of the bottom base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

# Calculate and print the area of the frustum
print("The area of the frustum of the cone is: ", frustum_area(radius1, radius2, height))
