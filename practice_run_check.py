
def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area of the triangle using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Input the three sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the area of the triangle
area = calculate_area(a, b, c)

print(f"The area of the triangle with sides {a}, {b}, and {c} is {area}")
