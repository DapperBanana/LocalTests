
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    max_length = max(lis)

    # Reconstructing the longest increasing subsequence
    subsequence = []
    current_length = max_length
    for i in range(n - 1, -1, -1):
        if lis[i] == current_length:
            subsequence.insert(0, arr[i])
            current_length -= 1

    return max_length, subsequence

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length, subsequence = longest_increasing_subsequence(arr)
print("Length of the longest increasing subsequence:", length)
print("Longest increasing subsequence:", subsequence)
