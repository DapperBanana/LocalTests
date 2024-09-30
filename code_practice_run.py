
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_list(numbers):
    if len(numbers) < 2:
        return None
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

numbers = [4, 6, 8, 10]
result = lcm_list(numbers)
print(f"The LCM of {numbers} is: {result}")
