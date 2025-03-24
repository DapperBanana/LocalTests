
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    result = []
    idx = lis.index(max_length)
    result.append(arr[idx])

    for i in range(idx - 1, -1, -1):
        if arr[i] < arr[idx] and lis[i] == lis[idx] - 1:
            result.append(arr[i])
            idx = i

    result.reverse()
    return result

# Test the function
arr = [3, 10, 2, 1, 20]
print("Input array:", arr)
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
