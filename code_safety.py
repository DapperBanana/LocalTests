
def calculate_median(numbers):
    numbers.sort()
    length = len(numbers)
    
    if length % 2 == 0:
        mid1 = length // 2
        mid2 = mid1 - 1
        median = (numbers[mid1] + numbers[mid2]) / 2
    else:
        median = numbers[length // 2]
        
    return median

# Test the function
numbers = [3, 5, 1, 9, 2, 6]
print("Input numbers:", numbers)
print("Median:", calculate_median(numbers))
