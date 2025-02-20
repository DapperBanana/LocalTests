
import math

def frustum_area(radius1, radius2, height):
    # Calculate the slant height of the frustum
    slant_height = math.sqrt((radius1 - radius2)**2 + height**2)

    # Calculate the lateral surface area of the frustum
    lateral_area = math.pi * (radius1 + radius2) * slant_height

    # Calculate the top and bottom surface areas of the frustum
    top_area = math.pi * radius1**2
    bottom_area = math.pi * radius2**2

    # Calculate the total surface area of the frustum
    total_area = top_area + bottom_area + lateral_area

    return total_area

# Get user input for radius1, radius2, and height
radius1 = float(input("Enter the radius of the top base of the frustum: "))
radius2 = float(input("Enter the radius of the bottom base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

# Calculate and print the area of the frustum
area = frustum_area(radius1, radius2, height)
print(f"The total surface area of the frustum of the cone is: {area}")
