
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    if length % 2 == 0:
        mid = length // 2
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        mid = length // 2
        median = sorted_numbers[mid]
    
    return median

# Example usage
numbers = [2, 4, 1, 5, 3]
median = calculate_median(numbers)
print("Median:", median)
