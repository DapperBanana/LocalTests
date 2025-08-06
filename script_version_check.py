
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_seq = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_seq = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_seq += 1
                
            longest_seq = max(longest_seq, current_seq)
    
    return longest_seq

# Test the function
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive_sequence([1, 2, 3, 4, 5, 6, 7]))  # Output: 7
print(longest_consecutive_sequence([5, 7, 3, 8, 6]))  # Output: 3
