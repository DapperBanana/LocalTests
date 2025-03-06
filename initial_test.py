
def find_longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_sequence = []
    
    for num in nums_set:
        if num - 1 not in nums_set:
            current_sequence = [num]
            current_num = num + 1
            while current_num in nums_set:
                current_sequence.append(current_num)
                current_num += 1
            
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
    
    return longest_sequence

# Test the function
nums = [100, 4, 200, 1, 3, 2, 5, 101]
print("Longest consecutive sequence:", find_longest_consecutive_sequence(nums))
