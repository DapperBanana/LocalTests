
# Function to calculate the area of a parallelogram
def parallelogram_area(base, height):
    area = base * height
    return area

# Input base and height from user
base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

# Calculate the area of the parallelogram
area = parallelogram_area(base, height)

# Print the area of the parallelogram
print("The area of the parallelogram is:", area)
