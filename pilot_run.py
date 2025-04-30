
def find_longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_seq = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            curr_num = num
            curr_seq = 1

            while curr_num + 1 in nums_set:
                curr_num += 1
                curr_seq += 1

            longest_seq = max(longest_seq, curr_seq)

    return longest_seq

# Example
nums = [100, 4, 200, 1, 3, 2]
print(find_longest_consecutive_sequence(nums))  # Output: 4
