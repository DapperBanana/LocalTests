
import math

def calculate_cone_volume(radius, height):
    volume = (math.pi * radius * radius * height) / 3
    return volume

# test the function
r = float(input("Enter the radius of the cone (in cm): "))
h = float(input("Enter the height of the cone (in cm): "))
volume = calculate_cone_volume(r, h)
print("The volume of the cone is", volume, "cubic cm")
