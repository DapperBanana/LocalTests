
def calculate_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Example list
numbers = [15, 25, 10, 5, 20]

print("List of numbers:", numbers)
print("Average of numbers:", calculate_average(numbers))
