
import sympy

def is_carmichael_number(n):
    if sympy.isprime(n):
        return False
    
    for a in range(2, n):
        if sympy.gcd(a, n) == 1 and pow(a, n-1, n) != 1:
            return False
    
    return True

# Input number to check
num = int(input("Enter a number to check if it's a Carmichael number: "))

if is_carmichael_number(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is not a Carmichael number.")
