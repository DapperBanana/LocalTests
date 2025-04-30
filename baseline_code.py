
def find_lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def calculate_lcm_of_list(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = find_lcm(lcm, numbers[i])
    return lcm

numbers = [4, 6, 8, 16]
print("List of numbers:", numbers)
print("LCM of the list of numbers:", calculate_lcm_of_list(numbers))
