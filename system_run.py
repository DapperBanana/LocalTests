
def trapezoidal_prism_area(a, b, h, H):
    base_area = (a + b) / 2 * h
    side_area = (a + b) / 2 * H
    top_and_bottom_area = a * b
    
    total_area = 2 * base_area + 2 * side_area + top_and_bottom_area
    
    return total_area

a = float(input("Enter the length of the top base of the trapezoid: "))
b = float(input("Enter the length of the bottom base of the trapezoid: "))
h = float(input("Enter the height of the trapezoid: "))
H = float(input("Enter the height of the trapezoidal prism: "))

area = trapezoidal_prism_area(a, b, h, H)
print(f"The area of the trapezoidal prism is {area}")
