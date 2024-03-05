
def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
        
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
        
    return lcm

def lcm_of_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = find_lcm(result, numbers[i])
        
    return result

# Test the program
numbers = [2, 3, 5, 7]
print("LCM of", numbers, "is:", lcm_of_list(numbers))
