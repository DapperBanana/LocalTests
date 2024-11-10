
def calculate_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Test the function with a sample list
numbers = [5, 10, 15, 20, 25]
print("The average of the numbers in the list is:", calculate_average(numbers))
