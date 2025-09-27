
def find_largest_element(lst):
    largest_element = lst[0]
    for num in lst:
        if num > largest_element:
            largest_element = num
    return largest_element

# Test the function
numbers = [10, 20, 5, 30, 15]
largest = find_largest_element(numbers)
print("The largest element in the list is:", largest)
