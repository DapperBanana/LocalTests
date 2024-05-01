
def is_narcissistic_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    narcissistic_sum = sum(int(digit)**num_digits for digit in num_str)
    
    return num == narcissistic_sum

num = int(input("Enter a number to check if it is a narcissistic number:"))

if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
