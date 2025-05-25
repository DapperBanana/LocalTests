
def second_largest_element(lst):
    if len(lst) < 2:
        return "List should have at least 2 elements"
    
    max_num = max(lst[0], lst[1])
    second_max = min(lst[0], lst[1])
    
    for num in lst[2:]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max:
            second_max = num
            
    return second_max

# Test the program
lst = [10, 20, 4, 45, 99]
print("Second largest element in the list:", second_largest_element(lst))
