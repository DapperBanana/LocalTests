
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median1 = numbers[n//2]
        median2 = numbers[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = numbers[n//2]
    return median

# Test the function
numbers = [4, 2, 7, 1, 5, 3, 6]
print("List of numbers:", numbers)
print("Median:", calculate_median(numbers))
