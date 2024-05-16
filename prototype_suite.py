
def find_largest_element(lst):
    max_element = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
    
    return max_element

# Test the function
my_list = [10, 30, 50, 20, 40]
largest_element = find_largest_element(my_list)
print("The largest element in the list is:", largest_element)
