
import math

def calculate_cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

volume = calculate_cone_volume(radius, height)
print(f"The volume of the cone is: {volume:.2f}")
