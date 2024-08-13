
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_carmichael_number(n):
    if n < 2:
        return False
    for a in range(2, n):
        if gcd(a, n) == 1 and pow(a, n-1, n) != 1:
            return False
    return True

number = int(input("Enter a number to check if it is a Carmichael number: "))

if is_carmichael_number(number):
    print(f"{number} is a Carmichael number.")
else:
    print(f"{number} is not a Carmichael number.")
