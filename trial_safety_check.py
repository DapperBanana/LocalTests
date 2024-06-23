
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        mid1 = numbers[n // 2]
        mid2 = numbers[n // 2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = numbers[n // 2]
        
    return median

numbers = [2, 5, 8, 10, 12, 15, 18, 20]
median = calculate_median(numbers)
print("The median of the list is:", median)
