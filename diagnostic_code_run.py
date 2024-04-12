
import math

def calculate_pentagonal_prism_area(s, h):
    area = 5 * (0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * s ** 2 + 2 * s * h)
    return area

# Taking input from user
s = float(input("Enter the side length of the pentagon: "))
h = float(input("Enter the height of the prism: "))

# Calculating the area of the regular pentagonal prism
area = calculate_pentagonal_prism_area(s, h)

print("The area of the regular pentagonal prism is:", area)
