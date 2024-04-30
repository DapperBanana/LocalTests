
from sympy import isprime, jacobi_symbol

def power_mod(a, n, m):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        n //= 2
    return result

def is_carmichael_number(n):
    if isprime(n):
        return False
    for a in range(2, n):
        if pow(a, n-1, n) != 1:
            return False
    return True

def is_lucas_pseudoprime(n):
    if jacobi_symbol(5, n) != 1:
        return False
    if power_mod(5, n//2, n) % n != (5 % n):
        return False
    return True

def is_lucas_carmichael_number(n):
    return is_carmichael_number(n) and is_lucas_pseudoprime(n)

number = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))

if is_lucas_carmichael_number(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
