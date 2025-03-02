
import math

def frustum_area(radius1, radius2, height):
    # Calculate slant height of frustum
    slant_height = math.sqrt((radius1 - radius2)**2 + height**2)
    
    # Calculate lateral surface area of frustum
    lateral_area = math.pi * (radius1 + radius2) * slant_height
    
    # Calculate top and bottom surface areas of frustum
    top_area = math.pi * radius1**2
    bottom_area = math.pi * radius2**2
    
    # Total surface area of frustum
    total_area = top_area + bottom_area + lateral_area
    
    return total_area

# Input variables
radius1 = float(input("Enter the radius of the top circle of the frustum: "))
radius2 = float(input("Enter the radius of the bottom circle of the frustum: "))
height = float(input("Enter the height of the frustum: "))

# Calculate and print the area of the frustum
area = frustum_area(radius1, radius2, height)
print(f"The area of the frustum is: {area}")
