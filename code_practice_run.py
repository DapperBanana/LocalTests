
def find_largest_element(lst):
    if not lst:
        return None

    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num

    return max_value

# Example list
numbers = [10, 20, 5, 30, 15]

largest_element = find_largest_element(numbers)
print("The largest element in the list is:", largest_element)
