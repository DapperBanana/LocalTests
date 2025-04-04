
def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_seq = []

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_seq = [current_num]

            while current_num + 1 in nums_set:
                current_num += 1
                current_seq.append(current_num)

            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq

    return longest_seq

# Test the function
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: [1, 2, 3, 4]
