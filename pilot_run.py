
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = 0
    for i in range(n):
        if max_length < lis[i]:
            max_length = lis[i]

    sequence = []
    last_num = float('-inf')
    for i in range(n-1, -1, -1):
        if lis[i] == max_length and arr[i] > last_num:
            sequence.insert(0, arr[i])
            max_length -= 1
            last_num = arr[i]

    return sequence


# Test the function with sample input
arr = [10, 22, 9, 33, 21, 50, 41, 60]
result = longest_increasing_subsequence(arr)
print("Length of LIS:", len(result))
print("Longest Increasing Subsequence:", result)
