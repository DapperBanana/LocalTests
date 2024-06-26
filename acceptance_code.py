
def is_vampire_number(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False
    
    digits = [int(x) for x in num_str]
    pairs = [(digits[i], digits[j]) for i in range(len(digits)) for j in range(len(digits)) if i != j]
    
    for pair in pairs:
        product = pair[0] * pair[1]
        product_str = str(product)
        if sorted(num_str) == sorted(product_str):
            return True
     
    return False

number = int(input("Enter a number: "))

if is_vampire_number(number):
    print(f"{number} is a vampire number.")
else:
    print(f"{number} is not a vampire number.")
