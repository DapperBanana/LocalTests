
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    if length % 2 == 0:
        median = (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    else:
        median = sorted_numbers[length // 2]
    
    return median

numbers = [2, 4, 6, 8, 10]
median = calculate_median(numbers)
print("Median:", median)
