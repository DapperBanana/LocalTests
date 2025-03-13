
def sum_of_list_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example list
my_list = [1, 2, 3, 4, 5]

# Find the sum of all elements in the list
sum_of_list = sum_of_list_elements(my_list)

print(f"The sum of all elements in the list is: {sum_of_list}")
