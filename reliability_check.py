
def calculate_trapezoidal_prism_area(a, b, h, H):
    base_area = (a + b) * h / 2
    lateral_area = 2 * base_area + (a + b) * H
    total_area = 2 * base_area + lateral_area
    return total_area

a = float(input("Enter the length of the top base of the trapezoidal prism: "))
b = float(input("Enter the length of the bottom base of the trapezoidal prism: "))
h = float(input("Enter the height of the trapezoidal prism: "))
H = float(input("Enter the length between the top and bottom base of the trapezoidal prism: "))

area = calculate_trapezoidal_prism_area(a, b, h, H)
print("The area of the trapezoidal prism is:", area)
