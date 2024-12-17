
def trapezoid_area(base1, base2, height):
    area = ((base1 + base2)/2) * height
    return area

def prism_area(base1, base2, height, depth):
    trapezoid_area_top = trapezoid_area(base1, base2, height)
    trapezoid_area_bottom = trapezoid_area(base1, base2, height)
    
    # Calculate the area of the four sides of the prism
    side1 = base1 * depth
    side2 = base2 * depth
    side3 = height * depth
    side4 = height * depth
    
    # Calculate the total surface area of the trapezoidal prism
    total_area = (2 * trapezoid_area_top) + (2 * side1) + side2 + side3 + side4
    
    return total_area

# Input the values for the bases, height, and depth of the trapezoidal prism
base1 = float(input("Enter the length of base 1: "))
base2 = float(input("Enter the length of base 2: "))
height = float(input("Enter the height of the trapezoid: "))
depth = float(input("Enter the depth of the prism: "))

# Calculate and print the area of the trapezoidal prism
area = prism_area(base1, base2, height, depth)
print("The area of the trapezoidal prism is: ", area)
