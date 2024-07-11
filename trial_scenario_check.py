
def is_carmichael_number(n):
    if is_prime(n):
        return False
    
    for a in range(2, n):
        if gcd(a, n) == 1:
            if pow(a, n-1, n) != 1:
                return False
    
    return True

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

number = int(input("Enter a number to check if it is a Carmichael number: "))

if is_carmichael_number(number):
    print(f"{number} is a Carmichael number.")
else:
    print(f"{number} is not a Carmichael number.")
