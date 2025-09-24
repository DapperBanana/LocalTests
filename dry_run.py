
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

def lucas_carmichael_number(n):
    if n < 2:
        return False

    if is_prime(n):
        return False

    for i in range(1, n):
        if pow(1 + pow(5, i), n-1, n) != 1 % n:
            return False

    return True

n = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))
if lucas_carmichael_number(n):
    print(f"{n} is a Lucas-Carmichael number.")
else:
    print(f"{n} is not a Lucas-Carmichael number.")
