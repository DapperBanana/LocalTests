
def trapezoidal_prism_area(base1, base2, height, length):
    prism_area = ((base1 + base2) / 2) * height + (2 * ((base1 + base2) / 2) * length)
    return prism_area

base1 = float(input("Enter the length of the top base of the trapezoid: "))
base2 = float(input("Enter the length of the bottom base of the trapezoid: "))
height = float(input("Enter the height of the trapezoidal prism: "))
length = float(input("Enter the length of the trapezoidal prism: "))

area = trapezoidal_prism_area(base1, base2, height, length)
print(f"The area of the trapezoidal prism is: {area}")
