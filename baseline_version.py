
def calculate_area_of_trapezoidal_prism(base1, base2, height_of_trapezoid, height_of_prism):
    area = ((base1 + base2) / 2) * height_of_trapezoid * height_of_prism
    return area

# Example usage:
base1 = 4
base2 = 6
height_of_trapezoid = 5
height_of_prism = 10

area = calculate_area_of_trapezoidal_prism(base1, base2, height_of_trapezoid, height_of_prism)
print("Area of the trapezoidal prism:", area)
