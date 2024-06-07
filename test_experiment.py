
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]

# Input list of numbers
numbers = [13, 7, 21, 15, 9, 5, 11]

# Find the median
median = find_median(numbers)

print("The median of the list is:", median)
