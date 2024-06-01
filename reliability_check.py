
def calculate_area(side1, side2, side3):
    # Heron's formula
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

area = calculate_area(side1, side2, side3)
print("The area of the triangle is:", area)
