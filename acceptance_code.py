
def calculate_median(numbers):
    numbers.sort()
    length = len(numbers)
    middle_index = length // 2

    if length % 2 == 0:
        median = (numbers[middle_index - 1] + numbers[middle_index]) / 2
    else:
        median = numbers[middle_index]

    return median

numbers = [5, 2, 9, 1, 7, 6]
median = calculate_median(numbers)
print("Median:", median)
