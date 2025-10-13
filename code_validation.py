
import math

def area_of_pentagon(side_length):
    apothem_length = side_length / (2 * math.tan(math.pi/5))
    area = (5 * side_length * apothem_length) / 2
    return area

side_length = float(input("Enter the length of a side of the pentagon: "))
pentagon_area = area_of_pentagon(side_length)
print(f"The area of the pentagon is: {pentagon_area}")
