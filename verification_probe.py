
def trapezoidal_prism_area(base1, base2, height, length):
    trapezoid_area = 0.5 * (base1 + base2) * height
    lateral_area = (base1 + base2) * length
    total_area = 2 * trapezoid_area + lateral_area
    return total_area

base1 = float(input("Enter the length of the top base of the trapezoid: "))
base2 = float(input("Enter the length of the bottom base of the trapezoid: "))
height = float(input("Enter the height of the trapezoidal prism: "))
length = float(input("Enter the length of the trapezoidal prism: "))

area = trapezoidal_prism_area(base1, base2, height, length)
print("The total surface area of the trapezoidal prism is:", area)
