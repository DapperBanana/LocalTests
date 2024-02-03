
import math

def calculate_area(side):
    area = (2 * (1 + math.sqrt(2))) * side**2
    return area

# Taking input from the user for the side length
side_length = float(input("Enter the length of one side of the octagon: "))

# Calculating the area
area = calculate_area(side_length)

# Displaying the result
print("The area of the regular octagon is:", area)
