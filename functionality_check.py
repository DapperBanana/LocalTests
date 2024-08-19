
def trapezoidal_prism_area(base1, base2, height, depth):
    lateral_area = (base1 + base2) * height
    base_area = ((base1 + base2) / 2) * depth
    total_area = 2 * base_area + lateral_area
    return total_area

base1 = float(input("Enter the length of base1 of the trapezoid: "))
base2 = float(input("Enter the length of base2 of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
depth = float(input("Enter the depth of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, depth)

print(f"The area of the trapezoidal prism is: {area}")
