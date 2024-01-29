
import math

def calculate_cone_volume(radius, height):
    if radius <= 0 or height <= 0:
        return "Invalid input. The radius and height must be positive numbers."

    volume = (math.pi * radius * radius * height) / 3
    return volume

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

volume = calculate_cone_volume(radius, height)
print("The volume of the cone is", volume)
