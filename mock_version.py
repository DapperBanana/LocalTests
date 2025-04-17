
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

numbers = [5, 10, 15, 20, 25]
median = calculate_median(numbers)
print("The median of the list is:", median)
