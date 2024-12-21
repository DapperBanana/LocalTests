
def trapezoidal_prism_area(a, b, h, height):
    base_area = (a + b) / 2 * h
    lateral_area = (a + b) * height
    top_area = a * h
    bottom_area = b * h

    total_area = 2 * base_area + lateral_area + top_area + bottom_area
    return total_area

a = float(input("Enter the length of the top base of the trapezoid: "))
b = float(input("Enter the length of the bottom base of the trapezoid: "))
h = float(input("Enter the height of the trapezoid: "))
height = float(input("Enter the height of the prism: "))

area = trapezoidal_prism_area(a, b, h, height)
print(f"The total surface area of the trapezoidal prism is: {area}")
