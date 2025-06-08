
def calculate_median(numbers):
    numbers.sort()  # sort the list in ascending order

    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2  # calculate median for even number of elements
    else:
        median = numbers[n//2]  # calculate median for odd number of elements

    return median

# Example
numbers = [2, 6, 4, 8, 10]
print("Median:", calculate_median(numbers))
