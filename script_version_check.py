
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result

numbers = [4, 6, 8, 10]
print("List of numbers:", numbers)
print("LCM of the list:", lcm_of_list(numbers))
