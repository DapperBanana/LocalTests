
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

def lucas_carmichael(n):
    if n < 2:
        return False
    if is_prime(n):
        return False
    for i in range(2, n):
        if pow(i, n-1, n) != 1:
            return False
    return True

num = int(input("Enter a number: "))
if lucas_carmichael(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
