
def second_largest_element(lst):
    if len(lst) < 2:
        return "List has less than 2 elements"
    
    max_element = max(lst[0], lst[1])
    second_max_element = min(lst[0], lst[1])

    for i in range(2, len(lst)):
        if lst[i] > max_element:
            second_max_element = max_element
            max_element = lst[i]
        elif lst[i] > second_max_element and lst[i] != max_element:
            second_max_element = lst[i]

    return second_max_element

# Test the function
lst = [3, 8, 1, 9, 5, 7]
print("Second largest element in the list is:", second_largest_element(lst))
