
def find_longest_sequence(lst):
    longest_sequence = []
    current_sequence = []
    lst.sort()

    for i in range(len(lst)):
        if i > 0 and lst[i] == lst[i-1] + 1:
            current_sequence.append(lst[i])
        else:
            current_sequence = [lst[i]]

        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence

    return longest_sequence

# Example usage
numbers = [100, 4, 200, 1, 3, 2, 99]
longest_sequence = find_longest_sequence(numbers)
print("Longest consecutive sequence:", longest_sequence)
