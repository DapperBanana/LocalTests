
def trapezoidal_prism_area(base1, base2, height, length):
    trap_area = ((base1 + base2) / 2) * height
    prism_area = 2 * trap_area + (base1 + base2) * length
    return prism_area

base1 = float(input("Enter the length of base1 of the trapezoid: "))
base2 = float(input("Enter the length of base2 of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
length = float(input("Enter the length of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, length)
print(f"The area of the trapezoidal prism is: {area}")
