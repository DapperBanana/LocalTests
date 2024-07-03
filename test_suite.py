
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_lucas_carmichael(number):
    if number % 2 == 0:
        return False
    
    prime_factors = []
    for i in range(2, number):
        if is_prime(i) and number % i == 0:
            prime_factors.append(i)
    
    for prime in prime_factors:
        if (number - 1) % (prime - 1) != 0:
            return False
    
    return True

number = int(input("Enter a number to check if it's a Lucas-Carmichael number: "))
if is_lucas_carmichael(number):
    print(f"{number} is a Lucas-Carmichael number.")
else:
    print(f"{number} is not a Lucas-Carmichael number.")
