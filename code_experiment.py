
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_lucas_carmichael(num):
    if num % 2 == 0:
        return False

    for p in range(2, num):
        if num % p == 0 and is_prime(p):
            if p % num != 1 and (num // p) % num != 1:
                return False

    return True

num = int(input("Enter a number: "))
if is_lucas_carmichael(num):
    print(num, "is a Lucas-Carmichael number.")
else:
    print(num, "is not a Lucas-Carmichael number.")
