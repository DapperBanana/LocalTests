
def trapezoidal_prism_area(base1, base2, height, depth):
    trapezoid_area = 0.5 * (base1 + base2) * height
    lateral_area = depth * (base1 + base2)
    base_area = base1 * base2

    total_area = 2 * trapezoid_area + lateral_area + base_area
    return total_area

base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
depth = float(input("Enter the depth of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, depth)
print("The total surface area of the trapezoidal prism is:", area)
