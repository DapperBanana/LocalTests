
def find_median(lst):
    lst.sort()
    n = len(lst)
    
    if n % 2 == 0:
        median1 = lst[n//2]
        median2 = lst[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = lst[n//2]
    
    return median

# Test the function with a list of numbers
numbers = [5, 2, 8, 1, 6, 3, 7, 4]
print("List of numbers:", numbers)
print("Median of the list:", find_median(numbers))
