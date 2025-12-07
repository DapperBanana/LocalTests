// Python code to find the median of a list of numbers
def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # If even, median is the average of the two middle numbers
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # If odd, median is the middle number
        median = sorted_numbers[mid]

    return median