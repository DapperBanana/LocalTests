
def longest_increasing_subsequence(nums):
    n = len(nums)
    lis = [1]*n
    
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    max_length = max(lis)
    subsequence = []
    index = lis.index(max_length)
    subsequence.append(nums[index])
    
    for i in range(index-1, -1, -1):
        if nums[i] < subsequence[-1] and lis[i] == lis[index]-1:
            subsequence.append(nums[i])
            index = i
    
    subsequence.reverse()
    
    return subsequence

# Test the function
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(nums))
