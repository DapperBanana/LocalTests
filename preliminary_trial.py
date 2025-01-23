
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median

# Input list of numbers
numbers = [5, 2, 8, 3, 1, 7]
median = find_median(numbers)

print("The median of the list is:", median)
