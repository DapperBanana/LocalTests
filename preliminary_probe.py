
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

def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

given_number = int(input("Enter a number: "))
next_prime_number = next_prime(given_number)
print("The smallest prime number greater than", given_number, "is:", next_prime_number)
