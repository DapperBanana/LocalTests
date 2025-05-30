
def is_narcissistic(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    
    if total == number:
        return True
    else:
        return False

# Test the function
number = 153
if is_narcissistic(number):
    print(f"{number} is a narcissistic number")
else:
    print(f"{number} is not a narcissistic number")
    
number = 370
if is_narcissistic(number):
    print(f"{number} is a narcissistic number")
else:
    print(f"{number} is not a narcissistic number")
