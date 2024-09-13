
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
    for m in range(2, n):
        if pow(m, n-1, n*n) == 1:
            if not is_prime(m):
                return False
    return True

num = int(input("Enter a number: "))
if is_lucas_carmichael(num):
    print(num, "is a Lucas-Carmichael number.")
else:
    print(num, "is not a Lucas-Carmichael number.")
