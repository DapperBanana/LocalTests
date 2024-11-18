
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

def calculate_lcm(numbers):
    if len(numbers) < 2:
        return "Please provide at least 2 numbers to calculate LCM."
    
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = find_lcm(lcm, numbers[i])
    
    return lcm

numbers = [4, 8, 12, 16]
print(f"LCM of {numbers} is: {calculate_lcm(numbers)}")
