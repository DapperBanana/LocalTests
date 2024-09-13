
def calculate_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Sample list
numbers = [10, 20, 30, 40, 50]

average = calculate_average(numbers)
print("The average of the numbers in the list is:", average)
