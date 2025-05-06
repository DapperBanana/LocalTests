
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Test the program with a list of numbers
numbers = [1, 2, 3, 4, 5]
print("List of numbers:", numbers)
print("Median:", calculate_median(numbers))

numbers = [1, 2, 3, 4, 5, 6]
print("List of numbers:", numbers)
print("Median:", calculate_median(numbers))
