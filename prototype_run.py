
def trapezoidal_prism_area(base1, base2, height, length):
    base_area = 0.5 * (base1 + base2) * height
    lateral_area = (base1 + base2) * length
    top_area = base1 * height
    bottom_area = base2 * height

    total_area = 2 * base_area + lateral_area + top_area + bottom_area

    return total_area

# Taking input from user
base1 = float(input("Enter the length of the top base of the trapezoidal prism: "))
base2 = float(input("Enter the length of the bottom base of the trapezoidal prism: "))
height = float(input("Enter the height of the trapezoidal prism: "))
length = float(input("Enter the length of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, length)
print(f"The area of the trapezoidal prism is: {area}")
