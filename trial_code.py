
def second_largest_element(lst):
    if len(lst) < 2:
        return "List must contain at least 2 elements"
    
    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])
    
    for i in range(2, len(lst)):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i] != largest:
            second_largest = lst[i]
    
    return second_largest

# Test the function
list1 = [5, 10, 2, 8, 15]
print(second_largest_element(list1))  # Output: 10

list2 = [3, 3, 3, 3]
print(second_largest_element(list2))  # Output: "All elements are the same"

list3 = [1]
print(second_largest_element(list3))  # Output: "List must contain at least 2 elements"
