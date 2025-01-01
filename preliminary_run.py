
def trapezoidal_prism_area(base1, base2, height, length):
    base_avg = (base1 + base2) / 2
    lateral_area = (base1 + base2) * height
    top_area = base_avg * length
    bottom_area = base_avg * length
    total_area = 2 * lateral_area + top_area + bottom_area
    return total_area

base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
length = float(input("Enter the length of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, length)
print("The area of the trapezoidal prism is:", area)
