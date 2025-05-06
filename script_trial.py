
def find_largest_element(lst):
    if len(lst) == 0:
        return None
    else:
        max_element = lst[0]
        for num in lst:
            if num > max_element:
                max_element = num
        return max_element

# Test the function
numbers = [3, 8, 2, 10, 5]
print(f"The largest element in the list is: {find_largest_element(numbers)}")
