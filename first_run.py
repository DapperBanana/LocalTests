
def find_largest_element(list):
    max_element = list[0]
    
    for element in list:
        if element > max_element:
            max_element = element
    
    return max_element

# Test the function
list1 = [1, 5, 9, 3, 7]
print("List:", list1)
print("Largest element:", find_largest_element(list1))

list2 = [-10, -5, -20, -3, -7]
print("\nList:", list2)
print("Largest element:", find_largest_element(list2))

list3 = [4, 7, 2, 11, 6]
print("\nList:", list3)
print("Largest element:", find_largest_element(list3))
