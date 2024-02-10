
import math

def calculate_area_of_nonagon(side_length):
    pi = math.pi
    area = (9 * side_length**2) / (4 * math.tan(pi/9))
    return area

# Test the function with a side length of 5
side_length = 5
area = calculate_area_of_nonagon(side_length)
print("Area of the regular nonagon is:", area)
