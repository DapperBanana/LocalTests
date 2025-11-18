
def is_narcissistic_number(num):
    power = len(str(num))
    total = sum(int(x) ** power for x in str(num))
    
    return total == num

num = int(input("Enter a number: "))
if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number.")
else:
    print(f"{num} is not a narcissistic number.")
