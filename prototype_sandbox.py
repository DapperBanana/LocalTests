
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm(numbers):
    lcm_value = numbers[0]
    for i in range(1, len(numbers)):
        lcm_value = lcm(lcm_value, numbers[i])
    return lcm_value

numbers = [4, 6, 8, 10]
result = find_lcm(numbers)
print(f"The LCM of {numbers} is: {result}")
