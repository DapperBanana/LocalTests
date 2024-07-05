
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    seq = []
    idx = lis.index(max_length)
    seq.append(arr[idx])

    for i in range(idx, -1, -1):
        if lis[i] == max_length - 1 and arr[i] < seq[-1]:
            seq.append(arr[i])
            max_length -= 1

    return list(reversed(seq))

# Test the function with an example
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("The longest increasing subsequence is:", longest_increasing_subsequence(arr))
