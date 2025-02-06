
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(limit):
    prime_sum = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum

limit = int(input("Enter a limit: "))
print("The sum of all prime numbers up to", limit, "is:", sum_primes(limit))
