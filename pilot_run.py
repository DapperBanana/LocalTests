
def calculate_sum(input_list):
    total = 0
    for num in input_list:
        total += num
    return total

# Test the function with a sample list
sample_list = [1, 2, 3, 4, 5]
result = calculate_sum(sample_list)
print("The sum of all elements in the list is:", result)
