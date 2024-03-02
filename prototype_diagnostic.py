
def find_median(numbers):
    n = len(numbers)
    numbers.sort()

    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (numbers[mid1] + numbers[mid2]) / 2
    else:
        mid = n // 2
        median = numbers[mid]

    return median

# Input list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
median = find_median(numbers)

print("List of numbers:", numbers)
print("Median:", median)
