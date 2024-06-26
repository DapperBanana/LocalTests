
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % p
        y = y // 2
        x = (x * x) % p
    return res

def is_lucas_carmichael(n):
    if not is_prime(n):
        return False
    for a in range(2, n):
        if power(a, n-1, n) != 1:
            return False
    return True

number = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))
if is_lucas_carmichael(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
