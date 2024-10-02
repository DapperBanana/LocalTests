
def is_narcissistic(num):
    num_str = str(num)
    num_len = len(num_str)
    result = 0
    
    for digit in num_str:
        result += int(digit) ** num_len
        
    return result == num

num = int(input("Enter a number: "))
if is_narcissistic(num):
    print(f"{num} is a narcissistic number")
else:
    print(f"{num} is not a narcissistic number")
