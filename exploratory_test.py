
def trapezoidal_prism_area(a, b, h1, h2, H):
    base_area = (a + b) / 2 * h1
    side_area = (a + b) * H
    top_area = (a + b) / 2 * h2
    total_area = 2 * base_area + side_area + top_area
    return total_area

a = float(input("Enter the length of the shorter base: "))
b = float(input("Enter the length of the longer base: "))
h1 = float(input("Enter the height of the shorter base: "))
h2 = float(input("Enter the height of the longer base: "))
H = float(input("Enter the height of the prism: "))

area = trapezoidal_prism_area(a, b, h1, h2, H)
print("The area of the trapezoidal prism is: ", area)
