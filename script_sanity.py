
import math

def calculate_volume(radius, height):
    base_area = math.pi * radius**2
    volume = base_area * height
    return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = calculate_volume(radius, height)
print("The volume of the cylinder is: %.2f" % volume)
