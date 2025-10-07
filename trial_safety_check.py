
def second_largest_element(nums):
    if len(nums) < 2:
        return "List must have at least two elements"
    
    max_num = max(nums[0], nums[1])
    second_max = min(nums[0], nums[1])
    
    for num in nums[2:]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    
    return second_max

# Test the function with a list
nums = [10, 20, 15, 30, 25]
result = second_largest_element(nums)
print("The second largest element is:", result)
