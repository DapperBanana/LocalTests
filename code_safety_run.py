
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

# Input list of numbers
numbers = [3, 5, 1, 7, 6, 10, 8, 2, 4, 9]

# Calculate median
median = calculate_median(numbers)

print("List of numbers:", numbers)
print("Median:", median)
