
def longest_consecutive_sequence(nums):
    if not nums:
        return []

    nums = sorted(set(nums))
    max_sequence = [nums[0]]
    current_sequence = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_sequence.append(nums[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = [nums[i]]

    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence

    return max_sequence

# Test the function
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: [1, 2, 3, 4]

nums = [1, 5, 3, 7, 8, 20, 4, 6]
print(longest_consecutive_sequence(nums))  # Output: [3, 4, 5, 6, 7, 8]
