
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def power_mod(a, b, n):
    res = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % n
        b = b // 2
        a = (a * a) % n
    return res

def is_carmichael_number(n):
    if is_prime(n):
        return False
    for a in range(2, n):
        if power_mod(a, n, n) != a:
            return False
    return True

num = int(input("Enter a number to check if it is a Carmichael number: "))
if is_carmichael_number(num):
    print(num, "is a Carmichael number.")
else:
    print(num, "is not a Carmichael number.")
