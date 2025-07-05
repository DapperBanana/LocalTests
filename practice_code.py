
def second_largest_element(lst):
    # Remove duplicates and sort the list in descending order
    sorted_lst = sorted(list(set(lst)), reverse=True)
    
    # Check if there are at least two elements in the list
    if len(sorted_lst) < 2:
        return "List does not have a second largest element"
    else:
        return sorted_lst[1]

# Test the function
my_list = [10, 20, 4, 45, 99]
print("Original list:", my_list)
print("Second largest element:", second_largest_element(my_list))
