
def is_carmichael_number(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def power_mod(a, n, p):
        result = 1
        while n > 0:
            if n % 2 == 1:
                result = (result * a) % p
            a = (a * a) % p
            n = n // 2
        return result

    if n < 1:
        return False

    if n == 1:
        return False

    for a in range(2, n):
        if gcd(a, n) == 1 and power_mod(a, n, n) != a:
            return False

    return True

if __name__ == "__main__":
    num = int(input("Enter a number to check if it is a Carmichael number: "))
    if is_carmichael_number(num):
        print(f"{num} is a Carmichael number.")
    else:
        print(f"{num} is not a Carmichael number.")
