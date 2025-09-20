
def calculate_area_of_triangle(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))

area = calculate_area_of_triangle(side1, side2, side3)
print(f"The area of the triangle is: {area}")
