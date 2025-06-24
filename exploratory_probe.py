
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

def next_prime(number):
    i = number + 1
    while True:
        if is_prime(i):
            return i
        i += 1

number = int(input("Enter a number: "))
next_prime_number = next_prime(number)
print(f"The smallest prime number greater than {number} is {next_prime_number}")
