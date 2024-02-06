
import math

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    base_area = math.pi * radius**2
    volume = base_area * height
    return volume

# Input the radius and height from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate and print the volume of the cylinder
volume = cylinder_volume(radius, height)
print("The volume of the cylinder is:", volume)
