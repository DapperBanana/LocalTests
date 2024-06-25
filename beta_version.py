
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_carmichael_number(n):
    if all(gcd(a, n) == 1 for a in range(1, n)):
        return False  # n is not a composite number
    for a in range(1, n):
        if gcd(a, n) == 1 and pow(a, n-1, n) != 1:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Enter a number to check if it is a Carmichael number: "))
    if is_carmichael_number(number):
        print(f"{number} is a Carmichael number.")
    else:
        print(f"{number} is not a Carmichael number.")
