
import math

def lucas_carmichael_number(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def lucas_carmichael_check(n):
        if n == 1:
            return False
        for x in range(1, n):
            if pow(2, x, n) == 1 and pow(1+x, n-1, n) == 1:
                return True
        return False
    
    if is_prime(num) and lucas_carmichael_check(num):
        return True
    else:
        return False

num = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))

if lucas_carmichael_number(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
