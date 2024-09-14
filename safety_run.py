
def is_narcissistic_number(num):
    num_str = str(num)
    power = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** power
    
    return total == num

num = int(input("Enter a number: "))
if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
