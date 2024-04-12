
def is_vampire_number(number):
    num_str = str(number)
    if len(num_str) % 2 != 0:
        return False
    
    pairs = [(num_str[i], num_str[j]) for i in range(len(num_str)) for j in range(len(num_str)) if i != j]
    
    for pair in pairs:
        vamp_num1 = int(pair[0] + pair[1])
        vamp_num2 = int(''.join([num for num in num_str if num not in pair]))
        if vamp_num1 * vamp_num2 == number:
            return True
    
    return False

number = int(input("Enter a number to check if it is a vampire number: "))
if is_vampire_number(number):
    print(f"{number} is a vampire number.")
else:
    print(f"{number} is not a vampire number.")
