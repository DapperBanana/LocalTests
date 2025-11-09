
def sum_of_elements(lst):
    total = 0
    for element in lst:
        total += element
    return total

# Test the program
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print("Sum of elements in the list:", result)
