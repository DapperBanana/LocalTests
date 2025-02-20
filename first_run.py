
def is_carmichael_number(n):
    def power(x, y, p):
        result = 1
        x = x % p
        while y > 0:
            if y % 2 == 1:
                result = (result * x) % p
            y = y // 2
            x = (x * x) % p
        return result

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    if n < 2:
        return False

    for b in range(2, n):
        if gcd(b, n) == 1 and power(b, n-1, n) != 1:
            return False

    return True

n = int(input("Enter a number to check if it's a Carmichael number: "))
if is_carmichael_number(n):
    print(f"{n} is a Carmichael number.")
else:
    print(f"{n} is not a Carmichael number.")
