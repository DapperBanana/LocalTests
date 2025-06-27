
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]
    return median

# Input list of numbers
numbers = [8, 2, 5, 9, 1, 6, 3, 7, 4]

# Find the median
median = find_median(numbers)

# Display the result
print("Median:", median)
