
def find_sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example list
my_list = [1, 2, 3, 4, 5]

# Find the sum of the list
sum_of_list = find_sum_of_list(my_list)

print(f"The sum of the list is: {sum_of_list}")
