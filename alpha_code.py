
import math

def calculate_area(side):
    area = (2 * (1 + math.sqrt(2)) * side**2)
    return area

side_length = float(input("Enter the length of a side of the octagon: "))
area_octagon = calculate_area(side_length)
print("The area of the regular octagon is:", area_octagon)
