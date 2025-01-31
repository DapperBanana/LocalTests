
# Function to sort a list of integers in ascending order
def sort_list(lst):
    lst.sort()
    return lst

# Take user input for a list of integers
nums = list(map(int, input("Enter a list of integers separated by space: ").split()))

# Sort the list
sorted_nums = sort_list(nums)

# Print the sorted list
print("Sorted list in ascending order:", sorted_nums)
