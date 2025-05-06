
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    subsequence = []
    index = lis.index(max_length)
    subsequence.append(arr[index])

    for i in range(index-1, -1, -1):
        if arr[i] < arr[index] and lis[i] == lis[index] - 1:
            subsequence.append(arr[i])
            index = i

    subsequence.reverse()

    return subsequence

arr = [3, 10, 2, 1, 20]
print("Longest Increasing Subsequence:", longest_increasing_subsequence(arr))
