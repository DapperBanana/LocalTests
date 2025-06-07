
import math

# Function to calculate the area of a regular pentagon
def pentagon_area(side_length):
    return (5/4) * (side_length ** 2) * math.sqrt(5 * (5 + 2 * math.sqrt(5)))

# Function to calculate the lateral area of a pentagonal prism
def lateral_area(side_length, height):
    return 5 * side_length * height

# Function to calculate the total surface area of a pentagonal prism
def total_surface_area(side_length, height):
    return pentagon_area(side_length) + lateral_area(side_length, height)

# Input side length and height of the pentagonal prism
side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

# Calculate and print the total surface area of the pentagonal prism
print("The total surface area of the pentagonal prism is:", total_surface_area(side_length, height))
