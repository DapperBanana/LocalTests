
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    
    return median

# Example list of numbers
numbers = [4, 3, 6, 8, 2, 9, 1, 5, 7]
median = calculate_median(numbers)

print(f"The median of the list {numbers} is: {median}")
