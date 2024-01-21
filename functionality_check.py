
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def calculate_lcm(numbers):
    lcm_result = 1
    for num in numbers:
        lcm_result = lcm(lcm_result, num)
    return lcm_result

# Example usage
numbers = [4, 5, 6, 10]
print(f"The LCM of {numbers} is: {calculate_lcm(numbers)}")
