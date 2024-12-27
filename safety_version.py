
def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    max_length = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Test the function
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: 4
