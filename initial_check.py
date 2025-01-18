
def calculate_average(lst):
    total = sum(lst)
    return total / len(lst)

# Example list
numbers = [10, 20, 30, 40, 50]

# Calculate average
average = calculate_average(numbers)

print(f"The average of the elements in the list is: {average}")
