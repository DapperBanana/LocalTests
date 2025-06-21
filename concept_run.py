
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

# Taking input from the user
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

# Calculating LCM of the list of numbers
result = lcm_of_list(numbers)
print(f"The LCM of the numbers {numbers} is: {result}")
