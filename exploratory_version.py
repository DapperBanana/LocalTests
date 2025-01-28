
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_lucas_carmichael(n):
    if n == 1:
        return False
    if is_prime(n):
        return False
    for p in range(2, n):
        if pow(2, p, n) == 1 and pow(1 + pow(5, 0.5), p, n) == 0:
            return True
    return False

num = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))
if is_lucas_carmichael(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
