
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

numbers = [5, 10, 15, 20]
print("List of numbers:", numbers)
print("LCM of the list:", lcm_of_list(numbers))
