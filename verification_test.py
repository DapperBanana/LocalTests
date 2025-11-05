
def find_second_largest(lst):
    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)

    # Remove duplicates
    unique_lst = list(set(sorted_lst))

    # Check if there are at least two unique elements in the list
    if len(unique_lst) < 2:
        return "No second largest element found"

    return unique_lst[1]

# Test the function with a list
lst = [10, 5, 8, 20, 15, 25]
print(f"The second largest element in the list is: {find_second_largest(lst)}")
