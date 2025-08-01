
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lucas_number(n):
    return (2 ** n) - 1

def is_lucas_carmichael_number(n):
    if n < 2:
        return False

    if not is_prime(n):
        return False

    for i in range(2, n):
        if (2 ** i) % n == 1 and gcd(i, n) == 1:
            return False

    return True

number = int(input("Enter a number: "))
if is_lucas_carmichael_number(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
