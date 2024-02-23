
def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 0:  # If n is even
        median = (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:  # If n is odd
        median = sorted_lst[n//2]
    
    return median

# Test the function
numbers = [7, 3, 8, 1, 5, 9]
print("List of numbers:", numbers)
print("Median:", find_median(numbers))
