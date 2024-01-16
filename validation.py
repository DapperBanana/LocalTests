
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
list_of_numbers = [2, 6, 7, 10, 13, 25, 34, 47, 55, 69, 72]
target_number = 25

result = binary_search(list_of_numbers, target_number)
if result != -1:
    print(f"The target number {target_number} was found at index {result}.")
else:
    print("The target number was not found in the list.")
