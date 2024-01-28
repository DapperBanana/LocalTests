
import math

def calculate_octagon_area(side_length):
    area = 2 * (1 + math.sqrt(2)) * side_length ** 2
    return area

# Take input from the user
side_length = float(input("Enter the side length of the octagon: "))

# Calculate the area
area = calculate_octagon_area(side_length)

# Print the result
print("The area of the regular octagon is:", area)
