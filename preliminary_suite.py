
import sympy

def is_carmichael_number(n):
    if not sympy.isprime(n):
        for a in range(2, n):
            if pow(a, n-1, n) != 1:
                return False
        return True
    return False

num = int(input("Enter a number to check if it is a Carmichael number: "))

if is_carmichael_number(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is not a Carmichael number.")
