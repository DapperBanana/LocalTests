
def find_second_largest(arr):
    arr.sort()
    return arr[-2]

# Example list
my_list = [1, 6, 3, 8, 2, 7, 5, 4]
second_largest = find_second_largest(my_list)

print(f"The second largest element in the list is: {second_largest}")
