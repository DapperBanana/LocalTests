
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    mid = length // 2
    
    if length % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    
    return median

# Test the program
numbers = [2, 5, 3, 9, 12, 15]
result = calculate_median(numbers)
print("Median:", result)
