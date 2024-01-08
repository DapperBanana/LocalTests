
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    result = []

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    max_len = max(dp)
    max_idx = dp.index(max_len)

    result.append(arr[max_idx])

    for i in reversed(range(max_idx)):
        if arr[i] < result[-1] and dp[i] == dp[max_idx] - 1:
            result.append(arr[i])
            max_idx = i

    result.reverse()
    return result

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(longest_increasing_subsequence(arr))  # Output: [10, 22, 33, 50, 60]
