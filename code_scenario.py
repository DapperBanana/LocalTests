
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Input list of numbers
numbers = [2, 4, 6, 8, 10]

# Calculate average
result = calculate_average(numbers)

print(f"The average of the numbers {numbers} is: {result}")
