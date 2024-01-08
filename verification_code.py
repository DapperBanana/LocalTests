
def find_longest_increasing_subsequence(arr):
    n = len(arr)
    lengths = [1] * n
    sequences = [[num] for num in arr]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                sequences[i] = sequences[j] + [arr[i]]

    max_length = max(lengths)
    max_index = lengths.index(max_length)
    longest_increasing_subsequence = sequences[max_index]

    return longest_increasing_subsequence


# Example usage
arr = [3, 10, 2, 1, 20]
result = find_longest_increasing_subsequence(arr)
print(result)
