
def find_second_largest(lst):
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
lst = [3, 5, 1, 7, 4, 9, 2]
print("The second largest element in the list is:", find_second_largest(lst))
