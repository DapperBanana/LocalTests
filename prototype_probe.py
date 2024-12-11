
def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_sequence = []
    
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_sequence = [current_num]
            
            while current_num + 1 in nums_set:
                current_num += 1
                current_sequence.append(current_num)
                
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
                
    return longest_sequence

# Example
nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_sequence(nums)
print(result)  # Output: [1, 2, 3, 4]
