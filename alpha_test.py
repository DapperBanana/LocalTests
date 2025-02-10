
def find_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# Input list
arr = [1, 2, 3, 4, 5]

# Calculate sum
sum_of_elements = find_sum(arr)

print("Sum of all elements in the list:", sum_of_elements)
