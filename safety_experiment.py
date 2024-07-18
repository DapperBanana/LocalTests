
import math

def area_of_pentagonal_prism(s, h):
    a = s / (2 * math.tan(math.pi / 5))  # Calculate the apothem
    area = 5 * (0.5 * s * (5 * a)) + (5 * h * s)
    return area

# Input the length of one side of the pentagon and the height of the prism
s = float(input("Enter the length of one side of the pentagon: "))
h = float(input("Enter the height of the prism: "))

# Calculate the area of the regular pentagonal prism
area = area_of_pentagonal_prism(s, h)

print(f"The area of the regular pentagonal prism is: {area}")
