
import math

def calculate_area(radius):
    # Calculate the area using the formula: Area = pi * radius^2
    area = math.pi * radius ** 2
    return area

# Prompt the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate and print the area of the circle
area = calculate_area(radius)
print("The area of the circle is:", area)
