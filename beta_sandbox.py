
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
        
    return median

# Test the program
numbers = [5, 2, 9, 1, 7, 3]
median = calculate_median(numbers)
print("The median of the list is:", median)
