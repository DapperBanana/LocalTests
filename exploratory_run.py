
def trapezoidal_prism_area(base1, base2, height, prism_height):
    trapezoidal_area = 0.5 * (base1 + base2) * height
    lateral_area = (base1 + base2) * prism_height
    top_area = base1 * height
    bottom_area = base2 * height
    total_area = 2 * trapezoidal_area + lateral_area + top_area + bottom_area
    return total_area

base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
prism_height = float(input("Enter the height of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, prism_height)
print(f"The area of the trapezoidal prism is: {area}")
