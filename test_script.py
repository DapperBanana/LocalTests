
def calculate_average(lst):
    if len(lst) == 0:
        return 0
    else:
        return sum(lst) / len(lst)

# Example usage
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average:", average)
