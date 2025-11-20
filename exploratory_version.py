
def find_second_largest(input_list):
    first_max = None
    second_max = None

    for num in input_list:
        if first_max is None or num > first_max:
            second_max = first_max
            first_max = num
        elif second_max is None or num > second_max:
            second_max = num

    return second_max

# Test the function with a list
input_list = [3, 6, 8, 1, 4, 9, 2, 5]
second_largest = find_second_largest(input_list)
print("The second largest element in the list is:", second_largest)
