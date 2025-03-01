
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

numbers = [4, 6, 8, 10]

print(f"The LCM of {numbers} is: {lcm_of_list(numbers)}")
