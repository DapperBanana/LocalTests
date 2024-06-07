
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def calculate_lcm(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

numbers = [4, 5, 6, 8, 10]
lcm_result = calculate_lcm(numbers)
print(f"The LCM of {numbers} is: {lcm_result}")
