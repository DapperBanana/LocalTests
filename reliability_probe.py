
def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    return area

# Input the three sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Calculate the area of the triangle
area = calculate_area(side1, side2, side3)

print(f"The area of the triangle is: {area}")
