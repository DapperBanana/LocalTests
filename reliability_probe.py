
def find_median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length//2 - 1] + numbers[length//2]) / 2
    else:
        median = numbers[length//2]
    return median

# Test the function with a list of numbers
numbers = [7, 3, 1, 9, 5]
median = find_median(numbers)
print("Median:", median)
