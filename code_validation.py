
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(numbers)

    if length % 2 == 0:
        middle_1 = sorted_numbers[length // 2]
        middle_2 = sorted_numbers[length // 2 - 1]
        median = (middle_1 + middle_2) / 2
    else:
        median = sorted_numbers[length // 2]

    return median

numbers = [5, 2, 8, 1, 4, 7, 3, 6]
median = calculate_median(numbers)
print("Median:", median)
