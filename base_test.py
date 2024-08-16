
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

# Test the function with a list of numbers
numbers = [5, 10, 15, 20, 25, 30]
print("List of numbers:", numbers)
print("Median:", calculate_median(numbers))
