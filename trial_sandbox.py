
from sympy import isprime

def power_mod(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent = exponent // 2
    return result

def is_lucas_carmichael_number(n):
    if isprime(n):
        return False
    
    for i in range(2, n):
        if n % i == 0:
            if power_mod(2, n-1, n) != 1:
                return False
    return True

# Input number to check
number = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))
if is_lucas_carmichael_number(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
