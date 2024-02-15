
def find_median(lst):
    lst.sort()  # Sort the list in ascending order
    
    n = len(lst)
    if n % 2 == 0:
        # If the list has an even number of elements, return the average of the middle two elements
        median = (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        # If the list has an odd number of elements, return the middle element
        median = lst[n // 2]
        
    return median

# Example usage:
numbers = [5, 2, 7, 3, 1, 6, 4]
print("Median:", find_median(numbers))
