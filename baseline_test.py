
def second_largest_element(lst):
    if len(lst) < 2:
        return None
    
    max_num = max(lst[0], lst[1])
    second_max = min(lst[0], lst[1])
    
    for i in range(2, len(lst)):
        if lst[i] > max_num:
            second_max = max_num
            max_num = lst[i]
        elif lst[i] > second_max and lst[i] != max_num:
            second_max = lst[i]
    
    return second_max

# Test the program
lst = [10, 5, 20, 8, 15]
print("List:", lst)
print("Second largest element:", second_largest_element(lst))
