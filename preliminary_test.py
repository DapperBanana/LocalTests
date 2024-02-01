
def longest_consecutive_sequence(nums):
    nums_set = set(nums)  # Convert the list to a set for faster searching
    longest_sequence = []

    for num in nums_set:
        # Check if the current number has a previous number in the sequence
        if num - 1 not in nums_set:
            current_sequence = [num]

            # Find the next consecutive numbers in the sequence
            while num + 1 in nums_set:
                num += 1
                current_sequence.append(num)

            # Update the longest sequence if the current sequence is longer
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence

    return longest_sequence


# Test the program with a sample list of integers
nums = [100, 4, 200, 1, 3, 2]
print("Longest consecutive sequence:", longest_consecutive_sequence(nums))
