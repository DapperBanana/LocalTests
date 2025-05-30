
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

def is_lucas_carmichael(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if not is_prime(num):
        return False
    for d in range(1, num):
        if (2 ** d) % num == 1:
            return False
    return True

num = int(input("Enter a number: "))
if is_lucas_carmichael(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
