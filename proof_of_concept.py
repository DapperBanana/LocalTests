
def calculate_average(lst):
    total = sum(lst)
    avg = total / len(lst)
    return avg

# Test the function
lst = [2, 4, 6, 8, 10]
average = calculate_average(lst)
print(f"The average of the elements in the list is: {average}")
