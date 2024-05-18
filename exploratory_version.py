
def calculate_average(lst):
    if len(lst) == 0:
        return 0
    total = sum(lst)
    return total / len(lst)

# Example list
my_list = [1, 2, 3, 4, 5]

average = calculate_average(my_list)
print("Average:", average)
