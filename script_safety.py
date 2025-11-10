
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

# Test the program
numbers = [12, 34, 56, 78, 90]
median = calculate_median(numbers)
print("Median:", median)
