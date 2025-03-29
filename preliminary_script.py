
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (numbers[mid1] + numbers[mid2]) / 2
    else:
        median = numbers[n // 2]
    
    return median

# Test the function
numbers = [7, 2, 5, 10, 8]
print("List of numbers:", numbers)
print("Median:", find_median(numbers))
