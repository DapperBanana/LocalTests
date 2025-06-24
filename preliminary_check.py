
def calculate_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example list
my_list = [1, 2, 3, 4, 5]

# Calculate sum of elements in the list
result = calculate_sum(my_list)
print("The sum of all elements in the list is:", result)
