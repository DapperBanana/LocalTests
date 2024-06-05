
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1]*n
    
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    result = []
    i = lis.index(max_length)
    result.append(arr[i])

    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i] and lis[j] == lis[i] - 1:
            result.insert(0, arr[j])
            i = j

    return result

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Longest Increasing Subsequence:")
print(longest_increasing_subsequence(arr))
