
def trapezoidal_prism_area(base1, base2, height, prism_height):
    trapezoid_area = ((base1 + base2) * height) / 2
    prism_area = 2 * trapezoid_area + ((base1 + base2) * prism_height)
    return prism_area

base1 = float(input("Enter the length of base 1 of the trapezoid: "))
base2 = float(input("Enter the length of base 2 of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
prism_height = float(input("Enter the height of the trapezoidal prism: "))

area = trapezoidal_prism_area(base1, base2, height, prism_height)
print(f"The area of the trapezoidal prism is: {area}")
