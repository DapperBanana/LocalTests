
def calculate_median(numbers):
    numbers.sort()
    length = len(numbers)
    
    if length % 2 == 0:
        mid1 = numbers[length // 2]
        mid2 = numbers[length // 2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = numbers[length // 2]
    
    return median

numbers = [5, 2, 7, 3, 8, 1, 6, 4]
print("List of numbers:", numbers)
print("Median:", calculate_median(numbers))
