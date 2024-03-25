
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def calculate_lcm(numbers):
    lcm_result = numbers[0]
    
    for number in numbers[1:]:
        lcm_result = lcm(lcm_result, number)
    
    return lcm_result

# Input list of numbers
numbers = [15, 20, 25, 30]

# Calculate LCM
result = calculate_lcm(numbers)

# Output
print(f"The LCM of {numbers} is: {result}")
