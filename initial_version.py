
# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Input the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = calculate_area(length, width)

# Display the result
print("The area of the rectangle is:", area)
