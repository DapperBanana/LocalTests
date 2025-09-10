
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

numbers = [4, 8, 2, 6, 3, 1, 5, 7]
median = find_median(numbers)

print(f"The median of the list {numbers} is: {median}")
