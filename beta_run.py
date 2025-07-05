
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    sum_primes = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            sum_primes += i
    return sum_primes

limit = int(input("Enter the limit: "))
print("Sum of all prime numbers up to", limit, "is:", sum_of_primes(limit))
