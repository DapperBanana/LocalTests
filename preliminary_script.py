
def calculate_median(numbers):
    numbers.sort()
    
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Example list of numbers
numbers = [5, 2, 8, 1, 6, 9, 3, 7, 4]

median = calculate_median(numbers)
print("Median:", median)
