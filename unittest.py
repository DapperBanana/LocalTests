
def find_largest_element(lst):
    if not lst:
        return None
    
    largest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    
    return largest

# Example usage
my_list = [10, 5, 20, 15, 30]
largest_element = find_largest_element(my_list)
print("The largest element in the list is:", largest_element)
