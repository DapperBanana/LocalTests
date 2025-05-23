
def find_longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return []

    lis = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    index = lis.index(max_length)

    subsequence = [arr[index]]
    current_length = max_length - 1

    for i in range(index-1, -1, -1):
        if arr[i] < arr[index] and lis[i] == current_length:
            subsequence.insert(0, arr[i])
            current_length -= 1
            index = i

    return subsequence

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Longest Increasing Subsequence:", find_longest_increasing_subsequence(arr))
