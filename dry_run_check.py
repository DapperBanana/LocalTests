
import math

def pentagon_area(side_length):
    return (5 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2

def pentagonal_prism_area(side_length, height):
    base_area = pentagon_area(side_length)
    lateral_area = 5 * side_length * height
    total_area = 2 * base_area + lateral_area
    return total_area

side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

area = pentagonal_prism_area(side_length, height)
print(f"The area of the regular pentagonal prism is: {area:.2f} square units")
