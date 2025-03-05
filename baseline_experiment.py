
def is_narcissistic_number(number):
    num_str = str(number)
    num_len = len(num_str)
    
    narcissistic_sum = sum([int(digit)**num_len for digit in num_str])
    
    return narcissistic_sum == number

# Test the program
number = 153
if is_narcissistic_number(number):
    print(f"{number} is a narcissistic number")
else:
    print(f"{number} is not a narcissistic number")
