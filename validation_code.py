
def find_median(nums):
    nums.sort()
    length = len(nums)
    
    if length % 2 == 0:
        mid1 = length // 2
        mid2 = mid1 - 1
        median = (nums[mid1] + nums[mid2]) / 2
    else:
        mid = length // 2
        median = nums[mid]
    
    return median

# Example usage
numbers = [4, 2, 7, 5, 9, 1, 3, 6, 8]
print("List of numbers:", numbers)
print("Median:", find_median(numbers))
