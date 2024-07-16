
import math

def frustum_area(radius1, radius2, height):
    slant_height = math.sqrt((radius1 - radius2) ** 2 + height ** 2)
    base_area1 = math.pi * radius1 ** 2
    base_area2 = math.pi * radius2 ** 2
    lateral_area = (radius1 + radius2) * math.pi * slant_height
    total_area = base_area1 + base_area2 + lateral_area
    return total_area

# Input values for the radius1, radius2, and height of the frustum
radius1 = float(input("Enter the radius of the top base of the frustum: "))
radius2 = float(input("Enter the radius of the bottom base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

# Call the frustum_area function and print the result
area = frustum_area(radius1, radius2, height)
print("The area of the frustum of the cone is:", area)
