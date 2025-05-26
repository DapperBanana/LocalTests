
def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    nums_set = set(nums)
    longest_seq = 0
    
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_seq = 1
            
            while current_num + 1 in nums_set:
                current_num += 1
                current_seq += 1
            
            longest_seq = max(longest_seq, current_seq)
    
    return longest_seq

# Test the function with a list of integers
nums = [100, 4, 200, 1, 3, 2, 5, 6]
print("Longest consecutive sequence length:", longest_consecutive_sequence(nums))
