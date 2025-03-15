
def find_median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    return median

# Test the function with a list of numbers
nums = [3, 7, 1, 8, 5, 9, 4]
print("List of numbers:", nums)
print("Median:", find_median(nums))
