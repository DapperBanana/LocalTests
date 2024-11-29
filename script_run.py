
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    max_length = max(dp)
    subsequence = []
    index = dp.index(max_length)
    subsequence.append(arr[index])

    for i in range(index - 1, -1, -1):
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            subsequence.insert(0, arr[i])
            index = i

    return subsequence

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Original array:", arr)
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
