
def trapezoidal_prism_area(base1, base2, height, depth):
    area = 0.5 * (base1 + base2) * height + ((base1 + base2) * depth)
    return area

base1 = float(input("Enter the length of the first base of the trapezoidal prism: "))
base2 = float(input("Enter the length of the second base of the trapezoidal prism: "))
height = float(input("Enter the height of the trapezoidal prism: "))
depth = float(input("Enter the depth of the trapezoidal prism: "))

area = trapezoidal_prism_area(base1, base2, height, depth)
print("The area of the trapezoidal prism is:", area)
