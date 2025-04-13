
def trapezoidal_prism_area(base1, base2, height, prism_height):
    trapezoid_area = 0.5 * (base1 + base2) * height
    lateral_area = 2 * (base1 + base2) * prism_height
    top_and_bottom_area = base1 + base2
    total_area = 2 * trapezoid_area + lateral_area + 2 * top_and_bottom_area
    return total_area

base1 = float(input("Enter the length of base 1: "))
base2 = float(input("Enter the length of base 2: "))
height = float(input("Enter the height of the trapezoid: "))
prism_height = float(input("Enter the height of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, prism_height)
print(f"The total surface area of the trapezoidal prism is: {area}")
