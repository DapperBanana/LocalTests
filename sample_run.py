
def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function with a list of numbers
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print(f"The sum of all elements in the list is: {result}")
