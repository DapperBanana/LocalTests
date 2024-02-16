
def longest_consecutive_sequence(nums):
    longest_seq = []  # variable to store the longest consecutive sequence found so far
    current_seq = []  # variable to store the current consecutive sequence being built

    for num in nums:
        # If the number is the start of a new sequence or it is consecutive to the previous number, add it to the current sequence
        if not current_seq or num == current_seq[-1] + 1:
            current_seq.append(num)
        else:
            # If the current sequence is longer than the previous longest sequence, update the longest sequence
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq
            current_seq = [num]  # Start a new sequence

    # Check if the last current sequence is longer than the previous longest sequence
    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq

    return longest_seq


# Test the function
nums = [100, 4, 200, 1, 3, 2, 5]
print(longest_consecutive_sequence(nums))  # Output: [1, 2, 3, 4, 5]
