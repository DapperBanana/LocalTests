
import math

def frustum_area(radius1, radius2, height):
    total_area = math.pi * (radius1**2 + radius2**2 + radius1 * radius2)
    slant_height = math.sqrt((radius1 - radius2)**2 + height**2)
    lateral_area = math.pi * (radius1 + radius2) * slant_height
    base_area1 = math.pi * radius1**2
    base_area2 = math.pi * radius2**2
    frustum_area = total_area + lateral_area

    print("Total area of the frustum of the cone is:", frustum_area)
    print("Base area of the top circle is:", base_area1)
    print("Base area of the bottom circle is:", base_area2)
    print("Lateral area of the frustum is:", lateral_area)

# Input parameters
radius1 = float(input("Enter the top circle radius: "))
radius2 = float(input("Enter the bottom circle radius: "))
height = float(input("Enter the height of the frustum: "))

frustum_area(radius1, radius2, height)
