
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    subsequence = []
    currentIndex = lis.index(max_length)
    currentLength = max_length

    for i in range(currentIndex, -1, -1):
        if lis[i] == currentLength:
            subsequence.insert(0, arr[i])
            currentLength -= 1

    return subsequence

# Test the function with an example
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
