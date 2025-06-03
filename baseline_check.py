
def calculate_area(base1, base2, height):
    area = ((base1 + base2) * height) / 2
    return area

base1 = float(input("Enter the length of base1: "))
base2 = float(input("Enter the length of base2: "))
height = float(input("Enter the height of the trapezoid: "))

area = calculate_area(base1, base2, height)
print("The area of the trapezoid is:", area)
