
import math

# Function to calculate the area of a regular octagon
def calculate_octagon_area(side_length):
    area = 2 * (1 + math.sqrt(2)) * side_length**2
    return area

# Take user input for side length
side_length = float(input("Enter the length of a side of the regular octagon: "))

# Calculate and print the area
area = calculate_octagon_area(side_length)
print("The area of the regular octagon is", area)
