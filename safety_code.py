
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    index = dp.index(max_length)
    lis = [arr[index]]
    for i in range(index-1, -1, -1):
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            lis.insert(0, arr[i])
            index = i

    return max_length, lis

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length, lis = longest_increasing_subsequence(arr)
print(f"Length of longest increasing subsequence: {length}")
print(f"Longest increasing subsequence: {lis}")
