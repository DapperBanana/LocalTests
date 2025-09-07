
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1]*n
    
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    max_length = max(lis)
    max_seq = []
    idx = lis.index(max_length)
    max_seq.append(arr[idx])
    max_length -= 1
    
    while max_length > 0:
        for i in range(idx-1, -1, -1):
            if arr[i] < arr[idx] and lis[i] == max_length:
                max_seq.insert(0, arr[i])
                idx = i
                max_length -= 1
                break
    
    return max_seq

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Input array:", arr)
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
