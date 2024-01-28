
def find_second_largest(nums):
    # Initialize variables to store largest and second largest elements
    largest = float('-inf')
    second_largest = float('-inf')

    # Iterate through the list
    for num in nums:
        # Update largest and second largest elements accordingly
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    # Return the second largest element
    return second_largest

# Test the program
list1 = [3, 1, 4, 2, 5]
second_largest1 = find_second_largest(list1)
print(f"The second largest element in {list1} is: {second_largest1}")

list2 = [5, 5, 5, 5, 5]
second_largest2 = find_second_largest(list2)
print(f"The second largest element in {list2} is: {second_largest2}")

list3 = [1, 2, 3, 4, 5]
second_largest3 = find_second_largest(list3)
print(f"The second largest element in {list3} is: {second_largest3}")
