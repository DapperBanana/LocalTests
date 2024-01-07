
# Function to calculate the area of a trapezium
def calculate_trapezium_area(base1, base2, height):
    return (base1 + base2) * height / 2

# Function to calculate the area of a trapezoidal prism
def calculate_trapezoidal_prism_area(base1, base2, height, prism_height):
    trapezium_area = calculate_trapezium_area(base1, base2, height)
    lateral_area = (base1 + base2) * prism_height
    top_bottom_area = 2 * calculate_trapezium_area(base1, base2, height)
    return trapezium_area + lateral_area + top_bottom_area

# Inputs
base1 = float(input("Enter the length of the first base of the trapezium: "))
base2 = float(input("Enter the length of the second base of the trapezium: "))
height = float(input("Enter the height of the trapezium: "))
prism_height = float(input("Enter the height of the trapezoidal prism: "))

# Calculating and printing the area
area = calculate_trapezoidal_prism_area(base1, base2, height, prism_height)
print("The area of the trapezoidal prism is:", area)
