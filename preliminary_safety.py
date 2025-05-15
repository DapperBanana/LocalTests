
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Test the function
numbers = [10, 20, 30, 40, 50]
avg = calculate_average(numbers)
print("The average of the numbers is:", avg)
