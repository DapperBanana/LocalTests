
import math

def area_of_pentagon(side_length):
    return (0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2)

side_length = float(input("Enter the length of a side of the pentagon: "))

area = area_of_pentagon(side_length)
print(f"The area of the pentagon with side length {side_length} is: {area}")
