
def calculate_area_of_trapezoid(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of base 1: "))
base2 = float(input("Enter the length of base 2: "))
height = float(input("Enter the height of the trapezoid: "))

area = calculate_area_of_trapezoid(base1, base2, height)
print(f"The area of the trapezoid is: {area}")
