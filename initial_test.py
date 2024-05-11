
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def power(a, n, p):
    res = 1
    a = a % p
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % p
        n = n // 2
        a = (a * a) % p
    return res

def is_carmichael_number(n):
    if n < 561:
        return False
    
    for a in range(2, n):
        if gcd(a, n) == 1:
            if power(a, n, n) != a:
                return False
            
    return True

num = int(input("Enter a number to check if it is a Carmichael number: "))
if is_carmichael_number(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is not a Carmichael number.")
