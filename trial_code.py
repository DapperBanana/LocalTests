
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

def calculate_lcm(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = find_lcm(lcm, numbers[i])

    return lcm

# Input list of numbers
numbers = [4, 6, 8, 10, 12]

# Calculate LCM
result = calculate_lcm(numbers)

print(f"The LCM of the numbers {numbers} is: {result}")
