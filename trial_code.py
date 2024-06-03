
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

def is_lucas_carmichael(n):
    if n == 2:
        return False
    for i in range(1, n):
        if pow(2, i, n) != 1:
            return False
    if is_prime(n) and n % 4 == 3:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_lucas_carmichael(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
