
import math

def calculate_area(s):
    area = math.sqrt(3) * (s ** 2)
    return round(area, 2)  # Rounding to 2 decimal places

# Test the function
s = float(input("Enter the length of the edges of the tetrahedron: "))
area = calculate_area(s)
print("The area of the regular tetrahedron is:", area)
