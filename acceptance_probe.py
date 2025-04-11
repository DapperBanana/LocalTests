
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Average:", average)
