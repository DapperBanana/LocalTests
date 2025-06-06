
import math

def pentagon_area(side_length):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length**2

def pentagonal_prism_area(side_length, height):
    base_area = 5 * pentagon_area(side_length)
    side_area = 5 * side_length * height
    total_area = base_area + side_area
    return total_area

side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

area = pentagonal_prism_area(side_length, height)
print("The area of the regular pentagonal prism is:", area)
