
def trapezoidal_prism_area(base1, base2, height, length):
    # Calculate the area of the trapezoidal prism
    area = ((base1 + base2) / 2) * height * length
    return area

# Input values from user
base1 = float(input("Enter the length of the first base of the trapezoidal prism: "))
base2 = float(input("Enter the length of the second base of the trapezoidal prism: "))
height = float(input("Enter the height of the trapezoidal prism: "))
length = float(input("Enter the length of the trapezoidal prism: "))

# Calculate the area of the trapezoidal prism
area = trapezoidal_prism_area(base1, base2, height, length)

print(f"The area of the trapezoidal prism is: {area}")
