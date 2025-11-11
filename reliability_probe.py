
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

# List of numbers
numbers = [4, 6, 8, 10]

# Calculate LCM of the list of numbers
result = lcm_of_list(numbers)

# Print the result
print("LCM of", numbers, "is:", result)
