
def calculate_area(length, width):
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

if length <= 0 or width <= 0:
    print("Length and width must be greater than 0.")
else:
    area = calculate_area(length, width)
    print(f"The area of the rectangle is: {area}")
