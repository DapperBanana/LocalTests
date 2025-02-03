
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    subsequence = []

    for i in range(n - 1, -1, -1):
        if lis[i] == max_length:
            subsequence.append(arr[i])
            max_length -= 1

    return subsequence[::-1]

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Original array:", arr)
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
