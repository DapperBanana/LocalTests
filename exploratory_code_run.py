
def calculate_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Test the function with a list of numbers
numbers = [10, 20, 30, 40, 50]
avg = calculate_average(numbers)
print(f"The average of the numbers is: {avg}")
