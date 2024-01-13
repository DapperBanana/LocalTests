
import math

def calculate_cylinder_volume(radius, height):
    base_area = math.pi * radius**2
    volume = base_area * height
    return volume

# Prompt user for radius and height of the cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate and print the volume of the cylinder
volume = calculate_cylinder_volume(radius, height)
print("The volume of the cylinder is", volume)
