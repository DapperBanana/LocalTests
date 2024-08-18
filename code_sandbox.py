
def is_vampire_number(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False
    
    num_digits = [int(d) for d in num_str]
    num_digits.sort()
    
    for i in range(10**((len(num_str)//2)-1), int(num**0.5)+1):
        if num % i == 0:
            j = num / i
            if sorted(str(i) + str(j)) == num_digits:
                return True
    return False

num = int(input("Enter a number: "))
if is_vampire_number(num):
    print(num, "is a vampire number.")
else:
    print(num, "is not a vampire number.")
