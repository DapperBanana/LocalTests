
def is_narcissistic(num):
    num_str = str(num)
    num_length = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** num_length
    
    return total == num

# Test the function
num = 153
if is_narcissistic(num):
    print(f"{num} is a narcissistic number")
else:
    print(f"{num} is not a narcissistic number")
