
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    length = max(lis)
    subsequence = []
    index = lis.index(length)

    while length > 0:
        subsequence.insert(0, arr[index])
        length -= 1
        for i in range(index - 1, -1, -1):
            if arr[i] < arr[index] and lis[i] == length:
                index = i
                break

    return subsequence

# Test the program
arr = [3, 10, 2, 1, 20]
print("Input array:", arr)
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
