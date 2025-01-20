
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(x, y):
    return gcd(x, y) == 1

def is_carmichael_number(n):
    if n < 2:
        return False
    
    for a in range(2, n):
        if is_coprime(a, n) and pow(a, n-1, n) != 1:
            return False
    
    return True

# Input number
num = int(input("Enter a number to check if it is a Carmichael number: "))

if is_carmichael_number(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is not a Carmichael number.")
