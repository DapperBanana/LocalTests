
def find_median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    
    if n % 2 == 0:
        # If the list has even number of elements, average the middle two numbers
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        # If the list has odd number of elements, return the middle element
        median = sorted_nums[n // 2]
        
    return median

# Test the function
numbers = [5, 2, 6, 8, 3, 1, 7, 4]
print("List of numbers:", numbers)
print("Median:", find_median(numbers))
