
def calculate_average(arr):
    total = sum(arr)
    average = total / len(arr)
    return average

# Test the function with a list of numbers
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average of the numbers in the list is:", average)
