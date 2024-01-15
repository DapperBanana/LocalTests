
import math

def hendecagon_area(side_length):
    cot = 1 / math.tan(math.pi / 11)
    area = (11 / 4) * side_length**2 * cot
    return area

# Test the function
side_length = float(input("Enter the length of the side of the hendecagon: "))
area = hendecagon_area(side_length)
print("The area of the regular hendecagon is:", area)
