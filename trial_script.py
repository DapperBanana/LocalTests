
import math

def calculate_pentagon_area(side_length):
    area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length**2
    return area

# Taking input from the user
side = float(input("Enter the length of a side of the pentagon: "))

# Calculating and printing the area
area = calculate_pentagon_area(side)
print("The area of the pentagon is:", area)
