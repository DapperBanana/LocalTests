
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Taking input from user
input_list = input("Enter a list of numbers separated by spaces: ")
list_of_numbers = list(map(int, input_list.split()))

# Calculate sum of list
result = sum_of_list(list_of_numbers)

print("Sum of all elements in the list: ", result)
