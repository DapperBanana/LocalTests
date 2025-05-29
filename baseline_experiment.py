
def find_median(nums):
    nums.sort()
    n = len(nums)
    
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n//2]

# Test the function
numbers = [5, 2, 9, 1, 7, 6]
print(f"The median of the list {numbers} is: {find_median(numbers)}")
