
def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
numbers = [1, 2, 3, 4, 5]
print("Sum of all elements in the list:", find_sum(numbers))
