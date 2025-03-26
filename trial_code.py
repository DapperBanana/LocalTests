
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_lucas_carmichael_number(n):
    if is_prime(n):
        return False
        
    for p in range(2, n):
        if n % p == 0 and is_prime(p) and gcd(p, n) == 1:
            if pow(p, n-1, n) != 1:
                return False

    return True

# Test the function
number = int(input("Enter a number: "))
if is_lucas_carmichael_number(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
