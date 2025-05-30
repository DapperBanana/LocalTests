
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Test the function with a list of numbers
numbers = [4, 2, 6, 8, 5, 1, 3, 7]
median = calculate_median(numbers)
print("The median of the list is:", median)
