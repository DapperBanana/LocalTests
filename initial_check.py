
def is_narcissistic_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
        
    return total == num

# Main program
num = int(input("Enter a number: "))
if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
