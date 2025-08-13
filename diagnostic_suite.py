
def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n//2]

# Test the function
numbers = [4, 7, 1, 3, 9]
print("List of numbers:", numbers)
print("Median:", find_median(numbers))
