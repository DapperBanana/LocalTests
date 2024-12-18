
def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example list
numbers = [1, 2, 3, 4, 5]

# Calculate sum of elements
result = find_sum(numbers)

print("Sum of elements in the list:", result)
