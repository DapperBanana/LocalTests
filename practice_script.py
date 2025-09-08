
def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        median = nums[n//2]
    return median

# Test the function with some example inputs
numbers1 = [3, 1, 5, 9, 2, 6]
print("Median of numbers1:", find_median(numbers1))

numbers2 = [2, 4, 6, 8]
print("Median of numbers2:", find_median(numbers2))

numbers3 = [1, 3, 5, 7, 9]
print("Median of numbers3:", find_median(numbers3))
