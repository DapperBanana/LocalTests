
def longest_consecutive_sequence(lst):
    if not lst:
        return []

    lst.sort()
    current_sequence = [lst[0]]
    longest_sequence = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == current_sequence[-1] + 1:
            current_sequence.append(lst[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence.copy()
            current_sequence = [lst[i]]

    return longest_sequence


# Test the function with a list of integers
lst = [100, 4, 200, 1, 3, 2, 5, 6, 7]
print("Longest consecutive sequence:", longest_consecutive_sequence(lst))
