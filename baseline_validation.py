
def calculate_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Example usage
numbers = [2, 4, 6, 8, 10]
print("List of numbers:", numbers)
print("Median:", calculate_median(numbers))
