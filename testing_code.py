
def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    if length % 2 == 0:  # if the length of the list is even
        middle = length // 2
        median = (sorted_numbers[middle-1] + sorted_numbers[middle]) / 2
    else:  # if the length of the list is odd
        middle = length // 2
        median = sorted_numbers[middle]

    return median

# Example usage:
numbers = [7, 3, 9, 2, 4, 5]
median = find_median(numbers)
print("The median of the list is:", median)
