
def trapezoidal_prism_area(base1, base2, height, prism_height):
    trapezoid_area = ((base1 + base2) / 2) * height
    lateral_area = (base1 + base2) * prism_height
    total_area = 2 * trapezoid_area + lateral_area
    return total_area

base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
prism_height = float(input("Enter the height of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, prism_height)
print(f"The total area of the trapezoidal prism is: {area}")
