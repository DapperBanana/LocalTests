
def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

# Input values from the user
base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))

# Calculate the area of the trapezoid
area = trapezoid_area(base1, base2, height)

print("The area of the trapezoid is:", area)
