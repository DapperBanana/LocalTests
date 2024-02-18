
def find_median(nums):
    nums.sort()
    n = len(nums)
    
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n//2]

# Example usage
numbers = [7, 12, 3, 1, 6, 9, 4]
median = find_median(numbers)
print("The median of the list is:", median)
