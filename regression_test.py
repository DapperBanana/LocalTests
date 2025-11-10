
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(numbers):
    if len(numbers) < 2:
        return None
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

numbers = [2, 3, 4, 5]
result = lcm_list(numbers)
print("The LCM of the numbers", numbers, "is:", result)
