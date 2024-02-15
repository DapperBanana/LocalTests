
import math

def calculate_cylinder_volume(radius, height):
    # Calculate the volume of a cylinder
    volume = math.pi * radius**2 * height
    return volume

# Read the radius and height from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate and print the volume of the cylinder
volume = calculate_cylinder_volume(radius, height)
print("The volume of the cylinder is", volume)
