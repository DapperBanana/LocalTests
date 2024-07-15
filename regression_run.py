
def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        median = nums[n//2]
    return median

# Test the function
nums = [3, 6, 2, 8, 4, 5]
median = find_median(nums)
print(f"The median of the list {nums} is: {median}")
