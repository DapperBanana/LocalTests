
def calculate_median(numbers):
    numbers.sort()
    length = len(numbers)
    
    if length % 2 == 0:
        median = (numbers[length//2 - 1] + numbers[length//2]) / 2
    else:
        median = numbers[length//2]
    
    return median

numbers = [4, 7, 2, 9, 5, 1, 8]
median = calculate_median(numbers)
print("Median:", median)
