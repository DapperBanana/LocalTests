
# Function to calculate GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate LCM
def lcm(a, b):
    return a * b // gcd(a, b)

# Function to calculate LCM of a list of numbers
def lcm_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

# Input list of numbers
numbers = [4, 6, 8, 10]

# Calculate LCM of the list of numbers
result = lcm_list(numbers)

# Output the result
print(f"LCM of {numbers} is: {result}")
