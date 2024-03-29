
def is_lucas_carmichael(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lucas_lehmer(p):
        if p == 2:
            return True
        mp = 2**p - 1
        s, n = 4, 4
        for _ in range(2, p):
            s = (s*s - 2) % mp
        return s == 0
    
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, n+1, 2):
        if gcd(i, n) == 1 and lucas_lehmer(i):
            return False
    return True

n = int(input("Enter a number: "))
if is_lucas_carmichael(n):
    print(f"{n} is a Lucas-Carmichael number.")
else:
    print(f"{n} is not a Lucas-Carmichael number.")
