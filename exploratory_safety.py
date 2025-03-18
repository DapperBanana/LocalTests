
def calculate_median(numbers):
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)
    
    if length % 2 == 0:
        mid1 = length // 2
        mid2 = mid1 - 1
        median = (sorted_nums[mid1] + sorted_nums[mid2]) / 2
    else:
        mid = length // 2
        median = sorted_nums[mid]
    
    return median

numbers = [3, 6, 9, 12, 15]
median = calculate_median(numbers)
print("The median of the list is:", median)
