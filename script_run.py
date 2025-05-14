
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_lucas_carmichael(n):
    if n < 2:
        return False
    
    for a in range(2, n):
        if pow(a, n-1, n) != 1:
            return False
    
    for p in range(2, n):
        if is_prime(p) and (n % p == 0):
            if (pow(2, n // p, n) == 1) or (pow(2, (n-1) // p, n) != 1):
                return False
    
    return True

num = int(input("Enter a number: "))

if is_lucas_carmichael(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
