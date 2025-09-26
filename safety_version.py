
def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test the function
nums = [1, 2, 3, 3, 4, 5, 5, 6]
print("Original list:", nums)
print("List with duplicates removed while preserving order:", remove_duplicates(nums))
