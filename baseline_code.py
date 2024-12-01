
def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    max_seq_length = 0
    
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_seq_length = 1
            
            while current_num + 1 in nums_set:
                current_num += 1
                current_seq_length += 1
                
            max_seq_length = max(max_seq_length, current_seq_length)
    
    return max_seq_length

# Test the function
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: 4
