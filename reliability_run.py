
import math

def pentagonal_prism_area(side_length, height):
    # Calculate the area of one of the pentagonal faces
    area_pentagon = 1.72048 * side_length**2

    # Calculate the area of one of the rectangular faces
    area_rectangle = 5 * side_length * height

    # Calculate the total surface area of the pentagonal prism
    total_area = 2*area_pentagon + area_rectangle

    return total_area

# Input the side length and height of the pentagonal prism
side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the pentagonal prism: "))

# Calculate the area of the pentagonal prism
area = pentagonal_prism_area(side_length, height)

print("The total surface area of the pentagonal prism is:", area)
