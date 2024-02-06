
import math

def calculate_octagon_area(side_length):
    area = 2 * (1 + math.sqrt(2)) * side_length**2
    return area

# Test the program
side_length = float(input("Enter the side length of the octagon: "))
area = calculate_octagon_area(side_length)
print("The area of the regular octagon is: ", area)
