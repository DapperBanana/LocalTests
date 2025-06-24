
def find_median(numbers):
    numbers.sort()
    n = len(numbers)

    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]

    return median

# Input list of numbers
numbers = [5, 2, 9, 1, 7, 3, 8, 6, 4]

# Find the median
median = find_median(numbers)

print("List of numbers:", numbers)
print("Median:", median)
