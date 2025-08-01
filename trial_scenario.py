
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def calculate_lcm(numbers):
    lcm_result = 1
    for num in numbers:
        lcm_result = lcm(lcm_result, num)
    return lcm_result

numbers = [4, 5, 6, 8, 10]
result = calculate_lcm(numbers)
print(f"The Least Common Multiple of {numbers} is: {result}")
