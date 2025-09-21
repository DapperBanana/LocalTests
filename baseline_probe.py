
def calculate_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Example list
numbers = [23, 56, 78, 94, 12]

# Calculate average of elements in the list
avg = calculate_average(numbers)

# Print the average
print("Average:", avg)
