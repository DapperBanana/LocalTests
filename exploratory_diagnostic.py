
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Test the function
numbers = [3, 1, 5, 7, 2, 8, 4, 6]
print("List of numbers:", numbers)
print("Median:", find_median(numbers))
