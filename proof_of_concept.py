
def is_narcissistic_number(num):
    num_str = str(num)
    power = len(num_str)
    sum_of_digits = sum(int(digit)**power for digit in num_str)
    
    return sum_of_digits == num

# Test the function
num = 153
if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
