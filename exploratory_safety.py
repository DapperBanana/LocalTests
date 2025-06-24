
def is_vampire_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    if num_digits % 2 != 0:
        return False
    
    num_list = list(num_str)
    for i in range(10**(num_digits//2), int(10**(num_digits//2+1))):
        if sorted(str(i) + num_str) == sorted(num_list):
            return True
    return False

num = int(input("Enter a number: "))
if is_vampire_number(num):
    print(f"{num} is a vampire number.")
else:
    print(f"{num} is not a vampire number.")
