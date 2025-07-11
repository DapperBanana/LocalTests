
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]
    return median

# Test the function
numbers = [3, 1, 7, 5, 9, 2, 6, 4, 8]
median = calculate_median(numbers)
print("Median:", median)
