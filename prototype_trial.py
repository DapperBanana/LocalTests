
import sympy

def check_carmichael(num):
    if not sympy.isprime(num): # Check if number is not a prime
        for a in range(2, num):
            if pow(a, num-1, num) != 1: # Check if (a^(num-1)) % num is not equal to 1
                return False
        return True
    return False

num = int(input("Enter a number: "))

if check_carmichael(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is not a Carmichael number.")
