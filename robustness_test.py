
def calculate_area(base1, base2, height, length):
    # Calculate the area of the trapezoid (top and bottom faces)
    top_area = ((base1 + base2) / 2) * height
    bottom_area = top_area
    
    # Calculate the perimeter of the trapezoid (top and bottom edges)
    perimeter = base1 + base2 + 2 * (length + height)
    
    # Calculate the area of the side faces
    side_area = perimeter * length
    
    # Calculate the total area of the trapezoidal prism
    total_area = 2 * top_area + 2 * side_area
    
    return total_area

base1 = float(input("Enter the length of the top base of the trapezoid: "))
base2 = float(input("Enter the length of the bottom base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
length = float(input("Enter the length of the trapezoidal prism: "))

area = calculate_area(base1, base2, height, length)
print("The area of the trapezoidal prism is:", area)
