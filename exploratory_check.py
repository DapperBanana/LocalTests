
def find_second_largest(lst):
    if len(lst) < 2:
        return "List should have at least two elements"
    
    first_max = max(lst[0], lst[1])
    second_max = min(lst[0], lst[1])
    
    for num in lst[2:]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
    
    return second_max

# Test the function
lst = [3, 8, 1, 5, 10, 6]
print("Second largest element in the list is:", find_second_largest(lst))
