
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_len = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1

            max_len = max(max_len, current_len)

    return max_len

# Test the program
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: 4
