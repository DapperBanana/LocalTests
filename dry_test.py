
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Test the program
numbers = [2, 3, 6, 8, 9]
print("List of numbers:", numbers)
print("Median:", calculate_median(numbers))
