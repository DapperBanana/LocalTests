
def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example list
my_list = [2, 4, 6, 8, 10]

# Calculate the sum of elements in the list
result = find_sum(my_list)

print(f"The sum of all elements in the list is: {result}")
