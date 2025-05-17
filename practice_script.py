
def find_largest_element(lst):
    max_num = lst[0]
    
    for num in lst:
        if num > max_num:
            max_num = num
            
    return max_num

# Example list
my_list = [5, 2, 8, 12, 3, 10, 7]

largest_element = find_largest_element(my_list)
print(f"The largest element in the list is: {largest_element}")
