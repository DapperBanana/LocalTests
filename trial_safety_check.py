
import math

def pentagon_area(side_length):
    return (5 * side_length ** 2 * math.tan(math.radians(54))) / 2

def prism_area(side_length, height):
    base_area = 5 * side_length * pentagon_area(side_length)
    lateral_area = 5 * side_length * height
    total_area = base_area + lateral_area
    return total_area

side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

area = prism_area(side_length, height)
print("The area of the regular pentagonal prism is: ", area)
