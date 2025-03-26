
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_lucas_carmichael(num):
    if is_prime(num):
        return False
    
    for i in range(2, num):
        if num % i == 0:
            if is_prime(i) and (i - 1) % (num - 1) != 0:
                return False

    return True

number = int(input("Enter a number: "))
if is_lucas_carmichael(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
