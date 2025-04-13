
def find_median(numbers):
    numbers.sort()  # Sort the list of numbers
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
        
    return median

# Test the function
numbers = [3, 1, 5, 2, 4]
print("The median of the list is:", find_median(numbers))
