
def second_largest_element(nums):
    nums.sort()
    return nums[-2]

# Example
numbers = [10, 20, 4, 45, 99]
print("Second largest element:", second_largest_element(numbers))
