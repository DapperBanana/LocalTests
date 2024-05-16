
from math import gcd, isqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def is_lucas_carmichael_number(n):
    if is_prime(n):
        return False
    for i in range(2, n):
        if n % i == 0:
            if is_prime(i) and (i-1) % (n-1) != 0:
                return False
    return True

# Test the function with some numbers
number = 399
if is_lucas_carmichael_number(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
