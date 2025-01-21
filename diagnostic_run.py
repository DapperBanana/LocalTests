
def longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return []
    
    lis = [1] * n
      
    for i in range (1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1 :
                lis[i] = lis[j] + 1
              
    max_len = max(lis)
    index = lis.index(max_len)
    
    result = [arr[index]]
    max_len -= 1
    
    for i in range(index-1, -1, -1):
        if lis[i] == max_len:
            result.insert(0, arr[i])
            max_len -=1
    
    return result

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Longest increasing subsequence:", longest_increasing_subsequence(arr))
