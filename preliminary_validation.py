
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

numbers = [4, 6, 8, 10]
result = lcm_of_list(numbers)
print(f"The LCM of {numbers} is: {result}")
