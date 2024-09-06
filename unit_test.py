
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_coprime(a, b):
    return gcd(a, b) == 1

def power_mod(a, n, m):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        n //= 2
    return result

def is_carmichael_number(n):
    if n < 2:
        return False
    
    for a in range(2, n):
        if is_coprime(a, n) and power_mod(a, n-1, n) != 1:
            return False
    
    return True

number = int(input("Enter a number to check if it is a Carmichael number: "))

if is_carmichael_number(number):
    print(f"{number} is a Carmichael number.")
else:
    print(f"{number} is not a Carmichael number.")
