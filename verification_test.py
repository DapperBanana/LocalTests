
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_carmichael_number(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return False

    for a in range(2, n):
        if gcd(a, n) == 1 and pow(a, n-1, n) != 1:
            return False

    return True

num = int(input("Enter a number: "))

if is_carmichael_number(num):
    print(num, "is a Carmichael number.")
else:
    print(num, "is not a Carmichael number.")
