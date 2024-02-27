
def is_vampire_number(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False

    for i in range(10**(len(num_str)//2, 10**(len(num_str)//2 + 1)):
        if num % i == 0:
            fang1 = str(i)
            fang2 = str(num // i)
            if sorted(fang1 + fang2) == sorted(num_str):
                return True
    
    return False

num = int(input("Enter a number to check if it is a vampire number: "))
if is_vampire_number(num):
    print(num, "is a vampire number.")
else:
    print(num, "is not a vampire number.")
