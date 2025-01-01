
import math

def calculate_pentagon_area(side_length):
    apothem_length = side_length / (2 * math.tan(math.pi / 5))
    area = (5 * side_length * apothem_length) / 2
    return area

side_length = float(input("Enter the side length of the pentagon: "))
area = calculate_pentagon_area(side_length)
print(f"The area of the pentagon is: {area}")
