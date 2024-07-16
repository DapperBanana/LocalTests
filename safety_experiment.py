
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def calculate_lcm(numbers):
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result

# Input list of numbers
numbers = [15, 20, 30, 45]

# Calculate LCM
lcm_result = calculate_lcm(numbers)

# Output
print(f"The LCM of the numbers {numbers} is: {lcm_result}")
