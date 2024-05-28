
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

numbers = [7, 2, 10, 5, 3, 6, 1]
median = find_median(numbers)

print("List of numbers:", numbers)
print("Median:", median)
