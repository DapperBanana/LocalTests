
def is_narcissistic_number(num):
    num_str = str(num)
    num_length = len(num_str)
    
    narcissistic_sum = 0
    for digit in num_str:
        narcissistic_sum += int(digit) ** num_length
    
    if narcissistic_sum == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
