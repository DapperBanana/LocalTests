
from math import gcd
from sympy import jacobi_symbol

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def lucas_carmichael_number(n):
    if is_prime(n):
        return False

    for i in range(1, n):
        if pow(2, i, n) == 1:
            factors = [d for d in range(2, n) if n % d == 0]
            if all(jacobi_symbol(d, n) == -1 for d in factors):
                return True
            break

    return False

n = int(input("Enter a number: "))
if lucas_carmichael_number(n):
    print(f"{n} is a Lucas-Carmichael number.")
else:
    print(f"{n} is not a Lucas-Carmichael number.")
