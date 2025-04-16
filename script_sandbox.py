
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    max_length = max(lis)
    indexes = [i for i in range(n) if lis[i] == max_length]
    result = [arr[index] for index in indexes]

    return result

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Input array:", arr)
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
