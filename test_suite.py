
def find_sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the program
lst = [1, 2, 3, 4, 5]
print(f"The sum of all elements in the list is: {find_sum_of_list(lst)}")
