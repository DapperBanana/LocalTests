
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[(n//2)-1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Example list of numbers
numbers = [4, 2, 7, 1, 5]

# Calculate the median
median = calculate_median(numbers)
print("The median of the list is:", median)
