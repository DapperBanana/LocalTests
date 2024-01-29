
def longest_increasing_subsequence(array):
    n = len(array)
    # 'lis' is the array to store the lengths of longest increasing subsequences
    lis = [1] * n
 
    # Compute the longest increasing subsequence values in bottom-up manner
    for i in range(1, n):
        for j in range(0, i):
            if array[i] > array[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
 
    # Initialize maximum length variable
    max_length = max(lis)
 
    # Find the longest increasing subsequence length
    index = lis.index(max_length)
    subsequence = [array[index]]
    current_length = max_length - 1
    for i in range(index - 1, -1, -1):
        if lis[i] == current_length and array[i] < subsequence[-1]:
            subsequence.append(array[i])
            current_length -= 1
 
    return subsequence[::-1]  # Reverse the subsequence to get the increasing order


# Test the program
array = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Original array:", array)
print("Longest increasing subsequence:", longest_increasing_subsequence(array))
