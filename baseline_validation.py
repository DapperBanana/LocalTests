
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

# Example
numbers = [7, 12, 4, 2, 5, 6]
median = find_median(numbers)
print("Median:", median)
