
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

numbers = [2, 3, 5, 7]  # List of numbers for which LCM needs to be calculated
result = lcm_list(numbers)
print(f"The LCM of {numbers} is: {result}")
