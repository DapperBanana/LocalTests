
def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
my_list = [1, 2, 3, 4, 5]
print("Sum of elements in list:", find_sum(my_list))
