
def is_carmichael_number(n):
    if n < 561:
        return False
    if is_prime(n):
        return False
    for a in range(2, n):
        if pow(a, n, n) != a:
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testing the program
number = int(input("Enter a number to check if it is a Carmichael number: "))
if is_carmichael_number(number):
    print(f"{number} is a Carmichael number.")
else:
    print(f"{number} is not a Carmichael number.")
