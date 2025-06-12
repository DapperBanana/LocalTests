
import math

def calc_pentagon_area(side_length):
    apothem = side_length / (2 * math.tan(math.pi / 5))
    area = (5 * side_length * apothem) / 2
    return area

side_length = float(input("Enter the side length of the pentagon: "))
area = calc_pentagon_area(side_length)
print("The area of the pentagon is: ", area)
