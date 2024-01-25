
import math

# Prompt the user to enter the radius and height of the cone
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

# Calculate the volume of the cone
volume = (1/3) * math.pi * radius**2 * height

# Print the volume of the cone
print("The volume of the cone is:", volume)
