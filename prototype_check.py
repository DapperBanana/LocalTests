
def is_narcissistic(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    
    return total == number

# Test the function with some examples
print(is_narcissistic(153))  # True
print(is_narcissistic(9474))  # True
print(is_narcissistic(12))  # False
