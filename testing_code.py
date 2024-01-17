
# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
area = calculate_area(length, width)
print("The area of the rectangle is", area)
