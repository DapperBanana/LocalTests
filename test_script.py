
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_lucas_carmichael(n):
    if n == 1:
        return False
    if not is_prime(n):
        return False
    for i in range(2, n):
        if pow(i, n-1, n) != 1:
            return False
    return True

num = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))
if is_lucas_carmichael(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
