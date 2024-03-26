
def is_narcissistic(num):
    num_str = str(num)
    n = len(num_str)
    
    total = 0
    for digit in num_str:
        total += int(digit) ** n
        
    if total == num:
        return True
    else:
        return False

# Test the program
num = 153
if is_narcissistic(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
