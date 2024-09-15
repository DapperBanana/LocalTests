
def find_largest_element(lst):
    if not lst:
        return None
    
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    
    return largest

# Test the function
my_list = [10, 5, 20, 15, 8]
print(f'The largest element in the list is: {find_largest_element(my_list)}')
