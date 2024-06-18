
def calculate_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Test the function with some sample data
sample_list = [1, 2, 3, 4, 5]
avg = calculate_average(sample_list)
print("Average of elements in the list:", avg)
