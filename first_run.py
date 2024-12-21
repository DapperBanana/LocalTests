
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_seq_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_seq_length += 1
            
            longest_sequence = max(longest_sequence, current_seq_length)
    
    return longest_sequence

# Test the function
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: 4
