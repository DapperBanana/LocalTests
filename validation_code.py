
def is_vampire_number(num):
    num_str = str(num)
    num_len = len(num_str)
    
    if num_len % 2 != 0:
        return False
    
    for i in range(10**(num_len//2 - 1), int(10**(num_len//2))):
        if num % i == 0:
            quotient = num // i
            if sorted(str(i) + str(quotient)) == sorted(num_str):
                return True
    return False

num = int(input("Enter a number to check if it is a vampire number: "))
if is_vampire_number(num):
    print(num, "is a vampire number.")
else:
    print(num, "is not a vampire number.")
