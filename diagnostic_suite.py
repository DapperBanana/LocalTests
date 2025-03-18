
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_lucas_carmichael_number(n):
    if is_prime(n):
        return False
    for i in range(1, n):
        if pow(i, n-1, n) != 1:
            return False
    return True

num = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))
if is_lucas_carmichael_number(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
