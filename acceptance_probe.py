
import math

def calculate_area_of_pentagon(side_length):
    area = (0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * side_length ** 2
    return area

side_length = float(input("Enter the side length of the pentagon: "))
area = calculate_area_of_pentagon(side_length)
print(f"The area of the pentagon is: {area}")
