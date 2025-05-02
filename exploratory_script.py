
def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
my_list = [1, 2, 3, 4, 5]
result = find_sum(my_list)
print("The sum of all elements in the list is:", result)
