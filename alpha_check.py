
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_carmichael_number(n):
    if n < 561:  # No Carmichael numbers below 561
        return False
    for a in range(2, n):
        if gcd(a, n) == 1 and pow(a, n-1, n) != 1:
            return False
    return True

# Test the program
number = 561
if is_carmichael_number(number):
    print(f"{number} is a Carmichael number.")
else:
    print(f"{number} is not a Carmichael number.")
