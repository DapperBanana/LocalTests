
import math

def calculate_area_of_frustum_of_cone(lower_radius, upper_radius, height):
    slant_height = math.sqrt((upper_radius - lower_radius)**2 + height**2)
    base_area = math.pi * (lower_radius**2 + upper_radius**2)
    lateral_area = math.pi * slant_height * (lower_radius + upper_radius)
    total_area = base_area + lateral_area

    return total_area

# Asking for input from the user
lower_radius = float(input("Enter the lower radius of the frustum of a cone: "))
upper_radius = float(input("Enter the upper radius of the frustum of a cone: "))
height = float(input("Enter the height of the frustum of a cone: "))

area_of_frustum_of_cone = calculate_area_of_frustum_of_cone(lower_radius, upper_radius, height)
print("The area of the frustum of a cone is:", area_of_frustum_of_cone)
