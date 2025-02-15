
import math

def calculate_volume_cylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = calculate_volume_cylinder(radius, height)
print(f"The volume of the cylinder is: {volume}")
