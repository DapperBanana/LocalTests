
def is_vampire_number(number):
    num_str = str(number)
    num_len = len(num_str)
    
    if num_len % 2 != 0:
        return False
    
    pairs = [(int(num_str[i]), int(num_str[num_len//2 + i])) for i in range(num_len//2)]
    
    for pair in pairs:
        product = pair[0] * pair[1]
        if str(product) not in num_str:
            return False
    
    return True

number = int(input("Enter a number: "))
if is_vampire_number(number):
    print(f"{number} is a vampire number.")
else:
    print(f"{number} is not a vampire number.")
