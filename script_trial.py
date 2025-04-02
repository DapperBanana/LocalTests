
def longest_consecutive_sequence(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()

    longest_seq = []
    current_seq = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] - 1 == arr[i - 1]:
            current_seq.append(arr[i])
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq
            current_seq = [arr[i]]

    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq

    return longest_seq

# Test the function
arr = [100, 4, 200, 1, 3, 2, 300, 6, 5]
result = longest_consecutive_sequence(arr)
print("The longest consecutive sequence is:", result)
