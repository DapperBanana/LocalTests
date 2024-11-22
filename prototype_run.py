
def find_median(nums):
    nums.sort()
    n = len(nums)
    
    if n % 2 == 0:
        median = (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        median = nums[n//2]
    
    return median

# Test the function
nums = [5, 2, 9, 1, 7]
print("Original list:", nums)
print("Median:", find_median(nums))
