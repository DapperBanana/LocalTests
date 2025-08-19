
def longest_consecutive_sequence(lst):
    longest_seq = 0
    current_seq = 1

    # Sort the list
    sorted_lst = sorted(lst)
    
    # Iterate through the list and find the longest consecutive sequence
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] == sorted_lst[i-1] + 1:
            current_seq += 1
        else:
            current_seq = 1
        
        if current_seq > longest_seq:
            longest_seq = current_seq

    return longest_seq

# Test the function
lst = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(lst))  # Output: 4
