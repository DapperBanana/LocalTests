
def is_vampire_number(num):
    num_str = str(num)

    if len(num_str) % 2 != 0:
        return False

    num_list = [int(d) for d in num_str]
    
    for i in range(10**(len(num_str)//2,10)):
        if i*i == num:
            return True
        for j in range(10**(len(num_str)//2)):
            if i*j == numb:
                return True

    return False

num = int(input("Enter a number: "))
if is_vampire_number(num):
    print(num, "is a vampire number.")
else:
    print(num, "is not a vampire number.")
