
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

# Input list of numbers
numbers = [5, 2, 8, 4, 1, 9]

# Calculate median
median = calculate_median(numbers)

# Print the median
print(f"The median of the list {numbers} is: {median}")
